import os
import Cards.Card as Card
print("This is the official MDB Credit Card Mod. This is the alongside version, meaning you still need to use the standard MDB alongside this.")
print("💡Hint: use split screen with MDB on one side, and MDB Credit Card Mod on the other.")
def wait(clearAfter):
    print("\n")
    notImportantVariable = input("Press enter to continue...")
    if(clearAfter == True):
        os.system("clear")
wait()
print("Enter the amount of players using a credit card (max 8)")
cardUserCount = int(input(">"))
def initiatePlayers():
    usersLeft = cardUserCount
    if(usersLeft == 8):
        print("Please enter your name")
        name = input(">")
        Card.listAvailable()
        cardChosen = input(">")
        print("Please read the Terms and conditions of using this card. If you disagree, type 'n', if you agree, type 'y':\n"+Card.listTerms(cardChosen))
        agreed = input(">")
        if(input == "y"):
            cardname = Card.cardname(cardChosen)
            player8 = [name,cardname]
            print("You have been registered for "+cardname+".")
        else:
            print("Sorry to see you disliked the terms")
    if(usersLeft == 7):
        print("Please enter your name")
        name = input(">")
        Card.listAvailable()
        cardChosen = input(">")
        print("Please read the Terms and conditions of using this card. If you disagree, type 'n', if you agree, type 'y':\n"+Card.listTerms(cardChosen))
        agreed = input(">")
        if(input == "y"):
            cardname = Card.cardname(cardChosen)
            player7 = [name,cardname]
            print("You have been registered for "+cardname+".")
        else:
            print("Sorry to see you disliked the terms")
    if(usersLeft == 6):
        print("Please enter your name")
        name = input(">")
        Card.listAvailable()
        cardChosen = input(">")
        print("Please read the Terms and conditions of using this card. If you disagree, type 'n', if you agree, type 'y':\n"+Card.listTerms(cardChosen))
        agreed = input(">")
        if(input == "y"):
            cardname = Card.cardname(cardChosen)
            player6 = [name,cardname]
            print("You have been registered for "+cardname+".")
        else:
            print("Sorry to see you disliked the terms")
    if(usersLeft == 5):
        print("Please enter your name")
        name = input(">")
        Card.listAvailable()
        cardChosen = input(">")
        print("Please read the Terms and conditions of using this card. If you disagree, type 'n', if you agree, type 'y':\n"+Card.listTerms(cardChosen))
        agreed = input(">")
        if(input == "y"):
            cardname = Card.cardname(cardChosen)
            player5 = [name,cardname]
            print("You have been registered for "+cardname+".")
        else:
            print("Sorry to see you disliked the terms")
    if(usersLeft == 4):
        print("Please enter your name")
        name = input(">")
        Card.listAvailable()
        cardChosen = input(">")
        print("Please read the Terms and conditions of using this card. If you disagree, type 'n', if you agree, type 'y':\n"+Card.listTerms(cardChosen))
        agreed = input(">")
        if(input == "y"):
            cardname = Card.cardname(cardChosen)
            player4 = [name,cardname]
            print("You have been registered for "+cardname+".")
        else:
            print("Sorry to see you disliked the terms")
    if(usersLeft == 3):
        print("Please enter your name")
        name = input(">")
        Card.listAvailable()
        cardChosen = input(">")
        print("Please read the Terms and conditions of using this card. If you disagree, type 'n', if you agree, type 'y':\n"+Card.listTerms(cardChosen))
        agreed = input(">")
        if(input == "y"):
            cardname = Card.cardname(cardChosen)
            player3 = [name,cardname]
            print("You have been registered for "+cardname+".")
        else:
            print("Sorry to see you disliked the terms")
    if(usersLeft == 2):
        print("Please enter your name")
        name = input(">")
        Card.listAvailable()
        cardChosen = input(">")
        print("Please read the Terms and conditions of using this card. If you disagree, type 'n', if you agree, type 'y':\n"+Card.listTerms(cardChosen))
        agreed = input(">")
        if(input == "y"):
            cardname = Card.cardname(cardChosen)
            player2 = [name,cardname]
            print("You have been registered for "+cardname+".")
        else:
            print("Sorry to see you disliked the terms")
    if(usersLeft == 1):
        print("Please enter your name")
        name = input(">")
        Card.listAvailable()
        cardChosen = input(">")
        print("Please read the Terms and conditions of using this card. If you disagree, type 'n', if you agree, type 'y':\n"+Card.listTerms(cardChosen))
        agreed = input(">")
        if(input == "y"):
            cardname = Card.cardname(cardChosen)
            player1 = [name,cardname]
            print("You have been registered for "+cardname+".")
        else:
            print("Sorry to see you disliked the terms")
initiatePlayers()
print("All players using credit cards have been added. The following is a list of what things can affect players in certain financial situations.")
propertyPurchase = "The following players are eligible for price changes during property purchases\n"
if(cardUserCount == 8):
    if(player8[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player8[0])
    if(player7[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player7[0])
    if(player6[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player6[0])
    if(player5[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player5[0])
    if(player4[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player4[0])
    if(player3[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player3[0])
    if(player2[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player2[0])
    if(player1[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player1[0])
if(cardUserCount == 7):
    if(player7[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player7[0])
    if(player6[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player6[0])
    if(player5[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player5[0])
    if(player4[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player4[0])
    if(player3[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player3[0])
    if(player2[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player2[0])
    if(player1[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player1[0])
if(cardUserCount == 6):
    if(player6[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player6[0])
    if(player5[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player5[0])
    if(player4[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player4[0])
    if(player3[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player3[0])
    if(player2[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player2[0])
    if(player1[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player1[0])
if(cardUserCount == 5):
    if(player5[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player5[0])
    if(player4[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player4[0])
    if(player3[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player3[0])
    if(player2[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player2[0])
    if(player1[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player1[0])
if(cardUserCount == 4):
    if(player4[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player4[0])
    if(player3[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player3[0])
    if(player2[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player2[0])
    if(player1[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player1[0])
if(cardUserCount == 3):
    if(player3[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player3[0])
    if(player2[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player2[0])
    if(player1[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player1[0])
if(cardUserCount == 2):
    if(player2[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player2[0])
    if(player1[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player1[0])
if(cardUserCount == 1):
    if(player1[1] in Card.propertyBenefits):
        propertyPurchase = (propertyPurchase+player1[0])