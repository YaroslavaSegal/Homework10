from collections import UserDict
from datetime import datetime, date


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @staticmethod
    def is_valid(value):
        if value:
            return True

    @value.setter
    def value(self, value):
        if self.is_valid(value):
            self.__value = value
        else:
            raise ValueError

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.__value = None
        self.value = value

    @staticmethod
    def is_valid(value):
        if value.isdigit() and len(value) == 10:
            return True


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self.__value = None
        self.value = value

    @staticmethod
    def is_valid(value):
        if datetime.strptime(value, '%d-%m-%Y').date():
            return True

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if self.is_valid(value):
            self.__value = datetime.strptime(value, '%d-%m-%Y').date()
        else:
            raise ValueError


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)

    @property
    def days_to_birthday(self):
        current_date = date.today()
        current_year = current_date.year
        user_date = self.birthday.value.replace(year=current_year)
        delta = user_date.toordinal() - current_date.toordinal()
        if delta == 0:
            return f'Today is your birthday! Congratulations!'
        elif delta > 0:
            return f'{delta} days left until your birthday'
        else:
            user_date = self.birthday.value.replace(year=current_year + 1)
            delta = user_date.toordinal() - current_date.toordinal()
            return f'{delta} days left until your birthday'

    def add_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                raise ValueError
        else:
            new_phone = Phone(number)
            self.phones.append(new_phone)

    def remove_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                self.phones.remove(phone)

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                new_phone = Phone(new_number)
                target_index = self.phones.index(phone)
                self.phones[target_index] = new_phone
                return new_phone
        else:
            raise ValueError

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone
        else:
            return None

    def __str__(self):
        return (f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)},"
                f" birthday: {self.birthday.value}")


class AddressBook(UserDict):

    def add_record(self, record: Record):
        if record.name.value not in self.data:
            self.data[record.name.value] = record
        else:
            raise ValueError

    def find(self, username):
        if username not in self.data:
            return None
        else:
            return self.data[username]

    def delete(self, username):
        if username in self.data:
            del self.data[username]

    def iterator(self, n):
        self.page = []

        for value in self.data.values():
            self.page.append(f'{value}')
            if len(self.page) == n:
                yield self.page
                self.page = []
        yield self.page
