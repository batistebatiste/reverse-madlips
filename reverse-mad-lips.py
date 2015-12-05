# Level easy
easy = [["Paris", "Tokyo", "Moscow", "Seoul"], "_1_ is the capital of France. _2_ is the capital of Japan. _3_ is the capital of Russia. _4_ is the capital of South Korea."]
# easy[0]=["Paris","Tokyo","Moscow","Seoul"]
# easy[1]= "_1_ is the capital of France. _2_ is the capital of Japan.
# _3_ is the capital of Russia. _4_ is the capital of South Korea."

# Level Medium
medium = [["Beijing", "Jakarta", "Cairo", "Ankara"], "_1_ is the capital of China. _2_ is the capital of Indonesia. _3_ is the capital of Egypt. _4_ is the capital of Turkey"]

# Level Hard
hard = [["Belgrad", "Tripoli", "Budapest", "Warsaw"], "_1_ is the capital of Serbia. _2_ is the capital of Lybia. _3_ is the capital of Hungary. _4_ is the capital of Poland."]


# function to check if the user's input is correct
def check(guess, correct):
    """
    does check if the user's guess is correct. 
    :param check: the user's guess and the correct answer 
    return: a boolean value
    """
    if guess == correct:
        return True
    else:
        return False


def play_game(level):
    """
    This is the function that let's you play the game for a given level
    :param play_game: the level (of difficulty) the user chose
    :return text when the level is completed with success 
    """
    print level[1]
    index = 0
    # the loop to go over every answer/response
    for cities in level[0]:
        user_input = raw_input("What city is " + str(index + 1) + "?: ")
        # check if the entry is correct et redemander jusqu a ce que le user mette la reponse correcte
        while not check(user_input, level[0][index]):
            user_input = raw_input("Wrong! Try again, what city is " + str(index + 1) + "?: ")
        print "correct!"
        # reprint the completed version of the txt. a chaque fois que t'as une rep bon il faut printer le txt avec le bon mot
        level[1] = level[1].split()
        blank_spot_nr = "_" + str(index + 1) + "_"
        x = 0
        for word in level[1]:
            if word == blank_spot_nr:
                level[1][x] = level[0][index]
            x += 1   
        level[1] = " ".join(level[1])
        index = index + 1
        print level[1]
    # you won the game
    text = "You got it right! congrats"
    return text


# choose the level you want to play and return the appropriate variable (list) so the play_game function can use it
def chose_level():
    """
    this function gives the user the possibility to choose among 3 level of difficulty
    :param chose_level: none
    :return: a list easy, medium or hard with the form list[["capital1]", "capital2"], "_1_ is the capital of country 1. _2_ is the capital of country 2"]
    """ 
    difficulty = raw_input("Type the difficulty level you want to play: easy, medium or hard: ")
    # check for correct entry
    while difficulty not in ("easy", "medium", "hard"):
        difficulty = raw_input("you did not enter a valid level. Type the difficulty level you want to play: easy, medium or hard: ")
    if difficulty == "easy":
        return easy
    if difficulty == "medium":
        return medium
    if difficulty == "hard":
        return hard


# to play the game reverse mad lips
print play_game(chose_level())
# le pb c'est qu'il l'interprete comme ca: print play_game("hard")