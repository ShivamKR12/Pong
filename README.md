# Pong for Android

[![Platform](https://img.shields.io/badge/platform-Android-green.svg)](https://www.android.com)
[![Pygame-ce](https://img.shields.io/badge/pygame--ce-latest-green.svg)](https://github.com/pygame-community/pygame-ce)
[![AnvPy X](https://img.shields.io/badge/AnvPy--X-purple.svg)](https://anvpy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Latest Release](https://img.shields.io/badge/release-v1.0.0--android-blue.svg)](https://github.com/ShivamKR12/Pong/releases/tag/v1.0.0-android)

A modern implementation of the classic **Pong** arcade game, built with **Python** and **Pygame-ce**, and optimized for Android devices.

This Branch is for the **Android version** of the game. For other platforms, please see the other branches.

---

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Controls](#controls)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [License](#license)
- [Author](#author)

---

## Features

* 📱 **Native Android Gameplay**: Full-screen experience optimized for mobile.
* 👉 **Touch Controls**: Intuitive touch-and-drag controls for the player paddle.
* 🤖 **AI Opponent**: A challenging computer-controlled opponent.
* 📐 **Responsive Design**: The layout automatically adapts to different screen sizes and orientations.
* 💥 **Physics-Based Collisions**: Accurate and satisfying sprite-based collision detection.
* 🔊 **Sound Effects**: Immersive audio feedback for bounces and scoring.
* ⏱️ **Countdown Timer**: A 3-second countdown before each round begins.
* 📊 **Live Score Tracking**: Keep track of the score in real-time.
* ⚡ **120 FPS Gameplay**: Runs at a smooth 120 frames per second for fluid animations.

---

## Installation

1.  **Download the APK** from the [latest release](https://github.com/ShivamKR12/Pong/releases/tag/v1.0.0-android).
2.  Open the downloaded `.apk` file on your Android device.
3.  You may need to allow installations from "Unknown Sources" in your device's security settings.
4.  Follow the on-screen prompts to install and launch the game.

**Compatibility:** Requires Android 7.0 (API 24) or higher.

> **Note:** This is a development build. Please report any issues or feedback you may have!

---

## Controls

*   **Move Paddle**: Touch the right half of the screen and drag your finger up or down.
*   **Objective**: Keep the ball in play and score points by getting it past your opponent's paddle.

---

## Project Structure

The project follows a clean structure, with game logic in `main.py` and assets organized in their own directory.

```text
Pong-Android/
│
├── assets/
│   ├── Ball.png
│   ├── Paddle.png
│   ├── pong.ogg
│   └── score.ogg
│
├── .manifest
├── main.py
├── README.md
└── LICENSE.md
```

---

## Technologies Used

*   **Python**: Core programming language.
*   **Pygame-CE**: Game development library for graphics, sound, and input.
*   **AnvPy X**: Used to package the Python application into an Android APK.
*   **Git & GitHub**: Version control and hosting.

---

## License

This project is released under the [MIT License](LICENSE).

---

## Author

**Shivam Kumar** (@ShivamKR12)
