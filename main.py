from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.check_phone()

    def check_phone(self):
        if not (self.value.isdigit() and len(self.value) == 10):
            raise ValueError("Incorrect phone number: enter 10 digits")
        else:
            return self.value


class Record:
    def __init__(self, Name):
        self.Name = Name
        self.Phone = []

    def add_phone(self, phone: Phone):
        if phone in self.Phone:
            raise ValueError("This phone number is already saved")
        else:
            self.Phone.append(phone)

    def remove_phone(self, phone: Phone):
        if phone in self.Phone:
            self.Phone.remove(phone)
        else:
            raise KeyError("Can't remove: this phone number doesn't exist")

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        if old_phone in self.Phone:
            target_index = self.Phone.index(old_phone)
            self.Phone[target_index] = new_phone
        else:
            raise ValueError("Can't edit: this phone number doesn't exist")

    def find_phone(self, phone: Phone):
        if phone in self.Phone:
            return Phone(phone)
        else:
            return None


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        record = Record(Name)

        self.data[record.Name] = record

    def add_record(self, record):
        if record.Name in self.data:
            raise ValueError("This user is already exist")
        else:
            self.data[record.Name] = record

    def find(self, name):
        if name not in self.data:
            return None
        else:
            return self.data[name]

    def delete(self, name):
        if name in self.data:
            del self.data[name]


def main():
    pass


if __name__ == "__main__":
    main()
