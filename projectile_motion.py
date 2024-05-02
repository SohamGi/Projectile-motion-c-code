import math

# Constants
GRAVITY = 9.81  # acceleration due to gravity (m/s^2)

def find_initial_velocity_and_angle(range_, max_height):
    """
    Calculate the initial velocity and launch angle for a given range and maximum height.

    Args:
    range_ (float): The horizontal range in meters.
    max_height (float): The maximum height in meters.

    Returns:
    tuple: Initial velocity (m/s) and launch angle (degrees).
    """
    # Solving for launch angle (theta) using the equation for max height
    theta = math.atan((4 * max_height) / range_)

    # Solving for initial velocity (u) using the launch angle
    u = math.sqrt((range_ * GRAVITY) / math.sin(2 * theta))

    # Converting angle from radians to degrees
    theta_deg = math.degrees(theta)

    return u, theta_deg

def calculate_vertical_launch(max_height):
    """
    Calculate the initial velocity and time of flight for a vertical launch.

    Args:
    max_height (float): The maximum height in meters.

    Returns:
    tuple: Initial velocity (m/s) and time of flight (seconds).
    """
    v = math.sqrt(2 * GRAVITY * max_height)
    time = (2 * v) / GRAVITY
    return v, time

def main():
    try:
        range_input = float(input("Enter the horizontal range (meters): "))
        max_height_input = float(input("Enter the maximum height (meters): "))

        if max_height_input < 0 or range_input < 0:
            print("Please enter non-negative values for range and height.")
        elif max_height_input == 0:
            print("Initial velocity: 0 m/s\nLaunch angle: 0 degrees\nTime of flight: 0 seconds")
        elif range_input == 0:
            initial_velocity, time_of_flight = calculate_vertical_launch(max_height_input)
            print(f"Initial velocity: {initial_velocity:.2f} m/s")
            print("Launch angle: 90 degrees")
            print(f"Time of flight: {time_of_flight:.2f} seconds")
        else:
            initial_velocity, launch_angle = find_initial_velocity_and_angle(range_input, max_height_input)
            print(f"Initial velocity: {initial_velocity:.2f} m/s")
            print(f"Launch angle: {launch_angle:.2f} degrees")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
