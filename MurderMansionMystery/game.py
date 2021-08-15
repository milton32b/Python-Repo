
#  IMPORTS  #

from dictionary import rooms
from utils import instructions, prologue, print_delay, seperator, boss_fight

# GLOBAL VARIABLES #


directions = ['north', 'south', 'east', 'west', 'quit']
current_room = rooms['Foyer']
contents = ['Badge', 'Flashlight', 'Radio', 'Handcuffs', 'Pistol', 'Key']
inventory = []

# PICK UP ITEM #


def get_item():
    print(' ')
    print_delay([current_room['item_desc']], 3)
    investigate = input('Would you like to investigate? \n').lower()
    if 'y' in investigate:
        #  ADD ITEM TO INVENTORY AND REMOVE FROM DICT  #
        print_delay(['\n' + current_room['item_pickup']], 1)
        for key, value in current_room.items():
            if value in contents:
                inventory.append(value)
                print('{} items in inventory:'.format(len(inventory)), ', '.join(inventory))
                seperator()
        del current_room['item']

# MOVEMENT FUNCTION #


def move(direction):
    global current_room
    if direction in directions:
        #  IF MOVING TO ATTIC, CHECK ITEMS BEFORE BOSS_FIGHT()  #
        if current_room['name'] == 'HALLWAY' and direction == 'south' and 'Key' not in inventory:
            print('This door is locked. Maybe there\'s a key somewhere.')
            return False
        elif current_room['name'] == 'HALLWAY' and direction == 'south' and len(inventory) != 6:
            print('Hmm... Maybe you should look for your missing items.\n')
            return False
        elif current_room['name'] == 'HALLWAY' and direction == 'south' and len(inventory) == 6:
            boss_fight()

        #  REGULAR MOVEMENT  #
        if direction in current_room:
            print('moving {}...\n'.format(direction))
            current_room = rooms[current_room[direction]]
            return True
        else:
            # BAD MOVEMENT, RETURN TO GAME LOOP #
            print("You can't go that way.")
    return False


# GAME LOOP #

def main():

    prologue()

    while True:

        # DISPLAY CURRENT LOCATION #
        print_delay(['You are in the {}.'.format(current_room['name'])], 2)
        print('...\n')
        print_delay([current_room['room_desc']], 2)
        seperator()

        #  CHECK FOR ITEM IN CURRENT_ROOM  #
        if 'item' in current_room:
            get_item()

        #  GET MOVEMENT  DIRECTION#
        print_delay([' '], 1)
        direction = input('\nWhat direction do you want to go? \nNORTH, SOUTH, EAST, or WEST?\n').strip().lower()

        # EXIT GAME #
        end_sequence = boss_fight()
        if end_sequence:
            break

        if direction.lower() in ('q', 'quit'):
            print('Thanks for playing - Bye')
            break

        # CALL THE MOVE FUNCTION #
        move(direction)

        # BAD COMMAND #
        if direction not in directions:
            print("I don't understand that command.")


print('Welcome to the Murder Mansion Mystery Text game!')
play = input('Would you like to play?\n').lower()
if 'y' in play:
    instructions()
    main()
else:
    print('So long!')



























