import numpy as np


class Body:
    def __init__(self, name: str, color: str, radius: float, mass: float, position, velocity):
        # Run basic validations to the received arguments
        assert mass >= 0, "Mass cannot be negative!"
        assert isinstance(position, np.ndarray), "Initial position must be a numpy array!"
        assert isinstance(velocity, np.ndarray), "Initial velocity must be a numpy array!"
        assert len(position) == len(velocity), "Initial position and velocity vectors must have the same dimensions!"
        assert np.issubdtype(position.dtype, np.number), "All values of the initial position must be numerical!"
        assert np.issubdtype(velocity.dtype, np.number), "All values of the initial velocity must be numerical!"

        # Assigning attributes
        self.__name = name
        self.__color = color
        self.__radius = radius
        self.__mass = mass
        self.__position = position
        self.__velocity = velocity
        self.__acceleration = []
        self.__new_position = []

    @staticmethod
    def string_to_vector(string):
        elements = string.strip('[]').split(',')
        vector = [float(element.strip()) for element in elements]
        return np.array(vector)

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
    def radius(self):
        return self.__radius

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

    @property
    def new_position(self):
        return self.__new_position

    @new_position.setter
    def new_position(self, value):
        self.__new_position = value
