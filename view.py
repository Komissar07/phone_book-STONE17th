import text_ru


def show_main_menu():
    for i, row in enumerate(text_ru.main_menu_items):
        print(f'\t{i}. {row}' if i else row)


def user_input(msg: str) -> str:
    return input(msg)


def user_input_contact(input_msg: str, fields: list[str]) -> list[str]:
    print(input_msg)
    contact_data = []
    for field in fields:
        data = user_input(field)
        contact_data.append(data)
    return contact_data


def print_message(msg: str) -> None:
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n')


def print_contact_list(contact_list: dict[str, dict[str, str]], msg_error) -> None:
    if contact_list:
        for cnt_id, cnt in contact_list.items():
            print(f"{cnt_id}. {cnt['name']} {cnt['phone']} {cnt['comment']}")
    else:
        print_message(msg_error)
