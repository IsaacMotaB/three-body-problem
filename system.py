import numpy as np
import matplotlib.pyplot as plt


plt.style.use('dark_background')


class System:
    def __init__(self, name: str, dimension: int):
        assert dimension == 2 or dimension == 3, f"There's no visualization for this choice of dimension!"

        self.dimension = dimension
        self.name = name
        self.bodies = []
        self.G = 1
        self.initial_coordinates = []

    def add_body(self, body):
        if len(body.position) != self.dimension or len(body.velocity) != self.dimension:
            raise ValueError("Body dimension must match system dimension!")
        self.bodies.append(body)

    def get_initial_coordinates(self):
        initial_coordinates = []

        for body in self.bodies:
            for i in range(self.dimension):
                initial_coordinates.append(abs(body.position[i]))

        return initial_coordinates

    def update(self, dt, iteration):
        for body in self.bodies:
            self._update_body(body, dt, iteration)

    def _update_body(self, body, dt, iteration):
        # Determine acceleration using Newton's law of universal gravitation
        new_acceleration = np.zeros(self.dimension)
        for other in self.bodies:
            if body != other:
                r = other.position - body.position
                mag_r = np.linalg.norm(r)
                if mag_r > 0:
                    new_acceleration += (self.G * other.mass / mag_r**2) * r
        body.acceleration = new_acceleration

        # Calculate new velocity using leapfrog integration technique
        if iteration != 0:
            new_velocity = body.velocity + body.acceleration * dt
            body.velocity = new_velocity
        else:
            new_velocity = body.velocity + body.acceleration * dt / 2
            body.velocity = new_velocity

        # Calculate new position using leapfrog integration technique
        new_position = body.position + body.velocity * dt
        body.position = new_position

    def run_simulation(self, total_time, dt):
        if self.dimension == 2:
            fig, ax = plt.subplots()
            scatter = ax.scatter([], [])
            ax.set_xlabel('X-axis')
            ax.set_ylabel('Y-axis')
            ax.set_title(f"Simulation of the {self.name}")

            initial_coordinates = self.get_initial_coordinates()
            window_range = max(initial_coordinates) + 10
            ax.set_xlim(-window_range, window_range)
            ax.set_ylim(-window_range, window_range)

            colors = [body.color for body in self.bodies]

            num_steps = int(total_time / dt)
            for i in range(num_steps):
                self.update(dt, i)
                x_positions = [body.position[0] for body in self.bodies]
                y_positions = [body.position[1] for body in self.bodies]

                scatter.set_offsets(np.column_stack((x_positions, y_positions)))
                scatter.set_color(colors)
                plt.pause(dt)

            plt.show()

        elif self.dimension == 3:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            initial_coordinates = self.get_initial_coordinates()
            window_range = max(initial_coordinates) + 10

            colors = [body.color for body in self.bodies]

            num_steps = int(total_time / dt)
            for i in range(num_steps):
                self.update(dt, i)
                x_positions = [body.position[0] for body in self.bodies]
                y_positions = [body.position[1] for body in self.bodies]
                z_positions = [body.position[2] for body in self.bodies]
                ax.clear()
                ax.set_xlabel('X-axis')
                ax.set_ylabel('Y-axis')
                ax.set_zlabel('Z-axis')
                ax.set_title(f"Simulation of the {self.name}")
                ax.set_xlim(-window_range, window_range)
                ax.set_ylim(-window_range, window_range)
                ax.set_zlim(-window_range, window_range)
                ax.scatter(x_positions, y_positions, z_positions, c=colors)
                plt.pause(dt)

            plt.show()
