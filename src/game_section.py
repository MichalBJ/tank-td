import pygame
from config import consts

class GameSection():

    def __init__(self, position, img, active):
        self.position = position
        self.image = pygame.image.load(img)
        self.active = active

    def draw(self, dest):
        dest.blit(self.image, self.position)


main_menu = GameSection(consts.MAIN_MENU_POS, consts.MAIN_MENU_IMG, consts.MAIN_MENU_ACTIVE)
game = GameSection(consts.GAME_POS, consts.GAME_IMG, consts.GAME_ACTIVE)
game_bg = GameSection(consts.GAME_BG_POS, consts.GAME_BG_IMG, consts.GAME_BG_ACTIVE)
between_level_upgrade = GameSection(consts.BETWEEN_LEVEL_UPGRADE_POS, consts.BETWEEN_LEVEL_UPGRADE_IMG, consts.BETWEEN_LEVEL_UPGRADE_ACTIVE)
credit = GameSection(consts.CREDIT_POS, consts.CREDIT_IMG, consts.CREDIT_ACTIVE)
