class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"Name: {self.name}, {self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self
        
# UPDATED - Chained Method calls
first_user = User("Guido van Rossum", "guido@python.com" )
second_user = User("Monty Python", "monty@python.com")
third_user = User("Jacob Sexton", "jake@example.com")
# Create 3 instances of user class
print(first_user.name)
print(second_user.name)
print(third_user.name)
first_user.display_user_balance()
second_user.display_user_balance()
third_user.display_user_balance()
# First user makes 3 deposits and 1 withdrawal, then display account balance
first_user.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(150).display_user_balance()
# Second User makes 2 deposits and 2 withdrawals, then display balance
second_user.make_deposit(200).make_deposit(400).make_withdrawal(100).make_withdrawal(150)
second_user.display_user_balance()
# Third user makes 1 deposit and 3 withdrawals, then display balance
third_user.make_deposit(10000000).make_withdrawal(825).make_withdrawal(50).make_withdrawal(40000).display_user_balance()
# Transfer first user's money to third user, the print both balances
first_user.transfer_money(third_user, 450)
first_user.display_user_balance()
third_user.display_user_balance()