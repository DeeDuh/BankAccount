class BankAccount:
    def __init__(self, bal):
        self._balance = bal

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print('Ошибка: недостаточно средств!')

    def get_balance(self):
        return self._balance
