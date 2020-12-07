#too many

import random
import time


choiceA = ["A", "a"]
choiceB = ["B","b"]


semiPreciousStone = 0 

resource = 0
health = 100
name = input("What is your name? ")  

#used this before using a class.
#name = input("What is your name? ")



#class semiPreciousStones:
 #   def __init__ (self, name):
  #      self.name= name
        
#semiPreciousStones = semiPreciousStones("Semi Precious Stone")        

#class player:
 #   def __init__(self, health):
  #      self.name = name
   #     self.health = 100
    #    self.semiPreciousStones = 0


#player =  player(input("What is your name? "))


   # def fight(self):
    #    choice = input("  ")
    #if choice in choiceA:
     #   self.health = self.health -  (random.randint(1,100))
      #  self.health = int(self.health)
    #elif choice in choiceB:
     #   optionGameOver()
        
   


def intro():
    #name = input("What is your name? ")    
    print(name, ", You have been asleep for sometime now, and we are glad you have awaken!!")
    time.sleep(3)
    print("A strange figure knocked you out, and took your belongings including your funny looking Key!")
    time.sleep(5)
    print("They took off afar over the hills, through the swamp, and it seems... up the mountain.")
    time.sleep(5)
    print("You must go, go face your fears, your self doubts, defeat your adversary, recover your lost poccessions, and retrieve your strange little key??")

    print("What will you do?")
    time.sleep(4)
    print(" a. Go after your lost items?\n or \n b. Go back to sleep?")
    
    global semiPreciousStone 

    global resource 
    global health 
    
    choice = input("  ")
    if choice in choiceA:
        optionAdventure()
    elif choice in choiceB:
        optionGameOver()
    
    
    
def optionAdventure():
    
    global semiPreciousStone 

    global resource 
    global health 
    print(" ahhh GREAT CHOICE! Before you go take this!")
    time.sleep(3)
    print("You received a Semi Precious Stone! They're practically valueless, but they look nice.") 
    semiPreciousStone = 1  
    time.sleep(3)
    print("Also I see you have gained some clarity in this decision!")
    resource = 2
    time.sleep(3)
    print ("\n You go into the hills, making your way, and breathing the fresh air, excited, \n anxious! you suddenly stop...")
    time.sleep(4)
    print("\n The bush to your left shakes...\n Do you \n a. Investigate? \n or \n b. Leave it alone?")
    
    #Choice to investigate
    choice = input("  ")
    if choice in choiceA:
        enemy1()
    elif choice in choiceB:
        runEnemy1()
    #Game over >>> work on listing at the end
def optionGameOver():
    print("GAME OVER")
    #semiPreciousStone = semiPreciousStone +1
    #resource = resource + 1
    print("Health", ":" , health) 
    print("Semi-Precious-Stones", ":", semiPreciousStone)
    print("Clarity",":",resource)
    


def enemy1():
    
    global semiPreciousStone 

    global resource 
    global health 
    ReafsselHealth = 10
    time.sleep(3)
    print("From behind the bush appears Reafssel!! \n A figured embodiment of your worst fears!")
    time.sleep(4)
    print("As your heart instantly drops into your ***hole, you realize you have 1 of 2 choices")
    time.sleep(3)
    print("Will you: \n a. Stand, fight, and face your greatest fears? \n or \n b. Will you Flee?")
    
    #choice to face fears
    choice = input("  ")
    if choice in choiceA:
        reafsselHealth = -10
        time.sleep(5)
        print("Shakingly you find some grit and you look in to Reafssel's scary demented eyes and ROAR!")
        print("The ROAR sends Reafssel flying back!")
        time.sleep(4)
        print("Reafssel shrieks and youre blinded by a bright light!")
        time.sleep(3)
        print("Once youre able to see again, you notice Reafssel has turned into one of those Semi Precious Stones!")
        semiPreciousStone = + 1
        resource  = + 2
        print("Great Job facing Reafssel, you were fearless! and have gained some clarity for being so.")
        time.sleep(4)
        swamp()
    #choice to run and not face fears
    elif choice in choiceB:
        runEnemy1()
#what happens if you do not face fears? >> continue to swamp and lessen clarity
        #Randomness needed / he may attack any way.
def runEnemy1():
    
    
    global semiPreciousStone 

    global resource 
    global health 
    #chance of random enemy encounter
    #random.choice[swamp(),enemy1()]
    #if choice in random:
     #   enemy1()
    
        #here is my problem
        
    print("you try to leave, but something nabbed you! You scurry off afraid and wimpy, after getting hit")
    health = -25
    print("While it is understandable to run from your fears, doing so will never help YOU in the long run, and has caused you to lose some clarity")
    resource = -1
    swamp()
    #elif choice in random:
        #here is my problem
        
       # resource = -1
        #print("While it is understandable to run from your fears, doing so will never help YOU in the long run, and has caused you to lose some clarity")
        #swamp()
    #swamp        
def swamp():
    time.sleep(3)
    print("You have made it to The Swamp!")
    time.sleep(4)
    print("The Swamp is marshy and wet, it has a foul odor and you realize your feet are wet and your toes have become soggy")
    time.sleep(4)
    print("You can not help but feel a strong feeling of self doubt, and start questioning yourself, your life choices, the choice to come on this adventure.")
    time.sleep(4)
    print("Suddenly \n")
    time.sleep(3)
    print("You notice a patch of soggy sog bubbling")
    time.sleep(3)
    print("do you: \n a. check it out \n or \n b. Keep going to the bottom of The Mountain?")
    
    
    choice = input("  ")
    if choice in choiceA:
        enemy2()
    elif choice in choiceB:
        runEnemy2()
        #random.choice[mountains() or ]
    global semiPreciousStone 

    global resource 
    global health 

def enemy2():
    
    
    
    global semiPreciousStone 

    global resource 
    global health 
    SodeluftHealth = [50]
    time.sleep(3)
    print("From underneath the nasty marsh appears Sodeluft!! \n Another creature that is a concrete embodiment of your self-doubt!")
    time.sleep(4)
    print("You are not sure what you should do, you question yourself... you come to the conclusion that you have 1 of 2 choices")
    time.sleep(3)
    print("Will you: \n a. Stand, fight, and face your self doubt and insecurities? \n or \n b. Will you cowardly flee?")
    
    #choice to face fears
    choice = input("  ")
    if choice in choiceA:
        SodeluftHealth = [-50]
        time.sleep(5)
        print("Unsure if youre making the right choice. You stand your ground and look Sodeluft in the eye with confidence")
        time.sleep(4)
        print("Sodeluft lets out a horrifying whale and again youre blinded by a bright light!")
        time.sleep(3)
        print("Once youre able to see again, you notice Sodeluft has turned into another one of those Semi Precious Stones!")
        semiPreciousStone =  1
        resource  =  3
        time.sleep(3)
        print("Great Job facing Sodeluft! Although you had your doubts, you over came them and were able to turn those doubts into confidence. By doing so you have gained some clarity.")
        time.sleep(7)
        mountains()
    #choice to run and not face fears
    elif choice in choiceB:
        runEnemy2()
        
    
    
    
def runEnemy2():
    
    
    
    global semiPreciousStone 

    global resource 
    global health 
    resource = -2
    
    #random crashing the game 
    #random.choice[enemy2(),mountains()]
    #if random.choice is mountains():
     #   resource += [-2]
    time.sleep(5)
    print("While it is understandable to run from your selfdoubts, doing so will never help YOU in the long run, will only make you lost in this life. This has caused you to lose some clarity")
    time.sleep(4)
    #elif choice is Enemy2():
    print("Something got ahold of you, you do not look so great")
    health = -50
      #  print("While it is understandable to run from your selfdoubts, doing so will never help YOU in the long run, will only make you lost in this life. This has caused you to lose some clarity")
    mountains()
        
        
def mountains():
    
    
    global semiPreciousStone 

    global resource 
    global health 
    
    print("You have made it to the bottom of the mountain... \n you look up at it, and feel this sensation as if you were meant to go up and also, at the same time, it would be the biggest mistake of your life.")
    time.sleep(5)
    print("As you head up the mountain you feel COLD... \n not cold as in *burrr* but cold as in a feeling you cannot explain.")
    time.sleep(4)
    print("As you almost make it to the top...")
    time.sleep(3)
    print("You hear",name, ", why have you come??")
    time.sleep(4)
    print("You look around and see no one!,and Then BOOM!!")
    time.sleep(7)
    print(name, "appears!!!... Super confused you realize...You must face your self!!! \n The strange figure is actually yourself, the person you love and hate the most!!")
    time.sleep(4)
    print("Will you look in the ""mirror"" and face yourself??? \n a. Face yourself \n or \n b. RUN?")    
    choice = input("  ")
    if choice in choiceA:
        semiPreciousStone = 1
        resource = 1
        time.sleep(5)
        faceYourself()
    elif choice in choiceB:
        print(name, "cracks you on top of the head")
        health = 0
        
        optionGameOver()
        
        
        
def faceYourself():
    
    
    global semiPreciousStone 

    global resource 
    global health 
    
    NegaYouHealth= -100
    print("You look your self in the eyes, and although you feel guilt, pride, regret, anxiety, and astonishment. You feel proud that you are able to accept the decisions you have made in your life. \n able to accept the person you are, able to accept", name)
    time.sleep(7)
    print("You look at your self with pride, disgust, and you yell with every thing you felt, ""you shall not pass!!!....you saw it in a movie once.")
    time.sleep(7)
    print(name, "looks you back in the eye and you gain this clear understanding of SELF, and with SELF you realize and understand you are able to understand others.")
    time.sleep(7)
    print("NEGA", name ,"folds and from it, grows a trinket")
    resource = 5
    semiPreciousStone = 5
           
    
    
    mountainTop()
    
    
def mountainTop():
    
    
    global semiPreciousStone 

    global resource 
    global health 
    
    time.sleep(8)
    print("Finally you have made it to The Mountain Top!")
    
    print("You feel weary and cold as you look around...")
    time.sleep(4)
    print("As you reflect on your journey you feel at ease with your self, and the clarity that you have gained.")
    time.sleep(4)
    print( "You look to the right and you see your belongings and your key!!!")
    print("What is the key for?? \n a. Tell what the key is for.  \n b. Keep it a secret??")
    
    choice = input("  ")
    if choice in choiceA:
        print("It is the key to Python!! and with it... hopefully you have passed your class!")
        optionGameOver()
    elif choice in choiceB:
        time.sleep(3)

        
        optionGameOver()
    







intro()    