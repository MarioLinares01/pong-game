# Mario Linares


"""A Scene class which represents all scenes in a Pong game."""

import pygame


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
