import numpy as np


class Body:
    def __init__(self, name: str, color: str, mass: float, position, velocity):
        # Run basic validations to the received arguments
        assert mass > 0, f"Mass must be positive!"
        assert isinstance(position, np.ndarray), "Initial position must be a numpy array!"
        assert isinstance(velocity, np.ndarray), "Initial velocity must be a numpy array!"
        assert len(position) == len(velocity), f"Initial position and velocity vectors must have the same dimensions!"
        assert np.issubdtype(position.dtype, np.number), "All values of the initial position must be numerical!"
        assert np.issubdtype(velocity.dtype, np.number), "All values of the initial velocity must be numerical!"

        # Assigning attributes
        self.__name = name
        self.__color = color
        self.__mass = mass
        self.__position = position
        self.__velocity = velocity
        self.__acceleration = []

    def __repr__(self):
        return self.__name

    # Defining getters and setters
    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def mass(self):
        return self.__mass

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, value):
        self.__velocity = value

    @property
    def acceleration(self):
        return self.__acceleration

    @acceleration.setter
    def acceleration(self, value):
        self.__acceleration = value
