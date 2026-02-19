import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(20, 20)
        self.text_font = pygame.font.SysFont(None, 30, bold=True, italic=True)
        self.score = 0

    def draw(self, screen):
        img = self.text_font.render(str(self.score), True, (255, 255, 255))
        screen.blit(img, self.position)
        pass

    def update(self, dt):
        pass

    def score_points(self, points):
        self.score += points
