from random import randint
import math

# A game where the user has to guess a random number in the range of two numbers they giev us
def number_guessing_game():

    #show instructions
    print("\n-----Welcome to the number guessing game.-----\n" 
          "Here are the intstructions:\n\n"
          "1. You will enter two numbers (Make sure the first is less than the second).\n"
          "2. I will choose a number between (and including) those two numbers.\n"
          "3. You have to guess the number I chose.\n"
          "4. We will calculate the maximum number of guesses based on the range you give us.\n"
          "5. If you get the number before you use up all your guesses, you win!\n"
          "Good luck :)\n")
    
    while True:
        #user inputs lowr and upper number of guessing range
        x1=input("Enter the lower number of the range (enter 'Quit' at any time to quit): ")
        #quit function
        if x1.lower() == 'quit':
             print("\n-----Bye! Thanks for playing our game!-----")
             break
        #check that input is a number
        try:
            x=int(x1)
        except ValueError:
                print("-----Please enter numbers or 'Quit' ONLY-----\n")
                continue
        else:
            y1=input("Enter the higher number of the range (enter ''Quit' at any time to quit): ")
            #quit function
            if y1.lower() == 'quit':
                print("\n-----Bye! Thanks for playing our game!-----")
                break
            else:
                #check that input is a number
                try:
                    y=int(y1)
                #if inputs are strings other than 'quit', go back to start
                except ValueError:
                    print("-----Please enter numbers or 'Quit' ONLY-----\n")
                    continue
                #continue if inputs are numbers
                else:
                    #if lower number is not less than higher number, go back to start
                    if x>y or x==y:
                        print("-----The higher number MUST BE greater than the lower number. Please input again.-----\n")
                        continue
                    else:
                        #set number of guesses and choose answer
                        number_of_guesses=int(math.log((y-x+1),2))
                        answer=randint(x,y)

                        #----------begin game----------
                        for attempt in range
                        print(f"\nGuesses left: {number_of_guesses}")
                        try:
                            attempt=int(input("Enter a guess of what the number is: "))
                        except ValueError:
                            print("-----Please enter a number ONLY-----\n")
                            continue
                        else: 





number_guessing_game()