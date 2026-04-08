while True:
    numGuesses = 1
    while numGuesses <= 5:
        guess = ''
        while len(guess) != 5 or not guess.isdecimal(): # Whle it's not *this* keep asking for something
            print('x0')
            guess = input('> ')
