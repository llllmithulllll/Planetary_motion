# Solar System Orbit Simulation

<img src="https://github.com/user-attachments/assets/6977e8e2-b74e-4091-8757-7dd53c89fa74" alt="system" width="300" height="200">


## Introduction

This project is a simple 2D simulation of a portion of our solar system, demonstrating the orbital mechanics of Mercury, Venus, Earth, and Mars around the Sun. Built using Python and the Pygame library, it visualizes the planets' paths based on gravitational forces, providing an engaging way to understand celestial motion.

---

## Features

* **Planets Included:** Simulates the orbits of Mercury, Venus, Earth, and Mars.
* **Central Star:** A static Sun at the center of the simulation.
* **Orbital Paths:** Traces the historical path of each planet, showing their elliptical orbits.
* **Gravitational Physics:** Calculates planetary motion based on Newton's Law of Universal Gravitation.
* **Dynamic Visualization:** Planets move smoothly along their calculated trajectories.
* **Starfield Background:** A simple starry background for an immersive space feel.

---

## How It Works

The simulation uses fundamental physics principles to calculate the positions of the planets over time:

1.  **Constants:** Defines real-world constants like the Gravitational Constant (`G`), masses of the Sun and planets, and the Astronomical Unit (`AU`) for scaling distances.
2.  **Initial Conditions:** Sets the initial positions and velocities for Earth, Mercury, Venus, and Mars relative to the Sun. These values are based on approximate orbital parameters.
3.  **Gravitational Force Calculation:** For each planet, the force of gravity exerted by the Sun is calculated using Newton's Law of Universal Gravitation ($$F = G \frac{m_1 m_2}{r^2}$$).
4.  **Acceleration:** The force is then used to determine the acceleration ($$a = \frac{F}{m}$$) of each planet.
5.  **Velocity and Position Update (Euler Integration):** The simulation uses a basic Euler integration method to update the velocity and position of each planet in small time steps (`dt`).
    * $$v_{new} = v_{old} + a \cdot dt$$
    * $$x_{new} = x_{old} + v_{new} \cdot dt$$
6.  **Pygame Visualization:**
    * Pygame is used to create the graphical window.
    * The calculated positions (which are in meters) are scaled down to fit the screen using a `scale` factor.
    * Circles are drawn for the Sun and planets.
    * Lines are drawn between consecutive points of the planets' paths to visualize their orbits.
    * The `frame` variable controls the animation, advancing through the pre-calculated positions.

---

## Requirements

To run this simulation, you need:

* Python 3.x
* Pygame library
* NumPy library

---

## How to Run

1.  **Install Python:** If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).
2.  **Install Libraries:** Open your terminal or command prompt and install the required libraries:
    ```bash
    pip install pygame numpy
    ```
3.  **Save the Code:** Save the provided Python code as a `.py` file (e.g., `solar_system.py`).
4.  **Run the Simulation:** Navigate to the directory where you saved the file in your terminal or command prompt and run:
    ```bash
    python solar_system.py
    ```

---

## Customization

You can modify the simulation parameters in the Python script:

* `dt_factor`: Adjust this value to change the simulation speed (e.g., `dt_factor = 1` for real-time scaling, `dt_factor = 10` for faster simulation).
* `total_time`: Change `total_time` to simulate for a longer or shorter duration.
* `scale`: Modify the `scale` variable to adjust how large the orbits appear on the screen.

---

Maths Used

## Credits

Developed by Mithlesh.
