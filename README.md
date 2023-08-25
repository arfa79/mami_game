# Mami Game

Welcome to the Mami Game! This is a simple game built using Tkinter, where you predict a missing word to win. The game includes features like a timer, chances, and even a cheat code for added fun.

## Table of Contents

- [Description](#description)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Dockerizing the Game](#dockerizing-the-game)
- [Contributing](#contributing)
- [License](#license)

## Description

In this game, you are presented with a sentence containing a missing word. Your task is to predict the missing word to win the game. The game includes features such as tracking your chances, a timer, and even a cheat code to help you if you're stuck!

## Getting Started
just find two words and the fun is getting start :)
### Prerequisites

- Python 3
- Docker (if you want to run the game in a Docker container)
- thinker

### Installation

1. Clone this repository to your local machine:

   git clone https://github.com/arfa79/mami_game.git

2. go to the game directory

    cd mami-game-predictions

Install the required dependencies:

    pip install -r requirements.txt

###Usage

    Run the game:

    python mami.py

    Follow the instructions displayed on the screen to play the game.

###Dockerizing the Game

You can also run the game inside a Docker container. Dockerizing graphical applications can be a bit tricky due to the nature of GUI applications.

Build the Docker image:

    docker build -t mami-game .

Run the Docker container:

    docker run -it --rm -p 6080:80 -p 5900:5900 mami-game

    Access the game using a VNC viewer at localhost:5900 (password: vncpassword) or a web browser at http://localhost:6080/.

Contributing

Contributions are welcome! If you find any issues or have improvements to suggest, please open an issue or submit a pull request.

###License

This project is licensed under the GPL License - see the LICENSE file for details.