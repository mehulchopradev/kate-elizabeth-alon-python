from .exceptions.min_bal_error import MinBalError

class Account:
    min_balance = 1000

    def __init__(self, acc_name, acc_type, acc_balance):
        self.acc_name = acc_name
        self.acc_type = acc_type
        self.acc_balance = acc_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Amount passed must be more than 0')
        if self.acc_balance - amount < Account.min_balance:
            raise MinBalError('Min bal of {0} to be maintained'.format(self.acc_balance))

        self.acc_balance -= amount
        return self.acc_balance