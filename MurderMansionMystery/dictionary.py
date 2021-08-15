
#  DICTIONARY THAT LINKS ROOMS, REFERENCES ITEMS, AND PROVIDES DIALOGUE FOR EACH ROOM AND ITEM  #

rooms = {
    'Foyer': {
        'name': 'FOYER',
        'east': 'Living Room',
        'room_desc': "The musty smell hits you like a ton of bricks.\n"
                     "There's nothing here but an empty coat rack and a double door to the EAST\n"},
    'Living Room': {
        'name': 'LIVING ROOM',
        'west': 'Foyer',
        'north': 'Cellar',
        'south': 'Hallway',
        'east': 'Kitchen',
        'room_desc': "Dimly lit by an old lamp on an end table you notice the furniture is covered in plastic.\n"
                     "Nothing else but an old floor model television against the wall.\n"
                     "To the NORTH you see a door ajar, steps leading down to a cellar.\n"
                     "To the SOUTH you see stairs that lead up with a door just beyond.\n"
                     "To the EAST you see a door that swings both directions.\n",
        'item': 'Badge',
        'item_desc': "In the dim light you notice a shimmer on the floor.\n",
        'item_pickup':"Your BADGE!\nThe suspect must have dropped it.\n"},
    'Cellar': {
        'name': 'CELLAR',
        'south': 'Living Room',
        'room_desc': "It's Dark...\nand cold.\nAs you reach the last step you step on something and find yourself on "
                     "the floor,\nyour fading headache sparks back to life with a list of other aches to accompany it.\n",
        'item': 'Flashlight',
        'item_desc': "You grope the floor in the darkness seeking the culprit of your latest misfortune.\n",
        'item_pickup': "It's a FLASHLIGHT!\nYou turn it on and inspect your surroundings.\n"
                       "Nothing but a bunch of cobwebs and old boxes and the stairway leading back to the SOUTH\n"},
    'Kitchen': {
        'name': 'KITCHEN',
        'west': 'Living Room',
        'north': 'Bathroom',
        'room_desc': "You're in a massive kitchen, big enough to serve half the city.\n"
                     "To the NORTH there's a door.\nThe faucet is running.\n"
                     "Not much else to note.\n",
        'item': 'Pistol',
        'item_desc': "But...\nwait...\n",
        'item_pickup': "Your police issue PISTOL.\n"
                       "The suspect must have dropped it while running away.\nGood, still loaded\n"},
    'Bathroom': {
        'name': 'BATHROOM',
        'south': 'Kitchen',
        'room_desc': "EEEW!!!\nIt stinks in here!\n",
        'item': 'Radio',
        'item_desc': "Before running out, you notice your RADIO in the toilet...\n"
                     "GROSS!!\n",
        'item_pickup': "You stick your hand in the disgusting brown water and pull out your\n"
                       "water logged RADIO. Hope you don't need any backup.\n"},
    'Hallway': {
        'name': 'HALLWAY',
        'north': 'Living Room',
        'room_desc': "Nothing to note here but three closed doors.\n"
                     "One to the EAST, one to the WEST, and one to the SOUTH\n",
        'south': 'Attic',
        'east': 'Master Bedroom',
        'west': 'Guest Bedroom'},
    'Guest Bedroom': {
        'name': 'GUEST BEDROOM',
        'room_desc': "A typical guest bedroom, doesn't look like anyone has stayed here in a long time.\n",
        'east': 'Hallway',
        'item': 'Handcuffs',
        'item_desc': "There's a pair of HANDCUFFS cuffed to the bedpost.\n"
                     "...\nAre those yours?\n",
        'item_pickup': "You pull the cuff key from your pocket and collect your cuffs.\n"},
    'Master Bedroom': {
        'name': 'MASTER BEDROOM',
        'room_desc': "The Master Bedroom. Now this is where the action happens... or once happened.\n"
                     "Looks well lived in.\n",
        'west': 'Hallway',
        'item': 'Key',
        'item_desc': "A small desk lamp on the nightstand illuminates a single KEY.\n",
        'item_pickup': "just an old door key"},
    'Attic': {
        'name': 'ATTIC'}
}