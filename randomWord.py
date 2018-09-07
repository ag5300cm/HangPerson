
import random

wordList5 = ["range", "space", "never", "false", "month", "juicy", "fuzzy", "pizza", "quack"]

vegetables = ["broccoli", "celery", "cauliflower", "cabbage", "spinach", "lettuce", "onion", "rhubarb", "carrot"]
vegetables.extend(("turnip", "pumpkin", "potato", "cucumber"))

space_craft = ["sputnik", "vostok", "gemini", "apollo", "columbia", "challenger", "discovery", "atlantis", "endeavour"]
space_craft.extend(("enterprise", "voyager"))

movies = ["titanic", "scarface", "inception", "casablanca", "vertigo", "gladiator", "zootopia", "zombieland", "platoon"]
movies.extend(("batman", "halloween", "predator", "goodfellas", "grease", "avatar", "frozen", "psycho", "braveheart"))

list_of_lists = [vegetables, space_craft, movies]
def random_choice_from_lists() :

    choice_list = random_list_choice()
    #print(choice_list)  # used for testing code
    choice_word = random.choice(choice_list)
    return choice_word

def random_list_choice() :
    choice_list = random.choice(list_of_lists)
    return choice_list




