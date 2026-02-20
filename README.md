# Pong (Pygame)

A Pong game built using Python and Pygame, implemented with an object-oriented and sprite-based architecture.

## Requirements

- Python 3.x
- pygame-ce (or pygame)

Install dependencies:

```

pip install -r requirements.txt

```

Or manually:

```

pip install pygame-ce

```

## How to Run

From the project directory:

```

python main.py

```

## Controls

- Up Arrow — Move paddle up  
- Down Arrow — Move paddle down  

## Features

- Object-oriented game structure
- Sprite-based collision handling
- AI-controlled opponent
- Score tracking system
- Countdown timer after each point
- Sound effects for paddle hits and scoring
- 120 FPS game loop

## Assets Required

The following asset files must be present in the project directory:

```

Paddle.png
Ball.png
pong.ogg
score.ogg

```

## Build Executable (Windows)

To create a standalone `.exe` using PyInstaller:

```

pyinstaller --onefile --windowed main.py

```

If a `.spec` file already exists:

```

pyinstaller main.spec

```

The executable will be created inside the `dist/` folder.

## Project Structure

```

main.py
requirements.txt
README.md
Paddle.png
Ball.png
pong.ogg
score.ogg

```

## Notes

- The game uses `pygame.sprite.Group` for object management.
- The game flow is managed through a central `GameManager` class.
- Designed as a refactored and scalable version of earlier procedural implementations.
