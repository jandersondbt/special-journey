guess = ''

while len(guess) != 3 or not guess.isdecimal():
    guess = input('Enter three digits: ')    
    if len(guess) == 1:
        print('\033[31m' + guess + '\033[0m')
    if len(guess) == 2:
        print('\033[32m' + guess + '\033[0m')
    if len(guess) == 3:
        print('\033[33m' + guess + '\033[0m')
    if len(guess) > 3:
        print('\033[34m' + guess + '\033[0m')
