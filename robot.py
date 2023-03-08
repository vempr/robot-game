import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Asteroids")
font = pygame.font.SysFont("Arial", 32)

clock = pygame.time.Clock()

robot = pygame.image.load("robot.png")
asteroid = pygame.image.load("rock.png")

position = 0

# controls (left key and right key with their corresponding x position increment)
controls = []
controls.append((pygame.K_LEFT, -5))
controls.append((pygame.K_RIGHT, 5))
key_pressed = {}

list_asteroids = []

clock = pygame.time.Clock()

ast_spacing = 0

points = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key_pressed[event.key] = True

        if event.type == pygame.KEYUP:
            del key_pressed[event.key]

        if event.type == pygame.QUIT:
            quit()

    for key in controls:
        if key[0] in key_pressed:
            position += key[1]
    
    # to make sure program doesn't spawn too many asteroids
    if ast_spacing % 100 == 0:
        x = randint(0, 640-asteroid.get_width())
        y = randint(-1000, -asteroid.get_height()) - randint(20, 40)
        list_asteroids.append([x, y])

    window.fill((0, 0, 0))
    window.blit(robot, (position, 480-robot.get_height()))

    for astr in list_asteroids:
        if 481 <= astr[1] <= 999:
            # if an asteroid has fallen through, reset all stats
            window.fill((0, 0, 0))
            position = 0
            window.blit(robot, (position, 480-robot.get_height()))
            list_asteroids = []
            points = 0
            break

        astr[1] += 2
        window.blit(asteroid, (astr[0], astr[1]))
        # check if asteroid x (or asteroid x + asteroid width) position is between robot x position and robot x + robot width
        if position <= astr[0]+asteroid.get_width() <= position+robot.get_width() or position <= astr[0] <= position+robot.get_width():
            # check if asteroid y (or asteroid y + asteroid height) position is between robot y position and robot y + robot height
            if 480-robot.get_height() <= astr[1]+asteroid.get_height() <= 480 or 480-robot.get_height() <= astr[1] <= 480:
                astr[1] = 1000
                points += 1

    text = font.render(f"Points: {points}", True, (255, 0, 0))
    window.blit(text, (510, 5))
    pygame.display.flip()

    ast_spacing += 1

    clock.tick(60)