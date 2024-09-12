###########################################################################################
# Name: Adam Stafford
# Date: 2023-12-8
# Description: A text adventure RPG with lore and different-styled combat throughout!
###########################################################################################


# import libraries
from time import sleep
from Room import Room
import random 
#random for boss battles, specifically Rathil.
# support for tab completion
# don't delete this!
try:
    TAB_COMPLETE = True
    import TabCompleter as TC                       # for tab completion (if available)
except ModuleNotFoundError:
    TAB_COMPLETE = False

###########################################################################################
# constants
# don't delete this!
VERBS = [ "go", "look", "take" ]                    # the supported vocabulary verbs
QUIT_COMMANDS = [ "exit", "quit", "bye" ]           # the supported quit commands

###########################################################################################
# creates the rooms
def createRooms():
    
    rooms = []
    # a list of rooms will store all of the rooms
    # r1 through r4 are the four rooms in the "mansion"
    # currentRoom is the room the player is currently in (which can be one of r1 through r4)
   
    # first, create the room instances so that they can be referenced below
    r1 = Room("Windswept Crag")
    r2 = Room("Traveler's Respite")
    r3 = Room("Icebound Oubliette")
    r4 = Room("The Rimfell Snowfields")
    r5 = Room("Harbinger's Seclude")
    r6 = Room("Warlord's Ruin, Tainted by Cold")
    r7 = Room("Warlord's Menagerie, Untouched by Time")

    # Windswept Crag
    r1.description = "A snowy precipice, burdened by an eternal winter. To the East you see a desolate lodging..."
    r1.addExit("east", r2)
    r1.addGrabbable("torch")
    r1.addItem("frozen_wayfarer", "An unfortunate soul bearing an eternal flame in this frigid world. Perhaps the torch he posseses can be used later?")
    r1.addItem("ruined_map", "Tattered and torn, the map is of no use, save for a warning on its only legible side: 'There is only death East of the Rimfell Fields'.")
    rooms.append(r1)

    # Traveler's Respite
    r2.description = "A refrain from the chill of the tundra, yet you know you can not linger. To the North you hear a screeching warcry"
    r2.addExit("west", r1)
    r2.addExit("north", r3)
#     r2.addGrabbable("enchanted_key")
    r2.addItem("grotesque_mural", "A disturbing image of a malformed knight is seen, marked with an insignia of a Warlord. You pray to never cross paths with either of them.")
    r2.addItem("frozen_pedestal", "An enchanted_key rests upon the pedestal, encased in ice. Maybe it can be melted with a fiery source?")
    rooms.append(r2)

    # Icebound Oubliette
    r3.description = "A cold dungeon, bearing a remnant of the past. You feel a frigid presence lurking among the corridors..."
    r3.addExit("south", r2)
    r3.addExit("east", r4)
    r3.addGrabbable("warlords_insignia")
    r3.addItem("ancient_cell", "An old prison cell left ajar by an abundance of sharp icicles. What could have possibly been trapped in here? Nothing inside is of value")
    rooms.append(r3)

    # The Rimfell Snowfields
    r4.description = "An unassuming plain plagued with a relentless blizzard. Vision hindered, take you next steps wisely, as they could be your last..."
    r4.addExit("south", r5)
    r4.addExit("west", r3)
    r4.addExit("east", None) # DEATH!
    r4.addItem("snowy_outpost", "Amidst the snowfall you encounter an outpost with a felled royal inside. Sheathed beside her is a sword too ornate for combat. You have no use for it, but it makes you wonder of the true nature of ruling parties in these frozen wastelands...")
    rooms.append(r4)
    
    # Harbinger's Seclude
    r5.description = "Safe from the perils of Rimfell, you stumble into a withered library. Despite its current state, you feel a wealth of knowledge lingering here among ancient texts..."
    r5.addExit("north", r4)
    r5.addExit("west", r6)
    r5.addGrabbable("candle")
    r5.addGrabbable("shadow")
    r5.addGrabbable("noise")
    r5.addItem("aged_riddles", "An unassuming children's book of riddles. You yawn as you sift through the pages, but some of the riddles' answers, like candle, shadow, and noise stand out... Maybe you should take the answers with you for your journey towards the Warlord's Ruins?")
    r5.addItem("ahamkara_scroll", "An ancient text depicting humanity barganing with Ahamkara, or Wish Dragons, for a better existence. Reading further, you discover that the treacherous Ahamkara always had a price...")
    r5.addItem("king_rathil", "A storied history of King Rathil, the Violent. Many of its pages seemed to have been intentionally burned, but the few left question the legitamacy of his rule, arguring his acquisition of the crown from knighthood happened under mystcial circumstances.")
    r5.addItem("fikrul,_beloved", "Seemingly a work of fiction, Fikrul, Beloved, details the symbiotic relationship of a King-turned-Warlord and a Wish Dragon in their quest for time itself. Almost fully intact, you notice the book's incessant mention of the dichotomy between the riddle-driven Dragon and the brutish Warlord." )
    rooms.append(r5)

    # Warlord's Ruins
    r6.description = "The remnants of battles long past linger here, revel in your victory over the brutish Warlord and deceptive Dragon. After you are satisfied, head toward the South to conclude your adventure!"
    r6.addExit("east", r5)
    r6.addExit("south", r7)
    r6.addGrabbable("ahamkara_armor")
    r6.addGrabbable("gold_coins")
    r6.addItem("ahamkara_armor", "Pieces of ahamkara_armor granted by the Wish Dragon, Fikrul. After the Ahamkara's death, it's cursed properties have ceased and is now free to claim.")
    r6.addItem("melting_banner", "A banner, unfrozen in time, depicting a now-forgotten warlord.")
    r6.addItem("treasure_trove", "Amidst the treasure trove is a plethora of gold_coins that only make sense to line your pockets!")
    rooms.append(r6)

    # Warlord's Menagerie, Untouched by Time. scrapped due to time constraints. it was just gonna be a treasure room anyway.
    r7.description = "Time seems to stand still in this trove of opulence. Not even Fikrul dared venture here... ."
#     r7.addGrabbable("")
#     r7.addItem(".")
#     r7.addItem(".")
    rooms.append(r7)
    #had to comment out most of this properties methods to get it to accept it as the good ending game over screen. stack overflow helped me realize that.
    

    # set room 1 as the current room at the beginning of the game
    currentRoom = r1
    #Sean Boyle mentioned that I could define the indivudal room classes like this to make calling them easier when I need to
    return {"r1": r1, "r2": r2, "r3": r3, "r4": r4, "r5": r5, "r6": r6, "r7": r7}, currentRoom

#simple rock papers scissors game that i imported from previous coding practice with a few tweaks for the boss fight.
def play_rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    player_score, boss_score = 0, 0
        
    while player_score < 5 and boss_score < 5:
        player_choice = input("Rathil demands audience! You must choose rock, paper, or scissors: ").lower()
        boss_choice = random.choice(choices)
        print("=" * 80)
        if player_choice not in choices:
            print("Rathil gawks at your insubordination! You must choose rock, paper, or scissors!")
            print("=" * 80)
            continue
        if player_choice == boss_choice:
            print("Rathil Grimaces...It's a tie!")
            
        elif (player_choice == "rock" and boss_choice == "scissors") or \
             (player_choice == "paper" and boss_choice == "rock") or \
             (player_choice == "scissors" and boss_choice == "paper"):
            print("Rathil screeches in defeat, but the battle is not over!")
            player_score += 1
        else:
            print("Rathil laughs at his triumph in this round!")
            boss_score += 1
            print(f" Battle Marks: You {player_score} - Rathil {boss_score}")
            print("=" * 80)
    return player_score > boss_score

#simple user inpput for desired output, rinse and repeat. style of placing riddles in {} found from CHATGPT for simplicity
def riddle_challenge():
    riddles = {
        "I'm tall when I'm young and I'm short when I'm old. What am I?": "candle",
        "I can only live where there is light, but I die if the light shines on me. What am I?": "shadow",
        "Children can make it, but never hold it or see it. What is it?": "noise"
    }

    print("Fikrul, The Ahamkara, appears before you. Seeing the Warlord's Insignia you possess, he seethes with vengeance for Rathil.")
    for riddle, answer in riddles.items():
        print("=" * 80)
        print(f"Fikrul deviously beckons you with riddles of one-word and tricky proportions: '{riddle}'")
        user_answer = input("What is your answer, human?: ").lower().strip()
        if user_answer != answer:
            print("Fikrul sneers at your incompetence and vanishes back into the shadows.")
            return False
        else:
            print("Fikrul lets out a pained grimace and moves onto the next riddle.")

    
    return True

#game over screen if you fall into the Rimfell caverns    
def game_over(reason):
    print("\n" + "=" * 80)
    print("GAME OVER")
    print(reason)
    print("Thank you for braving the winter! Try again?")
    print("=" * 80)

#     return rooms, currentRoom

###########################################################################################
# MAIN

# support for tab completion
# don't delete this!
if (TAB_COMPLETE):
    TC.parse_and_bind("tab: complete")

# START THE GAME!!!
inventory = []                      # nothing in inventory...yet
rooms, currentRoom = createRooms()  # add the rooms to the game
boss_defeated = False

# an introduction
print("Warlord's Ruin")
print("=" * 80)
print("You awake from a dreamless slumber in a frozen world...")

# play forever (well, at least until the player dies or asks to quit)
while (True):

    # set the status so the player has situational awareness
    # the status has room and inventory information
    status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)

    # if the current room is None, then the player is dead
    # this only happens if the player goes south when in room 4
    # exit the game
    if (currentRoom == None):
        #death() # you'll add this later
        break

    # support for tab completion
    # don't delete this!
    if (TAB_COMPLETE):
        # add the words to support
        words = VERBS + QUIT_COMMANDS + inventory + currentRoom.exits + currentRoom.items + currentRoom.grabbables
        # setup tab completion
        tc = TC.TabCompleter(words)
        TC.set_completer(tc.complete)

    # display the status
    print("=" * 80)
    print(status)

    # prompt for player input
    # the game supports a simple language of <verb> <noun>
    # valid verbs are go, look, and take
    # valid nouns depend on the verb
    action = input("What would you like to do? ")

    # set the user's input to lowercase to make it easier to compare the verb and noun to known values
    action = action.lower().strip()

    # exit the game if the player wants to leave (supports quit, exit, and bye)
    if (action in QUIT_COMMANDS):
        break

    # set a default response
    response = "I don't understand. Try verb noun. Valid verbs are {}.".format(", ".join(VERBS))
    # split the user input into words (words are separated by spaces) and store the words in a list
    words = action.split()

    # the game only understands two word inputs
    if (len(words) == 2):
        # isolate the verb and noun
        verb = words[0].strip()
        noun = words[1].strip()

        #go verb class was aided by Ethan Barnes, who assisted me in creating my if else statements for locked doors.
        if (verb in VERBS):
            # the verb is: go
            if (verb == "go"):
                if noun in currentRoom.exits:
                    next_room = currentRoom.exitLocations[currentRoom.exits.index(noun)]
                    #will check to see if you have the insignia in inventory, if not, will start boss battle.
                    if currentRoom.name == "Icebound Oubliette" and noun == "east":
                        
                        if "warlords_insignia" not in inventory:
                            
                            print("Rathil, First Broken Knight of Fikrul, blocks the way to the Rimfell Snowfields!")
        
                            boss_defeated = play_rock_paper_scissors()
                            if boss_defeated:
                                print("Rathil, First Broken Knight of Fikrul, collapses upon his defeat and drops the Warlord's Insignia! Even in defeat, Rathil's warcry seems to echo throughout the land eternally...")
                                inventory.append("warlords_insignia")
                                currentRoom = next_room
                            else:#if you get defeated, will send you back to previous room so you can try again
                                print("Rathil, First Broken Knight of Fikrul, has defeated you! With his insatiable lust of battle, he sends you back to Traveler's Respite in wait of another inevitable altercation..")
                                currentRoom = rooms["r2"]
                                continue
                        else:#death check for Rimfell fields, if you are in that room and choose east, you will get the bad ending game over screen
                            currentRoom = next_room
                    elif currentRoom.name == "The Rimfell Snowfields" and noun == "east":   
                        game_over("As you haphazardly venture east of the blinding Rimfell Snowfields, you realize it's a path few could ever return from. Lost, frozen, and afraid, your journey ends here...")
                        break
                    
                   #final battle, triggers upon entering room 6 and will lock you into it until you win or lose
                    elif next_room.name == "Warlord's Ruin, Tainted by Cold" and "dragons_tooth" not in inventory:
                        riddle_solved = riddle_challenge()
                        if riddle_solved:
                            print("Bested at his own game, Fikrul, with one last sneer, withers away into the wind, leaving nothing but a dragons_tooth behind")
                            inventory.append("dragons_tooth")
                            currentRoom = next_room
                          #same as with Rathil, will teleport you back to previous room if you lose. found it to be less evil than making you go all the way back :)      
                        else:
                            print("Fikrul's Ahamkara magic teleports you back to the Harbinger's Seclude, where he wishes you'd stay.")
                            currentRoom = rooms["r5"]
                            continue
                     #upon entering this room, will trigger the game over good ending. samne logic as previous boss battles.
                    elif next_room.name == "Warlord's Menagerie, Untouched by Time":
                        print("=" * 80)
                        print("Congratulations Traveler! You have braved the horrors of a world frozen by time and slayed the mighty Dragon and Warlord that reigned unchecked!")
                        print("As you bask in the Warlord's Menagerie, you understand that this is now your kingdom to rule, and rule it well")
                        print("Thanks for playing Warlord's Ruin!")
                        print("=" * 80)
                        break
                      #will check if you have item required to unlock door, otherwise you cannot progress.  
                    elif noun in currentRoom.exits:
                        if noun == "north" and currentRoom.name == "Traveler's Respite" and "enchanted_key" not in inventory:
                            response = "The Northward path is blocked by a mystical lock. Perhaps a key of magical proportions would unlock it?"       
                        else:
                            i = currentRoom.exits.index(noun)
                            currentRoom = currentRoom.exitLocations[i]
                            response = "You travel {} and encounter another area." .format(noun)
                    else:
                        currentRoom = next_room
                else:
                    response = "You can't venture in that direction"
            # the verb is: look
            elif (verb == "look"):
                
                # set a default response
                response = "You don't see that item."

                # check if the noun is a valid item
                if (noun in currentRoom.items):
                    # get its index
                    i = currentRoom.items.index(noun)
                    # set the response to the item's descriptio

                    response = currentRoom.itemDescriptions[i]
            # the verb is: take
            #condition for taking item and having its item description changed. will use this same logic for enchanted key as well.
            elif (verb == "take"):
                if noun == "torch" and "torch" in currentRoom.grabbables:
                    inventory.append("torch")
                    currentRoom.grabbables.remove("torch")
                    response = "You take the torch and feel its radiance ebb"
                    rooms["r1"].itemDescriptions[rooms["r1"].items.index("frozen_wayfarer")] = "An unfortunate soul, now without his eternal flame."
                   
                elif noun == "enchanted_key" and "frozen_pedestal" in currentRoom.items:
                    if "torch" in inventory:
                        response = "Using the torch's eternal flame, you melt the ice encasing the enchanted key and take it."
                        inventory.append("enchanted_key")
                        
                        currentRoom.itemDescriptions[currentRoom.items.index("frozen_pedestal")] = "An empty pedestal, where the enchanted key once was"
                    else:
                        response = "The enchanted key is encased in ice. You need something to melt the ice."
                elif noun in currentRoom.grabbables and noun not in inventory:
                    inventory.append(noun)
                    currentRoom.grabbables.remove(noun)
                    response = "You take {}" .format(noun)       
                else:
                    response = "You don't see that item."

                # check if the noun is a valid grabbable and is also not already in inventory
                if (noun in currentRoom.grabbables and noun not in inventory):
                    # get its index
                    i = currentRoom.grabbables.index(noun)
                    # add the grabbable item to the player's inventory
                    inventory.append(currentRoom.grabbables[i])
                    # set the response (success)
                    response = "You take {}.".format(noun)

    # display the response
    if (currentRoom != None):
        print("=" * 80)
        print(response)

