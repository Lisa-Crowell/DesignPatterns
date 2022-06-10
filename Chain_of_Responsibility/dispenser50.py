"A dispenser of 50 bills"
from interface_dispenser import IDispenser


class Dispenser50(IDispenser):
    "Dispenses $50 if applicable, otherwise continues to the next successor"

    def __init__(self):
        self._successor = None

    def next_successor(self, successor):
        "set the next successor"
        self._successor = successor

    def handle(self, amount):
        "handle the dispensing of bills"
        if amount >= 50:
            num = amount // 50
            remainder = amount % 50
            print(f"Dispensing {num} $50 bill")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)
