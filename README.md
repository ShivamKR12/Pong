# Pong (Pygame)

A simple Pong game built using Python and Pygame.

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

## Build Executable (Windows)

To create a standalone `.exe` using PyInstaller:

```

pyinstaller --onefile --windowed main.py

```

The executable will be created inside the `dist/` folder.

## Project Structure

```

main.py
requirements.txt
README.md

```

## Notes

- The opponent paddle uses a simple AI.
- The game runs at 60 FPS.
