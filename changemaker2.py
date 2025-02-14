# Project: Change Maker
# CP12 BLK 1
# by Melodie, Sophia, Larisa 

loop = True
interactionType = 0

# Code source: https://stackoverflow.com/questions/3525953/check-if-all-values-of-iterable-are-zero
def is_number(s): #checks if something is a real number
    try:
        float(s)
        return True
    except ValueError:
        return False

def changeCheck(amount): #Checks the amount of each coin a given amount will have
    change = [0,0,0,0,0]
    coins = ["toonies", "loonies", "quarters", "dimes", "nickels"]
    coinValue = [200,100,25,10,5]
    i=0
    while i < len(change): #for every type of coin...
        change[i] = amount // coinValue[i] #Calculates the amount of a certain coin
        amount -= change[i] * coinValue[i] #substracts the value of that coin from the amount
        if change[i] > 0: #checks if coins need to be given 
            print(f"    {change[i]} {coins[i]}") 
        i+=1

def costQuestion(cost):
    global calcPrice 
    global loop
    if is_number(cost): 
        calcPrice = float(cost) * 100 #The price but written in the thousands
        return True
    elif cost.lower() == "q": #quits the program
        print("Thank you, come again!")
        loop = False
        return False
    else: 
        print("Sorry, please try again.")
        return False
    
def depositCheck(price):
    deposit = 0
    depositValues = {
        "f":500,
        "t":200,
        "l":100,
        "q":25,
        "d":10,
        "n":5,
        "c":0
    }

    print("""Menu for deposits:
        f - five dollar bill
        t- toonie
        l - loonie
        q - quarter
        d - dime
        n - nickel
        c - cancel""")

    while deposit < price: #While you still owe money
        print(f"Amount Due: {(price-deposit)/100:.2f}") 
        depositInput = input("Enter your Deposit: \n")

        if depositInput in depositValues: #checks if your input was good
            deposit += depositValues[depositInput] #adds the according amount to your deposit
            if depositInput == "c": #Gives you back your change
                print(f"Please take the change: {deposit/100}")
                changeCheck(deposit) 
                return
        else:
            print("Sorry, please try again.")
    if deposit > price:
        print(f"Please take your change: {(deposit - price)/100:.2f}")
        changeCheck(deposit - price)
    else:
        print("No change Required.")
    
def vendingMachine(): # Main Function
    global loop
    print("Welcome to the Vending Machine!")
    while loop:
        if costQuestion(input("Please input the Purchase price, or press q to quit: \n")):
            depositCheck(calcPrice)
            cont = input("Do you want to buy something else? [y/n]\n")
            if cont.lower() == "n":
                print("Okay! Enjoy!")
                loop = False


vendingMachine()