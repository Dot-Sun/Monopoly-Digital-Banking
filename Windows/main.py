import transactions
import os
print("Welcome to Monopoly Digital Banking")

#set the banker PIN
print("Please set a banker PIN")
bankerPin = input("PIN>")

#a simple function that waits for the user to press enter
def wait():
    notImportantVariable = input(" ")

#player setup
print("How many players are there")
playerCount = input(">")
playerCount = int(playerCount)
print("Please fill out the required information for each player")
wait()
os.system("cls") #this line will be used to clear the console

#setup players
while(playerCount != 0):
    name = input("Name>")
    os.system("cls")
    print("Please give the device to "+name)
    wait()
    pin = input("PIN>")
    os.system("cls")
    print("Please give device to the banker")
    wait()
    playerNumber = playerCount
    playerNumber = [name,pin,1500]
    playerCount = playerCount -1

print("Ready for transactions")
print("Use the letters to choose a transaction option")
print("a)  Player to bank (e.g. property purchase)\nb)  Bank to player (e.g. for passing go)\nc)  Player to player (e.g. for a chance card)\n\nType cb)  Check player balance")