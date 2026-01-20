import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import odeint

# Use dark background for neon look
plt.style.use('dark_background')

class DoublePendulum:
    def __init__(self, L1=1.0, L2=1.0, M1=1.0, M2=1.0):
        self.L1 = L1
        self.L2 = L2
        self.M1 = M1
        self.M2 = M2
        self.g = 9.81
        
        # Initial state: th1, w1, th2, w2
        # Start high up for good energy
        self.state = np.array([np.pi/1.1, 0, np.pi/1.1, 0], dtype=float)
        
    def derivs(self, state, t):
        dydx = np.zeros_like(state)
        dydx[0] = state[1]

        delta = state[2] - state[0]
        den1 = (self.M1+self.M2) * self.L1 - self.M2 * self.L1 * np.cos(delta) * np.cos(delta)
        dydx[1] = ((self.M2 * self.L1 * state[1] * state[1] * np.sin(delta) * np.cos(delta)
                + self.M2 * self.g * np.sin(state[2]) * np.cos(delta)
                + self.M2 * self.L2 * state[3] * state[3] * np.sin(delta)
                - (self.M1+self.M2) * self.g * np.sin(state[0]))
               / den1)

        dydx[2] = state[3]

        den2 = (self.L2/self.L1) * den1
        dydx[3] = ((- self.M2 * self.L2 * state[3] * state[3] * np.sin(delta) * np.cos(delta)
                + (self.M1+self.M2) * self.g * np.sin(state[0]) * np.cos(delta)
                - (self.M1+self.M2) * self.L1 * state[1] * state[1] * np.sin(delta)
                - (self.M1+self.M2) * self.g * np.sin(state[2]))
               / den2)

        return dydx

    def step(self, dt):
        # Result is the state at t+dt. odeint returns [state_t, state_t+dt, ...]
        # We integrate over a small step dt
        t_span = [0, dt]
        next_state = odeint(self.derivs, self.state, t_span)[1]
        self.state = next_state
        return self.get_pos()

    def get_pos(self):
        th1, th2 = self.state[0], self.state[2]
        
        x1 = self.L1 * np.sin(th1)
        y1 = -self.L1 * np.cos(th1)

        x2 = x1 + self.L2 * np.sin(th2)
        y2 = y1 - self.L2 * np.cos(th2)
        
        return x1, y1, x2, y2

    def perturb(self, strength=2.0):
        # Add random angular velocity kick to simulate interaction/interference
        self.state[1] += np.random.uniform(-strength, strength)
        self.state[3] += np.random.uniform(-strength, strength)
        print("Pendulum Perturbed! New energy injected.")

# Global instances
sim = DoublePendulum(L1=1.0, L2=1.0, M1=1.0, M2=1.0)
dt = 0.04
history_x, history_y = [], []
max_history = 200

fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2.2, 2.2), ylim=(-2.2, 2.2))
ax.set_aspect('equal')
ax.grid(False) # Turn off grid for cleaner look
ax.axis('off') # Turn off axis for cinematic look

# Visual elements
# Rods: Cyan neon with glowing joints
line, = ax.plot([], [], 'o-', lw=3, color='#00FFFF', markersize=8, markeredgecolor='white', label='Pendulum')

# Trace: Magenta neon glow
# Main sharp line
trace, = ax.plot([], [], '-', lw=1.5, color='#FF00FF', alpha=0.9)
# Bloom effects (wider transparent lines)
trace_bloom1, = ax.plot([], [], '-', lw=4, color='#FF00FF', alpha=0.3)
trace_bloom2, = ax.plot([], [], '-', lw=8, color='#FF00FF', alpha=0.1)

info_text = ax.text(0.5, 0.95, 'CLICK anywhere to hit the pendulum!', 
                   transform=ax.transAxes, color='white', fontsize=12, 
                   ha='center', weight='bold')

def init():
    line.set_data([], [])
    trace.set_data([], [])
    trace_bloom1.set_data([], [])
    trace_bloom2.set_data([], [])
    return line, trace, trace_bloom1, trace_bloom2

def update(frame):
    global history_x, history_y
    
    # Physics step
    x1, y1, x2, y2 = sim.step(dt)
    
    # Update rods
    line.set_data([0, x1, x2], [0, y1, y2])
    
    # Update trace memory
    history_x.append(x2)
    history_y.append(y2)
    
    if len(history_x) > max_history:
        history_x.pop(0)
        history_y.pop(0)
        
    # Update trace lines
    trace.set_data(history_x, history_y)
    trace_bloom1.set_data(history_x, history_y)
    trace_bloom2.set_data(history_x, history_y)
    
    return line, trace, trace_bloom1, trace_bloom2

def on_click(event):
    if event.inaxes == ax:
        sim.perturb(strength=4.0)
        info_text.set_text("INTERFERENCE DETECTED")
        info_text.set_color('#FFFF00') # Yellow warning
        plt.draw()
        
        # Reset text color after a moment (conceptually) - hard to do perfectly in mpl event loop without timer
        # but the physics reaction will be obvious

fig.canvas.mpl_connect('button_press_event', on_click)

print("Double Pendulum Simulation with Interaction")
print("Click on the window to interfere with the pendulum.")

ani = animation.FuncAnimation(
    fig, update, frames=None, init_func=init,
    interval=dt*1000, blit=True
)

plt.show()
