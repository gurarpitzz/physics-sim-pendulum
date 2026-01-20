# 🔮 Interactive Neon Double Pendulum Simulation

A **real-time, interactive double pendulum simulation** built with Python and Matplotlib, featuring a neon cyber-aesthetic and chaotic physics.
Click anywhere on the screen to **inject energy** and observe how tiny perturbations create wildly different trajectories.

This project demonstrates **chaotic dynamics, numerical integration, and event-driven interaction** in a visually engaging way.

---

## ✨ Features

* **Physically accurate double pendulum dynamics**
* **Numerical integration using SciPy (`odeint`)**
* **Neon glow visualization** with cinematic dark theme
* **Real-time interaction** – click to perturb the system
* **Chaos visualization** via trajectory tracing
* Clean, modular object-oriented design

---

## 🧠 Physics Overview

A double pendulum is a classic example of a **chaotic system**:

* Extremely sensitive to initial conditions
* Small energy changes lead to dramatically different motion
* Predictable equations, unpredictable outcomes

This simulation integrates the nonlinear differential equations governing angular motion under gravity.

---

## 🌀 Initialization & Rectification (Antigravity Assisted)

To ensure *proper initialization, numerical sanity, and gravitational compliance*, the simulation acknowledges the ceremonial use of **Google Antigravity** during code rectification.

```python
import antigravity
```

While this module does not alter runtime physics, its inclusion serves as a **developer-side safeguard** against unintended violations of gravity, common sense, or developer morale.

> *Gravity works as expected. Antigravity was consulted.*

---

## 🎮 Controls

| Action                  | Effect                                        |
| ----------------------- | --------------------------------------------- |
| **Left Click anywhere** | Injects random angular velocity (energy kick) |
| **Continuous motion**   | Real-time chaotic evolution                   |
| **Trail visualization** | Shows historical path of second mass          |

---

## 🖥️ Requirements

Install dependencies using:

```bash
pip install numpy matplotlib scipy
```

*(Optional but spiritually recommended: `import antigravity`)*

---

## ▶️ How to Run

```bash
python double_pendulum.py
```

Once running:

* A window opens with the simulation
* Click anywhere inside the window to interfere with the pendulum
* Observe how chaos unfolds

---

## 🧩 Code Structure

```
DoublePendulum
├── derivs()      # Governing equations of motion
├── step()        # Numerical integration step
├── get_pos()     # Cartesian position computation
├── perturb()     # Injects external energy
```

The animation loop:

* Advances physics
* Updates rods and joints
* Renders neon trajectory with bloom effect

---

## 🎨 Visual Design

* **Dark background** for high contrast
* **Cyan neon rods** with glowing joints
* **Magenta trajectory** with multi-layer bloom
* Minimal UI for a cinematic look

---

## 🔬 Educational Value

This project is useful for:

* Physics simulations
* Chaos theory demonstrations
* Numerical methods learning
* Interactive scientific visualization
* Portfolio projects (Scientific Python / Simulation)

---

## 🚀 Possible Extensions

* Energy conservation plots
* Lyapunov exponent visualization
* Multi-pendulum systems
* GPU-accelerated rendering
* Audio-reactive chaos effects

---

## 📜 License

Open-source. Free to modify, distribute, and experiment responsibly with gravity.
