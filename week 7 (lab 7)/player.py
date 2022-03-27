import pygame
import os

# Setup
pygame.init()
running = True
play = False

screen = pygame.display.set_mode((800, 300))
font = pygame.font.SysFont("Futura", 40)
font2 = pygame.font.SysFont("Futura", 20)\

text = font.render("Music Player", True, (0, 0, 0))
text2 = font2.render("[W - Play] [O - Unpause] [P - Pause] [Q - Previous] [E - Next]", True, (0, 0, 0))

# Assets
disc = pygame.image.load(open('week 7 (lab 7)/assets/player_disc.png')) 
disc = pygame.transform.scale(disc, (160, 150))
folder = os.listdir("week 7 (lab 7)/assets/songs")
cnt = 0
pygame.mixer.music.load("week 7 (lab 7)/assets/songs/"+folder[cnt])

while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
            
            # Player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    pygame.mixer.music.play(0)
                if event.key == pygame.K_o:
                    pygame.mixer.music.unpause()
                if event.key == pygame.K_p:
                    pygame.mixer.music.pause()
                if event.key == pygame.K_e:
                    if cnt < 2 and cnt != 2:
                     cnt+=1
                     pygame.mixer.music.load("week 7 (lab 7)/assets/songs/"+folder[cnt])
                     pygame.mixer.music.play()
                    elif cnt == 2:
                     cnt = 0
                     pygame.mixer.music.load("week 7 (lab 7)/assets/songs/"+folder[cnt])
                     pygame.mixer.music.play()
                if event.key == pygame.K_q:
                    if cnt == 0:
                     cnt = 2
                     pygame.mixer.music.load("week 7 (lab 7)/assets/songs/"+folder[cnt])
                     pygame.mixer.music.play()
                    elif cnt == 2:
                     cnt = 1
                     pygame.mixer.music.load("week 7 (lab 7)/assets/songs/"+folder[cnt])
                     pygame.mixer.music.play()
                    elif cnt == 1:
                     cnt = 0
                     pygame.mixer.music.load("week 7 (lab 7)/assets/songs/"+folder[cnt])
                     pygame.mixer.music.play()
                     
        screen.fill((255, 255, 255))
        screen.blit(text, (290, 240))
        screen.blit(text2, (190, 280))
        screen.blit(disc, (296, 80))
        pygame.display.flip()