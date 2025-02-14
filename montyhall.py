# MONTY HALL PROBLEM 
# Hugo, Sophia, Larisa 

import random

game = True
wincount = 0
losecount = 0
playtime = 0
switchcount = 0
switchwincount = 0

print("Welcome to the Monty Hall Problem!")
print("You will be asked to chose between three doors, behind which are two goats and one car.") 
print("After you chose, a door will open and there will be a goat behind it.") 
print("You will then be asked if you would like to switch your answer to the other door.")

while game:
    # randomizes doors
    doors = ["goat", "goat", "car"]
    random.shuffle(doors)
    print(doors)

    indexarray = [0, 1, 2]
    pick = 0
    goatdoor = 0
    switchdoor = 0 

    #   Asks which door you choose first
    
    pick = input("\nChoose a door [1, 2, or 3]")
    pick = int(pick) - 1

    indexarray.remove(pick)
    print(indexarray)

    # opens the door with the goat
    if doors[pick] == "car":
        goatdoor = random.choice(indexarray)
    else:
        if doors[indexarray[0]] == "goat":
            goatdoor = indexarray[0]
        else:
            goatdoor = indexarray[1]
    print(f"\nI will now open door {goatdoor+1}. There is a goat behind it.")
    indexarray.remove(goatdoor)
    switchdoor = indexarray[0]

    # Asks if you want to switch your door
    switch = input(f"\nDo you want to switch your door to {switchdoor + 1}? [y/n]")
    if switch == "y":
        print(f"You will switch to door {switchdoor +1}")
        pick = switchdoor
        switchcount = switchcount + 1
    else: 
        print(f"OK, your door is {pick+1}")

    #   Win Condition Check
    if doors[pick] == "car":
        print("\nYOU WIN!!!!!!!!!!!!!!!!!!!!!!!!!")
        wincount = wincount + 1
        if switch == "y":
            switchwincount = switchwincount + 1
    else:
        print("You Lost :<")
        losecount = losecount + 1
    playtime = playtime + 1
    print(f"The car was behind door {doors.index("car") + 1}.")

    print("\nSTATS:")
    print(f"You have played {playtime} times. You have won {wincount} times and lost {losecount} times.")
    print(f"You have won {((wincount/playtime)*100):.2f}% of the time, and lost {((losecount/playtime)*100):.2f}% of the time.")
    print(f"You have switched {switchcount} times. You have won because of this {switchwincount} times.")


    x = input("\nDo you want to play again? [y/n]")
    if x == "y":
        print("Okay! Randomizing the doors...")
    else:
        print("okay! Have a good day!")
        game = False


