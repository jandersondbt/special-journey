import os, time, pygame

# SOUND
pygame.mixer.init()
pygame.mixer.music.load("/home/jandersonxyz/Temp/xyz/others/recycling_really_is_a_concept.flac")
pygame.mixer.music.play(-1)

# STATISTICS
start = time.time()
count = 0
# ... other imports .............................
usernames = []

try:
    while 1 != 2:
        os.system('clear')
        print(usernames)
        print("Ctrl-C to quit...")

        username = input(f'\n> Enter your username: ')
        count += 1
        usernames.append(username)

except KeyboardInterrupt:
    os.system('clear')
    elapsed = time.time() - start
    print(f"The program ran about {elapsed:.2f} seconds")
    print(f"You've ran about {count} iterations")
    print(f"\n--> Your final list: {usernames}")


