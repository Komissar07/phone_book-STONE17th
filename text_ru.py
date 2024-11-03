main_menu_items = [
    'Главное меню',
    'Открыть файл',
    'Сохранить файл',
    'Показать все контакты',
    'Создать контакт',
    'Найти контакт',
    'Изменить контакт',
    'Удалить контакт',
    'Выход',
]

main_menu_choice = 'Выберите пункт меню: '

empty_phone_book_error = 'Телефонная книга пуста или не открыта'

new_contact_msg = 'Создание нового контакта'
new_contact_fields = [
    'Введите имя: ',
    'Введите номер телефона: ',
    'Введите комментарий: ',
]


def update_contact_msg(contact_id: str) -> str:
    return f'Измените контакт c ID {contact_id}'


enter_to_no_change = ' или нажмите ENTER, чтобы оставить без изменений: '
update_contact_fields = [field[:-2] + enter_to_no_change for field in new_contact_fields]

phone_book_load_successful = 'Телефонная книга успешно загружена!'
phone_book_save_successful = 'Телефонная книга успешно сохранена!'

input_key_word = 'Введите ключевое слово для поиска: '

user_id_to_update = 'Введите ID контакта для изменения: '
user_id_to_del = 'Введите ID контакта для удаления: '


def main_menu_input_error(menu_len: int) -> str:
    return f'Введите целое число от 1 до {menu_len - 1}'


def new_contact_added_successful(contact_name: str) -> str:
    return f'Контакт {contact_name} успешно добавлен!'


def key_word_not_find_in_phone_book(key_word: str) -> str:
    return f'Контакты содержащие "{key_word}" не найдены!'


def contact_id_not_found(contact_id: str):
    return f'Контакт с ID {contact_id} не существует!'


def update_contact_successful(contact_name: str) -> str:
    return f'Контакт {contact_name} успешно обновлен!'


def msg_del_contact(contact_id: str, result: bool) -> str:
    if result:
        return f'Контакт с ID {contact_id} успешно удален!'
    return contact_id_not_found(contact_id)
