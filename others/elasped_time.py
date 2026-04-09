import time
import pygame

pygame.mixer.init()
pygame.mixer.music.load("/home/jandersonxyz/Temp/xyz/others/recycling_really_is_a_concept.flac")
pygame.mixer.music.play(-1) # -1 = loop indefinitely
start = time.time()
print(start)
# ... your ..............
try:
    while 1 + 1 != 5:
        print('Yes')

except KeyboardInterrupt:
    print('cool')    

elapsed = time.time() - start
print(f'{elapsed:.2f}')
