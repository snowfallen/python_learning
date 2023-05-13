class Account:
    def __init__(self, name: str, last_name: str, born_date: int, email: str, phone_number: int):
        self._name: str = name
        self._last_name: str = last_name
        self._born_date: int = born_date
        self._email: str = email
        self._phone_number: int = phone_number

    def get_name(self) -> str:
        return self._name

    def get_last_name(self) -> str:
        return self._last_name

    def get_born(self) -> int:
        return self._born_date

    def get_phone_number(self) -> int:
        return self._phone_number

    def get_email(self) -> str:
        return self._email

    def set_name(self, new_name_value: str) -> str:
        self._name = new_name_value
        return new_name_value

    def set_last_name(self, new_last_name_value: str) -> str:
        self._last_name = new_last_name_value
        return new_last_name_value

    def set_born(self, new_born_date_value: int) -> int:
        self._born_date = new_born_date_value
        return new_born_date_value

    def set_phone_number(self, new_phone_number_value: int) -> int:
        self._phone_number = new_phone_number_value
        return new_phone_number_value

    def set_email(self, new_email_value) -> str:
        self._email = new_email_value
        return new_email_value
