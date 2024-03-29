from random import randint
import math

# A game where the user has to guess a random number in the range of two numbers the player chooses
def number_guessing_game():

    #show instructions
    print("\n-----Welcome to the number guessing game.-----\n" 
          "Here are the intstructions:\n\n"
          "1. You will enter two numbers (Make sure the first is less than the second).\n"
          "2. I will choose a number between (and including) those two numbers.\n"
          "3. You have to guess the number I choose.\n"
          "4. We will calculate the maximum number of guesses based on the range you give us.\n"
          "5. If you get the number before you use up all your guesses, you win!\n"
          "Good luck :)\n")
    
    while True:
        #user inputs lower and upper number of guessing range
        x1=input("Enter the lower number of the range (enter 'Quit' at any time to quit): ")
        #quit function
        if x1.lower() == 'quit':
             print("\n-----Bye! Thanks for playing our game!-----")
             break
        #check that input is a number
        try:
            x=int(x1)
        #if input is string other than "quit", go back to start
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
                #if input is string other than 'quit', go back to start
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
                        for i in range(1, number_of_guesses+1):
                            print(f"\nGuesses left: {number_of_guesses}")
                            try:
                                attempt1=input("Enter a guess of what the number is\n(if you do not enter a number or enter nothing, the game will end): ")    
                                #end game if input left empty
                                if attempt1 == "":
                                    print("-----Please enter a number ONLY-----\n"
                                      "-----GAME OVER-----\n")
                                    break
                                attempt=int(attempt1)
                            #end game if string is entered instead of number
                            except ValueError:
                                print("-----Please enter a number ONLY-----\n"
                                      "-----GAME OVER-----\n")
                                break
                            else:
                                #message if guess is higher than answer
                                if attempt > answer:
                                    number_of_guesses -= 1
                                    if number_of_guesses >0:
                                        print("Try again! You guessed too high!")
                                    #end game if out of guesses
                                    elif number_of_guesses == 0:
                                        print("\nYou ran out of guesses! Better luck next time.\n"
                                              f"The answer was {answer}!"
                                              "\n-----GAME OVER-----\n")
                                        break
                                #message if guess is lower than answer
                                elif attempt < answer:
                                    number_of_guesses -= 1
                                    if number_of_guesses >0:
                                        print("Try again! You guessed too low!")
                                    #end game if out of guesses
                                    elif number_of_guesses == 0:
                                        print("\nYou ran out of guesses! Better luck next time.\n"
                                              f"The answer was {answer}!"
                                              "\n-----GAME OVER-----\n")
                                        break
                                #end game and message if player guesses the right answer!
                                elif attempt==answer:
                                    print(f"\n-----Congratulations, you won!-----\nYou got the answer in {i} guesses. "
                                          "Thanks for playing :)\n")
                                    break
                        break





number_guessing_game()