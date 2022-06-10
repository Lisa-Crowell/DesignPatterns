from dispenser10 import Dispenser10
from dispenser20 import Dispenser20
from dispenser50 import Dispenser50

class ATMDispenserChain:
    "The Chain Client"
    def __init__(self):
        #initializing the successors chain
        self.chain1 = Dispenser50()
        self.chain2 = Dispenser20()
        self.chain3 = Dispenser10()
        #setting a default successor chain that will process 50'2 first, then 20's, then 10'2
        #the successor chain will be recalculated dynamically at runtime.
        self.chain1.next_successor(self.chain2)
        self.chain2.next_successor(self.chain3)

