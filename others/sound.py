import time, pygame

# SOUND SETTINGS
pygame.mixer.init()
pygame.mixer.music.load("/home/jandersonxyz/Temp/xyz/others/recycling_really_is_a_concept.flac")
pygame.mixer.music.play(-1)

# PASS STUFF
secretPass = 'abc'
userGuess = None

# COUNT AND TIME 
count = 0
start = time.time()

# COLOR
RED = '\033[31m'
BLUE = '\033[34m'
GREEN = '\033[32m'
RESET = '\033[32m'

try:
    while secretPass != userGuess:
        count += 1 # Counting iterations in while loop
        userGuess = input(f'\n> Enter three digits (abc), guess the correct permutation: ')
except KeyboardInterrupt:
    elapsed = time.time() - start
    print(f"\n{GREEN}About {count} iterations in total")
    print(f"Finalized in about {elapsed:.2f} seconds")   
    
