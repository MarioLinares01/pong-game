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
        self._speed = 7

    def draw(self):
        """Draw the Paddle."""
        pygame.draw.rect(self._surface, self._color, self._paddle)

    def move(self):
        """Move the paddle."""
        pygame.key.set_repeat(1, 10)
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            
            self._paddle.move_ip(self._speed, 0)
        elif key[pygame.K_LEFT]:
            pygame.key.get_repeat()
            self._paddle.move_ip(-1 * self._speed, 0)


    def does_collide(self):
        """Check if the paddle collides with a ball."""
        pass
