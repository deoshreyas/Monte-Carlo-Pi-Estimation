import pygame  
from pygame.locals import *
from random import uniform
from math import hypot
pygame.init() 

# COLORS
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# WINDOW DIMENSIONS
WINDOW_WIDTH = 500 
WINDOW_HEIGHT = WINDOW_WIDTH + 100
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
pygame.display.set_caption("Pi Calculation using Monte Carlo Method")  
WINDOW.fill(WHITE)

# MONTE CARLO METHOD 
n = 30000 # total no of points
pointsInsideCircle = 0 
RADIUS = WINDOW_WIDTH/2

# GENERATING RANDOM POINTS
point_list = []
for i in range(n):
    x = uniform(1, WINDOW_WIDTH)
    y = uniform(1, WINDOW_WIDTH)
    point = (x, y)
    point_list.append(point)

# CALCULATING NO OF POINTS INSIDE CIRCLE
for i in point_list:
    dist = hypot(WINDOW_WIDTH/2-i[0], WINDOW_WIDTH/2-i[1])
    if dist<RADIUS:
        pointsInsideCircle += 1

# PROGRAM FUNCTIONS 
def draw_circle():
    pygame.draw.circle(WINDOW, BLACK, (WINDOW_WIDTH/2, WINDOW_WIDTH/2), RADIUS, width=1)

currentPointIndex = 0
currentPi = 0
pointsInCircle = 0
def draw_random_point():
    global currentPointIndex, pointsInCircle
    currentPoint = (point_list[currentPointIndex])
    dist = hypot(WINDOW_WIDTH/2-currentPoint[0], WINDOW_WIDTH/2-currentPoint[1])
    if dist>RADIUS:
        pygame.draw.circle(WINDOW, BLUE, currentPoint, 1)
    else: 
        pygame.draw.circle(WINDOW, RED, currentPoint, 1)
        if pointsInCircle<pointsInsideCircle: # the pre-calculated value for no of points inside the circle
            pointsInCircle += 1
    if currentPointIndex<len(point_list)-1:
        currentPointIndex+=1

currentN = 1
FONT = pygame.font.Font(None, 33)
def write_values():
    global currentN, pointsInCircle
    nValueText = FONT.render(f"total = {currentN}", True, BLACK, WHITE)
    insideValueText = FONT.render(f"inside = {pointsInCircle}", True, BLACK, WHITE)
    piValueText = FONT.render(f"pi = ~{round(4*pointsInCircle/currentN, 5)}", True, BLACK, WHITE)
    WINDOW.blit(nValueText, (10, 505))
    WINDOW.blit(insideValueText, (10, 540))
    WINDOW.blit(piValueText, (10, 575))
    if currentN<n:
        currentN += 1

# MAIN LOOP 
running = True
CLOCK = pygame.time.Clock()
FRAME_RATE = 5000
while running: 
    CLOCK.tick(FRAME_RATE) # run at specified frame rate 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False 
            pygame.quit() 
            exit()
    draw_circle()
    draw_random_point()
    write_values()
    pygame.display.update()  