print("This is a game for Robinson Crusoe Day. \nWritten by AW '23")

print("\nPress Run to start.")

name = input("Enter your nickname: ")
#function that is called when player dies
def death_message():
    print("You didn't pick the right choice and now you're dead 😔✋")
#introductory message and first question
def first_function():
    print("Hello "+name+"! Welcome to the Robinson Cruesoe Game. You are a voyager in the 1600s. During this game you will be presented with choices. Try to select \nthe answer that will keep you alive. Good Luck!")
#first question prints a "death message" no matter what, but then the game starts for real
    print("This is your first voyage! Where would you like to go? Your choices are to journey around Cape Horn or to the Bermuda Triangle")
    answertofirstquestion = int(input("Enter the number '1' for Cape Horn and '2' for the Bermuda Triangle: "))
    #I used the > sign instead of the = sign
    if answertofirstquestion > 1:
        print("Oh no! Your ship crashed. What a shame. You managed to make it into a lifeboat though, and after many days floating around on the ocean you get rescued.")
        #both options call the second function/choice
        second_function()
    else:
        print("Oh no! Your ship crashed. What a shame. You managed to make it into a lifeboat though, and after many days floating around on the ocean you get rescued.")
        second_function()

def second_function():
    print("When you make it back to England you manage to convince a rich landowner to finance another voyage. He wants you to captain an expedition to colonize foreign lands.")
    shipname = input("Enter your ship name: ")
    print(shipname+ " sets sail. On your way you encounter a swanky island with penguins and seals. Do you want to kidnap them?")
    #no matter what the player gets abandoned
    answertoquestion2 = int(input("Enter the number '1' to kidnap the seals and penguins and '2' to keep going."))
    #mini game if option 2 is selected in which the crew ends up dying no matter what
    if answertoquestion2 > 1:
        print ("It was nice of you to not kidnap seals and penguins but you still crashed.")
        mini_function()
    else:
        print ("Your vegan crew did not align with the morals of kidnapping animals and they abandoned you on the island. Tragic 😪")
        fourth_function()

#mini functon game
def mini_function():
    print("Your ship has been destroyed and your only chance of rescue is if a ship happens to pass by. You might be able to kill your crew during the night for food.")
    answertominigame = int(input("Enter '1' to attempt to kill them or '2' to let them live: "))
    if answertominigame > 1:
        print("The entire crew dies of Typhoid fever anyway 🥳")
        fourth_function()
    else:
        fifth_function()

def fourth_function():
    print("Your new goal of the game is to make it back to England. You are getting lonely on the island when you find a parrot.")
    #player is informed that their new goal is to make it back to england
    parrotname = str(input("Enter a name for your parrot: "))
    #parrot name is displayed in the next print message
    print("You scavenge the wrecked ship for supplies with " + str(parrotname)+" and find seeds to grow plants. Do you grow tobacco or corn?")
    #charcter dies if tobacco is planted
    fourthanswer = int(input("Enter '1' to grow corn or '2' to grow tobacco: "))
    if fourthanswer > 1:
        death_message()
    else:
        ("Good choice. You have food now.")
        fifth_function()

def fifth_function():
    #both choices lead to similar fquestions which both meet at function eight
    print("You discover a bible on the Island.")
    fifthfunctionanswer = int(input("Enter the number '1' to form a cult or '2' to study Christianity: "))
    if fifthfunctionanswer > 1:
        print ("With the aid of Christianity you are able to find relief in life alone on the island.")
        sixth_function() 
    else:
        cultname = str(input("Enter the name of your cult: "))
        cultgod = str(input("Enter the god of your cult: "))
        seventh_function()

def sixth_function():
    #player dies if they attempt to kill the cannibals
    print("You encounter cannibals on the island. ")
    sixthfunctionanswer = int(input("Enter '1' to kill the cannibals or '2' to teach them the bible: "))
    if sixthfunctionanswer > 1:
            print("The cannibals join your religion and you guys are having a fun time on the island.")
            eighth_function()
    else:
            print("That was a terrible idea. They were stronger than you. ")
            death_message()

def seventh_function():
    #very similar to the sixth function
    print("You encouunter cannibals on the island.")
    seventhfunctionanswer = int(input("Enter '1' to kill the cannibals or '2' to convert them into your cult: "))
    if seventhfunctionanswer > 1:
            print("The cannibals join your cult and you guys are having a fun time on the island.")
            eighth_function()
            #correct option leads to the eighth function like in the sixth function
    else:
            print("That was a terrible idea. They were stronger than you. ")
            death_message()

def eighth_function():
    print("A working ship passes by and your people manage to imprison the crew. The ship is fully working. ")
    eighthfunctionanswer = int(input("Enter '1' to sail back to England or '2' to stay on the island: "))
    #game ends if player does not choose to go to england
    if eighthfunctionanswer > 1:
        print("You live a long life on the island and die happily at the age of 666. You technically did not win, as you didn't make it back to England.")
    else:
        ninth_function()

def ninth_function():
    print("On your way back to England you encounter pirates.")
    ninthfunctionanswer = int(input("Enter '1' to fight the pirates or '2' to return to the island: "))
    #game ends if player does not make it to england
    if ninthfunctionanswer > 1:
        print("You live a long life on the island and die happily at the age of 666. You technically did not win, as you didn't make it back to England.")
    else:
        tenth_function()

def tenth_function():
    print("You are now battling the pirates.")
    tenthfunctionanswer = int(input("Enter '1' to fire cannons or '2' to attempt to board the ship: "))
    #character dies if they attempt to board the ship
    if tenthfunctionanswer > 1:
        death_message()
    else:
        eleventh_function()

def eleventh_function():
    #while loop, player dies if options 1-3 are chosen
    print("You successfully make it back to England. You should purchase a pet.")
    x = int(input("Enter '1' to adopt a cat, '2' for a bat, '3' for a fox, '4' for a rabbit, or '5' for a dog: "))
    while x < 4:
        print("Your pet gave you rabies.")
        death_message()
    else:
        twelfth_function()

def twelfth_function():
    #for loop
    emojis = ["🖐", "🤯", "😎", "🥵","🥳"]
    for y in emojis:
        print(y)
    print("You won the game!")

#first function is called in order to start the game
first_function()
