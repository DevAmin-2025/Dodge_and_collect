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
player_y = screen_height - (player_height + 5)
player_speed = 10
player_color = '#757575'

# Set variables for the Coin object
coin_radius = 15
coin_x = randint(coin_radius, (screen_width - coin_radius))
coin_y = -coin_radius
coin_speed = 4
coin_speed_increase = 0.2
coin_color = '#FBC02D'

# Set variables for the obstacle object
obstacle_width = 100
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
        # Quits the game if the user clicks on the close button
        if event.type == pygame.QUIT:
            running = False
        # Ckeck if the user pressed Enter to restart the game
        elif event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                # Reposition the player at the center of the window
                player_x = (screen_width // 2) - (player_width // 2)
                player_y = screen_height - (player_height + 10)
                # Reinitialize coin object
                coin_x = randint(coin_radius, (screen_width - coin_radius))
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

    obstacle_y += obstacle_speed
    if obstacle_y > screen_height:
        # Reinitialize obstacle object
        obstacle_x = randint(0, (screen_width - obstacle_width))
        obstacle_y = -obstacle_height
        obstacle_speed += obstacle_speed_increase

    coin_y += coin_speed
    if coin_y > screen_height:
        # Reinitialize coin object
        coin_x = randint(coin_radius, (screen_width - coin_radius))
        coin_y = -coin_radius
        coin_speed += coin_speed_increase

    # Move the player to left and right based on their keystroke
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if player_x >= 10:
            player_x -= player_speed
        else:
            player_x -= player_x
    elif keys[pygame.K_RIGHT]:
        if (player_x + player_width) <= (screen_width - player_speed):
            player_x += player_speed
        else:
            player_x += (screen_width - player_x) - player_width

    # Fill the screen with black or white color
    if dark_mode:
        screen.fill('black')
    else:
        screen.fill('white')

    if game_over:
        pass
    else:
        pygame.draw.rect(screen, obstacle_color, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
        pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
        pygame.draw.circle(screen, coin_color, (coin_x, coin_y), coin_radius)

    # update the display
    pygame.display.update()
    # Set the desired frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()