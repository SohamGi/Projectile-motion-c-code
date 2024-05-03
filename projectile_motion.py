import math 

h=9.8

def find_initial_velocity_and_angle(range_, max_height):
    g = 9.81  # acceleration due to gravity (m/s^2)

    # Solving for launch angle (theta) using the equation for max height
    theta = math.atan((4 * max_height) / range_)

    # Solving for initial velocity (u) using the launch angle
    u = math.sqrt((range_ * g) / math.sin(2 * theta))

    # Converting angle from radians to degrees
    theta_deg = math.degrees(theta)

    return u, theta_deg

# Example usage
range_input = float(input("Enter the horizontal range (meters): "))
max_height_input = float(input("Enter the maximum height (meters): "))

if (max_height_input==0):
    initial_velocity=0
    launch_angle=0
    print("The angle of launch is 0. However, since friction is absent and there is no air resistance,the object can have any velocity. Also this case is not considered as projectile motion")
    
elif (range_input==0):
    v=math.sqrt(2*h*max_height_input)
    launch_angle=90
    initial_velocity=v
    time=(2*v)/h
    print("Initial velocity:", initial_velocity,"m/s")
    print("Launch angle:", launch_angle, "degrees")
    print("Time of flight:", time,"seconds")
