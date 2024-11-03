import text_ru
import view
import model

PATH = 'phone_book.txt'


def _user_input():
    while True:
        user_data = view.user_input(text_ru.main_menu_choice)
        if model.validate_user_input(user_data, len(text_ru.main_menu_items)):
            return user_data
        view.print_message(text_ru.main_menu_input_error(len(text_ru.main_menu_items)))


def start():
    phone_book = model.PhoneBook(PATH)
    while True:
        view.show_main_menu()
        user_choice = _user_input()
        if user_choice == '1':
            phone_book.open()
            view.print_message(text_ru.phone_book_load_successful)
        elif user_choice == '2':
            phone_book.save()
            view.print_message(text_ru.phone_book_save_successful)
        elif user_choice == '3':
            view.print_contact_list(
                phone_book.get_contacts(),
                text_ru.empty_phone_book_error)
        elif user_choice == '4':
            contact = view.user_input_contact(
                text_ru.new_contact_msg,
                text_ru.new_contact_fields
            )
            phone_book.add_contact(contact)
            view.print_message(text_ru.new_contact_added_successful(contact[0]))

        elif user_choice == '5':
            key_word = view.user_input(text_ru.input_key_word)
            find_result = phone_book.find(key_word)
            view.print_contact_list(
                find_result,
                text_ru.key_word_not_find_in_phone_book(key_word),
            )
        elif user_choice == '6':
            user_id_to_update = view.user_input(text_ru.user_id_to_update)
            if int(user_id_to_update) in phone_book.contacts:
                updated_contact = view.user_input_contact(
                    text_ru.update_contact_msg(user_id_to_update),
                    text_ru.update_contact_fields,
                )
                new_name = phone_book.update(user_id_to_update, updated_contact)
                view.print_message(text_ru.update_contact_successful(new_name))
            else:
                view.print_message(text_ru.contact_id_not_found(user_id_to_update))
        elif user_choice == '7':
            user_id_to_del = view.user_input(text_ru.user_id_to_del)
            del_result = phone_book.delete(user_id_to_del)
            view.print_message(text_ru.msg_del_contact(user_id_to_del, del_result))

        elif user_choice == '8':
            print('Выход')
            break
