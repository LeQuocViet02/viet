class Wallet:
    def __init__(self, amount):
        self.amount = amount
        return None

    def __add__(self, another):
        return Wallet(self.amount + another.amount)

    def __repr__(self):
        return f'Wallet with ${self.amount}'

foo = Wallet(12)
bar = Wallet(7)
ham = foo + bar
print(ham)