import typing

# Identify module as main
# setting up main game loop and end game conditions
if __name__ == '__main__':
    # win condition
    # variable for game word
    WORD == "TESTS"
    try:
        while True:
        # variable for guess word
            GUESS = "BREAD"
            if WORD == GUESS:
                print("Well done, you've won!")
                break
    # exit condition
    except KeyboardInterrupt:
        print("Game Ended.")

def get_player_guess(wordlen: int, worlist: typing.Set[str]) -> str:
    """
    Ask player for word guess,
    function takes the length of the expected guess (int) and list of avaiilable game words (str).
    it will return type string (player guess). 
    Call validate function that will evaluate if the guess is in the right format,
    if not print an error and ask to re-enter a guess,
    if correct format, break and return the guess.
    """
    # continue to loop until a valid guess is received 
    while True: 
        # defines "guess" variable as user guess
        guess = input("Type a word: ")
        # overwrite variable guess with validation evaluation
        error, guess = validate(guess=guess, wordlen=wordlen, wordlist=wordlist)
        # if no error detected stop asking for input
        if error is None:
            break
        print(error)
    
    return guess

def validate(guess: str, wordlen: int, wordlist: typing.Set[str]) -> typing.Tuple[str,str]:
    """
    Validate a guess from the player.
    Takes in guess as string, length of game word and list of possible game words.
    Returns tuple of any error and the guess word converted to upper case.
    If no error is detected, None is returned for error.
    """
    # change guess into upper case if not already
    guess_upper = guess.upper()
    # if the length of the guess is not equal to the game word 
    # length return validation message
    if len(guess_upper) != wordlen:
        # return a tuple consisting of error and the guess word
        return f"Oops! Guess must be a length of {wordlen}, try again", guess_upper
    # if the guess is not in the wordlist of valid word guesses, return validation error message
    if guess_upper not in wordlist:
        # return a tuple consisting of error and the guess word
        return "Hmm, your guess doesn't appear to be a recognised word, try again.", guess_upper
    # if no error detected return tuple of None and the guess word  
    return None, guess_upper