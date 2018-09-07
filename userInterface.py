

# This is to try and meet the requirement of separating user interface from game logic

def userInput():
    userGuess = input("Care to guess a lowercase letter? ")  # getting user input
    userGuess = userGuess.lower()  # in case they guess a upper case letter
    return userGuess