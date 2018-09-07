
import mysql
import mysql.connector

#database = mysql.connecter.connect("localhost", "hangman", "noose", "dbhangman")

# this takes the three variables below and saves them
def saved_data(magicWord, listOfCorrectGuesses, guessNumber):

    save_string = "".join(listOfCorrectGuesses)  # converting to string because list can't be saved
    guessN_string_convert = str(guessNumber)   # converting to string because int's can't be saved

    filetoWrite = open("saveData.txt", 'w')  # finding the file to save to and letting them know we want to write
    filetoWrite.write(magicWord + "\n" + save_string + "\n" + guessN_string_convert)  # saving each item on a new line
    filetoWrite.close()


def read_data():

    # Got code below from Stackoverflow, added the return array and ins.close() part for usage in my code
    # https://stackoverflow.com/questions/3277503/in-python-how-do-i-read-a-file-line-by-line-into-a-list
    with open("saveData.txt", "r") as ins:  # to open file you want to read
        array = []  # Blank array to add data
        for line in ins:  # will go through each line that is saved
            array.append(line)  # adding the line read to the array

    ins.close()  # closing out the
    #print(array) # used to test data
    return array  # returning the arrary for use

































































# mySQL username is hangman
# mySQL password is noose
# database name is dbhangman