import time

# PRINT DELAY FUNCTION #


def print_delay(texts=[], delay=0):
    for text in texts:
        time.sleep(delay)
        print(text)

#  TEXT SEPERATOR FUNCTION  #


def seperator():
    print('_' * 70)

#  GAME INSTRUCTIONS  #


def instructions():
    print('\nTo move between rooms enter "North", "South", "East", and "West".\n')
    print('If there is an Item in the room enter "Yes" or "no" when prompted.\n')
    print('Enter "Quit" at any time to exit the game.\n')
    seperator()


#  GAME INTRO DIALOGUE  #


def prologue():
    print_delay(['\nYou are inspector Shirlee Colmbs, renowned inspector extraordinaire!\n'
                 'While investigating the murder of the old widow outside of her mansion\n'
                 'you are struck on the head and knocked cold!\n'
                 'When you finally come to all of your police gear has been taken!\n'
                 'With an awful headache you run to the front door of the mansion and barge through...\n'], 3)
    seperator()

#  END GAME  #


def boss_fight():
    seperator()
    print_delay(["Beyond the locked door there's a narrow staircase leading up to an Attic.\n"], 1)
    print_delay([], 1)
    print("Something feels...", end =" ")
    print_delay(['off...'], int(.2))
    print_delay(["You creep slowly up the stairs, Pistol gripped tightly in hand.\n"], 1)
    seperator()
    print_delay(["As soon as you reach the top of the stairs your struck from the darkness.\n"
                 "Your pistol hits the floor and goes off."], 1)
    print_delay(["Dumbstruck, def and half blind you can barely make out a silhouette backed by the \n"
                 "dim light seeping up from the hallway."], 1)
    print_delay(["The killer moves to strike again and you roll, kicking out and barely making contact.\n "
                 "The suspect, caught off guard, looses balance and falls down the narrow stairwell."], 1)
    print_delay(["Dizzy and disoriented you jump up and dive down the stairs on top of the suspect.\n"
                 "You strike the suspect over the head with your flashlight and knock him senseless."], 1)
    print_delay(["Without thinking you twist his arms behind his back and bind his hands with your cuffs."], 1)
    print_delay(["You pull out your radio, Thankfully its dried out enough to call for backup."], 1)
    print_delay(['Relieved and aching you sit at the top of the steps, \nwaiting and watching your barely conscious'
                 ' catch. \nThankfuly thats over.'], 1)
    seperator()
    print_delay(['**THE END**'], int(.5))
    return True

