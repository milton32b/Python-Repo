
#  END GAME  #

def boss_fight():
    print("you've reached the boss fight")

#  DICTIONARY THAT LINKS ROOMS, REFERENCES ITEMS, AND PROVIDES DIALOGUE FOR EACH ROOM AND ITEM  #

rooms = {
  'Foyer': {
    'name': 'FOYER',
    'east': 'Living Room',
    'room_desc': "The musty smell hits you like a ton of bricks.\n"
                 "There's nothing here but an empty coat rack and a double door to the east\n"},
  'Living Room': {
    'name': 'Living Room',
    'west': 'Foyer',
    'north': 'Cellar',
    'south': 'Hallway',
    'east': 'Kitchen',
    'room_desc': "Dimly lit by an old lamp on an end table you notice the furniture is covered in plastic.\n"
                 "Nothing else but an old floor model television against the wall\n"
                 "To the North you see a door ajar, steps leading down to a cellar\n"
                 "To the South you see stairs that lead up with a door just beyond\n"
                 "To the East you see a door that swings both directions\n",
    'item': 'Badge',
    'item_desc': "In the dim light you notice a shimmer on the floor.\n",
    'item_pickup':"Your badge!\nThe suspect must have dropped it.\n"},
  'Cellar': {
    'name': 'Cellar',
    'south': 'Living Room',
    'room_desc': "It's Dark...\nand cold.\nAs you reach the last step you step on something and find yourself on "
                 "the floor,\nyour fading headache sparks back to life with a list of other aches to accompany it.\n",
    'item': 'Flashlight',
    'item_desc': "You grope the floor in the darkness seeking the culprit of your latest misfortune.\n",
    'item_pickup': "It's a Flashlight!\nYou turn it on and inspect your surroundings.\n"
                   "Nothing but a bunch of cobwebs and old boxes and the stairway leading back to the South\n"},
  'Kitchen': {
    'name': 'Kitchen',
    'west': 'Living Room',
    'north': 'Bathroom',
    'room_desc': "You're in a massive kitchen, big enough to serve half the city.\n"
                 "To the north there's a door\nThe faucet is running.\n"
                 "Not much else to note.\n",
    'item': 'Pistol',
    'item_desc': "But...\nwait...\n",
    'item_pickup': "Your police issue Pistol.\n"
                   "The suspect must have dropped it while running away.\nGood, still loaded\n"},
  'Bathroom': {
    'name': 'Bathroom',
    'south': 'Kitchen',
    'room_desc': "EEEW!!!\nIt stinks in here!\n",
    'item': 'Radio',
    'item_desc': "Before running out you notice your Radio in the toilet...\n"
                 "GROSS!!\n",
    'item_pickup': "You stick your hand in the disgusting brown water and pull out your\n"
                 "water logged Radio. Hope you don't need any backup\n"},
  'Hallway': {
    'name': 'Hallway',
    'north': 'Living Room',
    'room_desc': "Nothing to note here but three closed doors.\n"
                 "One to the East, one to the West, and one to the South\n",
    'south': 'Attic',
    'east': 'Master Bedroom',
    'west': 'Guest Bedroom'},
  'Guest Bedroom': {
    'name': 'Guest Bedroom',
    'room_desc': "A typical guest bedroom, doesn't look like anyone has stayed here in a long time\n",
    'east': 'Hallway',
    'item': 'Handcuffs',
    'item_desc': "There's a pair of handcuffs cuffed to the bedpost.\n"
                 "...\nAre those yours?\n",
    'item_pickup': "You pull the cuff key from your pocket and collect your cuffs.\n"},
  'Master Bedroom': {
    'name': 'Master Bedroom',
    'room_desc': "The Master Bedroom. Now this is where the action happens... or once happened.\n"
                 "Looks well lived in.\n",
    'west': 'Hallway',
    'item': 'Key',
    'item_desc': "A small desk lamp on the nightstand illuminates a single key.\n",
    'item_pickup': "just an old door key"},
  'Attic': {
    'name': 'Attic'}
}

# GLOBAL VARIABLES #

directions = ['north', 'south', 'east', 'west', 'quit']
current_room = rooms['Foyer']
contents = ['Badge', 'Flashlight', 'Radio', 'Handcuffs', 'Pistol', 'Key']
inventory = []

#  GAME INSTRUCTIONS  #

def instructions():
    print('\nTo move between rooms enter "North", "South", "East", and "West".\n')
    print('If there is an Item in the room enter "Yes" or "no" when prompted.\n')
    print('Enter "Quit" at any time to exit the game.\n')

#  GAME INTRO DIALOGUE  #

def prologue():
    print('\nYou are inspector Shirlee Colmbs, renowned inspector extraordinaire!\n'
          'While investigating the murder of the old widow outside of her mansion\n'
          'you are struck on the head and knocked cold!\n'
          'When you finally come to all of your police gear has been taken!\n'
          'With an awful headache you run to the front door of the mansion and barge through...\n')


# PICK UP ITEM #

def get_item():
    print(current_room['item_desc'])
    investigate = input('Would you like to investigate? ').lower()
    if 'y' in investigate:
        print(current_room['item_pickup'])
        for key, value in current_room.items():
            if value in contents:
                inventory.append(value)
        del current_room['item']


# MOVEMENT FUNCTION #

def move(direction):
    global current_room
    if direction in directions:
        print('True')
        #  IF MOVING TO ATTIC, CHECK ITEMS BEFORE BOSS_FIGHT()  #
        if current_room['name'] == 'Hallway' and direction == 'south' and 'Key' not in inventory:
            print('some dialogue about finding the key')
            return False
        elif current_room['name'] == 'Hallway' and direction == 'south' and len(inventory) != 6:
            print('Hmm... Maybe you should look for your missing items.\n')
            return False
        elif current_room['name'] == 'Hallway' and direction == 'south' and len(inventory) == 6:
            boss_fight()

        #  REGULAR MOVEMENT  #
        if direction in current_room:
            print("moving {}...".format(direction))
            current_room = rooms[current_room[direction]]
            print("")
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
        print()
        print('You are in the {}.\n'.format(current_room['name']))
        print(inventory, len(inventory))
        print(current_room['room_desc'])

        #  CHECK FOR ITEM IN CURRENT_ROOM  #
        if 'item' in current_room:
            get_item()

        # MOVEMENT #
        direction = input('\nWhat direction do you want to go? ').strip().lower()
        print('DIRECTION:', direction)

        # EXIT GAME #
        if direction.lower() in ('q', 'quit'):
            print('Thanks for playing - Bye')
            break

        # CALL THE MOVE FUNCTION #
        is_move_successful = move(direction)
        print('SUCCESSFUL MOVE:', is_move_successful)

        #if is_move_successful == True:
            #print('TRUE')
            # print(current_room)

        # BAD COMMAND #
        if direction not in directions:
            print("I don't understand that command.")


print('Welcome to the Murder Mansion Mystery Text game!')
play = input('Would you like to play? ').lower()
if 'y' in play:
    instructions()
    main()
else:
    print('So long!')



























