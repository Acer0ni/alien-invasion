# Alien Invasion

Alien invasion is heavily inspired by the classic video game Space Invaders, and the game itself is made from a tutorial found in [Python crash course](https://nostarch.com/pythoncrashcourse2e) by Eric Matthes. It's written in python using pygame. It connects to a [global highscores client](https://github.com/Acer0ni/alien-invasion-api) that keeps track of all authentication and users highscores.

![blackformatedbadge](https://img.shields.io/badge/black-formated-red)

![licensebadge](https://img.shields.io/badge/license-GNU%20GPL%203.0-blue)

## Dependencies

- [Python 3.9](https://www.python.org/downloads/)

- [Pipenv](https://pipenv.pypa.io/en/latest/install/)

## Installation

1. Clone the repository - `git clone https://github.com/Acer0ni/alien-invasion.git`

2. Enter the repository - `cd alien-invasion`

3. Install the dependencies - `pipenv sync`

4. Run the game - `pipenv run python3 main.py`

## Development

To run the game for local development run `ENV=development python3 main.py `

## Register and login

![alien-invaders-login](https://i.imgur.com/bKzbbmR.png)

To make an account click on the sign-up button and choose a username and password. Once successful, it will bring you to the game screen automatically. If you already have an account, you can just log in and play. If you don't want to make an account you can choose skip login

**note**: If you skip login, the game will still attempt to get the score from the server but you will not be able to submit. Scores instead will be saved to `highscore.json`

## Play

![alien-invaders](https://i.imgur.com/o4OH62y.png)

To play, you can move left and right with the arrow keys and spacebar to shoot. The waves get harder after each wave, and are infinite.
