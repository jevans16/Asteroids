from typing import override

from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS
from constants import LINE_WIDTH


class Shot(CircleShape):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    @override
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        return super().draw(screen)

    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        return super().update(dt)
