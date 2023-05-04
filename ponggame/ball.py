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
        self._bounce_effect = pygame.mixer.Sound("ponggame/assets/audio/zapsplat_cartoon_pop_mouth_mid_pitch_003_86613.mp3")
        self._score_effect = pygame.mixer.Sound("ponggame/assets/audio/zapsplat_multimedia_game_sound_bright_win_bonus_complete_tone_78303.mp3")
        (self._width, self._height) = self._surface.get_size()
        self._x_velocity = 5
        self._y_velocity = 4
        self._ai_score = 0
        self._player_score = 0

    def draw(self):
        """Draw the Ball."""
        pygame.draw.rect(self._surface, self._color, self._ball)

    def bounce(self):
        """Bounce the ball off the walls."""
        # bounce of the balls
        if self._ball.x >= self._width or self._ball.x < 0:
            self._x_velocity *= -1
            self._ball.x += self._x_velocity
            self.bounce_effect()

    def update(self):
        self._ball.x += self._x_velocity
        self._ball.y += self._y_velocity
        self.bounce()

        if self._ball.y >= self._height:
            self.reset_ball()
            self._ai_score += 1
            self.score_effect()
        if self._ball.y < 0:
            self.reset_ball()
            self._player_score += 1
            self.score_effect()

    def reset_ball(self):
        """Rest the positon of the ball to the middle."""
        self._ball = pygame.Rect(300, 300, 12, 12)

    def reflect(self):
        """Reflect the ball."""
        self._y_velocity *= -1
    
    def bounce_effect(self):
        """Play the bounce sound effect."""
        pygame.mixer.Sound.play(self._bounce_effect)

    def score_effect(self):
        """PLays sound when a player scores."""
        pygame.mixer.Sound.play(self._score_effect)

    def does_collide(self, paddle):
        """Check if ball collides with a paddle."""
        collide = pygame.Rect.colliderect(self._ball, paddle)
        if collide:
            self.reflect()
            self.bounce_effect()