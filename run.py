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
        error, guess = validate(guess=guess, wordlen=wrdlen, wordlist=wordlist)
        # if no error detected stop asking for input
        if error is None:
            break
        print(error)
    
    return guess

