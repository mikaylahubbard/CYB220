from CYOAclass import CYOA
import tkinter as tk

root = tk.Tk()
c = CYOA(root=root)


def start():
    c.newQuestionPage("Save Story", "As you follow the story, we will be writing the results to a file. Please create a file to save your story to :)",
                      "Create File", "Quit", createFile, Quit)
    
def createFile():
    c.open_file_dialog()
    drawbridge()
 
def Quit():
    c.newContinuePage("Byeeeeee", "Thank you for your time :)", "BYE", root.destroy)

def intro():
    # the adventure starts here
    c.newQuestionPage("Start Adventure","Hi! welcome the the choose your own adventure following the adventures of a deaf dog named Cooper! Would you like to start?",
                    "Start", "Quit", start, Quit)
    
def end():
    c.write("THE END")
    c.newQuestionPage("THE END", "Thank you for playing! Would you like to start the story again?", "Start", "Quit", drawbridge, Quit)
    
def drawbridge():
    c.newQuestionPage("Drawbridge", "cooper heads to the castle door, but the drawbridge is up! What does he do?",
                    "A. Use puppy eyes to get the guard to open the drawbridge", "B. bite through the rope to let down the bridge",puppyEyes, biteRope,
                    "A long time ago in a kingdom far far away, there lived a dog named Cooper. Cooper had lived a good long life. Throoughout the years he had seen kings and kingdoms rise and fall. He had tasted the wares of many a palace cook (with and without their permission), and, unfortunately, he had also lost his hearing. However, Cooper longed for adventure, and as the days went by he decided it was time to take matters intohis own paws. And so, Cooper left the safety of the castle, setting out for adventure.",
                    write=True)

def puppyEyes():
    c.newQuestionPage("Puppy Eyes", "Cooper gives the guard on duty his best puppy-eyed stare. The guards melts, as they all do, and walks toward the kitchen to get a treat. while this wasn't his intention cooper is quite pleased and trots to the kitchen for his favorite - foodzzz. Once there, it seems the cook get bad at the guard, gesturing wildly with his knife and likely yelling (though cooper can't hear a thing, so it doesn't bother him) How does cooper react?",
                    "A. snatch a piece of steak and run away", "B. Bite at the cooks heels", stealSteak, biteHeels, write=True)

def biteRope():
    c.newQuestionPage("Crossing the Drawbridge", "Cooper dashes forward and bites the rope in 2. The drawbridge opens and Cooper runs off to his new adventure. To the left is a path leading to the beach, and to the right is a path going into a dark forest. Which way does Cooper go?",
                    "A. left", "B. right", left, right, write=True)
    
def stealSteak():
    c.newQuestionPage("Steak Theif", "While the cook is distracted, Cooper takes the opportunity to snatch a piece of steak and dart away as fast as his little legs could. The cooks promtly turns and dashes after him. Cooper approaches a fork in the hallway. Which way does he turn?",
                    "A. left", "B. right", hallwayLeft, hallwayRight, write=True)
    
def biteHeels():
    c.newQuestionPage("Biting", "Cooper begins biting at the cooks heels, which angers him even more. In a rage, the cook scoops up the little dog and throws him out of the palace. Although this wasn't Cooper's ideal means of exit, he realizes he has not gotten past the drawbridge drawback. Ahead of him are two paths. The left path goes towards a beach and the right, towards a dark forest. Which way does Cooper go?",
                    "A. left", "B. right", left, right, write=True)
    
def hallwayLeft():
    c.newQuestionPage("Dead End", "Cooper turns left. Alas! Dead end!  In a rage, the cook scoops up the little dog and throws him out of the palace. Although this wasn't Cooper's ideal means of exit, he realizes he has not gotten past the drawbridge drawback. Ahead of him are two paths. The left path goes towards a beach and the right, towards a dark forest. Which way does Cooper go?",
                    "A. left", "B. right", left, right, write=True)
    
def hallwayRight():
    c.newContinuePage("King", "Cooper decides to go right, immidiately running into the kind-hearted king who is obsessed with him. He is picked up by the king and handfed the steak then goes to sleep. I suppose he may run into adventure at another point in time",
                    "THE END", end, write=True)

def left():
    c.newQuestionPage("Beach", "Cooper trots towards the beach, taking in the amaxing weather. As he reaches the beach, he also reaches a conundrum. Does he play in the water or dig in the sand?", 
                    "A. play in the water", "B. dig in the sand", water, sand, write=True)
    
def right():
    c.newQuestionPage( "Dark Forest", "Cooper heads to where he imagines the most adventure to be: the dark forest. As he trots along, there is isinging in the distance. What does he do?",
                    "A. follow the singing", "B. stay on the path", singing, stay, write=True)
    
def singing():
    c.newContinuePage("Singing", "Did you foget that Cooper's deaf? He can't hear the singing, idiot.",
                    "Go Back", right)
    
def stay():
    c.newQuestionPage("Smells", "He trots along the path, then he smells sweets, he strays off the path following the smell. he comes across a clearnig and finds a cottage with smoke flowing out of the chimney. He stops, confused. THere are 2 smells. The first is the smell of sweets, coming from the cozy cottage. The second smell is that of bacon, coming from further on the path. WHich does he go to?",
                    "A. towards the sweets", "B. towards the bacon", sweets, bacon, write=True)
    
def sweets():
    c.newContinuePage("Sweets","He follows the sweers, finding an old lady with a sinister smile, stirring a large potions. The door shut ominously behind him. It seems the witch has found the final ingredient for her potion of youth. \nRIP Cooper \n",
                    "THE END", end, write=True)
    
def bacon():
    c.newContinuePage("Bacon", "following the scent of bacon, Cooper comes across a beshevled youngster along the side of the path. Excited to have a new furry friend, the boy lures copper over with a freshlyl made piece of bacon. Cooper inhales the bacon, and the child recruits the adventurous old dog into  a life of adventure and crime. Cooper has befriended a young vigilante and lives out the rest of his days being fed bacon and assisting in various schemes",
                    "THE END", end, write=True)
    
def water():
    c.newContinuePage("Ocean", "excited, Cooper bounds to the water, splashing around, pretending to be a pirate lost at sea. However, Cooper stumbles across and a hidden drop off, having explored a little to far into the ocean. He is whisked under the water, and is never seen again.\n RIP Cooper",
                    "THE END", end, write=True)
    
def sand():
    c.newQuestionPage("Digging", "As most dogs are inclined to do, Cooper excitedly starts digging a hole. He imagines he is a pirate digging for treasure, or a dilusional child hoping to reach the other side of the world. Howeber, Copper stumbles across something hard, made of metal. He pauses. Is this treasure or just something in getting in the way of his imporantt hole-digging quest?",
                    "A. keep digging", "B. make a better hole somewhere else", treasure, dig, write=True)
    
def treasure():
    c.newContinuePage("Treasure", "Cooper keeps digging, hoping for the best. What he uncovers is a small metal chest full of gold and jewelry. Cooper has struck rich! He picks up the chest and carries it back to the castle. Cooper is hailed as a hero, having found the most infamous buried treasure in the entire world. He lives the rest of his days in fame, given only the softest of sleeping places and as much steak as he can imagine.",
                    "THE END", end, write=True)
    
def dig():
    c.newContinuePage("More Diggin", "Disgruntled at the unfortunate piece of metal occupying his perfectly good hole, Cooper moves a couple feet over to restart his hole. Cooper digs and digs. He ends up creating an entire maze of tunnels, perfect for his own personal hideout. After days of living in these tunnels, Cooper returns to the castle. Cooper's king missed him so much and shower him with affectino upon his return. Although he never got on the cook's good side, Cooper lived the rest of his days safely at hope with occasionally escapades to his secret hideout.",
                    "THE END", end, write=True)
    
intro()
root.mainloop()
