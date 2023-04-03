# Mario Linares


"""This file contains the Ball class."""

import pygame


class Ball:
    """This class represents the ball in a Pong game."""

    def __init__(self, surface):
        """Initialization of the Ball."""
        self._surface = surface
        self._color = (255, 255, 255)
        self._ball = pygame.Rect(300, 300, 12, 12)

    def draw(self):
        """Draw the Ball."""
        pygame.draw.rect(self._surface, self._color, self._ball)
