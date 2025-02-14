# Read the dollar amount
# seperate into change

import math
vending = True

def changeCheck(amount):
    change = [0,0,0,0,0]
    #toonies
    change[0] = amount // 200
    amount -= change[0]*200

    #Loonies
    change[1] = amount // 100
    amount -= change[1] *100
    
    change[2] = amount // 25
    amount -= change[2] * 25

    change[3] = amount // 10
    amount -= change[3] * 10

    change[4] = amount // 5
    amount -= change[4] * 5
    if all([ x==0 for x in change]):
            print("No Change!")
    else:
        i=0 
        while i < len(change):
            #print(i)
            if change[i] != 0:
                if i == 0:
                    print(f"{change[0]} toonies")
                elif i == 1:
                    print(f"{change[1]} loonies")
                elif i == 2:
                    print(f"{change[2]} quarters")
                elif i == 3:
                    print(f"{change[3]} dimes")
                elif i == 4:
                    print(f"{change[4]} nickels")
            i+=1
    return change

def purchasePriceCheck():
    global purchasePrice
    global priceTrue
    global amount
    global vending
    
    purchasePrice = 1
    amount = 0
    priceTrue = 0

    while purchasePrice % 5 != 0:
        purchasePrice = input("Please input the purchase price, or press q to quit")
        priceTrue = purchasePrice
        if purchasePrice == "q":
            vending = False
            return
        else: 
            amount = purchasePrice
            purchasePrice = float(purchasePrice) * 100
            if purchasePrice % 5 != 0:
                print("Unfortunately that is not an acceptable number, please try again")
            else: 
                return

while vending:
    amount = 1
    purchasePrice = 1
    deposits = 0 


    print("Welcome to the vending machine!")
    purchasePriceCheck()

    if vending:
        print("Menu for Deposits:")
        print("f - five dollar bill")
        while deposits < purchasePrice:
            print(f"Amount Due: {amount}")
            depositEntered = input("Enter your Deposit")
            if depositEntered == "f":
                deposits += 500
                amount = (purchasePrice - deposits)/100
            elif depositEntered == "t":
                deposits += 200
                amount = (purchasePrice - deposits)/100
            elif depositEntered == "l":
                deposits += 100
                amount = (purchasePrice - deposits)/100
            elif depositEntered == "q":
                deposits += 25
                amount = (purchasePrice - deposits)/100
            elif depositEntered == "d":
                deposits += 10
                amount = (purchasePrice - deposits)/100
            elif depositEntered == "n":
                deposits += 5
                amount = (purchasePrice - deposits)/100
            elif depositEntered == "c":
                change = changeCheck(deposits)
                print(change)
                vending = False
        remainder = deposits - purchasePrice
        change = remainder
            
                #Get your money back
            

    '''while amount % 5 != 0: #checks if it is divisible by 5
        amount = input("Enter Dollar Amount: ")
        if amount % 5 != 0:
            print("That's not an acceptable number, please try again")
        else:
            price = float(amount) # price is the original value
            amount = float(amount)*100'''
        
    # Change Checker
    

    #quarters = math.round(amount / 0.25)

    #print(f"{toonies}, {loonies}, {quarters}, {dimes}, {nickels}")

