

import hangmanPic
import functions
import randomWord
import mySQLpyFile
import userInterface

guessNumber = 0  # this number counts how many times you got something wrong. 

magicWord = randomWord.random_choice_from_lists()  # get the word user needs to guess
#print(magicWord)  #used for testing code

listOfCorrectLetters = []  # this list is used for checking against the magic word

successOrBust = False
while successOrBust != True:  # will continue to go, until user is dead or they guess the correct word.
   print(hangmanPic.hangmanPic(guessNumber))  # will display the little hangman
   if guessNumber >= 6:  # will end the game if to many wrong guesses
        print("The hangman word was: " + magicWord)  # lets the user know what word they should have figured out
        exit(0)
   print(functions.displayWordForUser(listOfCorrectLetters, magicWord))  # shows what they got right if any
   print("Other options to type in: quit, save, load, hint")
   userGuess = userInterface.userInput()  # will summon function that gets user input
   if userGuess == "quit":
       exit(0)
   elif userGuess == "hint":
       list_name = (randomWord.random_list_choice())   # todo add hint, not quite working right
       print(list_name)
       guessNumber = guessNumber - 1   # this will cancel out the negative effects from asking for a hint  todo make a function?
   elif userGuess == "save":
        mySQLpyFile.saved_data(magicWord, listOfCorrectLetters, guessNumber)
        guessNumber = guessNumber - 1  # this will cancel out the negative effects from asking for a save
   elif userGuess == "load":
       data_array = mySQLpyFile.read_data()  # calling a function to read data
       #print(data_array)  # used for data testing
       magicWord = (data_array[0]).rstrip()  # this will make the magic word what it was saved as
       list_O_letters = "" + (data_array[1]).rstrip()  # this is a string to put the data from the array into
       for i in list_O_letters:  # going trought each letter in the string
           listOfCorrectLetters.append(i)  # adding it to the correct list of letters
       guessNumber = int((data_array[2]).rstrip())  # getting guess number from the array
       guessNumber = guessNumber - 1
   else:
       correctOrNot = functions.letterCheck(userGuess, magicWord)
       if correctOrNot == 0:  # if user got it wrong will add to guess number
            guessNumber = guessNumber + 1
       else:
            listOfCorrectLetters.append(correctOrNot)  # adding to the list of correct letters in the selected word


# use loops, functions, if-statements; you should read/write from a file; use exception handling where appropriate.
# Use functions to organize your code into logical blocks*.
# Use classes appropriately to organize and structure your program.
# Separate the game logic from the user interface
