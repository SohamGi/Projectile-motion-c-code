import math

# Constants
GRAVITY = 9.81  # acceleration due to gravity (m/s^2)
DRAG_COEFFICIENT = 0.1  # drag coefficient in kg/m
MASS = 1.0  # mass of the projectile in kg

def find_velocity_and_angle(range_, max_height, steps=1000):
    """
    Calculate the initial velocity and launch angle for a given range and maximum height,
    taking air resistance into account using a numerical approach.

    Args:
    range_ (float): The horizontal range in meters.
    max_height (float): The maximum height in meters.
    steps (int): Number of simulation steps for numerical integration.

    Returns:
    tuple: Initial velocity (m/s) and launch angle (degrees).
    """
    best_u = None
    best_theta = None
    min_error = float('inf')
    
    for u_trial in range(1, 100):
        for theta_trial in range(1, 90):
            theta_rad = math.radians(theta_trial)
            vx = u_trial * math.cos(theta_rad)
            vy = u_trial * math.sin(theta_rad)
            x, y = 0, 0
            max_y = 0

            for _ in range(steps):
                air_resistance = DRAG_COEFFICIENT * (vx**2 + vy**2)**0.5 / MASS
                ax = -air_resistance * vx
                ay = -GRAVITY - air_resistance * vy

                vx += ax * (range_ / steps / vx)
                vy += ay * (range_ / steps / vx)
                x += vx * (range_ / steps / vx)
                y += vy * (range_ / steps / vx)

                if y > max_y:
                    max_y = y
                if y < 0:
                    break

            range_error = abs(range_ - x)
            height_error = abs(max_height - max_y)
            total_error = range_error + height_error

            if total_error < min_error:
                min_error = total_error
                best_u = u_trial
                best_theta = theta_trial
    
    return best_u, best_theta

range_input = float(input("Enter the horizontal range (meters): "))
max_height_input = float(input("Enter the maximum height (meters): "))

initial_velocity, launch_angle = find_velocity_and_angle(range_input, max_height_input)
print(f"Initial velocity: {initial_velocity:.2f} m/s")
print(f"Launch angle: {launch_angle:.2f} degrees")
