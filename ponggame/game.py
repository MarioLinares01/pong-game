# Mario Linares


"""A pong game."""

import pygame
from ponggame.scene import GameScene
from ponggame.scene import TitleScene


class Pong:
    """This class represents a Pong game."""

    def __init__(self, window_width=600, window_height=600, window_title="Pong!"):
        pygame.init()
        self._window_size = (window_width, window_height)
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode(self._window_size)
        self._title = window_title
        pygame.display.set_caption(self._title)
        self._game_is_over = False
        if not pygame.font:
            print("Warning: Fonts are disabled.")
        if not pygame.mixer:
            print("Warning: Sound is disabled.")
        self._scene_graph = None

    def build_scene_graph(self):
        """Builds the scenes of the game."""
        self._scene_graph = [
            TitleScene("Pong!", self._screen, (0, 0, 0)),
            GameScene(self._screen, (0, 0, 0))
        ]

    def run(self):
        """A loop that will run the game."""
        for scene in self._scene_graph:
            while scene.is_valid:
                self._clock.tick(scene.frame_rate)
                for event in pygame.event.get():
                    scene.handle_event(event)
                scene.update()
                scene.draw()
                pygame.display.update()
        pygame.quit()
        return 0
