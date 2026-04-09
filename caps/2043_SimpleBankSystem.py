from collections import defaultdict
from typing import List

class Bank:

    def __init__(self, balance: List[int]):
        self.balances = balance
        self.lookup_balance = defaultdict(int)
        self.lookup_balance = {acct + 1: balance for acct, balance in enumerate(self.balances)}

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 in self.lookup_balance and self.lookup_balance[account1] >= money and account2 in self.lookup_balance:
            self.lookup_balance[account1] -= money
            self.lookup_balance[account2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account in self.lookup_balance:
            self.lookup_balance[account] += money
            return True
        return False


    def withdraw(self, account: int, money: int) -> bool:
        if account in self.lookup_balance and self.lookup_balance[account] >= money:
            self.lookup_balance[account] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)