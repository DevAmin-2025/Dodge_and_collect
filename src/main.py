from random import randint

import pygame

from src.vars import *


class DodgeAndCollect:
    """
    A game class for "Dodge & Collect" implemented using pygame.

    This class initializes the game window, loads fonts, handles game events,
    updates game state (like player, obstacle, and coin positions), detects collisions,
    and manages rendering for various game states (active play vs. game over).

    Attributes:
        screen: The game display surface.
        clock: Clock to control the frame rate.
        normal_font: Font for normal text rendering.
        game_over_font: Font for game over text rendering.
        score: The current score of the game.
        dark_mode: If True, uses a dark background.
        running: If True, the game loop is active.
        game_over: If True, the game is over.
        player_x: The player's horizontal position.
        player_y: The player's vertical position.
        coin_x: The coin's horizontal position.
        coin_y: The coin's vertical position.
        coin_speed: The falling speed of the coin.
        obstacle_x: The obstacle's horizontal position.
        obstacle_y: The obstacle's vertical position.
        obstacle_speed: The falling speed of the obstacle.
    """
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.normal_font = pygame.font.Font('fonts/Roboto-Black.ttf', 40)
        self.game_over_font = pygame.font.Font('fonts/Archivo-Bold.ttf', 80)
        self.score = 0
        self.dark_mode = True
        self.running = True
        self.game_over = False
        self.player_x = (screen_width // 2) - (player_width // 2)
        self.player_y = screen_height - (player_height + 5)
        self.coin_x = randint(coin_radius, (screen_width - coin_radius))
        self.coin_y = -coin_radius
        self.coin_speed = coin_speed
        self.obstacle_x = randint(0, (screen_width - obstacle_width))
        self.obstacle_y = -obstacle_height
        self.obstacle_speed = obstacle_speed

    def handle_events(self):
        """
        Process game events.

        Handles user input events such as quitting the game or restarting the game
        (when Enter is pressed after the game is over).

        :return: None
        """
        for event in pygame.event.get():
            # Quits the game if the user clicks on the close button
            if event.type == pygame.QUIT:
                self.running = False
            # Ckeck if the user pressed Enter to restart the game
            elif event.type == pygame.KEYDOWN and self.game_over:
                if event.key == pygame.K_RETURN:
                    # Reposition the player at the center of the window
                    self.player_x = (screen_width // 2) - (player_width // 2)
                    self.player_y = screen_height - (player_height + 5)
                    # Reinitialize coin object
                    self.coin_x = randint(coin_radius, (screen_width - coin_radius))
                    self.coin_y = -coin_radius
                    self.coin_speed = 4
                    # Reinitialize obstacle object
                    self.obstacle_x = randint(0, (screen_width - obstacle_width))
                    self.obstacle_y = -obstacle_height
                    self.obstacle_speed = 3
                    # Reset the score to zero
                    self.score = 0
                    # Reset the state of game_over variable
                    self.game_over = False

    def choose_background_color(self):
        """
        Displays a pre-game menu where the user can choose the background color.

        the user is prompted to press "D" for dark mode or "L" for light mode.
        Once a valid key is pressed, the `dark_mode` attribute is set accordingly.

        :return: None
        """
        # Loop until the user selects a mode or quits.
        choosing = True
        while choosing:
            # Fill with a neutral color for the selection screen.
            self.screen.fill('grey')
            prompt_text = self.normal_font.render("Press D for Dark Mode, L for Light Mode", True, 'white')
            self.screen.blit(
            prompt_text,
            (screen_width // 2 - prompt_text.get_width() // 2, screen_height // 2)
            )
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    choosing = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        self.dark_mode = False
                        choosing = False
                    elif event.key == pygame.K_d:
                        self.dark_mode = True
                        choosing = False

    def update_objects(self):
        """
        Update game objects' positions and speeds.

        If the obstacle or coin moves below the screen, this method resets
        their vertical positions to the top and increases their speeds.

        :return: None
        """
        if self.obstacle_y > screen_height:
            # Reinitialize obstacle object
            self.obstacle_x = randint(0, (screen_width - obstacle_width))
            self.obstacle_y = -obstacle_height
            self.obstacle_speed += obstacle_speed_increase

        if self.coin_y > screen_height:
            # Reinitialize coin object
            self.coin_x = randint(coin_radius, (screen_width - coin_radius))
            self.coin_y = -coin_radius
            self.coin_speed += coin_speed_increase

    def move_player(self):
        """
        Update the player's position based on keyboard input.

        Checks for left/right arrow key presses and moves the player accordingly,
        ensuring the player remains within the screen boundaries.

        :return: None
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.player_x >= 10:
                self.player_x -= player_speed
            else:
                self.player_x -= self.player_x
        elif keys[pygame.K_RIGHT]:
            if (self.player_x + player_width) <= (screen_width - player_speed):
                self.player_x += player_speed
            else:
                self.player_x += (screen_width - self.player_x) - player_width

    def handle_collisions(self):
        """
        Check and handle collisions between the player and game objects.

        Detects collisions between the player and the obstacle, setting the game over state.
        Also detects when the player collects a coin, increases the score, and resets the coin.

        :return: None
        """
        # Check if the player and the obstacle has collided
        if (
            self.player_x < (self.obstacle_x + obstacle_width)
            and
            (self.player_x + player_width) > self.obstacle_x
            and
            (self.obstacle_y + obstacle_height) > self.player_y
        ):
            self.game_over = True

        # Check if the player has gained the coin
        if (
            self.player_x < (self.coin_x + coin_radius)
            and
            (self.player_x + player_width) > (self.coin_x - coin_radius)
            and
            (self.coin_y + coin_radius) > self.player_y
        ):
            self.score += 10
            # Reinitialize coin object
            self.coin_x = randint(coin_radius, (screen_width - coin_radius))
            self.coin_y = -coin_radius
            self.coin_speed += coin_speed_increase

    def refresh_screen(self):
        """
        Refresh the game screen by setting the background color.

        Fills the display with either a dark or light color,
        depending on the dark_mode flag.

        :return: None
        """
        if self.dark_mode:
            self.screen.fill('black')
        else:
            self.screen.fill('white')

    def display_game_over(self):
        """
        Display the game over screen.

        Renders the game over message, restart instructions, and the final score onto the screen.

        :return: None
        """
        # Display extra text after game over
        game_over_text = self.game_over_font.render('Game Over!', True, '#BDBDBD')
        self.screen.blit(
            game_over_text,
            (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height())
        )
        restart_text = self.normal_font.render('Enter press to restart', True, '#BDBDBD')
        self.screen.blit(
            restart_text,
            (screen_width // 2 - restart_text.get_width() // 2, screen_height // 2 + 20)
        )
        final_score_text = self.normal_font.render(f'Final Score: {self.score}', True, '#BDBDBD')
        self.screen.blit(
            final_score_text,
            (screen_width // 2 - final_score_text.get_width() // 2, screen_height // 2 + 85)
        )

    def run_game_loop(self):
        """
        Run the main game loop.

        Continuously processes events, updates game object positions,
        checks for collisions, and renders the game state until the game is quit.

        :return: None
        """
        while self.running:
            self.handle_events()
            if self.game_over:
                self.display_game_over()
            else:
                self.obstacle_y += self.obstacle_speed
                self.coin_y += self.coin_speed
                self.update_objects()
                self.move_player()
                self.handle_collisions()
                self.refresh_screen()
                if not self.game_over:
                    # Draw the objects on the screen
                    pygame.draw.rect(
                        self.screen,
                        obstacle_color,
                        (self.obstacle_x, self.obstacle_y, obstacle_width, obstacle_height)
                    )
                    pygame.draw.rect(
                        self.screen,
                        player_color,
                        (self.player_x, self.player_y, player_width, player_height)
                    )
                    pygame.draw.circle(
                        self.screen,
                        coin_color,
                        (self.coin_x, self.coin_y),
                        coin_radius
                    )
                    # display updated state of the score
                    score_text = self.normal_font.render(f'Score: {self.score}', True, '#BDBDBD')
                    self.screen.blit(score_text, (10, 10))
            # update the display
            pygame.display.update()
            # Set the desired frame rate
            self.clock.tick(60)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Dodge & Collect')

    game = DodgeAndCollect()
    # Let the user choose the background color before the game begins.
    game.choose_background_color()
    # Proceed only if the user hasn't closed the window during selection.
    if game.running:
        game.run_game_loop()
    pygame.quit()
