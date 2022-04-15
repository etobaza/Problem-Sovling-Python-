import pygame
import sys
from pygame.locals import *

DISPLAYSURF = pygame.display.set_mode((1000, 800))

# Colors

GREEN = (0, 255, 0)
GRAY = (197, 197, 197)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_GRAY = (107, 104, 99)
PINK = (249, 57, 255)
LIGHT_BLUE = (54, 207, 241)
YELLOW = (255, 241, 73)
ORANGE = (252, 155, 64)
PURPLE = (167, 0, 238)
DARK_GREEN = (58, 158, 73)
WHITE = (255, 255, 255)
BROWN = (85, 46, 46)
BLUE_ANOTHER = (0, 238, 195)

RADIUS = 25
BRUSH_SIZE = 5
draw = False
figurePicked = False
brush_color = GREEN
figure = "circle"

# Images
circle = pygame.image.load("week 8 and 9/assets/circle.jpg")
rectangle = pygame.image.load("week 8 and 9/assets/rectangle.jpg")
square = pygame.image.load("week 8 and 9/assets/square.png")
right_triangle = pygame.image.load("week 8 and 9/assets/rtriangle.jpg")
eq_triangle = pygame.image.load("week 8 and 9/assets/eqtriangle.png")
rhombus = pygame.image.load("week 8 and 9/assets/rhombus.png")
eraser = pygame.image.load("week 8 and 9/assets/eraser.jpg")

circle_button = pygame.transform.scale(circle, (40, 40))
rectangle_button = pygame.transform.scale(rectangle, (40, 40))
square_button = pygame.transform.scale(square, (40, 40))
right_triangle_button = pygame.transform.scale(right_triangle, (40, 40))
eq_triangle_button = pygame.transform.scale(eq_triangle, (40, 40))
rhombus_button = pygame.transform.scale(rhombus, (40, 40))
eraser_button = pygame.transform.scale(eraser, (40, 40))

# Outlines for butttons
circle_rect = pygame.Rect(140, 5, 40, 40)
rectangle_rect = pygame.Rect(185, 5, 40, 40)
square_rect = pygame.Rect(230, 5, 40, 40)
right_triangle_rect = pygame.Rect(275, 5, 40, 40)
eq_triangle_rect = pygame.Rect(320, 5, 40, 40)
rhombus_rect = pygame.Rect(365, 5, 40, 40)

pygame.init()

# Fonts
body_font = pygame.font.Font(None, 40)
clear_font = pygame.font.Font(None, 50)
clear_text = clear_font.render("CLEAR", True, BLACK)


# Interface
menu_rect = pygame.Rect(0, 0, 1000, 130)
screen_rect = pygame.Rect(0, 100, 980, 720)

# Colors outlines
red_rect = pygame.Rect(10, 5, 20, 20)
green_rect = pygame.Rect(35, 5, 20, 20)
blue_rect = pygame.Rect(60, 5, 20, 20)
yellow_rect = pygame.Rect(85, 5, 20, 20)
pink_rect = pygame.Rect(35, 30, 20, 20)
light_blue_rect = pygame.Rect(10, 55, 20, 20)
orange_rect = pygame.Rect(60, 55, 20, 20)
purple_rect = pygame.Rect(10, 30, 20, 20)
dark_green_rect = pygame.Rect(85, 30, 20, 20)
brown_rect = pygame.Rect(35, 55, 20, 20)
white_rect = pygame.Rect(60, 30, 20, 20)
pretty_blue_rect = pygame.Rect(85, 55, 20, 20)

clear_rect = pygame.Rect(5, 80, 120, 35)
eraser_rect = pygame.Rect(410, 5, 40, 40)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            draw = True
        if event.type == MOUSEBUTTONUP:
            draw = False
        if event.type == KEYDOWN:
            if event.key == K_r:
             BRUSH_SIZE += 5
        if event.type == KEYDOWN:
            if event.key == K_t and BRUSH_SIZE > 5:
             BRUSH_SIZE -= 5

    brush_text = body_font.render("BRUSH SIZE:" + str(BRUSH_SIZE), True, BLACK)
    
    # Draw logic
    mouse_pos = pygame.mouse.get_pos()
    if draw and mouse_pos[1] > 100 and not figurePicked:
        pygame.draw.circle(DISPLAYSURF, brush_color, mouse_pos, BRUSH_SIZE)

    # Figure logic
    mouse_pos = pygame.mouse.get_pos()
    if draw and mouse_pos[1] > 100 and figure == "circle" and figurePicked:
        pygame.draw.circle(DISPLAYSURF, brush_color, mouse_pos, RADIUS, 2)
        draw = False

    mouse_pos = pygame.mouse.get_pos()
    if draw and mouse_pos[1] > 100 and figure == "rectangle" and figurePicked:
        pygame.draw.rect(DISPLAYSURF, brush_color, pygame.Rect(mouse_pos[0], mouse_pos[1], 50, 25), 2)
        draw = False

    mouse_pos = pygame.mouse.get_pos()
    if draw and mouse_pos[1] > 100 and figure == "square" and figurePicked:
        pygame.draw.rect(DISPLAYSURF, brush_color, pygame.Rect(mouse_pos[0], mouse_pos[1], 50, 50), 2)
        draw = False

    mouse_pos = pygame.mouse.get_pos()
    if draw and mouse_pos[1] > 100 and figure == "right_triangle" and figurePicked:
        pygame.draw.polygon(DISPLAYSURF, brush_color,
                            [[mouse_pos[0], mouse_pos[1]], [mouse_pos[0], mouse_pos[1] + 50],
                             [mouse_pos[0] + 50, mouse_pos[1] + 50]], 2)
        draw = False

    mouse_pos = pygame.mouse.get_pos()
    if draw and mouse_pos[1] > 100 and figure == "eq_triangle" and figurePicked:
        pygame.draw.polygon(DISPLAYSURF, brush_color,
                            [[mouse_pos[0], mouse_pos[1]], [mouse_pos[0] - 35, mouse_pos[1] + 60],
                             [mouse_pos[0] + 35, mouse_pos[1] + 60]], 2)
        draw = False

    mouse_pos = pygame.mouse.get_pos()
    if draw and mouse_pos[1] > 100 and figure == "rhombus" and figurePicked:
        pygame.draw.polygon(DISPLAYSURF, brush_color,
                            [[mouse_pos[0], mouse_pos[1]], [mouse_pos[0] + 20, mouse_pos[1] + 35],
                             [mouse_pos[0], mouse_pos[1] + 70], [mouse_pos[0] - 20, mouse_pos[1] + 35]], 2)
        draw = False

    # Check if figure pressed
    if draw:
        if green_rect.collidepoint(mouse_pos):
            brush_color = GREEN
            figurePicked = False
        if red_rect.collidepoint(mouse_pos):
            brush_color = RED
            figurePicked = False
        if blue_rect.collidepoint(mouse_pos):
            brush_color = BLUE
            figurePicked = False
        if pink_rect.collidepoint(mouse_pos):
            brush_color = PINK
            figurePicked = False
        if light_blue_rect.collidepoint(mouse_pos):
            brush_color = LIGHT_BLUE
            figurePicked = False
        if yellow_rect.collidepoint(mouse_pos):
            brush_color = YELLOW
            figurePicked = False
        if orange_rect.collidepoint(mouse_pos):
            brush_color = ORANGE
            figurePicked = False
        if purple_rect.collidepoint(mouse_pos):
            brush_color = PURPLE
            figurePicked = False
        if dark_green_rect.collidepoint(mouse_pos):
            brush_color = DARK_GREEN
            figurePicked = False
        if white_rect.collidepoint(mouse_pos):
            brush_color = WHITE
            figurePicked = False
        if brown_rect.collidepoint(mouse_pos):
            brush_color = BROWN
            figurePicked = False
        if pretty_blue_rect.collidepoint(mouse_pos):
            brush_color = BLUE_ANOTHER
            figurePicked = False
        if eraser_rect.collidepoint(mouse_pos):
            brush_color = BLACK
            figurePicked = False
        if clear_rect.collidepoint(mouse_pos):
            pygame.draw.rect(DISPLAYSURF, BLACK, screen_rect)


    pygame.draw.rect(DISPLAYSURF, WHITE, menu_rect)
    pygame.draw.rect(DISPLAYSURF, YELLOW, clear_rect)
    DISPLAYSURF.blit(clear_text, (5, 80))
    DISPLAYSURF.blit(brush_text, (140, 60))

    # Change figure
    if draw:
        if circle_rect.collidepoint(mouse_pos):
            figure = "circle"
            figurePicked = True
        if square_rect.collidepoint(mouse_pos):
            figure = "square"
            figurePicked = True
        if rectangle_rect.collidepoint(mouse_pos):
            figure = "rectangle"
            figurePicked = True
        if right_triangle_rect.collidepoint(mouse_pos):
            figure = "right_triangle"
            figurePicked = True
        if eq_triangle_rect.collidepoint(mouse_pos):
            figure = "eq_triangle"
            figurePicked = True
        if rhombus_rect.collidepoint(mouse_pos):
            figure = "rhombus"
            figurePicked = True

    # Color panel
    pygame.draw.rect(DISPLAYSURF, GREEN, green_rect)
    if brush_color == GREEN:
        border = 2
    else:
        border = 1
    pygame.draw.rect(DISPLAYSURF, BLACK, green_rect, border)

    pygame.draw.rect(DISPLAYSURF, RED, red_rect)
    if brush_color == RED:
        border = 2
    else:
        border = 1
    pygame.draw.rect(DISPLAYSURF, BLACK, red_rect, border)

    pygame.draw.rect(DISPLAYSURF, BLUE, blue_rect)
    if brush_color == BLUE:
        border = 2
    else:
        border = 1
    pygame.draw.rect(DISPLAYSURF, BLACK, blue_rect, border)

    pygame.draw.rect(DISPLAYSURF, PINK, pink_rect)
    if brush_color == PINK:
        border = 2
    else:
        border = 1
    pygame.draw.rect(DISPLAYSURF, BLACK, pink_rect, border)

    pygame.draw.rect(DISPLAYSURF, LIGHT_BLUE, light_blue_rect)
    if brush_color == LIGHT_BLUE:
        border = 2
    else:
        border = 1
    pygame.draw.rect(DISPLAYSURF, BLACK, light_blue_rect, border)

    pygame.draw.rect(DISPLAYSURF, YELLOW, yellow_rect)
    if brush_color == YELLOW:
        border = 2
    else:
        border = 1
    pygame.draw.rect(DISPLAYSURF, BLACK, yellow_rect, border)

    pygame.draw.rect(DISPLAYSURF, ORANGE, orange_rect)
    if brush_color == ORANGE:
        border = 2
    else:
        border = 1
    pygame.draw.rect(DISPLAYSURF, BLACK, orange_rect, border)

    pygame.draw.rect(DISPLAYSURF, ORANGE, orange_rect)
    if brush_color == ORANGE:
        border = 2
    else:
        border = 1
    pygame.draw.rect(DISPLAYSURF, BLACK, orange_rect, border)

    pygame.draw.rect(DISPLAYSURF, DARK_GREEN, dark_green_rect)
    if brush_color == DARK_GREEN:
        border = 2
    else:
        border = 1
    pygame.draw.rect(DISPLAYSURF, BLACK, dark_green_rect, border)

    pygame.draw.rect(DISPLAYSURF, PURPLE, purple_rect)
    if brush_color == PURPLE:
        border = 2
    else:
        border = 1
    pygame.draw.rect(DISPLAYSURF, BLACK, purple_rect, border)

    pygame.draw.rect(DISPLAYSURF, WHITE, white_rect)
    if brush_color == WHITE:
        border = 2
    else:
        border = 1
    pygame.draw.rect(DISPLAYSURF, BLACK, white_rect, border)

    pygame.draw.rect(DISPLAYSURF, BROWN, brown_rect)
    if brush_color == BROWN:
        border = 2
    else:
        border = 1
    pygame.draw.rect(DISPLAYSURF, BLACK, brown_rect, border)

    pygame.draw.rect(DISPLAYSURF, BLUE_ANOTHER, pretty_blue_rect)
    if brush_color == BLUE_ANOTHER:
        border = 2
    else:
        border = 1
    pygame.draw.rect(DISPLAYSURF, BLACK, pretty_blue_rect, border)

    # Clear button
    DISPLAYSURF.blit(eraser_button, eraser_rect)
    if brush_color == BLACK:
        border = 2
    else:
        border = 1
    pygame.draw.rect(DISPLAYSURF, BLACK, eraser_rect, border)


    if figure == "circle":
        figure_outline = 2
    else:
        figure_outline = 1
    DISPLAYSURF.blit(circle_button, (140, 5))
    pygame.draw.rect(DISPLAYSURF, BLACK, circle_rect, figure_outline)

    if figure == "square":
        figure_outline = 2
    else:
        figure_outline = 1
    DISPLAYSURF.blit(square_button, (230, 5))
    pygame.draw.rect(DISPLAYSURF, BLACK, square_rect, figure_outline)


    if figure == "rectangle":
        figure_outline = 2
    else:
        figure_outline = 1
    DISPLAYSURF.blit(rectangle_button, (185, 5))
    pygame.draw.rect(DISPLAYSURF, BLACK, rectangle_rect, figure_outline)


    if figure == "right_triangle":
        figure_outline = 2
    else:
        figure_outline = 1
    DISPLAYSURF.blit(right_triangle_button, (275, 5))
    pygame.draw.rect(DISPLAYSURF, BLACK, right_triangle_rect, figure_outline)

    if figure == "eq_triangle":
        figure_outline = 2
    else:
        figure_outline = 1
    DISPLAYSURF.blit(eq_triangle_button, (320, 5))
    pygame.draw.rect(DISPLAYSURF, BLACK, eq_triangle_rect, figure_outline)

    if figure == "rhombus":
        figure_outline = 2
    else:
        figure_outline = 1
    DISPLAYSURF.blit(rhombus_button, (365, 5))
    pygame.draw.rect(DISPLAYSURF, BLACK, rhombus_rect, figure_outline)


    pygame.display.update()
