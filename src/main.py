from random import randint

import pygame

# Initializes Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 800

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
# Set a title for the window
pygame.display.set_caption('Coin Collector')

# Set variables for the player
player_width = 50
player_height = 50
player_x = (screen_width // 2) - (player_width // 2)
player_y = screen_height - (player_height + 10)
player_speed = 10

# Set variables for the Coin object
coin_radius = 15
coin_x = randint(coin_radius, (player_width - coin_radius))
coin_y = -coin_radius
coin_speed = 4
coin_speed_increase = 0.2
coin_color = '#FBC02D'

# Set variables for the obstacle object
obstacle_width = 70
obstacle_height = 20
obstacle_x = randint(0, (screen_width - obstacle_width))
obstacle_y = -obstacle_height
obstacle_speed = 3
obstacle_speed_increase = 0.2
obstacle_color = '#E53935'


# General attributes
score = 0
dark_mode = True
# Control the flow of the game
running = True
game_over = False

# Create a clock object
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Ckeck if the user pressed Enter to restart the game
        elif event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                # Reposition the player at the center of the window
                player_x = (screen_width // 2) - (player_width // 2)
                player_y = screen_height - (player_height + 10)

                # Reinitialize coin object
                coin_x = randint(coin_radius, (player_width - coin_radius))
                coin_y = -coin_radius
                coin_speed = 4

                # Reinitialize obstacle object
                obstacle_x = randint(0, (screen_width - obstacle_width))
                obstacle_y = -obstacle_height
                obstacle_speed = 3

                # Reset the score to zero
                score = 0
                # Reset the state of game_over variable
                game_over = False


    # Fill the screen with black or white color
    if dark_mode:
        screen.fill('black')
    else:
        screen.fill('white')

    # update the display
    pygame.display.update()

    # Set the desired frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()