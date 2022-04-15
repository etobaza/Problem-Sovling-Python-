import pygame
import random
import threading
import time
pygame.init()

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
LINE_COLOR = (50, 50, 50)
HEIGHT = 400
WIDTH = 400
BLOCK_SIZE = 20
FOOD_SCORE = 0
font = pygame.font.SysFont("Verdana", 16)
level = 1
speed = 5

if level == 2:
    time.sleep(5)

class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


class Wall:
    def __init__(self):
        global level
        self.body = []
        f = open("week 8 and 9/levels/level{}.txt".format(level), "r")

        for y in range(0, HEIGHT // BLOCK_SIZE + 1):
            for x in range(0, WIDTH // BLOCK_SIZE + 1):
                if f.read(1) == '#':
                    self.body.append(Point(x, y))

    def draw(self):
        for point in self.body:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (226, 135, 67), rect)


class Food:
    def __init__(self, wall, snake):
        self.pos1, self.pos2 = twoRandomPos(wall, snake)
        self.location = Point(self.pos1, self.pos2)

    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (235, 0, 0), rect)

    def redrawFood(self, wall, snake):
        global FOOD_SCORE
        self.pos1, self.pos2 = twoRandomPos(wall, snake)
        self.location = Point(self.pos1, self.pos2)
        FOOD_SCORE += 1

class SuperFood:

    def __init__(self, wall, snake, food):
        self.pos1, self.pos2 = twoRandomPos(wall, snake)
        self.location = Point(self.pos1, self.pos2)

    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), rect)

    def redrawFood(self, wall, snake):
        global FOOD_SCORE
        self.pos1, self.pos2 = twoRandomPos(wall, snake)
        self.location = Point(self.pos1, self.pos2)
        FOOD_SCORE += 3

class Snake:
    def __init__(self):
        self.body = [Point(10, 5)]
        self.dx = 0
        self.dy = 0

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # Moving direction
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        if self.body[0].x * BLOCK_SIZE > WIDTH - BLOCK_SIZE:
            pygame.quit()
        if self.body[0].y * BLOCK_SIZE > HEIGHT - BLOCK_SIZE:
            pygame.quit()
        if self.body[0].x < 0:
            pygame.quit()
        if self.body[0].y < 0:
            pygame.quit()

    def draw(self):
        
        # Move head
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (0, 255, 0), rect)

        # Move body
        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (0, 255, 0), rect)

    def isCollideFood(self, food, wall):
        # Check food collision
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                self.body.append(Point(food.location.x, food.location.y))
                return True


    def isCollideSuperFood(self, superfood, wall):
        # Check food collision
        if self.body[0].x == superfood.location.x:
            if self.body[0].y == superfood.location.y:
                self.body.append(Point(superfood.location.x, superfood.location.y))
                return True
        
    def isCollideWall(self, wall):
        # Check wall collision
        wallPos = []
        for i in wall.body:
            wallPos.append((i.x, i.y))
        if (self.body[0].x, self.body[0].y) in wallPos:
            pygame.quit()

    def isCollideSelf(self):
        # Check own body collision
        for point in self.body[1:]:
            if point.x == self.body[0].x and point.y == self.body[0].y:
                    pygame.quit()


# Check if available
def isEmptyPos(randPos1, randPos2, wall, snake):
    WallSnakePos = []
    for i in wall.body:
        WallSnakePos.append((i.x, i.y))
    for i in snake.body:
        WallSnakePos.append((i.x, i.y))
    if (randPos1, randPos2) in WallSnakePos:
        return False
    return True

# Assign two random positions
def twoRandomPos(wall, snake):
    check = False
    while not check:
        pos1 = random.randint(0, 19)
        pos2 = random.randint(0, 19)
        if isEmptyPos(pos1, pos2, wall, snake):
            return pos1, pos2


def main():
    global SCREEN, CLOCK, level, speed
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    # Vars
    wall = Wall()
    snake = Snake()
    food = Food(wall, snake)
    superfood = SuperFood(wall, snake, food)

    # Redraw SuperFood after 8 seconds
    def redrawTime():
        global FOOD_SCORE
        FOOD_SCORE -= 3
        SuperFood.redrawFood(superfood, wall, snake)
        threading.Timer(8, redrawTime).start()
    redrawTime()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and snake.dx != -1:
                    snake.dx = 1
                    snake.dy = 0
                if event.key == pygame.K_LEFT and snake.dx != 1:
                    snake.dx = -1
                    snake.dy = 0
                if event.key == pygame.K_UP and snake.dy != 1:
                    snake.dx = 0
                    snake.dy = -1
                if event.key == pygame.K_DOWN and snake.dy != -1:
                    snake.dx = 0
                    snake.dy = 1

        snake.move()
        snake.isCollideSelf()
        snake.isCollideFood(food, wall)
        snake.isCollideSuperFood(superfood, wall)
        snake.isCollideWall(wall)

        SCREEN.fill(BLACK)
        if snake.isCollideFood(food, wall):
            Food.redrawFood(food, wall, snake)
            snake.body.pop(-1)

        if snake.isCollideSuperFood(superfood, wall):
            SuperFood.redrawFood(superfood, wall, snake)
        
        snake.draw()
        wall.draw()
        food.draw()
        superfood.draw()
        drawGrid()

        if FOOD_SCORE >= 10:
            level = 2
            speed = 7
            wall = Wall()

        SCREEN.blit(font.render("Score: " + str(FOOD_SCORE), True, YELLOW), (10, 10))
        SCREEN.blit(font.render("Level: " + str(level), True, YELLOW), (10, 30))
        pygame.display.update()
        CLOCK.tick(speed)


def drawGrid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, LINE_COLOR, rect, 1)

main()
