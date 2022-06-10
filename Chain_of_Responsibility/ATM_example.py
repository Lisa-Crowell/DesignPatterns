#!/usr/bin/env python

import sys
from atm_dispenser_chain import ATMDispenserChain

"An ATM Dispenser that dispenses denomination of bills"

ATM = ATMDispenserChain()
AMOUNT = int(input('Enter amount to withdraw: '))
if AMOUNT < 10 or AMOUNT % 10 != 0:
    print("Amount should be in multiples of 10's.")
    sys.exit()
#process the request
ATM.chain1.handle(AMOUNT)
print("Have a wonderful day!")
