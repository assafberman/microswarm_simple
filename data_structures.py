from phi.flow import *
from math import floor
from numpy.random import rand


class Member:
    def __init__(self, location=None, radius: float = 0, direction: float = 0, density=1):
        if location is None:
            location = {'x': 0, 'y': 0}
        self.location = location
        self.radius = radius
        self.direction = direction
        self.density = density

    def as_sphere(self):
        return Sphere(x=self.location['x'], y=self.location['y'], radius=self.radius)


class Swarm:
    def __init__(self, num_x: int = 0, num_y: int = 0, left_location: float = 0, bottom_location: float = 0,
                 member_interval_x: float = 0, member_interval_y: float = 0, member_radius: float = 0,
                 member_density=1):
        s = []
        for i in range(num_x):
            for j in range(num_y):
                s.append(
                    Member(location={'x': left_location + i * member_interval_x,
                                     'y': bottom_location + j * member_interval_y}, radius=member_radius,
                           direction=rand() * 2 * np.pi, density=member_density))
        self.members = s
        self.num_x = num_x
        self.num_y = num_y
        self.left_location = left_location
        self.bottom_location = bottom_location
        self.member_interval_x = member_interval_x
        self.member_interval_y = member_interval_y
        self.member_radius = member_radius

    def as_obstacle_list(self) -> list:
        return [Obstacle(Sphere(x=m.location['x'], y=m.location['y'], radius=m.radius)) for m in self.members]

    def as_sphere_list(self) -> list:
        return [Sphere(x=m.location['x'], y=m.location['y'], radius=m.radius) for m in self.members]


class Inflow:
    def __init__(self, frequency: float = 0, amplitude: float = 0, radius: float = 0, center_x: float = 0,
                 center_y: float = 0):
        self.frequency = frequency
        self.amplitude = amplitude
        self.radius = radius
        self.center_x = center_x
        self.center_y = center_y


class Fluid:
    def __init__(self, viscosity: float):
        self.viscosity = viscosity


class Simulation:
    def __init__(self, length_x: float = 0, length_y: float = 0, resolution: tuple[int, int] = (0, 0), dt: float = 0,
                 total_time: float = 0):
        self.length_x = length_x
        self.length_y = length_y
        self.resolution = resolution
        self.dx = self.length_x / self.resolution[0]
        self.dy = self.length_y / self.resolution[1]
        self.dt = dt
        self.total_time = total_time
        self.time_steps = floor(self.total_time / self.dt)
