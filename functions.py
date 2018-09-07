

def numberOfSpaces(magicWord): # this function go through how many letters there are in the word for the user to guess and will show blank spaces for them

    spaces_needed = len(magicWord)
    display_word = ""
    for i in range(0, spaces_needed):
        display_word = display_word + "_ "

    return display_word

def letterCheck(char, magicWord): # this function will check if the users letter guess matches one of the letters in the magic word

    return_me_letter = ""
    returnMeNoose = 0  # zero

    for i in magicWord: # checking each letter in magicword to see if it matches
        if char == i:
            return_me_letter = char
            print("Correct!") # letting user know it was correct
            return return_me_letter  # could probably just return char

    print("Nope sorry") # letting user know their guess was no good
    return returnMeNoose

def displayWordForUser(listLetters, magicWord):  # this def will display what the user has got so far

    if not listLetters: # will show how many spaces there are for the user
        showing_blank_spaces = numberOfSpaces(magicWord)
        #print("_ _ _ _ _ ")
        return showing_blank_spaces

    display_word_for_user = ""
    if len(listLetters) > 0:  # checks that the user has one correct letter before going through the stuff below
        for letter_Magic in magicWord: # going through each letter in magic word
            letter_check_empty = False  # used to make sure we add only one letter or one blank space for the magic word
            for letter_L in listLetters:  # going trough the list of correct letter guesses so far
                if letter_L == letter_Magic:  # do we have a match? do below
                    display_word_for_user = display_word_for_user + letter_L + " "  # adding the letter to the magic word for display
                    letter_check_empty = True
                    break
                #else:
                #    display_word_for_user = display_word_for_user + "_ "
            if letter_check_empty == False: # no match will just add a Blank line and a space
                display_word_for_user = display_word_for_user + "_ "

    win_check(display_word_for_user)

    return display_word_for_user

def win_check(display_word_for_user):  # this checks if the user wins and will stop asking for letters

    win_question_mark = True  # boolean for if user won, currently set to Win! or True

    for i in display_word_for_user:  # goes through the word will check for blank spaces meaning the user has not won
        if i in ["_", "_ "]:
            win_question_mark = False  # The user has not won yet

    if win_question_mark == True:  # if the user wins, will do below
        print("You Win !!!!!!!!")  # letting user know they won
        exit(0)


