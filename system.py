import numpy as np
import matplotlib.pyplot as plt


plt.style.use('dark_background')


class System:
    def __init__(self, name: str, dimension: int):
        assert dimension == 2 or dimension == 3, "There's no visualization for this choice of dimension!"

        self.dimension = dimension
        self.name = name
        self.bodies = []
        # Given the units:
        # UA = Distance Earth-Moon;
        # UM = Earth's mass;
        # UT = 1 month;
        # the gravitational constant is approximately given by
        self.G = 5  # UA.UM^(-1).UT^(-2)
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
        for body in self.bodies:
            body.position = body.new_position

    def _update_body(self, body, dt, iteration):
        # Determine acceleration using Newton's law of universal gravitation
        new_acceleration = np.zeros(self.dimension)
        for other in self.bodies:
            if body != other:
                r = other.position - body.position
                mag_r = np.linalg.norm(r)
                if mag_r > 0:
                    new_acceleration += (self.G * other.mass / mag_r**3) * r
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
        body.new_position = new_position

    def run_simulation(self, total_time, dt, window_increase):
        if self.dimension == 2:
            colors = [body.color for body in self.bodies]
            radii = [body.radius for body in self.bodies]

            fig, ax = plt.subplots()
            scatter = ax.scatter([], [], s=20)
            ax.set_title(f"Simulation of the {self.name}")
            ax.set_xlabel('X-axis (UA)')
            ax.set_ylabel('Y-axis (UA)')
            initial_coordinates = self.get_initial_coordinates()
            window_range = max(initial_coordinates) + window_increase
            ax.set_xlim(-window_range, window_range)
            ax.set_ylim(-window_range, window_range)

            num_steps = int(total_time / dt)
            month_count = 0
            subtitle = ax.text(0.5, 0.05, "", color='white', fontsize=10, transform=ax.transAxes, ha='center')
            for i in range(num_steps):
                self.update(dt, i)
                x_positions = [body.position[0] for body in self.bodies]
                y_positions = [body.position[1] for body in self.bodies]

                scatter.set_offsets(np.column_stack((x_positions, y_positions)))
                scatter.set_color(colors)
                scatter.set_sizes(radii)

                if ((i+1) * dt) - int((i+1) * dt) == 0:
                    month_count += 1
                subtitle.remove()
                subtitle = ax.text(0.5, 0.05, f"Month {month_count}", color='white', fontsize=10, transform=ax.transAxes, ha='center')
                plt.pause(dt)

            plt.show()

        elif self.dimension == 3:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            initial_coordinates = self.get_initial_coordinates()
            window_range = max(initial_coordinates) + window_increase

            colors = [body.color for body in self.bodies]
            radii = [body.radius for body in self.bodies]

            num_steps = int(total_time / dt)
            month_count = 0
            for i in range(num_steps):
                self.update(dt, i)
                x_positions = [body.position[0] for body in self.bodies]
                y_positions = [body.position[1] for body in self.bodies]
                z_positions = [body.position[2] for body in self.bodies]
                ax.clear()
                ax.set_title(f"Simulation of the {self.name}")
                ax.set_xlabel('X-axis (UA)')
                ax.set_ylabel('Y-axis (UA)')
                ax.set_zlabel('Z-axis (UA)')
                ax.set_xlim(-window_range, window_range)
                ax.set_ylim(-window_range, window_range)
                ax.set_zlim(-window_range, window_range)
                ax.scatter(x_positions, y_positions, z_positions, s=radii, c=colors)

                if ((i+1) * dt) - int((i+1) * dt) == 0:
                    month_count += 1
                subtitle_text = f"Month {month_count}"
                ax.text(0.5, 0.05, 0.05, subtitle_text, color='white', fontsize=10, transform=ax.transAxes, ha='center')
                plt.pause(dt)

            plt.show()
