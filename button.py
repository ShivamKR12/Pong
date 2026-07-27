# button.py

import pygame


class Button:
    def __init__(self, text, x, y, width, height, font, bg_color, text_color):
        self.rect = pygame.Rect(x - width // 2, y - height // 2, width, height)
        self.bg_color = bg_color
        self.update_text(text, font, text_color)

    def update_text(self, text, font, text_color):
        self.text_surface = font.render(text, True, text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect, border_radius=12)
        screen.blit(self.text_surface, self.text_rect)

    def check_click(self, px, py):
        return self.rect.collidepoint(px, py)
