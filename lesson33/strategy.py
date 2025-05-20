#!/usr/bin/python3

"""
• Write a Python program, strategy.py, and demonstrate the following:
      ◦ Write a Transaction class, which models transactions between merchants and customers and CashStrategy, CreditCardStrategy, BitcoinStrategy, and PayPalStrategy classes to model different payment types for ‘transactions’
      ◦ All ‘payment strategies’ should print a simple message when they are used
      ◦  CreditCardStrategy objects must require a card number
      ◦  BitcoinStrategy objects must require an ‘address’ (a random string of letters and numbers)
      ◦  PayPalStrategy objects must require an ‘email address’
"""


class Context:
    def __init__(self):
        self.strategies = {
            "CashStrategy": CashStrategy,
            "CreditCardStrategy": CreditCardStrategy,
            "BitcoinStrategy": BitcoinStrategy,
            "PayPallStrategy": PayPallStrategy,
        }
        self.obj = None  # Strategy
        self.selectedStrategy = None

    def setStrat(self, strategy: str):
        self.obj = self.strategies[strategy]()

    def execute(self, data):
        if self.obj is None:
            raise Exception("No strategy set. Call setStrat() first.")
        return self.obj.pay(data)


# Interface
class Strategy:
    def pay(self, data):
        pass


class CashStrategy(Strategy):
    def pay(self, data):
        print(f"payed with cash. needed {data}")


class CreditCardStrategy(Strategy):
    def pay(self, data: int):
        print(f"payed with credit card. needed {data}")


class BitcoinStrategy(Strategy):
    def pay(self, data: str):
        print(f"payed with bitcoin. needed {data}")


class PayPallStrategy(Strategy):
    def pay(self, data: str):
        print(f"payed with paypall. needed {data}")


if __name__ == "__main__":
    ctx = Context()

    # Cash payment
    ctx.setStrat("CashStrategy")
    ctx.execute(100)

    # Credit card payment (card number required)
    ctx.setStrat("CreditCardStrategy")
    ctx.execute("1234-5678-9012-3456")

    # Bitcoin payment (address required)
    ctx.setStrat("BitcoinStrategy")
    ctx.execute("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")

    # PayPal payment (email required)
    ctx.setStrat("PayPallStrategy")
    ctx.execute("user@example.com")
