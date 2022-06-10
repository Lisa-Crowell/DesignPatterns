"A dispenser of 20 bills"
from interface_dispenser import IDispenser


class Dispenser20(IDispenser):
    "Dispenses $20 if applicable, otherwise continues to the next successor"

    def __init__(self):
        self._successor = None

    def next_successor(self, successor):
        "set the next successor"
        self._successor = successor

    def handle(self, amount):
        "handle the dispensing of bills"
        if amount >= 20:
            num = amount // 20
            remainder = amount % 20
            print(f"Dispensing {num} $20 bill")
            if remainder != 0:
                self._successor.handle(remainder)
        else:
            self._successor.handle(amount)
