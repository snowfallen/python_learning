from BankAccount import BankAccount


class Bank:
    def __init__(self, bank_name: str):
        self._bank_name: str = bank_name

    @staticmethod
    def create_user() -> BankAccount:
        user_name: str = input('Write user name... ')
        user_last_name: str = input('Write user last name... ')
        user_born_date: int = int(input('Write user born date... '))
        user_email: str = input('Write user email... ')
        user_phone_number: int = int(input('Write user phone number... '))
        user_id_number: str = input('Write id user number... ')
        user_country: str = input('Write user country... ')
        user_city: str = input('Write user city... ')

        user_account = BankAccount(
            user_name,
            user_last_name,
            user_born_date,
            user_email,
            user_phone_number,
            user_id_number,
            user_country,
            user_city)

        return user_account


user_bank_account = Bank.create_user()
print(user_bank_account.get_name())
print(user_bank_account.get_city())
print(user_bank_account.get_phone_number())
