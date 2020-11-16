from com.abc.banking.account import Account
from com.abc.banking.exceptions.min_bal_error import MinBalError

from traceback import print_exc

a1 = Account('mehul', 'savings', 10000)

try:
    print(a1.withdraw(8000))
except MinBalError:
    print('Min bal not mantained')
    print_exc()
except ValueError:
    print_exc()