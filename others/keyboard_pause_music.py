import pygame


pygame.mixer.init()
pygame.mixer.music.load("/home/jandersonxyz/Temp/xyz/others/recycling_really_is_a_concept.flac")
pygame.mixer.music.play(-1) # Loop... I guess

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pygame.mixer.music.play
        print('Running...')
except KeyboardInterrupt:
    print('Stopped')
