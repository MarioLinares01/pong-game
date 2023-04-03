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
        (self._width, self._height) = self._surface.get_size()
        self._x_velocity = 3
        self._y_velocity = 6

    def draw(self):
        """Draw the Ball."""
        pygame.draw.rect(self._surface, self._color, self._ball)

    def bounce(self):
        """Bounce the ball off the walls."""
        # bounce of the balls
        if self._ball.x >= self._width or self._ball.x < 0:
            self._x_velocity *= -1
            self._ball.x += self._x_velocity

    def update(self):
        self._ball.x += self._x_velocity
        self._ball.y += self._y_velocity
        self.bounce()

        if self._ball.y >= self._height or self._ball.y < 0:
            self.reset_ball()
            # change score
        


    def reset_ball(self):
        """Rest the positon of the ball to the middle."""
        self._ball.x = 300
        self._ball.y = 300
    
    def reflect(self):
        """Reflect the ball."""
        self._y_velocity *= -1
    
    def does_collide(self, paddle):
        """Check if ball collides with a paddle."""
        collide = pygame.Rect.colliderect(self._ball, paddle)
        if collide:
            self.reflect()