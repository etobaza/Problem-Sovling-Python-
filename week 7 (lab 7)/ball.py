import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
x = 50
y = 50
color = (255, 0, 0)
clock = pygame.time.Clock()
speed = 20

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 20
        if pressed[pygame.K_DOWN]: y += 20
        if pressed[pygame.K_LEFT]: x -= 20
        if pressed[pygame.K_RIGHT]: x += 20

        if x > 375:
                x = 375
        if y > 275:
                y = 275
        if x < 25:
                x = 25
        if y < 25:
                y = 25

        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, color, (x, y), 25)
        pygame.display.flip()
        clock.tick(30)