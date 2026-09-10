from typing import override
import random
from circleshape import CircleShape
from logger import log_event
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)


    @override
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        return super().draw(screen)

    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

        return super().update(dt)

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle =random.uniform(20, 50)
            first_velocity = self.velocity.rotate(new_angle)
            second_velocity = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = first_velocity * 1.2
            asteroid_2.velocity = second_velocity * 1.2
