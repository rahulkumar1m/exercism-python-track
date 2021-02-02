class BankAccount:
    def __init__(self):
        self.status = 'CLOSE'
        self.balance = 0

    def get_balance(self):
        if self.status == 'OPEN':
            return self.balance
        else:
            raise ValueError('Closed Account')

    def open(self):
        if self.status == 'CLOSE':
            self.status = 'OPEN'
        else:
            raise ValueError('Already Opened Account')

    def deposit(self, amount):
        if (self.status == 'OPEN') & (amount >= 0):
            self.balance += amount
        else:
            raise ValueError('Account Closed')

    def withdraw(self, amount):
        if (self.status == 'OPEN') & (self.balance >= amount) & (amount >= 0):
            self.balance -= amount
        else:
            raise ValueError('Account Closed / Withdraw amount > balance amount / Cannot withdraw negative amount')

    def close(self):
        if self.status == 'OPEN':
            self.status = 'CLOSE'
            self.balance = 0
        else:
            raise ValueError('Account already closed')
