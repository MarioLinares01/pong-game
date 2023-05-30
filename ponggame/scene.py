# Mario Linares


"""A Scene class which represents all scenes in a Pong game."""

import pygame
from ponggame.ball import Ball
from ponggame.paddle import Paddle
from ponggame.paddle import AI


class Scene:
    """This class represents the scenes in a Pong game."""

    def __init__(self, screen, background_color, soundtrack=None):
        """Initialize a Scene object."""
        self._screen = screen
        self._background = pygame.Surface(self._screen.get_size())
        self._background.fill((background_color))
        self._is_valid = True
        self._frame_rate = 60

    def update(self):
        """Update a Scene object."""
        pass

    def draw(self):
        """Draw a scene."""
        self._screen.blit(self._background, (0, 0))

    @property
    def is_valid(self):
        """Returns a bool that tells if a Scene is valid."""
        return self._is_valid

    @property
    def frame_rate(self):
        """Returns the frame rate of a Scene."""
        return self._frame_rate

    def handle_event(self, event):
        """Controls for the Scene."""
        if event.type == pygame.KEYDOWN and \
            event.key == pygame.K_SPACE:
            self._is_valid = False

class TitleScene(Scene):
    """A child of Scene that represents a Title scene."""

    def __init__(self, title, screen, background_color, soundtrack=None):
        """Initialize a title scene."""
        super().__init__(screen, background_color)
        self._title = title

    def draw(self):
        """Draw the TitleScene."""
        super().draw()
        (width, height) = self._screen.get_size()
        title_font = pygame.font.Font("ponggame/assets/fonts/square_sans_serif_7.ttf", 70)
        rendered_title = title_font.render(self._title, True, (0, 250, 0))
        title_position = rendered_title.get_rect(center=(width / 2, height / 2))

        self._screen.blit(rendered_title, title_position)


class GameScene(Scene):
    """A child of Scene that represents a Game scene."""
    def __init__(self, screen, background_color):
        super().__init__(screen, background_color)
        self._frame_rate = 60
        self._clock = pygame.time.Clock()
        self._winner = ""
        self._play_again = ""
        self._ai_score = 0
        self._player_score = 0
        self._paddle = Paddle(self._screen)
        self._ball = Ball(self._screen)
        self._ai = AI(self._screen)

    def draw(self):
        """Draw a game scene."""
        super().draw()
        (width, height) = self._screen.get_size()
        midline = pygame.draw.line(self._screen, (0, 255, 0), [0, height / 2], [600, height / 2], width=3)

        score_font = pygame.font.Font("ponggame/assets/fonts/square_sans_serif_7.ttf", 70)
        ai_rendered_score = score_font.render(str(self._ai_score), True, (0, 250, 0))
        ai_score_position = ai_rendered_score.get_rect(center=(570, 272))
        self._screen.blit(ai_rendered_score, ai_score_position)

        player_rendered_score = score_font.render(str(self._player_score), True, (0, 250, 0))
        player_score_position = player_rendered_score.get_rect(center=(570, 328))
        self._screen.blit(player_rendered_score, player_score_position)

        replay_font = pygame.font.Font("ponggame/assets/fonts/square_sans_serif_7.ttf", 40)
        replay_rendered = replay_font.render(self._winner, True, (0, 250, 0))
        replay_position = replay_rendered.get_rect(center=(300, 200))
        self._screen.blit(replay_rendered, replay_position)

        replay_font = pygame.font.Font("ponggame/assets/fonts/square_sans_serif_7.ttf", 18)
        replay_rendered = replay_font.render(self._play_again, True, (0, 250, 0))
        replay_position = replay_rendered.get_rect(center=(300, 250))
        self._screen.blit(replay_rendered, replay_position)

        self._paddle.draw()
        self._ai.draw()
        self._ball.draw()
    
    def update_score(self):
        """Update the scoreboard."""
        score_font = pygame.font.Font("ponggame/assets/fonts/square_sans_serif_7.ttf", 70)
        ai_rendered_score = score_font.render(str(self._ai_score), True, (0, 250, 0))
        ai_score_position = ai_rendered_score.get_rect(center=(570, 272))
        self._screen.blit(ai_rendered_score, ai_score_position)

        player_rendered_score = score_font.render(str(self._player_score), True, (0, 250, 0))
        player_score_position = player_rendered_score.get_rect(center=(570, 328))
        self._screen.blit(player_rendered_score, player_score_position)

    def play_again(self):
        """Loop the GameScene if player would like to play again."""
        play_again = GameScene(self._screen, (0, 0, 0))
        while play_again.is_valid:
            self._clock.tick(play_again.frame_rate)
            for event in pygame.event.get():
                play_again.handle_event(event)
            play_again.update()
            play_again.draw()
            pygame.display.update()

    def update(self):
        """Update the GameScene"""
        self._paddle.move()
        self._ai.move(self._ball._ball)
        self._ball.update()
        self._ai_score = self._ball._ai_score
        self._player_score = self._ball._player_score
        self._ball.does_collide(self._paddle._paddle)
        self._ball.does_collide(self._ai._paddle)
        self.update_score()
        if self._ai_score == 5:
            self._winner = "You lost!!"
            self._play_again = "Would you like to play again?[y/n]"
            self._ball.freeze_ball()
            key = pygame.key.get_pressed()
            if key[pygame.K_n]:
                self._is_valid = False
            elif key[pygame.K_y]:
                self.play_again()
        elif self._player_score == 5:
            self._winner = "You won!!"
            self._play_again = "Would you like to play again?[y/n]"
            self._ball.freeze_ball()
            key = pygame.key.get_pressed()
            if key[pygame.K_n]:
                self._is_valid = False
            elif key[pygame.K_y]:
                self.play_again()
