from Account import Account


class BankAccount(Account):
    __password: str

    def __init__(
            self,
            name: str,
            last_name: str,
            born_date: int,
            email: str,
            phone_number: int,
            id_number: str,
            country: str,
            city: str,
    ):
        super().__init__(
            name,
            last_name,
            born_date,
            email,
            phone_number)

        self.__id_number: str = id_number
        self.__country: str = country
        self.__city: str = city

    def get_id_number(self) -> str:
        return self.__id_number

    def get_country(self) -> str:
        return self.__country

    def get_city(self) -> str:
        return self.__city

    def generate_password(self) -> str:
        self.__password = '34r34r34f3r'
        return 'Success! Password was created.'

    def get_password(self) -> str:
        return self.__password

    def set_id_number(self, new_id_value: str) -> str:
        self.__id_number = new_id_value
        return new_id_value

    def set_country(self, new_country_value: str) -> str:
        self.__country = new_country_value
        return new_country_value

    def set_city(self, new_city_value: str) -> str:
        self.__city = new_city_value
        return new_city_value