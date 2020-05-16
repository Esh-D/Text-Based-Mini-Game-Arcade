'''
#Eshika Dey 
#Jan 22 2017
#A compilation of 5 mini-games in one program (hence,  a text-based Mini Game Arcade)

# NOTE: I use "player" and "user" interchangably in the comments

Aspects of "Eshika's Mini-Game Arcade:
  Main Menu
    User will be welcomed to the Arcade.
    User will choose which game they would like to play.
    Chosen game will begin.
  Games
    1. Guess the Number
      User is greeted to the game.
      User is told how to play/given a description of the game.
      User sets the range of numbers they would like to guess from.
      User attempts to guess the number.
      Game is over when the user guesses the number correctly.
      User is asked if they want to PLAY AGAIN or GO BACK TO MENU
      IF user Plays Again they are asked if they want to change the number range.
      IF user Plays Again, game begins again.
      
    2. Rock, Paper, Scissors
      User is greeted to the game.
      User is told how to play.
      User is asked to choose Rock, Paper, Scissors (1,2,or 3).
      Computer (randomly) chooses Rock, Paper, or Scissors (1,2,or 3).
      Display "(User's choice) vs (Computer's choice)".
      Winner is displayed.
      User is asked if they want to PLAY AGAIN or GO BACK TO MENU
      Game begins again.
    
    3. Multiplication game 
      User is greeted to the game.
      User is told how to play.
      User is given a (2-digit multiplication) question and answers it.
      If the user is wrong, it is game over.
      If the user is consecutive correct 5 times, they move on to the next Level.
      Every level adds one more digit to the questions.
      Their are 5 levels. If you finish level 5 you win.
    
        
    4. Addition game (Same concept and basically the same code as the "Multiplication Game" but with addition)
      User is greeted to the game.
      User is told how to play.
      User is given a (2-digit addition) question and answers it.
      If the user is wrong, it is game over.
      If the user is consecutive correct 5 times, they move on to the next Level.
      Every level adds one more digit to the questions.
      Their are 9 levels. If you finish level 9 you win.
    
    5. Sprinter
      User is greeted to the game.
      User is told how to play.
      User begins continuously pressing the 'enter' key
      1 press is 1 step. 
      There are 25 steps in the sprint
      There is a time limit for every level
      If the user finishs before the time limit is reached they move on to the next level.
      If they don't, it is GAME OVER.
      There are 10 levels, if the player beats them all, they WIN.
      
      
  
'''
import time

# Welcoming player to the Arcade
print("WELCOME TO ESHIKA'S MINI-GAME ARCADE!")

# Initializing in order for the Arcade loop to begin (the variable "menu")
menu = True

# ================= BEGINING OF THE ARCADE LOOP ==========================
while menu == True:
  #Displaying the header and the game choices, and also what the enter if the user wants to exit the arcade
  print("\n********** MAIN MENU ******************************")
  print("\nChoose a game you would like to play:")
  print("\nEnter the corresponding number to play the game:")
  print("1 = Guess the Number\n2 = Rock, Paper, Scissors\n3 = The Multiplication Game\n4 = The Addition Game\n5 = Sprinter")
  
  print("\nEnter 'E' to EXIT the Arcade.")
  
  #used to move the input area("game") down to the bottom of the page, to make it look like an actual Menu Page
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  
  #The user chooses which game they would like to play (1,2,3,4,5)
  # or they can choose to exit the Arcade ('E')
  game = input("")
  
  #Divder
  print("\n_________________________________________________________________\n")
  # =========== POSSIBILITIES based on the input of "game" ===============

  #If the user wishs to exit the Arcade (end the Arcade loop)
  #They need to enter "E" on the menu screen
  #This stops the whole program
  # E stands for exit
  if game == "E":
    menu = False
  
###############  GUESS THE NUMBER  #######################################
# NOTE: the arrow beside the line 89 marker isn't working, the block of code might be too big, so I'm just gonna leave this one open
# if the user wants to play "Guess the Numer", they type '1' into the "game" input
  if game == "1":
  #========== Creating / Gathering Beginning Info =============
    #Greeting the user
    print("Welcome to 'Guess the Number'!")
    
    #Explaination of game
    print("\nINSTRUCTIONS:")
    print("First, you will enter the range of numbers you would like to guess from.\n")
    print("The computer will then choose a number within that range.\n")
    print("Your objective is to guess that number correctly.\n")
    print("If you are wrong, the computer will tell you whether you are 'Too High' or 'Too Low'.\n")
    print("You have unlimited guess.\n")
    
    #Divider
    print("______________________________\n")
    
    # Gathering the parameters for the random number generation
    # User enters the range of numbers he/she would like to guess from
    print("Enter the range of numbers you would like to guess from.\n")
    lowR = int(input("Lowest Number:"))
    highR = int(input("Highest Number:"))
      
    # Generating the number the user will be guessing
    import random 
    num = random.randint(lowR,highR)
    
    #Divider
    print("______________________________")
    
    #Initializing the "again" variable
    again = "y"
    #============ START OF GAME LOOP ============================
    # The While Loop is used to allow the user to Play Again, it also lets the user guess more than once
    while again == "y":
      
      # The user guesses a number
      guess = int(input("\nGuess the Number."))
      #============= OUTCOMES ======================
      # If the user's guess is more than the number,
      # the program tells the user it is too high
      if guess > num:
        print("\nThat number is too HIGH.")
        
        #Divider
        print("______________________________")
        
      # If the user's guess is less than the number
      # the program tells the user it is too low
      if guess < num: 
        print("\nThat number is too LOW.")
        
        #Divider 
        print("______________________________")
      
      # If the user answers correctly
      # the program tells the user it is correct 
      if guess == num:
        print("\nThat is CORRECT!\n")
        
        #Reseting the "guess" variable
        guess = None
        
        #Player is asked if they would like to Play Again or go Back to the Menu
        again = input("\nEnter 'y' to Play Again\nEnter 'n' to Go Back to the Menu\n")
        
        #if player wants to Play Again
        if again == "y":
          #Ask if the user wants to change the range of numbers they want to guess from
          numR = input("Would you like to change the number range? 'y' or 'n'(yes or no).")
          
          #If the user does not want to change the number range,
          #A new number is generated from the old number range
          #This new number is the number the user will try to guess in the next round
          if numR == "n":
            num = random.randint(lowR,highR)
            #Divider 
            print("______________________________________________________________")
          
          #if the user wants to change the number range,
          if numR == "y":
            #They are prompted for the lowest number and the highest number of the range of numbers they would like to guess from
            print("\nEnter the range of numbers you would like to guess from.\n")
            lowR = int(input("Lowest Number:"))
            highR = int(input("Highest Number:"))
            
            #After that a new number is generated from the new number range
            #This new number is the number the user will try to guess in the next round
            num = random.randint(lowR,highR)
    
            #Divider
            print("______________________________________________________________")
        #If the user doesn't not like to play again
        #If the user wants to go back to the Main Menu
        if again == "n":
          print("________________________________________________________________")
          #Thanks the user for playing
          print("\nThank you for playing!")
          #Gives the user the time to see the thank you message before going back to the Main Menu
          time.sleep(1)
          print("\n_________________________________________________________________\n")
      #================ END OF GAME LOOP ==========================
    
################  ROCK PAPER SCISSORS  ###################################
  #NOTE: the time.sleep()'s are to space out the code. In this particular game, the code would show up all at once and the game would be over in a second.
  
  # If user wants to play "Rock, Paper, Scissors", they type '2' into the "game" input
  if game == "2":
    print("Welcome to 'Rock, Paper, Scissors'!")
    
    print("\nINSTRUCTIONS:")
    print("You choose either 1(rock), 2(paper), or 3(scissors).\n")
    print("Then the computer will randomly choose 1 of the 3 options.\n")
    print("The program will then determine the winner.\n")

    print("REMEMBER:")
    print("Rock beats Scissors.")
    print("Scissors beats Paper.")
    print("Paper beats Rock.")
    
    #Divider
    print("\n_______________________________________________\n")
    
    #Initializing the "again" variable
    again = "y"
    
    #============ START OF GAME LOOP ============================
    # The While Loop is used to allow the user to Play Again
    while again == "y":
      #Player's Play 
      P = int(input("\nRock, Paper, or Scissors?\n\n1 = Rock\n2 = Paper\n3 = Scissors\t"))
      
      #Generating Computers Play
      rock = 1
      paper = 2
      scissors = 3 
      
      import random
      C = random.randint(1,3)
      
      time.sleep(1)
      print("\nComputer's choice:", C, "\n")
      
      if P == 1:
        weaponP = "Rock"
      if C == 1:
        weaponC = "Rock"
      if P == 2:
        weaponP = "Paper"
      if C == 2:
        weaponC = "Paper"
      if P == 3:
        weaponP = "Scissors"
      if C == 3:
        weaponC = "Scissors"
      
      time.sleep(.5)
      print("_________________________")
      print(weaponP, "vs", weaponC)
      print("_________________________")
      
      time.sleep(2)
      
      #============= OUTCOMES ======================
    
      # WINNING OUTCOMES (C v P)
      #rock vs paper
      if C == 1 and P == 2:
        print("\nYou have WON!")
      # paper vs scissors
      if C == 2 and P == 3:
        print("\nYou have WON!")
      # scissors vs rock
      if C == 3 and P == 1:
        print("\nYou have WON!")
      
      # LOSING OUTCOMES (P v C)
      # rock vs paper
      if P == 1 and C == 2:
        print("\nYou have LOST!")
      # paper vs scissors
      if P == 2 and C == 3:
        print("\nYou have LOST!")
      # scissors vs rock
      if P == 3 and C == 1:
        print("\nYou have LOST!")
      
      # TIED OUTCOME
      # if they both choose the same item
      # rock vs rock, paper vs paper, scissors vs scissors
      if C == P:
        print("\nYou have TIED!")
        
      time.sleep(1)
      
      again = input("\nEnter 'y' to Play Again\nEnter 'n' to Go Back to the Menu\n")
      
      print("\n_______________________________________________\n")
      
      if again == "n":
        print("Thanks for playing!")
        time.sleep(1)
        print("\n_________________________________________________________________\n")
    #================ END OF GAME LOOP ==========================

###############  THE MULTIPLICATION GAME  ################################
  # If user wants to play "The Multiplication Game", they type '3' into the "game" input
  if game == "3":
    
    #welcomes player to the game
    print("Welcome to 'The Multiplication Game'!\n\n\n")
    
    #Explaination of game:
    print("INSTRUCTIONS:")
    print("The game will begin on Level 1, the game will give you 2-digit multiplication questions.\n")
    print("When answering these questions, if you get one wrong, it is GAME OVER.\n")
    print("When you get 5 of these questions consecutively correct, you move on to the next level.\n")
    print("Level 2 will have 3-digit multiplication questions.\n")
    print("This cyle continues until the you finish Level 5 (6-digit multiplication) and the YOU WIN the game.\n")
    print("You may use mental math or pen and paper to answer these questions.\n") 
    print("Calculators are not permitted, however I won't know if you use one...\n") 
    
    #Divider
    print("\n_______________________________________________\n")

    # ======== Initializers ===============
    # begins on level 1
    lvl = 1
    # The number of correct guesses is 0 in the beginnning
    count = 0 
    
    #The ending parameters for the random numbers (on lvl 1)
    # For the explaination of why I'm using these variables, go to the section of comments above "import random" and the assignements of num1, num2, etc.
    # (it is a couple lines of code under this comment)
    eNum1 = 10
    eNum2 = 10
    eNum3 = 1
    eNum4 = 1
    eNum5 = 1
    eNum6 = 1
    
    # initializing the variable "again" in order for the while loop to run
    again = "y"
    
    #============ START OF GAME LOOP ============================
    # The While Loop is used to allow the user to Play Again and generate new questions
    while again == "y":
    
      # Anything multiplied by 1 is itself
      # making the beginning and ending parameters 1 and 1, sets the varible to 1
      # During the all the levels, all the variables are in use, however depending on the level a certain amount of the variables have no affect on the answer(they are set to 1)
      # As the level increases, these ending parameters will be reassigned (ex. when the player enters level 2, the value of "eNum3" gets reassigned to 10.)
      import random
      num1 = random.randint(1,eNum1)
      num2 = random.randint(1,eNum2)
      num3 = random.randint(1,eNum3)
      num4 = random.randint(1,eNum4)
      num5 = random.randint(1,eNum5)
      num6 = random.randint(1,eNum6)
    
      # Calculating answer of randomly generated numbers
      answer = num1 * num2 * num3 * num4 * num5 * num6
    
      # Depending on what level the user is on, the program will display different variables to the user
      # The displayed variables will be the ones that have an affect on the answer (the ones whose ending parameters are not set to 1)
      if lvl == 1:
        print ("\nWhat is", num1, "x", num2, "?")
        # variable "guess" is the user's answer
        guess = int(input("What is your answer?"))
        
      elif lvl == 2:
        print ("\nWhat is", num1, "x", num2, "x", num3, "?")
        guess = int(input("What is your answer?"))
        
      elif lvl == 3:
        print ("\nWhat is", num1, "x", num2, "x", num3, "x", num4, "?")
        guess = int(input("What is your answer?"))
        
      elif lvl == 4:
        print ("\nWhat is", num1, "x", num2, "x", num3, "x", num4, "x", num5, "?")
        guess = int(input("What is your answer?"))
        
      elif lvl == 5:
        print ("\nWhat is", num1, "x", num2, "x", num3, "x", num4, "x", num5, "x", num6, "?")
        guess = int(input("What is your answer?"))
        
      # if the user's answer is correct
      if guess == answer:
        #the number of correct answers goes up by one
        count += 1
        #tells the user that they are correct
        print("CORRECT!")
      
      #if the user's answer is not correct
      elif guess != answer:
        #divider
        print("\n_______________________________________________\n")
        #Tells the user that it is GAME OVER
        print("\nGAME OVER!")
        #Gives them a choice between playing again or going back to the menu
        again = input("\nEnter 'y' to Play Again\nEnter 'n' to Go Back to the Menu\n")
        
        #divider
        print("\n_______________________________________________\n")
        
        # if the user wants to play again
        if again == "y":
          # The variables get reset to their initialized values
          count = 0 
          lvl = 1
          
          eNum1 = 10
          eNum2 = 10
          eNum3 = 1
          eNum4 = 1
          eNum5 = 1
          eNum6 = 1
        
        # if the user wants to go back to the menu and doesn't want to play again
        if again == "n":
          #Thanks the player for playing 
          print("\nThank you for playing!")
          # A delay that allows the user to see the thank you message before the menu loop gets activiated from the beginning again
          time.sleep(1)
          #divider
          print("\n_________________________________________________________________\n")
      # if the user gets 5 consecutive answers correct
      if count == 5:
        #The count resets to 0
        count = 0
        
        # if the level the player is on is not the last level
        if lvl < 5:
          print("\nLEVEL UP!")
          #Player moves on to the next level
          lvl += 1
          
          #Reassigning the ending parameters depending on the level the player has moved to
          if lvl == 2:
            eNum3 = 10
          elif lvl == 3:
            eNum4 = 10
          elif lvl == 4:
            eNum5 = 10
          elif lvl == 5:
            eNum6 = 10
          
          #if it is the last level
        else:
          #divider
          print("\n_______________________________________________\n")
          #telling the user that they won
          print("\nYOU WIN!")
          #Asking them if they want to play again or go back to the menu
          again = input("\nEnter 'y' to Play Again\nEnter 'n' to Go Back to the Menu\n")
          #divider
          print("\n_______________________________________________\n")
          
          #if the user wants to play again
          if again == "y":
          # The variables get reset to their initialized values
            count = 0 
            lvl = 1
            
            eNum1 = 10
            eNum2 = 10
            eNum3 = 1
            eNum4 = 1
            eNum5 = 1
            eNum6 = 1
          
          #if they don't want to play again
          if again == "n":
            #thanks the user for playing
            print("\nThank you for playing!")
            #a delay to allow the user to read the thank you message before the menu shows up
            time.sleep(1)
            #Divider
            print("\n_________________________________________________________________\n")
    #================ END OF GAME LOOP ==========================

  ###############  THE ADDITION GAME  ####################################
  # If user wants to play "The Addition Game", they type '4' into the "game" input  
  if game == "4":

    print("Welcome to 'The Addition Game'!\n\n\n")
    
    #Explaination of game:
    print("INSTRUCTIONS:")
    print("The game will begin on Level 1, the game will give you 2-digit addition questions.\n")
    print("When answering these questions, if you get one wrong, it is GAME OVER.\n")
    print("When you get 5 of these questions consecutively correct, you move on to the next level.\n")
    print("Level 2 will have 3-digit addition questions.\n")
    print("This cyle continues until the you finish Level 9 (10-digit addition) and the YOU WIN the game.\n")
    print("You may use mental math or pen and paper to answer these questions.\n") 
    print("Calculators are not permitted, however I won't know if you use one...\n") 
    
    #Divider
    print("\n_______________________________________________\n")

    # ======== Initializers ===============
    # begins on level 1
    lvl = 1
    # The number of correct guesses is 0 in the beginnning
    count = 0 
    
    #The ending parameters for the random numbers (on lvl 1)
    # For the explaination of why I'm using these variables, go to the section of comments above "import random" and the assignements of num1, num2, etc.
    # (it is a couple lines of code under this comment)
    eNum1 = 10
    eNum2 = 10
    eNum3 = 0
    eNum4 = 0
    eNum5 = 0
    eNum6 = 0
    eNum7 = 0
    eNum8 = 0
    eNum9 = 0
    eNum10 = 0
    
    #initializing the variable "again" so that the while loop will run
    again = "y"
    
    #============ START OF GAME LOOP ============================
    # The While Loop is used to allow the user to Play Again and generate new questions
    while again == "y":
    
      # Anything plus 0 is itself
      # making the beginning and ending parameters 0 and 0, sets the varible to 0
      # During the all the levels, all the variables are in use, however depending on the level a certain amount of the variables have no affect on the answer(they are set to 0)
      # As the level increases, these ending parameters will be reassigned (ex. when the player enters level 2, the value of "eNum3" gets reassigned to 10.)
      import random
      num1 = random.randint(0,eNum1)
      num2 = random.randint(0,eNum2)
      num3 = random.randint(0,eNum3)
      num4 = random.randint(0,eNum4)
      num5 = random.randint(0,eNum5)
      num6 = random.randint(0,eNum6)
      num7 = random.randint(0,eNum7)
      num8 = random.randint(0,eNum8)
      num9 = random.randint(0,eNum9)
      num10 = random.randint(0,eNum10)
    
      #Calculating the sum of the randomly generated numbers
      answer = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10
      
      # Depending on what level the user is on, the program will display different variables to the user
      # The displayed variables will be the ones that have an affect on the answer (the ones whose ending parameters are not set to 0)
      if lvl == 1:
        print ("\nWhat is", num1, "+", num2, "?")
        guess = int(input("What is your answer?"))
        
      elif lvl == 2:
        print ("\nWhat is", num1, "+", num2, "+", num3, "?")
        guess = int(input("What is your answer?"))
        
      elif lvl == 3:
        print ("\nWhat is", num1, "+", num2, "+", num3, "+", num4, "?")
        guess = int(input("What is your answer?"))
        
      elif lvl == 4:
        print ("\nWhat is", num1, "+", num2, "+", num3, "+", num4, "+", num5, "?")
        guess = int(input("What is your answer?"))
        
      elif lvl == 5:
        print ("\nWhat is", num1, "+", num2, "+", num3, "+", num4, "+", num5, "+", num6, "?")
        guess = int(input("What is your answer?"))
        
      elif lvl == 6:
        print ("\nWhat is", num1, "+", num2, "+", num3, "+", num4, "+", num5, "+", num6, "+", num7, "?")
        guess = int(input("What is your answer?"))
        
      elif lvl == 7:
        print ("\nWhat is", num1, "+", num2, "+", num3, "+", num4, "+", num5, "+", num6, "+", num7, "+", num8, "?")
        guess = int(input("What is your answer?"))
        
      elif lvl == 8:
        print ("\nWhat is", num1, "+", num2, "+", num3, "+", num4, "+", num5, "+", num6, "+", num7, "+", num8, "+", num9, "?")
        guess = int(input("What is your answer?"))
        
      elif lvl == 9:
        print ("\nWhat is", num1, "+", num2, "+", num3, "+", num4, "+", num5, "+", num6, num7, "+", num8, "+", num9, "+", num10, "?")
        guess = int(input("What is your answer?"))
        
      # if the user's answer is correct
      if guess == answer:
        #the number of correct answers goes up by one
        count += 1
        #tells the user that they are correct
        print("CORRECT!")
        
      #if the user's answer is not correct
      elif guess != answer:
        #divider
        print("\n_______________________________________________\n")
        #Tells the user that it is GAME OVER
        print("\nGAME OVER!")
        #Gives the user a choice between playing again or going back to the menu
        again = input("\nEnter 'y' to Play Again\nEnter 'n' to Go Back to the Menu\n")
        
        #divider
        print("\n_______________________________________________\n")
        
        # if the user wants to play again
        if again == "y":
          # The variables get reset to their initialized values
          count = 0 
          lvl = 1
          
          eNum1 = 10
          eNum2 = 10
          eNum3 = 0
          eNum4 = 0
          eNum5 = 0
          eNum6 = 0
          eNum7 = 0 
          eNum8 = 0 
          eNum9 = 0 
          eNum10 = 0 
          
        # if the user wants to go back to the menu and doesn't want to play again
        if again == "n":
          #Thanks the player for playing 
           print("\nThank you for playing!")
           # A delay that allows the user to see the thank you message before the menu loop gets activiated from the beginning again
           time.sleep(1)
           #divider
           print("\n_________________________________________________________________\n")
    
      # if the user gets 5 consecutive answers correct
      if count == 5:
        #The count resets to 0
        count = 0
        
        # if the level the player is on is not the last level
        if lvl < 9:
          #Player moves on to the next level
          print("\nLEVEL UP!")
          lvl += 1
          
          #Reassigning the ending parameters depending on the level the player has moved to
          if lvl == 2:
            eNum3 = 10
          elif lvl == 3:
            eNum4 = 10
          elif lvl == 4:
            eNum5 = 10
          elif lvl == 5:
            eNum6 = 10
          elif lvl == 6:
            eNum6 = 10
          elif lvl == 7:
            eNum6 = 10
          elif lvl == 8:
            eNum6 = 10
          elif lvl == 9:
            eNum6 = 10
          
          #if it is the last level
        else:
          #divider
          print("\n_______________________________________________\n")
          #telling the user that they won
          print("\nYOU WIN!")
          #Asking them if they want to play again or go back to the menu
          again = input("\nEnter 'y' to Play Again\nEnter 'n' to Go Back to the Menu\n")
          #divider
          print("\n_______________________________________________\n")
          
          #if the user wants to play again
          if again == "y":
          # The variables get reset to their initialized values
            count = 0 
            lvl = 1
            
            eNum1 = 10
            eNum2 = 10
            eNum3 = 0
            eNum4 = 0
            eNum5 = 0
            eNum6 = 0
            eNum7 = 0 
            eNum8 = 0 
            eNum9 = 0 
            eNum10 = 0 
          
          #if they don't want to play again
          if again == "n":
            #thanks the user for playing
            print("\nThank you for playing!")
            #a delay to allow the user to read the thank you message before the menu shows up
            time.sleep(1)
            #divider
            print("\n_________________________________________________________________\n")
    #================ END OF GAME LOOP ==========================

  ############### SPRINTER ###############################################
  # If user wants to play "Sprinter", they type '5' into the "game" input
  if game == "5":
    
    #greeting the user
    print("Welcome to 'Sprinter'!")
    
    # Explaining how the game works
    print("\nINSTRUCTIONS:")
    print("The sprint is 25 steps.\n")
    print("One step is one press of the 'enter' key.\n")
    print("Every level has a maximum amount of time you can spend on it, you need to finish the sprint before time runs out!\n")
    print("Continuously press (DO NOT press and hold) the 'enter' key on your keyboard to take multiple steps. \n")
    print("The timer for every level begins once you press 'enter' for the first time!\n")
    print("Finish level 10 and YOU WIN!\n")
    
    print("\n_______________________________________________\n")
    
    #===== Initializers ===================
    lvl = 0
    again = "y"
    
    #=========== BEGINNING OF GAME LOOP =======================
    while again == "y":
      #whenever this loop runs, it is a another level, so level increases by one
      lvl += 1
      
      #There is 10 levels
      #Each level has it's maximum amout of time. The player needs to finish the level before they run out of time
      if lvl == 1:
        #"maxTime" is measured in seconds
        maxTime = 20
        
      elif lvl == 2:
        maxTime = 15
        
      elif lvl == 3:
        maxTime = 13
        
      elif lvl == 4:
        maxTime = 10
        
      elif lvl == 5:
        maxTime = 8 
        
      elif lvl == 6:
        maxTime = 6   
        
      elif lvl == 7:
        maxTime = 5
        
      elif lvl == 8:
        maxTime = 4
        
      elif lvl == 9:
        maxTime = 3.5
        
      elif lvl == 10:
        maxTime = 3.25
        
      #Level header
      print("\n====== LEVEL", lvl, "======")
      #Reiterating that the sprint is 25 steps
      print("\nThe sprint is 25 steps!")
      #Telling the user the corresponding time limit on the level
      print("\nOBJECTIVE:")
      print("Finish it in less than [ ", maxTime, " ] seconds!")
      
      #The player has taken 0 steps at the beginning of every level
      steps = 0
      
      #Declaring the start time value to use for the first run of the while loop
      #This value gets replaced by the value in the while loop, between the "key" variable and the "steps variable"
      #This is to start the timer when the player takes their first step
      start = round(time.time())
      
      #rounding time.time() to make it an integer and not a float
      
      #time.time() is the seconds from Jan 1 1970 to now
      #If I store the value of the time when the user presses enter for the first time and when the user finishes the race. 
      #I can subtract the two to see how much time has passed
      
      # The loop runs if the time that has passed is less than the "maxTime"
      while round(time.time()) - start < maxTime and steps < 25:
        #User presses the 'enter' key
        key = input()
        #Storing the time value of when the user first pressed the 'enter' key
        #reassigning 'start'
        if steps == 0:
          start = round(time.time())
        #when the user presses 'enter' once, steps goes up by 1
        steps += 1
        #displays the step count for every step the user takes
        print(steps, "_")
      
      #if the user reaches 25 steps
      if steps == 25:
        #tells them they have finished the level
        print("\nYou have reached the FINISH LINE!")
        #if it is the last level
        if lvl == 10:
          #divider
          print("\n_______________________________________________\n")
          #tells the user that they won
          print("\nYOU WIN!")
          #declaring the 'stop' variable
          stop = ""
          #since the user is constantly pressing the 'enter' key, this loop allows the user to stop pressing before displaying the "again" message
          while stop != "y":
            stop = input("\nEnter 'y' to indicate that you've stopped pressing then enter key.")
          #Asks the user if they want to play again or go back to the main menu
          again = input("\nEnter 'y' to Play Again\nEnter 'n' to Go Back to the Menu\n")
          
          #divider
          print("\n_______________________________________________\n")
          
          #if they want to play again
          if again == "y":
            #the level variable resets to 0
            lvl = 0
          #if they want to go back to the menu
          if again == "n":
            #Thanks the user for playing
            print("\nThank you for playing!")
            #delay so that the user can see the message before the menu pops up
            time.sleep(1)
            #divider
            print("\n_________________________________________________________________\n")
      # if the user did not reach 25 steps on a level
      else:
        #divider
        print("\n_______________________________________________\n")
        #tells the user that it is GAME OVER
        print("\nGAME OVER!")
        #divider
        print("\n_______________________________________________\n")
        #delcaring 'stop'
        stop = ""
        #To allow the user to stop pressing the 'enter' key before displaying the next message
        while stop != "y":
          stop = input("\nEnter 'y' to indicate that you've stopped pressing the enter key.")
        #divider
        print("\n_______________________________________________\n")
        #asks the user if they would like to play again or go back to the menu
        again = input("\nEnter 'y' to Play Again\nEnter 'n' to Go Back to the Menu\n")
        #divider
        print("\n_______________________________________________\n")
        
        #if they want to play again
        if again == "y":
          #"lvl" gets reset to 0
          lvl = 0
        #if they want to go to the menu
        if again == "n":
          #Thanks them for playing
          print("\nThank you for playing!")
          #Delay so the user can see the message before the menu pops up
          time.sleep(1)
          #divider
          print("\n_________________________________________________________________\n")
    #================ END OF GAME LOOP ==========================







