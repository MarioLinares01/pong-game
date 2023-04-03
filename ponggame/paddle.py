# Mario Linares


"""This file contains the Paddle class."""

import pygame


class Paddle:
    """This class represents the paddle in a Pong game."""
    
    def __init__(self, surface):
        """Initialization of the Paddle."""
        self._surface = surface
        self._color = (255, 255, 255)
        self._paddle = pygame.Rect(290, 570, 80, 8)
        self._speed = 10

    def draw(self):
        """Draw the Paddle."""
        pygame.draw.rect(self._surface, self._color, self._paddle)

    def move(self):
        """Move the paddle."""
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            if self._paddle.x < 510:
                self._paddle.move_ip(self._speed, 0)
        elif key[pygame.K_LEFT]:
             if self._paddle.x > 10:
                self._paddle.move_ip(-1 * self._speed, 0)

class AI(Paddle):
    """This class represents the ai paddle in a Pong game."""

    def __init__(self, surface):
        """Imitializes the AI paddle."""
        super().__init__(surface)
        self._paddle = pygame.Rect(290, 5, 80, 8)
        self._speed = 5

    
