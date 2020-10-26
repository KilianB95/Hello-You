# Instructions Textbased game your choice will make the story. You have different choices in directions input()
# First prologue(Epilogue) a little story about the attack of Japan in Indonesia.
# There will be choices made of how the game will start after the prologue.
# You play as a person who works for the Sultan of Borneo(Kalimatan) and this is his story.

def option_story1_5():
    print("---------------------------------------------------")
    print("You and your family part ways they go towards the palace and you are going to the streets to get people to safety.\nAfter your arrival there you here that the japanese has entered the city.\nYou look shocked and try to get the last few people into safety before you can get yourself into safety.\nBut when you try to safe a person you see that the japanese soldiers are approaching you fast.\nYou have to make a quick decision, hide or run.")
    ant9 = input("hide or run:")

    if ant9 == "hide" or ant9 == "HIDE":
        option_story4()
    elif ant9 == "run" or ant9 == "RUN":
        option_story2()



def option_story1_4():
    print("---------------------------------------------------")
    print("You go together with your family towards the palace, when you arrive at the palace you see that the soldiers are preparing defences.\nYou look at the soldiers and then you look at your family.\nWhat will you do help the soldiers and let your family walk on their own further to the palace.\nOr will you go together with your family towards the palace.")
    ant8 = input("defences or family:")

    if ant8 == "defences" or ant8 == "DEFENCES":
        option_story1_8()
    elif ant8 == "family" or ant8 == "FAMILY":
        option_story1_9()
    



def option_story1_3():
    print("---------------------------------------------------")
    print("You run towards the palace after a few minutes you arrive at the palace.\nYou go inside the palace and asks where the sultan is you are given directions of where his whereabouts are.\nYou walk towards the directions given to you, and you see the Sultan.\nHe greets you and you immediatly tells the story you heard on the streets.\nWhere he replies that he knows about it and that he allready informed the soldiers to get people to safety.\nYou sigh of relieving and say that you are getting your family where the Sultan replies that they are allready been brought to safety into the palace.\nThe Sultan asks you to stay here and help the soldiers to prepare defences.\nWhen you reply that that the you can also help with getting more people to safety.\The choice is yours says the Sultan.\nWhat will you do prepare defences or helping people to get to safety.")
    ant7 = input("defences or help:")

    if ant7 == "defences" or ant7 == "DEFENCES":
        option_story1_8()
    elif ant7 == "help" or ant7 == "HELP":
        option_story2()
    


def option_story1_2():
    print("---------------------------------------------------")
    print("You run towards home after a few minutes later you arrive at home.\nHoping everybody is home you feel relieved that everybody is home and starts telling with what is going on.\nAfter telling them you tell them to go to the palace for safety.\nYour family asks what you will do.\nWill you go with them to the palace for safety or will you go helpin people get to safety in the city.")
    ant6 = input("palace or help:")

    if ant6 == "palace" or ant6 == "PALACE":
        option_story1_4()
    elif ant6 == "help" or ant6 == "HELP":
        option_story1_5()
            
    
def option_story1():
    print("---------------------------------------------------")
    print("You walk down the street and hear people talking about an attack of the Japanese army.\nYou stop walking and you try to listen to the conversation.\nWhen you listen to the conversation you hear that the Japanese army has succeded to invade the first part of the island.\nWhen hearing this you want to decide to run towards home or towards the palace of the Sultan.\type home to go towards home, type palace to go to the Sultan.")
    ant5 = input("home or palace:")

    if ant5 == "home" or ant5 == "HOME":
        option_story1_2()
    elif ant5 == "palace" or ant5 == "PALACE":
        option_story1_3()

        
def option_prologue3():
    print("---------------------------------------------------")
    print("You see a hole next to you, you crawl desperatly towards the hole.\nYou play dead and you hope that you won't be seen.\nSuddenly you pass away after a few hours you awaken.\nWhen you open your eyes you see that you are in a cabin you look around and see that you are in a hospik cabin.\nYou see a sergeant and you call him.\nThe sergeant looks at you and walks towards you and asks how you are and if you are willing to tel the story of what happend.\nYou say yes and you tell the sergeant the story.\nAfter you told the story the Sergeant tells you that Japan has succeed to invade further into the island and has already taken several villages and sieging towns and cities.\nYou know after hearing this that you've lost to defend the people of Borneo and that only a miracle can appear to win this war.\nIf you type in yes the story will start.")
    ant4 = input("yes:")

    if ant4 == "yes" or ant4 == "YES":
        option_story3()


def option_prologue2():
    print("---------------------------------------------------")
    print("You look at the battle you see a lot of people die.\nWhen seeing all those people die you chose to run away from the battle.\nYou try to get back to the forest but when you are almost there you get hit by a bullet and you died immediatly.\nNow the prologue has ended you have two choices to make yes or run\nYes wil start the story from the start and run will start the game when you'll get chased.")
    ant3 = input("yes or run:")

    if ant3 == "yes" or ant3 == "YES":
          option_story1()
    elif ant3 == "run" or ant3 == "RUN":
        option_story2()


def option_prologue1():
    print("---------------------------------------------------")
    print("You charge into the battlefield with a warcry RAAARGGGGHHHH!!!!\nYou feel the adrenaline rush flowing through your body.\nYou begin to shoot recklessly but then suddenly you get shot.\nYou fall on the ground and you know you are done for.\nBut in your thoughts you know you can still survive if you do something.\nYou see next to you a hole in the ground what was made by a mortar.\nWhat will you do go in there and hide or scream for help.")
    ant2 = input("hide or help:")
    

    if ant2 == "hide" or ant2 == "HIDE":
        option_prologue3()
    elif ant2 == "help" or ant2 == "HELP":
        option_story2()
          

def prologue():
    print("---------------------------------------------------")
    print("It is December 16th 1941 Japan attacks the island called Borneo.\nYou hear about the attack and you get deployed immediatly towards the battle.\nWhen you arrive at the battlefield you see that the Japanese forces are to strong to fight against.\n What will you do fight them or run away from the battle.")
    ant1 = input("fight or run:")
    

    if ant1 == "fight" or ant1 == "FIGHT":
        option_prologue1()
    elif ant1 == "run" or ant1 == "RUN":
        option_prologue2()



print("Welcome at my textbased game about ..... first you will have an list of instructions.")
print("After the instructions the game will start, it will start with a prolugue.")
print("Where your choices are crucial for the start of the game/storyline goodluck")
print("Intructions: The choices you can make are made with North, East, South, West, Yess, No, Run, Hide or Fight")
print("These options will be shown of which choice is available to choose.")
print("Type yes to start the game")
choice = input()

prologue()



