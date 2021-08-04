class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def dispaly_account_info(self):
        print(f' Balance = {self.balance }')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(.2, 5000)

    def display_user_balance(self):
        print(
            f"User: {self.name}, Balance {self.account.dispaly_account_info()}")
        return self


nick = User("nick")

nick.account.deposit(100)
nick.display_user_balance()
