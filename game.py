# Description: SAVE THE CHRISTMAS game!

import pygame
import random

pygame.init()

# CONSTANTS:
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 224, 84)
DARKER_GREEN = (20, 166, 32)
DARKEST_GREEN = (15, 117, 24)
SKIN_COLOR = (239, 242, 191)
ORANGE = (247, 196, 69)
DARK_RED = (147, 13, 4)
DARKEST_RED = (111, 10, 4)
PINK = (242, 153, 224)
DARK_PINK = (168, 118, 158)
BACKGROUND_COLOR = (255, 255, 255)  # WHITE
BORDEAUX = (153, 24, 44)
REDVIOLET = (219, 38, 69)
PURPLE = (79, 1, 130)

# Variables:
width = 800
height = 600
SIZE = (width, height)
screen = pygame.display.set_mode(SIZE)
characterSpeed = 10
opponentSpeed = 3
clockTime = pygame.time.Clock()
gameBorderLine = 70
gameBorder = 130
giftsDistance = 100  # Gifts distance from the left game border.
d = 25  # distance of the gifts/oppoent/bigOpponent to the character used for collisions

# Booleans:
running = True  # The game loop
winCondition = False  # The win loop
loseCondition = False  # The lose loop
key_left = False
key_right = False
key_down = False
key_up = False
key_space = False
magic_weapon = 2

# Initiliazers:
opponent = -100  # Draws the opponents
x = width - 150  # Draws the character
y = height - 400  # Draws the character
nobillityGiftsPoints = 0
score = 0
evergreenLife = 100
radius = 10
max_radius = 150
# The number of opponents and its x and y coordinate initialized in the loop below:
opponents = 10
opponent_X = []
opponent_Y = []
opponent_Direction = []
hel_Opponent_X = 300
hel_Opponent_Y = 300
hel_Opponent_Direction = "RD"


# Image/font/sound uploads:
fontBig = pygame.font.SysFont("Times New Roman", 40)  # Initialize a font of 40 size
fontSmall = pygame.font.SysFont("Times New Roman", 15)  # Initialize a font 15 size
fontMed = pygame.font.SysFont("Times New Roman", 30)  # Initialize a font 30 size
background = pygame.image.load("Background.png")
back = pygame.Rect(0, 0, background.get_width(), background.get_height())
menu = pygame.image.load("Menu.png")
menu_back = pygame.Rect(0, 0, menu.get_width(), menu.get_height())
win_page = pygame.image.load("Win.png")
win_back = pygame.Rect(0, 0, win_page.get_width(), win_page.get_height())
lose_page = pygame.image.load("lose.png")
lose_back = pygame.Rect(0, 0, lose_page.get_width(), lose_page.get_height())


# Function that draws the character:
def draw_character(x, y):
    pygame.draw.circle(screen, GREEN, (x + 50, y + 100), 15)  # HEAD
    pygame.draw.ellipse(screen, GREEN, pygame.Rect(x + 48, y + 80, 20, 30))
    pygame.draw.circle(screen, DARKEST_GREEN, (x + 45, y + 103), 3)
    pygame.draw.circle(screen, GREEN, (x + 44, y + 103), 2)
    pygame.draw.circle(screen, DARKEST_GREEN, (x + 42, y + 107), 5)
    pygame.draw.circle(screen, GREEN, (x + 41, y + 108), 4)
    pygame.draw.line(screen, DARKEST_GREEN, (x + 36, y + 93), (x + 40, y + 97), 1)
    pygame.draw.ellipse(screen, DARKEST_GREEN, pygame.Rect(x + 43, y + 98, 7, 5))
    pygame.draw.ellipse(screen, GREEN, pygame.Rect(x + 43, y + 96, 7, 5))
    pygame.draw.ellipse(screen, DARKEST_GREEN, pygame.Rect(x + 47, y + 82, 7, 5))  # Eye Brows
    pygame.draw.ellipse(screen, GREEN, pygame.Rect(x + 47, y + 84, 7, 5))
    pygame.draw.circle(screen, BLACK, (x + 50, y + 90), 4)  # EYE
    pygame.draw.circle(screen, WHITE, (x + 50, y + 90), 3)
    pygame.draw.circle(screen, DARKER_GREEN, (x + 49, y + 90), 2)
    pygame.draw.ellipse(screen, DARKEST_GREEN, pygame.Rect(x + 48, y + 88, 3, 4))
    pygame.draw.circle(screen, BLACK, (x + 48, y + 90), 1)
    pygame.draw.circle(screen, BLACK, (x + 35, y + 97), 2)  # NOSE
    pygame.draw.circle(screen, DARKEST_GREEN, (x + 35, y + 97), 1)
    pygame.draw.rect(screen, RED, pygame.Rect(x + 42, y + 112, 19, 10))  # Clothes
    pygame.draw.ellipse(screen, RED, pygame.Rect(x + 39, y + 112, 7, 10))
    pygame.draw.ellipse(screen, RED, pygame.Rect(x + 58, y + 112, 7, 10))
    pygame.draw.circle(screen, BLACK, (x + 40, y + 116), 5)
    pygame.draw.circle(screen, WHITE, (x + 40, y + 116), 4)
    pygame.draw.circle(screen, WHITE, (x + 43, y + 116), 4)
    pygame.draw.circle(screen, BLACK, (x + 61, y + 110), 5)
    pygame.draw.circle(screen, WHITE, (x + 61, y + 110), 4)
    pygame.draw.circle(screen, WHITE, (x + 46, y + 115), 4)
    pygame.draw.circle(screen, WHITE, (x + 49, y + 114), 4)
    pygame.draw.circle(screen, WHITE, (x + 52, y + 113), 4)
    pygame.draw.circle(screen, WHITE, (x + 55, y + 112), 4)
    pygame.draw.circle(screen, WHITE, (x + 58, y + 111), 4)
    pygame.draw.circle(screen, BLACK, (x + 65, y + 80), 10)  # HAT
    pygame.draw.circle(screen, RED, (x + 65, y + 80), 9)
    pygame.draw.circle(screen, BLACK, (x + 75, y + 100), 4)
    pygame.draw.circle(screen, RED, (x + 75, y + 100), 3)
    pygame.draw.line(screen, BLACK, (x + 70, y + 80), (x + 73, y + 100), 1)
    pygame.draw.line(screen, BLACK, (x + 75, y + 80), (x + 75, y + 100), 1)
    pygame.draw.line(screen, RED, (x + 72, y + 80), (x + 74, y + 100), 3)
    pygame.draw.line(screen, RED, (x + 73, y + 80), (x + 73, y + 100), 2)
    pygame.draw.circle(screen, BLACK, (x + 55, y + 80), 4)  # HAT
    pygame.draw.circle(screen, WHITE, (x + 55, y + 80), 3)
    pygame.draw.circle(screen, BLACK, (x + 66, y + 88), 4)
    pygame.draw.circle(screen, WHITE, (x + 66, y + 88), 3)
    pygame.draw.circle(screen, WHITE, (x + 58, y + 82), 3)
    pygame.draw.circle(screen, WHITE, (x + 61, y + 84), 3)
    pygame.draw.circle(screen, WHITE, (x + 63, y + 86), 3)
    point_list = [[x + 30, y + 50], [x + 35, y + 45], [x + 40, y + 50], [x + 43, y + 55],
                  [x + 27, y + 55]]  # POLYGON PYGAME!
    pygame.draw.polygon(screen, RED, point_list)  # polygon
    # pygame.draw.circle(screen, PINK, (x + 50, y + 100), 10)


# Function that draws the gifts:
def gifts(x, y):
    pygame.draw.rect(screen, BLACK, pygame.Rect(x + 19, y - 13, 32, 30))
    pygame.draw.rect(screen, (random.randint(100, 220), random.randint(10, 20), 0), pygame.Rect(x + 20, y, 30, 15))
    pygame.draw.rect(screen, BLACK, pygame.Rect(x + 20, y - 10, 30, 10))
    pygame.draw.rect(screen, (random.randint(100, 220), random.randint(10, 20), 0), pygame.Rect(x + 20, y - 12, 30, 10))
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x + 22, y - 6, 12, 9))
    pygame.draw.ellipse(screen, ORANGE, pygame.Rect(x + 23, y - 5, 10, 7))
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(x + 36, y - 6, 12, 9))
    pygame.draw.ellipse(screen, ORANGE, pygame.Rect(x + 37, y - 5, 10, 7))
    pygame.draw.circle(screen, BLACK, (x + 35, y), 5)
    pygame.draw.circle(screen, DARKER_GREEN, (x + 35, y), 4)
    # pygame.draw.circle(screen, PINK, (x + 35, y), 10)


# Function that draws the opponent:
def draw_opponent(x, y):
    pygame.draw.rect(screen, RED, pygame.Rect(x - 25, y - 8, 12, 5))  # EARS
    pygame.draw.ellipse(screen, RED, pygame.Rect(x - 23, y - 5, 10, 5))
    pygame.draw.rect(screen, RED, pygame.Rect(x + 13, y - 8, 12, 5))
    pygame.draw.ellipse(screen, RED, pygame.Rect(x + 11, y - 5, 10, 5))
    pygame.draw.ellipse(screen, DARKEST_RED, pygame.Rect(x + 15, y - 7, 8, 4))
    pygame.draw.ellipse(screen, DARKEST_RED, pygame.Rect(x - 23, y - 7, 8, 4))
    pygame.draw.circle(screen, BLACK, (x, y), 16)  # Head
    pygame.draw.circle(screen, RED, (x, y), 15)
    pygame.draw.circle(screen, SKIN_COLOR, (x - 6, y - 2), 4)  # eye
    pygame.draw.circle(screen, SKIN_COLOR, (x + 6, y - 2), 4)
    pygame.draw.circle(screen, RED, (x - 6, y - 3), 1)
    pygame.draw.circle(screen, RED, (x + 6, y - 3), 1)
    pygame.draw.rect(screen, RED, pygame.Rect(x + 2, y, 7, 2))
    pygame.draw.rect(screen, RED, pygame.Rect(x - 10, y, 7, 2))
    pygame.draw.line(screen, BLACK, (x + 8, y - 9), (x + 3, y - 10), 2)  # Eyebrows
    pygame.draw.line(screen, BLACK, (x + 8, y - 9), (x + 10, y - 7), 1)
    pygame.draw.line(screen, BLACK, (x - 8, y - 9), (x - 3, y - 10), 2)
    pygame.draw.line(screen, BLACK, (x - 8, y - 9), (x - 10, y - 7), 1)
    pygame.draw.ellipse(screen, DARK_RED, pygame.Rect(x - 3, y - 5, 6, 10))  # Nose
    pygame.draw.circle(screen, DARKEST_RED, (x - 6, y + 7), 3)  # Mouth
    pygame.draw.circle(screen, DARKEST_RED, (x - 6, y + 8), 3)
    pygame.draw.circle(screen, DARKEST_RED, (x - 4, y + 9), 3)
    pygame.draw.circle(screen, DARKEST_RED, (x - 2, y + 9), 3)
    pygame.draw.circle(screen, DARKEST_RED, (x, y + 9), 3)
    pygame.draw.circle(screen, DARKEST_RED, (x + 1, y + 9), 3)
    pygame.draw.circle(screen, DARKEST_RED, (x + 2, y + 9), 3)
    pygame.draw.circle(screen, DARKEST_RED, (x + 4, y + 8), 3)
    pygame.draw.circle(screen, DARKEST_RED, (x + 6, y + 7), 3)
    pygame.draw.ellipse(screen, PINK, pygame.Rect(x - 4, y + 10, 8, 11))  # Tongue
    pygame.draw.line(screen, DARK_PINK, (x - 1, y + 11), (x - 1, y + 17), 1)
    pygame.draw.line(screen, SKIN_COLOR, (x - 15, y - 10), (x - 10, y - 15), 5)  # HORN
    pygame.draw.line(screen, SKIN_COLOR, (x + 15, y - 10), (x + 10, y - 15), 5)
    pygame.draw.ellipse(screen, SKIN_COLOR, pygame.Rect(x + 13, y - 19, 7, 10))
    pygame.draw.ellipse(screen, SKIN_COLOR, pygame.Rect(x - 20, y - 19, 7, 10))
    pygame.draw.circle(screen, SKIN_COLOR, (x - 5, y + 7), 1)
    pygame.draw.circle(screen, SKIN_COLOR, (x, y + 7), 1)
    pygame.draw.circle(screen, SKIN_COLOR, (x + 5, y + 7), 1)


def hel_Opponent():
    global hel_Opponent_Direction
    hel_Opponent_Direction_list = ["RU", "RD", "LU", "LD"]
    hel_Opponent_Direction = get_random_direction(hel_Opponent_Direction, 1, hel_Opponent_Direction_list)
    global hel_Opponent_X, hel_Opponent_Y
    # if (hel_Opponent_X > (width - gameBorder)) or (hel_Opponent_Y < gameBorder):
    #     hel_Opponent_Direction = get_random_direction(hel_Opponent_Direction, 100, hel_Opponent_Direction_list)
    # if (hel_Opponent_X > (width - gameBorder)) or (hel_Opponent_Y > (height - gameBorder)):
    #     hel_Opponent_Direction = get_random_direction(hel_Opponent_Direction, 100, hel_Opponent_Direction_list)
    # if (hel_Opponent_X < gameBorder) or (hel_Opponent_Y < gameBorder):
    #     hel_Opponent_Direction = get_random_direction(hel_Opponent_Direction, 100, hel_Opponent_Direction_list)
    # if (hel_Opponent_X < gameBorder) or (hel_Opponent_Y > (height - gameBorder)):
    #     hel_Opponent_Direction = get_random_direction(hel_Opponent_Direction, 100, hel_Opponent_Direction_list)

    if hel_Opponent_Direction == "RU":
        if ((hel_Opponent_X < (width - gameBorder)) and hel_Opponent_X > gameBorder ) and ((hel_Opponent_Y > gameBorder) and (hel_Opponent_Y < (height - gameBorder))):
            hel_Opponent_X += opponentSpeed
            hel_Opponent_Y -= opponentSpeed
        else:
            hel_Opponent_X -= opponentSpeed
            hel_Opponent_Y += opponentSpeed
            hel_Opponent_Direction = get_random_direction(hel_Opponent_Direction, 100, hel_Opponent_Direction_list)

    if hel_Opponent_Direction == "RD":

        if ((hel_Opponent_X < (width - gameBorder)) and hel_Opponent_X > gameBorder ) and ((hel_Opponent_Y > gameBorder) and (hel_Opponent_Y < (height - gameBorder))):
            hel_Opponent_X += opponentSpeed
            hel_Opponent_Y += opponentSpeed
        else:
            hel_Opponent_X -= opponentSpeed
            hel_Opponent_Y -= opponentSpeed
            hel_Opponent_Direction = get_random_direction(hel_Opponent_Direction, 100, hel_Opponent_Direction_list)


    if hel_Opponent_Direction == "LU":
        if ((hel_Opponent_X < (width - gameBorder)) and hel_Opponent_X > gameBorder ) and ((hel_Opponent_Y > gameBorder) and (hel_Opponent_Y < (height - gameBorder))):
            hel_Opponent_X -= opponentSpeed
            hel_Opponent_Y -= opponentSpeed
        else:
            hel_Opponent_X += opponentSpeed
            hel_Opponent_Y += opponentSpeed
            hel_Opponent_Direction = get_random_direction(hel_Opponent_Direction, 100, hel_Opponent_Direction_list)

    if hel_Opponent_Direction == "LD":
        if ((hel_Opponent_X < (width - gameBorder)) and hel_Opponent_X > gameBorder ) and ((hel_Opponent_Y > gameBorder) and (hel_Opponent_Y < (height - gameBorder))):
            hel_Opponent_X -= opponentSpeed
            hel_Opponent_Y += opponentSpeed
        else:
            hel_Opponent_X += opponentSpeed
            hel_Opponent_Y -= opponentSpeed
            hel_Opponent_Direction = get_random_direction(hel_Opponent_Direction, 100, hel_Opponent_Direction_list)

    pygame.draw.circle(screen, PURPLE, (hel_Opponent_X, hel_Opponent_Y), 40)
    pygame.draw.circle(screen, PURPLE, (hel_Opponent_X, hel_Opponent_Y - 40), 20)


def collision_magic_weapon(x, y, radius, O_x, O_y):
    d = (x - O_x) ** 2 + (y - O_y) ** 2
    if d < (radius ** 2):
        return True
    else:
        return False


#  Function draws the weapon:
def magicWeapon(x, y):
    global radius, key_space, magic_weapon
    if key_space == True and (magic_weapon > 0):
        radius += 2
        if radius < max_radius:
            pygame.draw.circle(screen, (0, 255 - int((radius / 2)), 70 + radius), (x, y), radius, 10)
            for i in range(len(opponent_X)):
                collision = collision_magic_weapon(x, y, radius, opponent_X[i], opponent_Y[i])
                if collision == True:
                    opponent_X[i] = 100
                    opponent_Y[i] = 150
        else:
            key_space = False
            magic_weapon -= 1
            radius = 10

        # Function that draws the evergreen life percentage:


def life(e):
    if e > 0:
        x = int(e * (80 / 100))

    else:
        x = 0
    pygame.draw.rect(screen, RED, pygame.Rect(55, 550, x, 10))
    pygame.draw.line(screen, BLACK, (55, 550), (135, 550), 5)
    pygame.draw.line(screen, BLACK, (135, 550), (135, 560), 5)
    pygame.draw.line(screen, BLACK, (135, 560), (55, 560), 5)
    pygame.draw.line(screen, BLACK, (55, 560), (55, 550), 5)
    text = fontMed.render((str(e) + str("%")), 1, RED)
    screen.blit(text, pygame.Rect(55, 565, 50, 50))


# Detects collisions between the character and the gift(s):
def gifts_collision(x_collision, y_collision):
    global d
    # the x and y are 0,0 so we add certain numbers to detect collision around the gift/character which aren't at point 0,0:
    if (((x + 50) - d) < (x_collision + 35) < ((x + 50) + d)) and (
            ((y + 100) - 2 * d) < y_collision < ((y + 100) + 1.5 * d)):
        return True
    else:
        return False


# Function that shows the number of gifts collected by the chracter:
def nobilityGifts(screen):
    text = fontBig.render(str(nobillityGiftsPoints), 1, RED)
    screen.blit(text, pygame.Rect(240, 550, 400, 100))


# Detects collisions between the character and the opponent(s):
def opponent_collision(x_collision, y_collision):
    global d
    if (((x + 50) - d) < x_collision < ((x + 50) + d)) and (((y + 100) - 2 * d) < y_collision < ((y + 100) + 1.5 * d)):
        return True
    else:
        return False


# Funcion that has directions from left, right, up and down ,randomizes it and moves/changes positions the opponents when is necessary:
def get_random_direction(dir, p, directions):
    d = dir
    # This if statement keeps checking if position = 100 and when the while loop continues to change the position and at some point is not it will proceed to the next:
    if p == 100:
        while d == dir:
            d = random.choice(directions)
        return d
    rand = random.random()*100
    print(rand)
    if rand < p:
        while d == dir:
            d = random.choice(directions)
        return d
    else:
        return dir


# Detects when the character wins by finding using trees' location (x and y coordinates) and with all the gifts collected:
def win():
    global d
    # character: x + 50
    # character: y + 100
    # tree x range: 100 - 150
    # tree y range: 270 - 350
    if (100 < x + 50 < 150) and (270 < y + 100 < 350) and nobillityGiftsPoints == giftNumber:
        return True
    else:
        return False


# Detects when the character loses by the evergreen life reaching 0:
def lose():
    if evergreenLife <= 0:
        return True
    else:
        return False

    # Function that exits the game:


def exit():
    mouse = pygame.mouse.get_pos()
    if 700 + 80 > mouse[0] > 700 and 563 + 30 > mouse[1] > 563:
        pygame.draw.rect(screen, BORDEAUX, pygame.Rect(700, 563, 80, 30))
    else:
        pygame.draw.rect(screen, REDVIOLET, pygame.Rect(700, 563, 80, 30))
    text = fontMed.render("Exit", 1, BLACK)
    screen.blit(text, pygame.Rect(715, 560, 80, 30))


# list and variable later used to determine the directions of each opponent:
giftNumber = 6
gifts_X = []
gifts_Y = []
for i in range(giftNumber):
    gifts_X.append(0)
    gifts_Y.append(0)

# The number of opponents and its x and y coordinate initialized in the loop below:
for i in range(opponents):
    opponent_X.append(0)
    opponent_Y.append(0)
    opponent_Direction.append(random.choice(["R", "L", "D", "U"]))

# The number of big opponents and its x and y coordinate initialized in the loop below:
# bigOpponents = 2
# bigOpponent_X = []
# bigOpponent_Y = []
# bigOpponent1_Direction = []
# bigOpponent2_Direction = []
# for i in range(opponents):
# bigOpponent_X.append(0)
# bigOpponent_Y.append(0)
# bigOpponent1_Direction.append(["U"])
# bigOpponent2_Direction.append(["R"])


# Randomizing the x and y coordinates of the opponents at the start position:
for i in range(len(opponent_X)):
    opponent_X[i] = random.randint(gameBorder, width - gameBorder)
    opponent_Y[i] = random.randint(gameBorder, height - gameBorder)

# Randomizing the x and y coordinates of each of the gifts:
for i in range(len(gifts_X)):
    gifts_X[i] = random.randrange(gameBorder + giftsDistance, width - gameBorder - giftsDistance, 30)
    gifts_Y[i] = random.randrange(gameBorder, height - gameBorder, 30)

# The Menu loop:
gameMenu = True
while gameMenu == True:
    loseCondition = False
    screen.blit(menu, menu_back)
    # Function that draws the exit:
    exit()
    text1 = fontBig.render("START", 1, BLACK)
    text2 = fontBig.render("Manual", 1, BLACK)
    screen.blit(text1, pygame.Rect(350, 220, 100, 100))
    screen.blit(text2, pygame.Rect(350, 380, 100, 100))
    # pygame.draw.circle(screen, PINK, (300, 200), 10)
    # pygame.draw.circle(screen, PINK, (530, 300), 10)
    pygame.display.flip()

    # Loop which developes the Buttons:
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            gameMenu = False
            running = False
            winCondition = False
        if evnt.type == pygame.MOUSEBUTTONDOWN:
            mx, my = evnt.pos
            if 295 < mx < 530 and 195 < my < 300:
                gameMenu = False
            # Displays the exit when clicked:
            if 700 < mx < 780 and 570 < my < 595:
                gameMenu = False
                running = False

# The Game loop:
while running:
    # Loop which developes the Buttons:
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False
        if evnt.type == pygame.MOUSEBUTTONDOWN:
            mx, my = evnt.pos
            # Displays the exit when clicked:
            if 700 < mx < 780 and 570 < my < 595:
                running = False
        if evnt.type == pygame.KEYDOWN:
            if evnt.key == pygame.K_SPACE:
                key_space = True

                # Set up the Characters movements:
    if evnt.type == pygame.KEYDOWN:
        if evnt.key == pygame.K_LEFT:
            key_left = True
        if evnt.key == pygame.K_RIGHT:
            key_right = True
        if evnt.key == pygame.K_DOWN:
            key_down = True
        if evnt.key == pygame.K_UP:
            key_up = True
        # if evnt.key == pygame.K_SPACE:
        #     key_space = True

    if evnt.type == pygame.KEYUP:
        if evnt.key == pygame.K_LEFT:
            key_left = False
        if evnt.key == pygame.K_RIGHT:
            key_right = False
        if evnt.key == pygame.K_DOWN:
            key_down = False
        if evnt.key == pygame.K_UP:
            key_up = False

    if key_left == True:
        if x > 70:
            x = x - characterSpeed
    if key_right == True:
        if x < width - 170:
            x = x + characterSpeed
    if key_down == True:
        if y < height - 230:
            y = y + characterSpeed
    if key_up == True:
        if y > 40:
            y = y - characterSpeed

    key_left = False
    key_right = False
    key_down = False
    key_up = False

    # Loop that moves the Opponents:
    for i in range(len(opponent_X)):
        dir = opponent_Direction[i]
        directions = ["L", "R", "U", "D"]
        if dir == "R":
            if opponent_X[i] < (width - gameBorder):
                opponent_X[i] += opponentSpeed
                opponent_Direction[i] = get_random_direction(opponent_Direction[i], 2, directions)
            else:
                opponent_Direction[i] = get_random_direction(opponent_Direction[i], 100, directions)
        elif dir == "L":
            if opponent_X[i] > gameBorder:
                opponent_X[i] -= opponentSpeed
                opponent_Direction[i] = get_random_direction(opponent_Direction[i], 2, directions)
            else:
                opponent_Direction[i] = get_random_direction(opponent_Direction[i], 100, directions)
        elif dir == "U":
            if opponent_Y[i] > gameBorder:
                opponent_Y[i] -= opponentSpeed
                opponent_Direction[i] = get_random_direction(opponent_Direction[i], 2, directions)
            else:
                opponent_Direction[i] = get_random_direction(opponent_Direction[i], 100, directions)
        else:  # dir = D
            if opponent_Y[i] < (height - gameBorder):
                opponent_Y[i] += opponentSpeed
                opponent_Direction[i] = get_random_direction(opponent_Direction[i], 2, directions)
            else:
                opponent_Direction[i] = get_random_direction(opponent_Direction[i], 100, directions)

    # Filling the background, calling the game border and the exit function so the game would look better:
    screen.fill(BACKGROUND_COLOR)
    screen.blit(background, back)
    exit()
    pygame.draw.circle(screen, PINK, (100, 270), 10)
    pygame.draw.circle(screen, PINK, (150, 350), 10)

    # startingButton(x, y)
    # drawScene(screen)
    # screenBorder()

    # Calling the function based on the number of values in the each list as numbers of gifts which draws and detects collision with the Character:
    for i in range(len(gifts_X)):
        gifts(gifts_X[i], gifts_Y[i])
        collision = gifts_collision(gifts_X[i], gifts_Y[i])
        if collision:
            nobillityGiftsPoints += 1
            gifts_X[i] = -100
            gifts_Y[i] = -100

    # Calling the function to draw the Character:
    draw_character(x, y)

    # Calling the function based on the number of values in the each list as numbers of opponents and draws them:
    for i in range(len(opponent_X)):
        draw_opponent(opponent_X[i], opponent_Y[i])

    for i in range(len(opponent_X)):
        collision = opponent_collision(opponent_X[i], opponent_Y[i])
        if collision:
            evergreenLife -= 2

    nobilityGifts(screen)
    life(evergreenLife)
    magicWeapon(x + 50, y + 100)
    hel_Opponent()
    # Stops the game loop/game to run when the character wins:
    w = win()
    if w == True:
        winCondition = True
        running = False

    # Stops the game loop/game to run when the character loses:
    l = lose()
    if l == True:
        loseCondition = True
        running = False

    pygame.display.flip()
    clockTime.tick(30)

# Loop that determines if the character wins:
while winCondition == True:
    loseCondition = False
    screen.blit(win_page, win_back)
    text1 = fontSmall.render("'CONGRATS, YOU SAVED THE CHRISTMAS!'", 5, BLACK)
    text2 = fontSmall.render("Score:", 1, BLACK)
    text3 = fontSmall.render("Merry Christmas!", 1, BLACK)
    text4 = fontSmall.render("REPLAY", 1, BLACK)
    screen.blit(text1, pygame.Rect(240, 220, 50, 20))
    screen.blit(text2, pygame.Rect(250, 315, 10, 5))
    screen.blit(text3, pygame.Rect(340, 240, 50, 20))
    screen.blit(text4, pygame.Rect(450, 315, 10, 5))
    # Function that draws the exit:
    exit()
    # Final Score:
    giftScore = (nobillityGiftsPoints * 100) / giftNumber
    evergreenLifeScore = evergreenLife
    finalScore = (giftScore + evergreenLifeScore) / 2
    score = fontMed.render(str("%2i" % finalScore + str("%")), 1, RED)  # put % and change color
    screen.blit(score, pygame.Rect(310, 310, 50, 50))

    # Loop which developes the Buttons:
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            winCondition = False
        if evnt.type == pygame.MOUSEBUTTONDOWN:
            mx, my = evnt.pos
            # Displays the exit when clicked:
            if 700 < mx < 780 and 570 < my < 595:
                loseCondition = False
                # pygame.draw.circle(screen, PINK, (300, 200), 10)
    # pygame.draw.circle(screen, PINK, (530, 300), 10)
    pygame.display.flip()

# Loop that determines if the character loses:
while loseCondition == True:
    winCondition = False
    screen.blit(lose_page, lose_back)
    text1 = fontBig.render("'YOU LOST!'", 5, BLACK)
    text2 = fontSmall.render("REPLAY", 1, BLACK)
    text3 = fontSmall.render("'Save The Christmas'", 1, BLACK)
    screen.blit(text1, pygame.Rect(290, 220, 50, 20))
    screen.blit(text2, pygame.Rect(350, 360, 10, 5))
    screen.blit(text3, pygame.Rect(320, 380, 10, 5))
    # Function that draws the exit:
    exit()
    # pygame.draw.circle(screen, PINK, (295, 195), 10)
    # pygame.draw.circle(screen, PINK, (530, 300), 10)
    pygame.display.flip()
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            loseCondition = False
        if evnt.type == pygame.MOUSEBUTTONDOWN:
            mx, my = evnt.pos
            # Displays the exit when clicked:
            if 700 < mx < 780 and 570 < my < 595:
                loseCondition = False

            # if 295 < mx < 530 and 195 < my < 300:
            # gameMenu = True       # REPLAY

    pygame.display.flip()

pygame.quit()