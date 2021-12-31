import os
print("Welcome to Monopoly Digital Banking")

#set the banker PIN
print("Please set a banker PIN")
bankerPin = input("PIN>")

#a simple function that waits for the user to press enter
def wait():
    notImportantVariable = input(" ")

#player setup
print("How many players are there? (Limit 8, you will have to start a new instance of the applacation for more)")#Limited players due to how transaction functions and player setup works. To commiters: Please try to fix this.
playerCount = input(">")
playerCount = int(playerCount)
print("Please fill out the required information for each player")
wait()
os.system("cls") #this line will be used to clear the console

#setup players
if(playerCount == 8):
    name = input("Name>")
    os.system("cls")
    print("Please give the device to "+name)
    wait()
    pin = input("PIN>")
    os.system("cls")
    print("Please give device to the banker")
    wait()
    player8 = [name,pin,1500]
    playerCount = playerCount -1
if(playerCount == 7):
    name = input("Name>")
    os.system("cls")
    print("Please give the device to "+name)
    wait()
    pin = input("PIN>")
    os.system("cls")
    print("Please give device to the banker")
    wait()
    player7 = [name,pin,1500]
    playerCount = playerCount -1
if(playerCount == 6):
    name = input("Name>")
    os.system("cls")
    print("Please give the device to "+name)
    wait()
    pin = input("PIN>")
    os.system("cls")
    print("Please give device to the banker")
    wait()
    player6 = [name,pin,1500]
    playerCount = playerCount -1
if(playerCount == 5):
    name = input("Name>")
    os.system("cls")
    print("Please give the device to "+name)
    wait()
    pin = input("PIN>")
    os.system("cls")
    print("Please give device to the banker")
    wait()
    player5 = [name,pin,1500]
    playerCount = playerCount -1
if(playerCount == 4):
    name = input("Name>")
    os.system("cls")
    print("Please give the device to "+name)
    wait()
    pin = input("PIN>")
    os.system("cls")
    print("Please give device to the banker")
    wait()
    player4 = [name,pin,1500]
    playerCount = playerCount -1
if(playerCount == 3):
    name = input("Name>")
    os.system("cls")
    print("Please give the device to "+name)
    wait()
    pin = input("PIN>")
    os.system("cls")
    print("Please give device to the banker")
    wait()
    player3 = [name,pin,1500]
    playerCount = playerCount -1
if(playerCount == 2):
    name = input("Name>")
    os.system("cls")
    print("Please give the device to "+name)
    wait()
    pin = input("PIN>")
    os.system("cls")
    print("Please give device to the banker")
    wait()
    player2 = [name,pin,1500]
    playerCount = playerCount -1
if(playerCount == 1):
    name = input("Name>")
    os.system("cls")
    print("Please give the device to "+name)
    wait()
    pin = input("PIN>")
    os.system("cls")
    print("Please give device to the banker")
    wait()
    player1 = [name,pin,1500]
    playerCount = playerCount -1


#transactions
def playerToBank():
    print("What is the players name?")
    name = input(">")
    if(player8[0] == name):
        print("How much does the transaction cost?")
        price = input("$")
        price = int(price)
        balanceAfter = player8[2] - price
        if(balanceAfter >= 0):
            print(name+" would like to make a purchase for $"+price+". "+name+"has enough money to make this purchase. Please validate it with the bankers PIN. Press enter without entering your PIN to cancel the payment.")
            userInput = input("PIN>")
            if(userInput == bankerPin):
                os.system("ctl")
                print("Please pass the device to "+name)
                wait()
                print("Would you like to make a purchase of $"+price+"? Your balance afterward will be $"+balanceAfter+". Please validate the purchase with your PIN. Press enter without entering your PIN to cancel the payment.")
                userInput = input("PIN>")
                if(userInput == player8[1]):
                    player8[1] = player8[1]-price
                    print("PAYMENT COMPLETE!\nPlease pass the device back to the banker.")
                    wait()
                    os.system("ctl")
                else:
                    print("The PIN was incorrect or payment was canceled. If this is an accident, have the banker retry the purchase,\notherwise pass the device back to the banker")
                    wait()
                    os.system("ctl")
            else:
                print("The PIN was incorrect or payment was canceled. If this is an accident, have the banker retry the purchase,\notherwise pass the device back to the banker")
                wait()
                os.system("ctl")
    if(player7[0] == name):
        print("How much does the transaction cost?")
        price = input("$")
        price = int(price)
        balanceAfter = player7[2] - price
        if(balanceAfter >= 0):
            print(name+" would like to make a purchase for $"+price+". "+name+"has enough money to make this purchase. Please validate it with the bankers PIN. Press enter without entering your PIN to cancel the payment.")
            userInput = input("PIN>")
            if(userInput == bankerPin):
                os.system("ctl")
                print("Please pass the device to "+name)
                wait()
                print("Would you like to make a purchase of $"+price+"? Your balance afterward will be $"+balanceAfter+". Please validate the purchase with your PIN. Press enter without entering your PIN to cancel the payment.")
                userInput = input("PIN>")
                if(userInput == player7[1]):
                    player7[1] = player7[1]-price
                    print("PAYMENT COMPLETE!\nPlease pass the device back to the banker.")
                    wait()
                    os.system("ctl")
                else:
                    print("The PIN was incorrect or payment was canceled. If this is an accident, have the banker retry the purchase,\notherwise pass the device back to the banker")
                    wait()
                    os.system("ctl")
            else:
                print("The PIN was incorrect or payment was canceled. If this is an accident, have the banker retry the purchase,\notherwise pass the device back to the banker")
                wait()
                os.system("ctl")
    if(player6[0] == name):
        print("How much does the transaction cost?")
        price = input("$")
        price = int(price)
        balanceAfter = player6[2] - price
        if(balanceAfter >= 0):
            print(name+" would like to make a purchase for $"+price+". "+name+"has enough money to make this purchase. Please validate it with the bankers PIN. Press enter without entering your PIN to cancel the payment.")
            userInput = input("PIN>")
            if(userInput == bankerPin):
                os.system("ctl")
                print("Please pass the device to "+name)
                wait()
                print("Would you like to make a purchase of $"+price+"? Your balance afterward will be $"+balanceAfter+". Please validate the purchase with your PIN. Press enter without entering your PIN to cancel the payment.")
                userInput = input("PIN>")
                if(userInput == player6[1]):
                    player8[1] = player6[1]-price
                    print("PAYMENT COMPLETE!\nPlease pass the device back to the banker.")
                    wait()
                    os.system("ctl")
                else:
                    print("The PIN was incorrect or payment was canceled. If this is an accident, have the banker retry the purchase,\notherwise pass the device back to the banker")
                    wait()
                    os.system("ctl")
            else:
                print("The PIN was incorrect or payment was canceled. If this is an accident, have the banker retry the purchase,\notherwise pass the device back to the banker")
                wait()
                os.system("ctl")
    if(player5[0] == name):
        print("How much does the transaction cost?")
        price = input("$")
        price = int(price)
        balanceAfter = player5[2] - price
        if(balanceAfter >= 0):
            print(name+" would like to make a purchase for $"+price+". "+name+"has enough money to make this purchase. Please validate it with the bankers PIN. Press enter without entering your PIN to cancel the payment.")
            userInput = input("PIN>")
            if(userInput == bankerPin):
                os.system("ctl")
                print("Please pass the device to "+name)
                wait()
                print("Would you like to make a purchase of $"+price+"? Your balance afterward will be $"+balanceAfter+". Please validate the purchase with your PIN. Press enter without entering your PIN to cancel the payment.")
                userInput = input("PIN>")
                if(userInput == player5[1]):
                    player5[1] = player5[1]-price
                    print("PAYMENT COMPLETE!\nPlease pass the device back to the banker.")
                    wait()
                    os.system("ctl")
                else:
                    print("The PIN was incorrect or payment was canceled. If this is an accident, have the banker retry the purchase,\notherwise pass the device back to the banker")
                    wait()
                    os.system("ctl")
            else:
                print("The PIN was incorrect or payment was canceled. If this is an accident, have the banker retry the purchase,\notherwise pass the device back to the banker")
                wait()
                os.system("ctl")
    if(player4[0] == name):
        print("How much does the transaction cost?")
        price = input("$")
        price = int(price)
        balanceAfter = player4[2] - price
        if(balanceAfter >= 0):
            print(name+" would like to make a purchase for $"+price+". "+name+"has enough money to make this purchase. Please validate it with the bankers PIN. Press enter without entering your PIN to cancel the payment.")
            userInput = input("PIN>")
            if(userInput == bankerPin):
                os.system("ctl")
                print("Please pass the device to "+name)
                wait()
                print("Would you like to make a purchase of $"+price+"? Your balance afterward will be $"+balanceAfter+". Please validate the purchase with your PIN. Press enter without entering your PIN to cancel the payment.")
                userInput = input("PIN>")
                if(userInput == player4[1]):
                    player4[1] = player4[1]-price
                    print("PAYMENT COMPLETE!\nPlease pass the device back to the banker.")
                    wait()
                    os.system("ctl")
                else:
                    print("The PIN was incorrect or payment was canceled. If this is an accident, have the banker retry the purchase,\notherwise pass the device back to the banker")
                    wait()
                    os.system("ctl")
            else:
                print("The PIN was incorrect or payment was canceled. If this is an accident, have the banker retry the purchase,\notherwise pass the device back to the banker")
                wait()
                os.system("ctl")
    if(player3[0] == name):
        print("How much does the transaction cost?")
        price = input("$")
        price = int(price)
        balanceAfter = player3[2] - price
        if(balanceAfter >= 0):
            print(name+" would like to make a purchase for $"+price+". "+name+"has enough money to make this purchase. Please validate it with the bankers PIN. Press enter without entering your PIN to cancel the payment.")
            userInput = input("PIN>")
            if(userInput == bankerPin):
                os.system("ctl")
                print("Please pass the device to "+name)
                wait()
                print("Would you like to make a purchase of $"+price+"? Your balance afterward will be $"+balanceAfter+". Please validate the purchase with your PIN. Press enter without entering your PIN to cancel the payment.")
                userInput = input("PIN>")
                if(userInput == player3[1]):
                    player3[1] = player3[1]-price
                    print("PAYMENT COMPLETE!\nPlease pass the device back to the banker.")
                    wait()
                    os.system("ctl")
                else:
                    print("The PIN was incorrect or payment was canceled. If this is an accident, have the banker retry the purchase,\notherwise pass the device back to the banker")
                    wait()
                    os.system("ctl")
            else:
                print("The PIN was incorrect or payment was canceled. If this is an accident, have the banker retry the purchase,\notherwise pass the device back to the banker")
                wait()
                os.system("ctl")
    if(player2[0] == name):
        print("How much does the transaction cost?")
        price = input("$")
        price = int(price)
        balanceAfter = player2[2] - price
        if(balanceAfter >= 0):
            print(name+" would like to make a purchase for $"+price+". "+name+"has enough money to make this purchase. Please validate it with the bankers PIN. Press enter without entering your PIN to cancel the payment.")
            userInput = input("PIN>")
            if(userInput == bankerPin):
                os.system("ctl")
                print("Please pass the device to "+name)
                wait()
                print("Would you like to make a purchase of $"+price+"? Your balance afterward will be $"+balanceAfter+". Please validate the purchase with your PIN. Press enter without entering your PIN to cancel the payment.")
                userInput = input("PIN>")
                if(userInput == player2[1]):
                    player2[1] = player2[1]-price
                    print("PAYMENT COMPLETE!\nPlease pass the device back to the banker.")
                    wait()
                    os.system("ctl")
                else:
                    print("The PIN was incorrect or payment was canceled. If this is an accident, have the banker retry the purchase,\notherwise pass the device back to the banker")
                    wait()
                    os.system("ctl")
            else:
                print("The PIN was incorrect or payment was canceled. If this is an accident, have the banker retry the purchase,\notherwise pass the device back to the banker")
                wait()
                os.system("ctl")
    if(player1[0] == name):
        print("How much does the transaction cost?")
        price = input("$")
        price = int(price)
        balanceAfter = player1[2] - price
        if(balanceAfter >= 0):
            print(name+" would like to make a purchase for $"+price+". "+name+"has enough money to make this purchase. Please validate it with the bankers PIN. Press enter without entering your PIN to cancel the payment.")
            userInput = input("PIN>")
            if(userInput == bankerPin):
                os.system("ctl")
                print("Please pass the device to "+name)
                wait()
                print("Would you like to make a purchase of $"+price+"? Your balance afterward will be $"+balanceAfter+". Please validate the purchase with your PIN. Press enter without entering your PIN to cancel the payment.")
                userInput = input("PIN>")
                if(userInput == player1[1]):
                    player1[1] = player1[1]-price
                    print("PAYMENT COMPLETE!\nPlease pass the device back to the banker.")
                    wait()
                    os.system("ctl")
                else:
                    print("The PIN was incorrect or payment was canceled. If this is an accident, have the banker retry the purchase,\notherwise pass the device back to the banker")
                    wait()
                    os.system("ctl")
            else:
                print("The PIN was incorrect or payment was canceled. If this is an accident, have the banker retry the purchase,\notherwise pass the device back to the banker")
                wait()
                os.system("ctl")
def playerToPlayer():
    print("To ensure that player to player transactions are allowed in this game, please enter the banker PIN")
    userInput = input("PIN>")
    if(userInput == bankerPin):
        print("What is the senders name?")
        senderName = input(">")
        print("What is the recievers name?")
        recieverName = input(">")
        if(senderName == player8[0]):
            if(recieverName == player7[0]):
                os.system("ctl")
                print("Please give the device to "+player8[0])
                wait()
                print("How much would you like to send?")
                ammount = input("$")
                ammount = int(ammount)
                balanceAfter = player8[2] - ammount
                print(player8[0]+", would you like to give"+player7[0]+" $"+ammount+"? Your balance after will be $"+balanceAfter+". Validate by entering your PIN. Press enter to cancel.")
                userInput = input("PIN>")
                if(player8[1] == userInput):
                    player8[2] = balanceAfter
                    player7[2] = player7[2] + ammount
                    print("TRANSACTION COMPLETE")
                    print("Please give the device back to the banker.")
                    wait()
                    os.system("ctl")
            if(recieverName == player6[0]):
                os.system("ctl")
                print("Please give the device to "+player8[0])
                wait()
                print("How much would you like to send?")
                ammount = input("$")
                ammount = int(ammount)
                balanceAfter = player8[2] - ammount
                print(player8[0]+", would you like to give"+player6[0]+" $"+ammount+"? Your balance after will be $"+balanceAfter+". Validate by entering your PIN. Press enter to cancel.")
                userInput = input("PIN>")
                if(player8[1] == userInput):
                    player8[2] = balanceAfter
                    player6[2] = player6[2] + ammount
                    print("TRANSACTION COMPLETE")
                    print("Please give the device back to the banker.")
                    wait()
                    os.system("ctl")
            if(recieverName == player5[0]):
                os.system("ctl")
                print("Please give the device to "+player8[0])
                wait()
                print("How much would you like to send?")
                ammount = input("$")
                ammount = int(ammount)
                balanceAfter = player8[2] - ammount
                print(player8[0]+", would you like to give"+player5[0]+" $"+ammount+"? Your balance after will be $"+balanceAfter+". Validate by entering your PIN. Press enter to cancel.")
                userInput = input("PIN>")
                if(player8[1] == userInput):
                    player8[2] = balanceAfter
                    player5[2] = player5[2] + ammount
                    print("TRANSACTION COMPLETE")
                    print("Please give the device back to the banker.")
                    wait()
                    os.system("ctl")
            if(recieverName == player4[0]):
                os.system("ctl")
                print("Please give the device to "+player8[0])
                wait()
                print("How much would you like to send?")
                ammount = input("$")
                ammount = int(ammount)
                balanceAfter = player8[2] - ammount
                print(player8[0]+", would you like to give"+player4[0]+" $"+ammount+"? Your balance after will be $"+balanceAfter+". Validate by entering your PIN. Press enter to cancel.")
                userInput = input("PIN>")
                if(player8[1] == userInput):
                    player8[2] = balanceAfter
                    player4[2] = player4[2] + ammount
                    print("TRANSACTION COMPLETE")
                    print("Please give the device back to the banker.")
                    wait()
                    os.system("ctl")
            if(recieverName == player3[0]):
                os.system("ctl")
                print("Please give the device to "+player8[0])
                wait()
                print("How much would you like to send?")
                ammount = input("$")
                ammount = int(ammount)
                balanceAfter = player8[2] - ammount
                print(player8[0]+", would you like to give"+player3[0]+" $"+ammount+"? Your balance after will be $"+balanceAfter+". Validate by entering your PIN. Press enter to cancel.")
                userInput = input("PIN>")
                if(player8[1] == userInput):
                    player8[2] = balanceAfter
                    player3[2] = player3[2] + ammount
                    print("TRANSACTION COMPLETE")
                    print("Please give the device back to the banker.")
                    wait()
                    os.system("ctl")
            if(recieverName == player2[0]):
                os.system("ctl")
                print("Please give the device to "+player8[0])
                wait()
                print("How much would you like to send?")
                ammount = input("$")
                ammount = int(ammount)
                balanceAfter = player8[2] - ammount
                print(player8[0]+", would you like to give"+player2[0]+" $"+ammount+"? Your balance after will be $"+balanceAfter+". Validate by entering your PIN. Press enter to cancel.")
                userInput = input("PIN>")
                if(player8[1] == userInput):
                    player8[2] = balanceAfter
                    player2[2] = player2[2] + ammount
                    print("TRANSACTION COMPLETE")
                    print("Please give the device back to the banker.")
                    wait()
                    os.system("ctl")
            if(recieverName == player1[0]):
                os.system("ctl")
                print("Please give the device to "+player8[0])
                wait()
                print("How much would you like to send?")
                ammount = input("$")
                ammount = int(ammount)
                balanceAfter = player8[2] - ammount
                print(player8[0]+", would you like to give"+player1[0]+" $"+ammount+"? Your balance after will be $"+balanceAfter+". Validate by entering your PIN. Press enter to cancel.")
                userInput = input("PIN>")
                if(player8[1] == userInput):
                    player8[2] = balanceAfter
                    player1[2] = player1[2] + ammount
                    print("TRANSACTION COMPLETE")
                    print("Please give the device back to the banker.")
                    wait()
                    os.system("ctl")      
        if(senderName == player7[0]):
            if(recieverName == player8[0]):
                os.system("ctl")
                print("Please give the device to "+player7+[0])
                wait()
                print("How much would you like to send?")
                ammount = input("$")
                ammount = int(ammount)
                balanceAfter = player7[2] - ammount
                print(player7[0]+", would you like to give"+player8[0]+" $"+ammount+"? Your balance after will be $"+balanceAfter+". Validate by entering your PIN. Press enter to cancel.")
                userInput = input("PIN>")
                if(player7[1] == userInput):
                    player7[2] = balanceAfter
                    player8[2] = player7[2] + ammount
                    print("TRANSACTION COMPLETE")
                    print("Please give the device back to the banker.")
                    wait()
                    os.system("ctl")
            if(recieverName == player6[0]):
                os.system("ctl")
                print("Please give the device to "+player7[0])
                wait()
                print("How much would you like to send?")
                ammount = input("$")
                ammount = int(ammount)
                balanceAfter = player7[2] - ammount
                print(player7[0]+", would you like to give"+player6[0]+" $"+ammount+"? Your balance after will be $"+balanceAfter+". Validate by entering your PIN. Press enter to cancel.")
                userInput = input("PIN>")
                if(player7[1] == userInput):
                    player7[2] = balanceAfter
                    player6[2] = player6[2] + ammount
                    print("TRANSACTION COMPLETE")
                    print("Please give the device back to the banker.")
                    wait()
                    os.system("ctl")
            if(recieverName == player5[0]):
                os.system("ctl")
                print("Please give the device to "+player7[0])
                wait()
                print("How much would you like to send?")
                ammount = input("$")
                ammount = int(ammount)
                balanceAfter = player7[2] - ammount
                print(player7[0]+", would you like to give"+player5[0]+" $"+ammount+"? Your balance after will be $"+balanceAfter+". Validate by entering your PIN. Press enter to cancel.")
                userInput = input("PIN>")
                if(player7[1] == userInput):
                    player7[2] = balanceAfter
                    player7[2] = player5[2] + ammount
                    print("TRANSACTION COMPLETE")
                    print("Please give the device back to the banker.")
                    wait()
                    os.system("ctl")
            if(recieverName == player7[0]):
                os.system("ctl")
                print("Please give the device to "+player8[0])
                wait()
                print("How much would you like to send?")
                ammount = input("$")
                ammount = int(ammount)
                balanceAfter = player7[2] - ammount
                print(player7[0]+", would you like to give"+player4[0]+" $"+ammount+"? Your balance after will be $"+balanceAfter+". Validate by entering your PIN. Press enter to cancel.")
                userInput = input("PIN>")
                if(player7[1] == userInput):
                    player7[2] = balanceAfter
                    player4[2] = player4[2] + ammount
                    print("TRANSACTION COMPLETE")
                    print("Please give the device back to the banker.")
                    wait()
                    os.system("ctl")
            if(recieverName == player3[0]):
                os.system("ctl")
                print("Please give the device to "+player8[0])
                wait()
                print("How much would you like to send?")
                ammount = input("$")
                ammount = int(ammount)
                balanceAfter = player7[2] - ammount
                print(player7[0]+", would you like to give"+player3[0]+" $"+ammount+"? Your balance after will be $"+balanceAfter+". Validate by entering your PIN. Press enter to cancel.")
                userInput = input("PIN>")
                if(player7[1] == userInput):
                    player7[2] = balanceAfter
                    player3[2] = player3[2] + ammount
                    print("TRANSACTION COMPLETE")
                    print("Please give the device back to the banker.")
                    wait()
                    os.system("ctl")
            if(recieverName == player2[0]):
                os.system("ctl")
                print("Please give the device to "+player7[0])
                wait()
                print("How much would you like to send?")
                ammount = input("$")
                ammount = int(ammount)
                balanceAfter = player7[2] - ammount
                print(player7[0]+", would you like to give"+player2[0]+" $"+ammount+"? Your balance after will be $"+balanceAfter+". Validate by entering your PIN. Press enter to cancel.")
                userInput = input("PIN>")
                if(player7[1] == userInput):
                    player7[2] = balanceAfter
                    player2[2] = player2[2] + ammount
                    print("TRANSACTION COMPLETE")
                    print("Please give the device back to the banker.")
                    wait()
                    os.system("ctl")
            if(recieverName == player1[0]):
                os.system("ctl")
                print("Please give the device to "+player7[0])
                wait()
                print("How much would you like to send?")
                ammount = input("$")
                ammount = int(ammount)
                balanceAfter = player7[2] - ammount
                print(player7[0]+", would you like to give"+player1[0]+" $"+ammount+"? Your balance after will be $"+balanceAfter+". Validate by entering your PIN. Press enter to cancel.")
                userInput = input("PIN>")
                if(player7[1] == userInput):
                    player7[2] = balanceAfter
                    player1[2] = player1[2] + ammount
                    print("TRANSACTION COMPLETE")
                    print("Please give the device back to the banker.")
                    wait()
                    os.system("ctl")
    else:
        print("Incorect PIN or player to player transactions aren't allowed in this game")
        wait()
        os.system("ctl")
def bankToPlayer():
    print("What is the players name?")
    name = input(">")
    if(player8[0] == name):
        print("How much money is the player getting?")
        money = input("$")
        money = int(money)
        print("Would you like to give "+name+" $"+money+"? Validate with the banker PIN. Press enter without typing the PIN to cancel the transaction.")
        userInput = input("PIN>")
        if(bankerPin == userInput):
            player8[2] = player8[2] + money
            print("TRANSACTION COMPLETE")
            wait()
            os.system("cts")
        else:
            print("The PIN was incorrect or payment was canceled. If this is an accident, retry the purchase.")
            wait()
            os.system("ctl")
    if(player7[0] == name):
        print("How much money is the player getting?")
        money = input("$")
        money = int(money)
        print("Would you like to give "+name+" $"+money+"? Validate with the banker PIN. Press enter without typing the PIN to cancel the transaction.")
        userInput = input("PIN>")
        if(bankerPin == userInput):
            player7[2] = player7[2] + money
            print("TRANSACTION COMPLETE")
            wait()
            os.system("cts")
        else:
            print("The PIN was incorrect or payment was canceled. If this is an accident, retry the purchase.")
            wait()
            os.system("ctl")
    if(player6[0] == name):
        print("How much money is the player getting?")
        money = input("$")
        money = int(money)
        print("Would you like to give "+name+" $"+money+"? Validate with the banker PIN. Press enter without typing the PIN to cancel the transaction.")
        userInput = input("PIN>")
        if(bankerPin == userInput):
            player6[2] = player6[2] + money
            print("TRANSACTION COMPLETE")
            wait()
            os.system("cts")
        else:
            print("The PIN was incorrect or payment was canceled. If this is an accident, retry the purchase.")
            wait()
            os.system("ctl")
    if(player5[0] == name):
        print("How much money is the player getting?")
        money = input("$")
        money = int(money)
        print("Would you like to give "+name+" $"+money+"? Validate with the banker PIN. Press enter without typing the PIN to cancel the transaction.")
        userInput = input("PIN>")
        if(bankerPin == userInput):
            player5[2] = player5[2] + money
            print("TRANSACTION COMPLETE")
            wait()
            os.system("cts")
        else:
            print("The PIN was incorrect or payment was canceled. If this is an accident, retry the purchase.")
            wait()
            os.system("ctl")
    if(player4[0] == name):
        print("How much money is the player getting?")
        money = input("$")
        money = int(money)
        print("Would you like to give "+name+" $"+money+"? Validate with the banker PIN. Press enter without typing the PIN to cancel the transaction.")
        userInput = input("PIN>")
        if(bankerPin == userInput):
            player4[2] = player4[2] + money
            print("TRANSACTION COMPLETE")
            wait()
            os.system("cts")
        else:
            print("The PIN was incorrect or payment was canceled. If this is an accident, retry the purchase.")
            wait()
            os.system("ctl")
    if(player3[0] == name):
        print("How much money is the player getting?")
        money = input("$")
        money = int(money)
        print("Would you like to give "+name+" $"+money+"? Validate with the banker PIN. Press enter without typing the PIN to cancel the transaction.")
        userInput = input("PIN>")
        if(bankerPin == userInput):
            player3[2] = player3[2] + money
            print("TRANSACTION COMPLETE")
            wait()
            os.system("cts")
        else:
            print("The PIN was incorrect or payment was canceled. If this is an accident, retry the purchase.")
            wait()
            os.system("ctl")
    if(player2[0] == name):
        print("How much money is the player getting?")
        money = input("$")
        money = int(money)
        print("Would you like to give "+name+" $"+money+"? Validate with the banker PIN. Press enter without typing the PIN to cancel the transaction.")
        userInput = input("PIN>")
        if(bankerPin == userInput):
            player2[2] = player2[2] + money
            print("TRANSACTION COMPLETE")
            wait()
            os.system("cts")
        else:
            print("The PIN was incorrect or payment was canceled. If this is an accident, retry the purchase.")
            wait()
            os.system("ctl")
    if(player1[0] == name):
        print("How much money is the player getting?")
        money = input("$")
        money = int(money)
        print("Would you like to give "+name+" $"+money+"? Validate with the banker PIN. Press enter without typing the PIN to cancel the transaction.")
        userInput = input("PIN>")
        if(bankerPin == userInput):
            player1[2] = player1[2] + money
            print("TRANSACTION COMPLETE")
            wait()
            os.system("cts")
        else:
            print("The PIN was incorrect or payment was canceled. If this is an accident, retry the purchase.")
            wait()
            os.system("ctl")
def checkBalance():
    print("Please enter your name")
    name = input(">")
    if(player8[0] == name):
        print("What is your PIN?")
        userInput = input(">")
        if(userInput == player8[1]):
            print("Hello, "+name+"\nYour balance is "+player8[2]+".\nYour PIN is "+player8[1])
            wait()
            os.system("ctl")
        else:
            print("Incorrect PIN")
            wait()
            os.system("ctl")
    if(player7[0] == name):
        print("What is your PIN?")
        userInput = input(">")
        if(userInput == player7[1]):
            print("Hello, "+name+"\nYour balance is "+player7[2]+".\nYour PIN is "+player7[1])
            wait()
            os.system("ctl")
        else:
            print("Incorrect PIN")
            wait()
            os.system("ctl")
    if(player6[0] == name):
        print("What is your PIN?")
        userInput = input(">")
        if(userInput == player6[1]):
            print("Hello, "+name+"\nYour balance is "+player6[2]+".\nYour PIN is "+player6[1])
            wait()
            os.system("ctl")
        else:
            print("Incorrect PIN")
            wait()
            os.system("ctl")
    if(player5[0] == name):
        print("What is your PIN?")
        userInput = input(">")
        if(userInput == player5[1]):
            print("Hello, "+name+"\nYour balance is "+player5[2]+".\nYour PIN is "+player5[1])
            wait()
            os.system("ctl")
        else:
            print("Incorrect PIN")
            wait()
            os.system("ctl")
    if(player4[0] == name):
        print("What is your PIN?")
        userInput = input(">")
        if(userInput == player4[1]):
            print("Hello, "+name+"\nYour balance is "+player4[2]+".\nYour PIN is "+player4[1])
            wait()
            os.system("ctl")
        else:
            print("Incorrect PIN")
            wait()
            os.system("ctl")
    if(player3[0] == name):
        print("What is your PIN?")
        userInput = input(">")
        if(userInput == player3[1]):
            print("Hello, "+name+"\nYour balance is "+player3[2]+".\nYour PIN is "+player3[1])
            wait()
            os.system("ctl")
        else:
            print("Incorrect PIN")
            wait()
            os.system("ctl")
    if(player2[0] == name):
        print("What is your PIN?")
        userInput = input(">")
        if(userInput == player2[1]):
            print("Hello, "+name+"\nYour balance is "+player2[2]+".\nYour PIN is "+player2[1])
            wait()
            os.system("ctl")
        else:
            print("Incorrect PIN")
            wait()
            os.system("ctl")
    if(player1[0] == name):
        print("What is your PIN?")
        userInput = input(">")
        if(userInput == player1[1]):
            print("Hello, "+name+"\nYour balance is "+player1[2]+".\nYour PIN is "+player1[1])
            wait()
            os.system("ctl")
        else:
            print("Incorrect PIN")
            wait()
            os.system("ctl")





print("Ready for transactions")
print("Use the letters to choose a transaction option")
print("a)  Player to bank (e.g. property purchase)\nb)  Bank to player (e.g. for passing go)\nc)  Player to player (e.g. for a chance card)\n\nType cb)  Check player balance")