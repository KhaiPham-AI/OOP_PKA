class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self._amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if type(amount) != int:
            raise ValueError("please use int for amount")
        self._transactions.append(amount)

    @property
    def balance(self):
        return self._amount + sum(self._transactions)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self._amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self._amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return self._transactions[::-1]

    def __add__(self, other):
        owner = f"{self.owner}&{other.owner}"
        amount = self._amount + other._amount
        transactions = self._transactions + other._transactions
        new_account = Account(owner, amount)
        new_account._transactions = transactions
        return new_account

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def validate_transaction(self, other, amount_to_add):
        other.add_transaction(amount_to_add)
        if other.balance < 0:
            raise ValueError("sorry cannot go in debt!")
        return f"New balance: {other.balance}"

acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)