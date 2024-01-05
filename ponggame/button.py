# Mario Linares


"""This file contains the Button class."""

import pygame


class Button:
    """This class represents a Button."""

    def __init__(self, surface, text, color, x_pos, y_pos):
        """Initialization of the Button."""
        self._surface = surface
        self._text = text
        self._color = color
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._font = pygame.font.Font("ponggame/assets/fonts/square_sans_serif_7.ttf", 45)
        self._render_button = self._font.render(self._text, True, self._color)
        self._button_positon = self._render_button.get_rect(center=(self._x_pos, self._y_pos))
        self._rect = pygame.Rect(self._button_positon.left, self._button_positon.top, 
                                 self._button_positon.width, self._button_positon.height)

    def draw(self):
        """Draw the Button."""
        self._surface.blit(self._render_button, self._button_positon)
        pygame.draw.rect(self._surface, (0, 0, 0), self._rect, 1)
    
    def hover_text(self):
        """Hover over text"""
        mouse_position = pygame.mouse.get_pos()
        if self._rect.collidepoint(mouse_position):
            self._render_button = self._font.render(self._text, True, (50, 50, 50))
        else:
            self._render_button = self._font.render(self._text, True, self._color)

    def button_pressed(self):
        """Update the state."""
        mouse_position = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if mouse_pressed and self._rect.collidepoint(mouse_position):
            return True
        else:
            return False
