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
