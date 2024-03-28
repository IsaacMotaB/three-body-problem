import numpy as np
from body import Body
from system import System


def simulate_system(name, dimension, bodies):
    system = System(name, dimension)
    for body in bodies:
        system.add_body(body)

    total_time = int(input("For how long do you the simulation to run (in seconds)? "))
    dt = float(input("What should be the time interval between frames (in seconds)? "))
    system.run_simulation(total_time, dt)


# Example usage
system_name = "arbitrary system"
system_dimension = 3
body1 = Body(name="Body 1", color="red", mass=1, position=np.array([0, 0, 0]), velocity=np.array([0, 0, 0]))
body2 = Body(name="Body 2", color="blue", mass=1, position=np.array([-1, -1, -1]), velocity=np.array([0, 0, 0]))
body3 = Body(name="Body 3", color="green", mass=1, position=np.array([2.5, 2.5, 2.5]), velocity=np.array([0, 0, 0]))
body4 = Body(name="Body 4", color="yellow", mass=1, position=np.array([2, 0, -2]), velocity=np.array([0, 0, 0]))
system_bodies = [body1, body2, body3, body4]

simulate_system(system_name, system_dimension, system_bodies)
