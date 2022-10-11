import pygame
from config import consts

class Base():
    def __init__(self, position, img, live, live_max, bar_w, bar_h):
        self.position = position
        self.image = pygame.image.load(img)
        self.live_max = live_max
        self.live = live
        self.bar_w = bar_w
        self.bar_w_g = bar_w
        self.bar_h = bar_h

    def render_base_and_live_bar(self, dest):
        dest.blit(self.image, self.position)
        pygame.draw.rect(dest, 'red', [self.position[0] + 20, self.position[1] - 50, self.bar_w, self.bar_h])
        pygame.draw.rect(dest, 'green', [self.position[0] + 20, self.position[1] - 50, self.bar_w_g, self.bar_h])


player_base = Base(consts.PLAYER_BASE_POS,
                   consts.PLAYER_BASE_IMG,
                   consts.PLAYER_BASE_LIVE,
                   consts.PLAYER_BASE_LIVE_MAX,
                   consts.PLAYER_BASE_BAR_W,
                   consts.PLAYER_BASE_BAR_H)

enemy_base = Base(consts.ENEMY_BASE_POS,
                   consts.ENEMY_BASE_IMG,
                   consts.ENEMY_BASE_LIVE,
                  consts.ENEMY_BASE_LIVE_MAX,
                   consts.ENEMY_BASE_BAR_W,
                   consts.ENEMY_BASE_BAR_H)