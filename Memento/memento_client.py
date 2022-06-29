"""Memento example use case"""


from game_character import GameCharacter
from caretaker import CareTaker


GAME_CHARACTER = GameCharacter()
CARETAKER = CareTaker(GAME_CHARACTER)

# Start the game
GAME_CHARACTER.register_kill()
GAME_CHARACTER.move_forward(1)
GAME_CHARACTER.add_inventory("sword")
GAME_CHARACTER.register_kill()
GAME_CHARACTER.add_inventory("rifle")
GAME_CHARACTER.move_forward(1)
print(GAME_CHARACTER)

# Save progress
CARETAKER.save()

GAME_CHARACTER.register_kill()
GAME_CHARACTER.move_forward(1)
GAME_CHARACTER.progress_to_next_level()
GAME_CHARACTER.register_kill()
GAME_CHARACTER.add_inventory("motorcycle")
GAME_CHARACTER.move_forward(10)
GAME_CHARACTER.register_kill()
print(GAME_CHARACTER)

# save progress
CARETAKER.save()
GAME_CHARACTER.move_forward(1)
GAME_CHARACTER.progress_to_next_level()
GAME_CHARACTER.register_kill()
print(GAME_CHARACTER)

# decide you made a mistake, go back to the first save
CARETAKER.restore(0)
print(GAME_CHARACTER)

# continue
GAME_CHARACTER.register_kill()
