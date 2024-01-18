from collections import UserDict


class Field:
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError
        self.value = value

    def is_valid(self, value):
        return True

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)



    def is_valid(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError
        else:
            return value


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        phone = Phone(number)
        if phone in self.phones:
            raise ValueError("This phone number is already saved")
        else:
            self.phones.append(phone)

    def remove_phone(self, number):
        phone = Phone(number)
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            raise KeyError("Can't remove: this phone number doesn't exist")

    def edit_phone(self, old_number, new_number):
        old_phone = Phone(old_number)
        new_phone = Phone(new_number)
        if old_phone in self.phones:
            target_index = self.phones.index(old_phone)
            self.phones[target_index] = new_phone
        else:
            raise ValueError("Can't edit: this phone number doesn't exist")

    def find_phone(self, number):
        phone = Phone(number)
        if phone in self.phones:
            return phone
        else:
            return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self, record=None):
        super().__init__()
        record = Record(record)
        # self.data[record.name] = record

    def add_record(self, text):
        record = Record(text)
        if record.name in self.data:
            raise ValueError("This user is already exist")
        else:
            self.data[record.name] = record

    def find(self, name):
        if name not in self.data:
            return None
        else:
            return self.data[name]

    def delete(self, name):
        if name in self.data:
            del self.data[name]



