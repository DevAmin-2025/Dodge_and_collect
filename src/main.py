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

# Define font and size
normal_font = pygame.font.Font('../fonts/Roboto-Medium.ttf', 40)
game_over_font = pygame.font.Font('../fonts/Archivo-Bold.ttf', 80)

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

    if not game_over:
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

        # Check if the player and the obstacle has collided
        if (
            player_x < (obstacle_x + obstacle_width)
            and
            (player_x + player_width) > obstacle_x
            and
            (obstacle_y + obstacle_height) > player_y
        ):
            game_over = True

        # Check if the player has gained the coin
        if (
            player_x < (coin_x + coin_radius)
            and
            (player_x + player_width) > (coin_x - coin_radius)
            and
            (coin_y + coin_radius) > player_y
        ):
            score += 10
            # Reinitialize coin object
            coin_x = randint(coin_radius, (screen_width - coin_radius))
            coin_y = -coin_radius
            coin_speed += coin_speed_increase

    # Fill the screen with black or white color
    if dark_mode:
        screen.fill('black')
    else:
        screen.fill('white')

    if game_over:
        # Display extra text after game over
        game_over_text = game_over_font.render('Game Over!', True, '#BDBDBD')
        screen.blit(
            game_over_text,
            (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height())
        )
        restart_text = normal_font.render('Enter press to restart', True, '#BDBDBD')
        screen.blit(
            restart_text,
            (screen_width // 2 - restart_text.get_width() // 2, screen_height // 2 + 20)
        )
        final_score_text = normal_font.render(f'Final Score: {score}', True, '#BDBDBD')
        screen.blit(
            final_score_text,
            (screen_width // 2 - final_score_text.get_width() // 2, screen_height // 2 + 85)
        )
    else:
        # Draw the objects on the screen
        pygame.draw.rect(screen, obstacle_color, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
        pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
        pygame.draw.circle(screen, coin_color, (coin_x, coin_y), coin_radius)

        # display updated state of the score
        score_text = normal_font.render(f'Score: {score}', True, '#BDBDBD')
        screen.blit(score_text, (10, 10))

    # update the display
    pygame.display.update()
    # Set the desired frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
