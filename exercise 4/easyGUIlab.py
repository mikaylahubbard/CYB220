
from easygui import *
#choose your own adventure - these functions are the different path options. After each question, the program adds that path to the file with the completed story
def dig():
    msgbox("Disgruntled at the unfortunate piece of metal occupying his perfectly good hole, Cooper moves a couple feet over to restart his hole. Cooper digs and digs. He ends up creating an entire maze of tunnels, perfect for his own personal hideout. After days of living in these tunnels, Cooper returns to the castle. Cooper's king missed him so much and shower him with affectino upon his return. Although he never got on the cook's good side, Cooper lived the rest of his days safely at hope with occasionally escapades to his secret hideout.",
           "More Digging", "THE END")
    file.write(f"Disgruntled at the unfortunate piece of metal occupying his perfectly good hole, Cooper moves a couple feet over to restart his hole. Cooper digs and digs. He ends up creating an entire maze of tunnels, perfect for his own personal hideout. After days of living in these tunnels, Cooper returns to the castle. Cooper's king missed him so much and shower him with affectino upon his return. Although he never got on the cook's good side, Cooper lived the rest of his days safely at hope with occasionally escapades to his secret hideout.\n\n")
    
def treasure():
    msgbox("Cooper keeps digging, hoping for the best. What he uncovers is a small metal chest full of gold and jewelry. Cooper has struck rich! He picks up the chest and carries it back to the castle. Cooper is hailed as a hero, having found the most infamous buried treasure in the entire world. He lives the rest of his days in fame, given only the softest of sleeping places and as much steak as he can imagine.",
           "Treasure", "THE END")
    file.write(f"Cooper keeps digging, hoping for the best. What he uncovers is a small metal chest full of gold and jewelry. Cooper has struck rich! He picks up the chest and carries it back to the castle. Cooper is hailed as a hero, having found the most infamous buried treasure in the entire world. He lives the rest of his days in fame, given only the softest of sleeping places and as much steak as he can imagine.\n\n")

def sand():
    answer = indexbox("As most dogs are inclined to do, Cooper excitedly starts digging a hole. He imagines he is a pirate digging for treasure, or a dilusional child hoping to reach the other side of the world. Howeber, Copper stumbles across something hard, made of metal. He pauses. Is this treasure or just something in getting in the way of his imporantt hole-digging quest?",
                      "Digging", ["A. keep digging", "B. make a better hole somewhere else"] )
    file.write(f"As most dogs are inclined to do, Cooper excitedly starts digging a hole. He imagines he is a pirate digging for treasure, or a dilusional child hoping to reach the other side of the world. Howeber, Copper stumbles across something hard, made of metal. He pauses. Is this treasure or just something in getting in the way of his imporantt hole-digging quest?\n\n")
    if answer == 0:
        treasure()
    elif answer == 1:
        dig()

def water():
    msgbox("excited, Cooper bounds to the water, splashing around, pretending to be a pirate lost at sea. However, Cooper stumbles across and a hidden drop off, having explored a little to far into the ocean. He is whisked under the water, and is never seen again.\n RIP Cooper",
           "Ocean", "THE END")
    file.write(f"excited, Cooper bounds to the water, splashing around, pretending to be a pirate lost at sea. However, Cooper stumbles across and a hidden drop off, having explored a little to far into the ocean. He is whisked under the water, and is never seen again.\n RIP Cooper\n\n")

def bacon():
    msgbox("following the scent of bacon, Cooper comes across a beshevled youngster along the side of the path. Excited to have a new furry friend, the boy lures copper over with a freshlyl made piece of bacon. Cooper inhales the bacon, and the child recruits the adventurous old dog into  a life of adventure and crime. Cooper has befriended a young vigilante and lives out the rest of his days being fed bacon and assisting in various schemes",
           "Bacon", "THE END")
    file.write(f"following the scent of bacon, Cooper comes across a beshevled youngster along the side of the path. Excited to have a new furry friend, the boy lures copper over with a freshlyl made piece of bacon. Cooper inhales the bacon, and the child recruits the adventurous old dog into  a life of adventure and crime. Cooper has befriended a young vigilante and lives out the rest of his days being fed bacon and assisting in various schemes\n\n")
    
def sweets():
    msgbox("He follows the sweers, finding an old lady with a sinister smile, stirring a large potions. The door shut ominously behind him. It seems the witch has found the final ingredient for her potion of youth. \nRIP Cooper \n",
           "Sweets", "THE END")
    file.write(f"following the scent of bacon, Cooper comes across a beshevled youngster along the side of the path. Excited to have a new furry friend, the boy lures copper over with a freshlyl made piece of bacon. Cooper inhales the bacon, and the child recruits the adventurous old dog into  a life of adventure and crime. Cooper has befriended a young vigilante and lives out the rest of his days being fed bacon and assisting in various schemes\n\n")
    

def stay():
    answer = indexbox(" He trots along the path, then he smells sweets, he strays off the path following the smell. he comes across a clearnig and finds a cottage with smoke flowing out of the chimney. He stops, confused. THere are 2 smells. The first is the smell of sweets, coming from the cozy cottage. The second smell is that of bacon, coming from further on the path. WHich does he go to?",
                      "Smells", ["A. towards the sweets", "B. towards the bacon"])
    file.write(f"He trots along the path, then he smells sweets, he strays off the path following the smell. he comes across a clearnig and finds a cottage with smoke flowing out of the chimney. He stops, confused. THere are 2 smells. The first is the smell of sweets, coming from the cozy cottage. The second smell is that of bacon, coming from further on the path. WHich does he go to?\n\n")
    if answer == 0:
        sweets()
    elif answer == 1:
        bacon()

def singing():
    msgbox("Did you foget that Cooper's deaf? He can't hear the singing, idiot.", "Singing", "Go Back")
    right()

def right():
    answer = indexbox("Cooper heads to where he imagines the most adventure to be: the dark forest. As he trots along, there is isinging in the distance. What does he do?",
                      "Dark Forest", ["A. follow the singing", "B. stay on the path"])
    file.write(f"Cooper heads to where he imagines the most adventure to be: the dark forest. As he trots along, there is isinging in the distance. What does he do?\n\n")
    if answer == 0:
        singing()
    elif answer == 1:
        stay()

def left():
    answer = indexbox("Cooper trots towards the beach, taking in the amaxing weather. As he reaches the beach, he also reaches a conundrum. Does he play in the water or dig in the sand?",
                      "Beach", ["A. play in the water", "B. dig in the sand"])
    file.write("Cooper trots towards the beach, taking in the amaxing weather. As he reaches the beach, he also reaches a conundrum. Does he play in the water or dig in the sand?\n\n")
    if answer == 0:
        water()
    elif answer == 1:
        sand()

def hallwayRight():
    msgbox(f"Cooper decides to go right, immidiately running into the kind-hearted king who is obsessed with him. He is picked up by the king and handfed the steak then goes to sleep. I suppose he may run into adventure at another point in time", 
           "King", "THE END")
    file.write(f"Cooper decides to go right, immidiately running into the kind-hearted king who is obsessed with him. He is picked up by the king and handfed the steak then goes to sleep. I suppose he may run into adventure at another point in time\n\n")


def hallwayLeft():
    answer = indexbox("Cooper turns left. Alas! Dead end!  In a rage, the cook scoops up the little dog and throws him out of the palace. Although this wasn't Cooper's ideal means of exit, he realizes he has not gotten past the drawbridge drawback. Ahead of him are two paths. The left path goes towards a beach and the right, towards a dark forest. Which way does Cooper go?",
                      "Dead End", ["A. left", "B. right"])
    file.write(f"Cooper turns left. Alas! Dead end!  In a rage, the cook scoops up the little dog and throws him out of the palace. Although this wasn't Cooper's ideal means of exit, he realizes he has not gotten past the drawbridge drawback. Ahead of him are two paths. The left path goes towards a beach and the right, towards a dark forest. Which way does Cooper go?")
    if answer == 0:
            left()
    elif answer == 1:
        right()

def biteHeels():
    answer = indexbox("Cooper begins biting at the cooks heels, which angers him even more. In a rage, the cook scoops up the little dog and throws him out of the palace. Although this wasn't Cooper's ideal means of exit, he realizes he has not gotten past the drawbridge drawback. Ahead of him are two paths. The left path goes towards a beach and the right, towards a dark forest. Which way does Cooper go?", 
                      "Biting", ["A. left", "B. right"])
    file.write(f"Cooper begins biting at the cooks heels, which angers him even more. In a rage, the cook scoops up the little dog and throws him out of the palace. Although this wasn't Cooper's ideal means of exit, he realizes he has not gotten past the drawbridge drawback. Ahead of him are two paths. The left path goes towards a beach and the right, towards a dark forest. Which way does Cooper go?\n\n")
    if answer == 0:
        left()
    elif answer == 1:
        right()

def stealSteak():
    answer = indexbox("While the cook is distracted, Cooper takes the opportunity to snatch a piece of steak and dart away as fast as his little legs could. The cooks promtly turns and dashes after him. Cooper approaches a fork in the hallway. Which way does he turn?",
                      "Steak Theif", ["A. left", "B. right"])
    file.write(f"hile the cook is distracted, Cooper takes the opportunity to snatch a piece of steak and dart away as fast as his little legs could. The cooks promtly turns and dashes after him. Cooper approaches a fork in the hallway. Which way does he turn?\n\n")
    if answer == 0:
        hallwayLeft()
    elif answer == 1:
        hallwayRight()

def biteRope():
    answer = indexbox("Cooper dashes forward and bites the rope in 2. The drawbridge opens and Cooper runs off to his new adventure. To the left is a path leading to the beach, and to the right is a path going into a dark forest. Which way does Cooper go?",
                      "Crossing the Drawbridge", ["A. left", "B. right"])
    file.write(f"Cooper dashes forward and bites the rope in 2. The drawbridge opens and Cooper runs off to his new adventure. To the left is a path leading to the beach, and to the right is a path going into a dark forest. Which way does Cooper go?\n\n")
    if answer == 0:
        left()
    elif answer == 1:
        right()
        
def puppyEyes():
    answer = indexbox("Cooper gives the guard on duty his best puppy-eyed stare. The guards melts, as they all do, and walks toward the kitchen to get a treat. while this wasn't his intention cooper is quite pleased and trots to the kitchen for his favorite - foodzzz. Once there, it seems the cook get bad at the guard, gesturing wildly with his knife and likely yelling (though cooper can't hear a thing, so it doesn't bother him) How does cooper react?",
                          "Puppy Eyes", ["A. snatch a piece of steak and run away", 
                                              "B:Bite at the cooks heels"])
    file.write(f"Cooper gives the guard on duty his best puppy-eyed stare. The guards melts, as they all do, and walks toward the kitchen to get a treat. while this wasn't his intention cooper is quite pleased and trots to the kitchen for his favorite - foodzzz. Once there, it seems the cook get bad at the guard, gesturing wildly with his knife and likely yelling (though cooper can't hear a thing, so it doesn't bother him) How does cooper react?\n\n")
    if answer == 0:
        stealSteak()
    elif answer == 1:
        biteHeels()

#this is the main function. You can replay as long as you want until you reach the end then press cancel
active = True
while active:
    # This asks if the user wants to start/restart the story
    start = ccbox("Hi! welcome the the choose your own adventure following the adventures of a deaf dog named Cooper! Would you like to continue?",
                  "Choose Your Own Adventure", image="cooper.png")
    if start:
        # Ask the user to create a file where we will be writing the finished story
        openVwrite = buttonbox("We will be writing your story to a file. Would you like to open a current file or save to a new file?",
                               "Saving Story", ["open file", "create new"])
        if openVwrite == "open file":
            output = fileopenbox("Choose a file to write to:", "open file")
        else: 
            output = filesavebox("Please create a file to write to:", "create file")
        # open the file for writing
        file = open(output, 'a')
        message = f"A long time ago in a kingdom far far away, there lived a dog named Cooper. Cooper had lived a good long life. Throoughout the years he had seen kings and kingdoms rise and fall. He had tasted the wares of many a palace cook (with and without their permission), and, unfortunately, he had also lost his hearing. However, Cooper longed for adventure, and as the days went by he decided it was time to take matters intohis own paws. And so, Cooper left the safety of the castle, setting out for adventure."
        msgbox(message)
        file.write(f"{message}\n\n")
         #Begin the story with the first prompt
        answer = indexbox("cooper heads to the castle door, but the drawbridge is up! What does he do",
                          "Drawbridge", ["A. Use puppy eyes to get the guard to open the drawbridge", 
                                      "B. bite through the rope to let down the bridge"])
        file.write(f"cooper heads to the castle door, but the drawbridge is up!\n\n")
        if answer == 0:
            puppyEyes()
        elif answer == 1:
            biteRope()
        #once the series of methods have come to an end, it finishes the story. After this happens, it begins the loop again
        file.write("\nTHE END\n")
    else:
        # if the user chooses cancel in the continue/cancel box, it goes here and quits the program
        msgbox("Thank you for your time, and have a great day :)")
        active = False
        
        
#below is the construction of my story:  
        
# A long time ago in a kingdom far far away, there lived a dog named Cooper. Cooper had lived a good long  life. 
# Throoughout the years he had seen kings and kingdoms rise and fall. He had tasted the wares of many a palace cook (with and without their permission), and, 
# unfortunately, he had also lost his hearing. However, Cooper longed for adventure, and as the days went by he decided it was time to take matters into
# his own paws. And so, Cooper left the safety of the castle, setting out for adventure.
#   
# cooper heads to the castle door, but the drawbridge is up! What does he do?
# A: Use puppy eyes to get the guard to open the drawbridge  B. bite through the rope to let down the bridge

#A: 

# Cooper gives the guardon duty his best puppy-eyed stare. The guards melts, as they all do, and walks toward the kitchen to get a treat.
#while this wasn't his intention cooper is quite pleased and trots to the kitchen for his favorite - foodzzz. Once there, it seems the cook get bad at the guard, 
# gesturing wildly with his knife and likely yelling (though cooper can't hear a thing, so it doesn't bother him)
# How does cooper react?
#A: snatch a piece of steak and run away  B:Bite at the cooks heels

#B 
# bites the rope, the drawbridge opens, and he dashes out. to the left is a path leading to the beach, and the left goes into the dark woods
#A: go left, B: go right


#AA
# steals a piece of steak, cook chases him, go left or right


#ABxw
# he bites at the cooks heals, which anger him and the cook kicks him out of the palace
#to the left is a path leading to the beach, and the left goes into the dark woods
#A: go left, B: go right


#AAA
#he goes left. Dead end. Cook catches him and kicks him out of the palace. 
# to the left is a path leading to the beach, and the left goes into the dark woods
#A: go left, B: go right

#AAB
#he goes right, running into the kind-hearted king who is obssesed with him. 
# He is picked up by the king and handfed the steak then goes to sleep. I suppose 
# he may run into adventure at another point in time
# END

#ABA / BA / AAAA
#goes left towards the beach
#A: plays in the water B: digs in the sand  ---------- need to follow this line


#ABB/ BB / AAAB
#goes right towards the forest
# there's singing in the disyance
# A: follows the singing B: stays on the path


#ABBA / BBA / AAB
#did you forget Cooper's deaf? He cant hear the singing, idiot
#go back


#ABBB / BBAB / AABB
# He trots along the path, then he smells sweets, he strays off the path following the smell. he comes across a clearnig and finds a cottage with smoke 
# flowing out of the chimney. He stops, confused. THere are 2 smells. The first is the smell of sweets, coming from the cozy cottage. The second smell is 
# That of bacon, coming from further on the path. WHich does he go to?
# A. sweets B. Bacon


# ABBBA / BBABA/ AABBA
# He follows the sweers, finding an old lady with a sinister smile, stirring a large potions. The door shut ominously behind him. It seems the witch
#  has found the final ingredient for her potion of youth. RIP COOPER
# THE END

#AABBAB / BBAB / AABB
# following the scent of bacon, Cooper comes across a beshevled youngster along the side of the path. 
# Excited to have a new furry friend, the boy lures copper over with a freshlyl made piece of bacon. Cooper inhales the bacon, and 
# the child recruits the adventurous old dog into  a life of adventure and crime. Cooper has befriended a young vigilante and lives out
# the rest of his days being fed bacon and assisting in various schemes. 
# END


# ABAA / BAA / AAAAA
# excited, Cooper bounds to the water, splashing around, pretending to be a pirate lost at sea. However, Cooper stumbles across and a hidden drop off]
# having explored a little to far into the ocean. He is whisked under the water, and is never seen again. RIP Cooper
# END


#ABAB / BAB / AAAAB 
# As most dogs are inclined to do, Cooper excitedly starts digging a hole. He imagines he is a pirate digging for treasure, or a dilusional child hoping
# to reach the other side of the world. Howeber, Copper stumbles across something hard, made of metal. He pauses. Is this treasure or just something in
# getting in the way of his imporantt hole-digging quest?
# A. Keep digging B. make a better hole somewhere else


#ABABA / BABA / AAAABA
# Cooper keeps digging, hoping for the best. What he uncovers is a small metal chest full of gold and jewelry. Cooper has struck rich! He picks up the chest and carries
# it back to the castle. Cooper is hailed as a hero, having found the most infamous buried treasure in the entire world. He lives the rest of his days in
# fame, given only the softest of sleeping places and as much steak as he can imagine.
# THE END


#ABABB / BABB / AAAABB
# Disgruntled at the unfortunate piece of metal occupying his perfectly good hole, Cooper moves a couple feet over to restart his hole. Cooper digs and 
# digs. He ends up creating an entire maze of tunnels, perfect for his own personal hideout. After days of living in these tunnels, Cooper returns to the castle. 
# Cooper's king missed him so much and shower him with affectino upon his return. Although he never got on the cook's good side, Cooper lived the rest of his
# days safely at hope with occasionally escapades to his secret hideout.
# THE END

