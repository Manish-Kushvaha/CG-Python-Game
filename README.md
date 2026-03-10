<div align="center">

# 🎮 Catch The Falling Ball

### Simple Python Game using Pygame

A beginner-friendly **2D computer graphics game** where the player controls a basket to catch falling balls and increase the score.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pygame](https://img.shields.io/badge/Pygame-Game%20Library-green)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

</div>

---

# 📌 Project Overview

**Catch The Falling Ball** is a simple Python game built using the **Pygame library** to demonstrate basic **computer graphics concepts** such as:

- Object rendering
- Animation
- Keyboard interaction
- Collision detection
- Game loop logic

This project was created as part of a **Computer Graphics mini-project**.

---

# 🎮 Gameplay

- A **ball falls from the top of the screen**
- The player moves a **basket** left and right
- Catching the ball **increases the score**
- If the ball hits the ground, the **game ends**

---

# ✨ Features

- 🎮 Simple gameplay
- ⌨️ Keyboard controls
- 🔴 Animated falling ball
- 🟦 Movable basket
- 💯 Score tracking
- ❌ Game over condition

---

# 🛠 Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python | Programming Language |
| Pygame | Game development & graphics |

---

# 📦 Installation

Install pygame:

```bash
pip install pygame
```

---

# ▶️ Running the Game

Run the game using:

```bash
python3 game.py
```

---

# 🎮 Controls

| Key | Action |
|----|--------|
| ⬅ Left Arrow | Move basket left |
| ➡ Right Arrow | Move basket right |

---

# 🖼 Game Preview

Add a screenshot here:

```
![Game Screenshot](screenshot.png)
```

---

# ⚙️ Linux Setup & Troubleshooting

While running the game on Linux, the following **OpenGL / Mesa error** occurred:

```
libGL error: failed to load driver: iris
libGL error: failed to load driver: swrast
X_GLXCreateContext error
```

### Solution

Install the required Mesa OpenGL drivers:

```bash
sudo apt update
sudo apt install libgl1-mesa-dri libgl1-mesa-glx mesa-utils
```

Verify OpenGL installation:

```bash
glxinfo | grep OpenGL
```

Example output:

```
OpenGL renderer string: Mesa Intel UHD Graphics 730
OpenGL version string: 4.6 Mesa
```

---

# 🐍 Conda Environment Issue

Running the game inside the **conda base environment** caused pygame display issues.

Deactivate conda before running the game:

```bash
conda deactivate
```

Then run:

```bash
python3 game.py
```

---

# 🚀 Future Improvements

- Add start screen
- Add restart button
- Add sound effects
- Increase difficulty level
- Track high score

---

# 👨‍💻 Author

**Manish Kushvaha**

Computer Engineering Student  
Python | Java | MERN Stack

---

⭐ If you like this project, consider giving it a **star** on GitHub.
