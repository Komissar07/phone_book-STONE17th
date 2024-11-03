from collections import namedtuple

SEPARATOR = ';'


def validate_user_input(user_data: str, len_menu: int) -> bool:
    return user_data.isdigit() and (0 < int(user_data) < len_menu)


Contact = namedtuple('Contact', 'name phone comment')


class PhoneBook:
    def __init__(self, path: str):
        self._path = path
        self.contacts: dict[int, Contact] = {}

    def _next_id(self):
        if not self.contacts:
            return 1
        return max(self.contacts) + 1

    def open(self):
        with open(self._path, 'r', encoding='UTF-8') as file:
            for row in file.readlines():
                cur_id = self._next_id()
                name, phone, comment = row.strip().split(SEPARATOR)
                contact = Contact(name, phone, comment)
                self.contacts[cur_id] = contact

    def _contact_dict_to_str(self) -> str:
        contact_list = []
        for contact_id, contact in self.contacts.items():
            contact_list.append(SEPARATOR.join(contact))
        return '\n'.join(contact_list)

    def save(self):
        with open(self._path, 'w', encoding='UTF-8') as file:
            file.write(self._contact_dict_to_str())

    @staticmethod
    def _dict_to_json(contacts_list: dict[int, Contact]):
        _json = {}
        for contact_id, contact in contacts_list.items():
            _json[str(contact_id)] = {
                'name': contact.name,
                'phone': contact.phone,
                'comment': contact.comment,
            }
        return _json

    def get_contacts(self):
        return self._dict_to_json(self.contacts)

    def add_contact(self, contact: list[str]) -> None:
        cur_id = self._next_id()
        new_contact = Contact(*contact)
        self.contacts[cur_id] = new_contact

    @staticmethod
    def _key_word_in_contact(contact: Contact, key_word: str) -> bool:
        for field in contact:
            if key_word in field:
                return True
        return False

    def find(self, key_word: str):
        find_result = {}
        for contact_id, contact in self.contacts.items():
            if self._key_word_in_contact(contact, key_word):
                find_result[contact_id] = contact
        return self._dict_to_json(find_result)

    def update(self, contact_id: str, update_contact: list[str]):
        cur_contact = self.contacts[int(contact_id)]
        updated_contact = Contact(
            update_contact[0] if update_contact[0] else cur_contact.name,
            update_contact[1] if update_contact[1] else cur_contact.phone,
            update_contact[2] if update_contact[2] else cur_contact.comment,
        )
        self.contacts[int(contact_id)] = updated_contact
        return updated_contact.name

    def delete(self, contact_id: str):
        if int(contact_id) in self.contacts:
            deleted_id = self.contacts.pop(int(contact_id))
            return deleted_id
        return False
