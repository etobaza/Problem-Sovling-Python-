import pygame
import datetime

# Setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
reftime = pygame.time.Clock()
secpos = (390, 210)
minpos = (305, 210)

# Load images
clock = pygame.image.load(open('week 7 (lab 7)/assets/clock.png')) 
minarr = pygame.image.load(open('week 7 (lab 7)/assets/minutes.png'))
secarr = pygame.image.load(open('week 7 (lab 7)/assets/seconds.png'))

# Resize images
clock = pygame.transform.scale(clock, (800, 600))
secarr = pygame.transform.scale(secarr, (130, 100))
minarr = pygame.transform.scale(minarr, (100, 100))

def blitRotate(screen, image, pos, originPos, angle):

    # Offset from pivot to center
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]- originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # Roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # Roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # Get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # Rotate and blit the image
    screen.blit(rotated_image, rotated_image_rect)

pos = (screen.get_width()/2, screen.get_height()/2)

# Origin positions 
origin_s = [8, 100]
origin_m = [90, 100]

# Angles
angle_s = 0
angle_m = 0
date = datetime.datetime.now()

while running:
    reftime.tick(60)

    # Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Position clock image
    screen.blit(clock, (0, 0))

    # Blit functions
    blitRotate(screen, secarr, pos, origin_s, angle_s)
    blitRotate(screen, minarr, pos, origin_m, angle_m)
    angle_s = -(datetime.datetime.now().second/60 * 360)+45
    angle_m = -(datetime.datetime.now().minute/60 * 360)-40

    pygame.display.flip()


    
