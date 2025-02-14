# MONTY HALL PROBLEM 
# Hugo, Sophia, Larisa 

import random

game = True
playtime = 0

wincount = 0
losecount = 0
switchcount = 0

switchwincount = 0
switchlosecount = 0

staywincount = 0 
staylosecount = 0

print("Welcome to the Monty Hall Problem!")
print("You will be asked to chose between three doors, behind which are two goats and one car.") 
print("After you chose, a door will open and there will be a goat behind it.") 
print("You will then be asked if you would like to switch your answer to the other door.")

while playtime<100:
    # randomizes doors
    doors = ["goat", "goat", "car"]
    random.shuffle(doors)
    #print(doors)

    indexarray = [0, 1, 2]
    pick = 0
    goatdoor = 0
    switchdoor = 0 

    #   Asks which door you choose first
    pick = random.choice(indexarray)
    print(f"The door selected was door {pick+1}")
    indexarray.remove(pick)

    # opens the door with the goat
    if doors[pick] == "car":
        goatdoor = random.choice(indexarray)
    else:
        if doors[indexarray[0]] == "goat":
            goatdoor = indexarray[0]
        else:
            goatdoor = indexarray[1]
    print(f"Door opened is {goatdoor+1}. There is a goat behind it.")
    indexarray.remove(goatdoor)

    switchdoor = indexarray[0]

    # Asks if you want to switch your door
    switch = random.randint(0,1)
    if switch == 1:
        print(f"The computer switches to door {switchdoor +1}")
        pick = switchdoor
        switchcount = switchcount + 1
    else: 
        print(f"The computer does not switch and keeps door {pick+1}")

    #   Win Condition Check
    if doors[pick] == "car":
        print("It's a win!")
        wincount = wincount + 1
        if switch == 1:
            switchwincount = switchwincount + 1
        else: 
            staywincount = staywincount+1 
    else:
        print("It's a loss")
        losecount = losecount + 1
        if switch == 1:
            switchlosecount = switchlosecount + 1
        else:
            staylosecount = staylosecount + 1
    
    print(f"The car was behind door {doors.index("car") + 1}.\n")
    playtime = playtime + 1

print("\nSTATS:")
print(f"played {playtime} times. Won {wincount} times and lost {losecount} times.")
print(f"Won {((wincount/playtime)*100):.2f}% of the time, and lost {((losecount/playtime)*100):.2f}% of the time.")

print(f"\nWins - switched: {switchwincount}")
print(f"Losses - switched: {switchlosecount}")
print(f"winning percentage: {(switchwincount/(switchwincount+switchlosecount)*100):.2f}%")

print(f"\nWins - not switched: {staywincount}")
print(f"Losses - not switched: {staylosecount}")
print(f"winning percentage: {(staywincount/(staywincount+staylosecount)*100):.2f}%")


