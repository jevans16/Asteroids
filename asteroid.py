from typing import override

from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH

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
