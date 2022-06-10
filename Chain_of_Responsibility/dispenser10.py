"A dispenser of 10 bills"
from interface_dispenser import IDispenser


class Dispenser10(IDispenser):
    "Dispenses $10 if applicable, otherwise continues to the next successor"

    def __init__(self):
        self._successor = None

    def next_successor(self, successor):
        "set the next successor"
        self._successor = successor

    def handle(self, amount):
        "handle the dispensing of bills"
        if amount >= 10:
            num = amount // 10
            remainder = amount % 10
            print(f"Dispensing {num} $10 bill")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)
