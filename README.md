# Dodge & Collect

**Dodge & Collect** is a simple game built with Python and Pygame. In this game, you control a player that must dodge falling obstacles while collecting coins to increase your score. Before the game begins, you get to choose your preferred background mode (dark or light) to enhance your gaming experience.

## Features

- Background Mode Selection: Before the game begins, the player can choose between dark mode (black background) and light mode (white background) using a simple menu.

- Dynamic Gameplay: As the game progresses, both obstacles and coins increase in speed, making the gameplay more challenging.

- Score Tracking: Collect coins to earn points. The current score is displayed during gameplay and the final score is shown on the Game Over screen.

- Simple Controls: Use the left/right arrow keys to dodge obstacles and collect coins. When the game ends, press Enter to restart.

## Setup Instructions

### Project Structure
```
dodge-and-collect/
├── src/
│   ├── main.py
│   └── vars.py
├── fonts/
│   ├── Roboto-Black.ttf
│   └── Archivo-Bold.ttf
├── .gitignore
├── README.md
├── requirements.txt
└── LICENSE
```
### Customize Configuration
Make sure the file src/vars.py contains all the required configuration variables such as `screen_width`, `screen_height`, `player_width`, `player_height`, `coin_radius`, `obstacle_width`, `obstacle_height`, `coin_speed`, `obstacle_speed`, `coin_speed_increase`, `obstacle_speed_increase`, and any color values (e.g., `player_color`, `obstacle_color`, `coin_color`).

## How to Run
1. **Clone the Repository**: Open your terminal and run the following command to clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```
    Replace `your-username` and `your-repo` with the actual GitHub username and repository name.

2. Move to the main project directory and add the current directory to `PYTHONPATH`.

    ```bash
    cd Dodge_and_collect
    export PYTHONPATH=$PYTHONPATH:$(pwd)
    ```
2. Install necessary requirements.

    ```bash
    pip install -r requirements.txt
    ```
3. Run the main script.

    ```bash
    python src/main.py
    ```

## How to Play
Pre-game Menu:
- Background Choice: When the game starts, a selection screen will appear:
    - Press D for Dark Mode (black background).
    - Press L for Light Mode (white background).

Gameplay Controls:
- Use the Left Arrow and Right Arrow keys to move your player.

- Avoid colliding with obstacles.

- Collect coins to increase your score.

- When you collide with an obstacle, the game displays a Game Over screen.

- Press Enter on the Game Over screen to restart the game.

## License
This project is licensed under the MIT License. Feel free to modify and distribute in accordance with the license terms.
