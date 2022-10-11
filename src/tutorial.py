import pygame
import os

page_images = []

for x in range(1, 12):
    add_str = str(x)
    page_images.append(pygame.image.load(os.path.join('img/tutorial', 'page' + add_str + '.png')))

arrow_images = [pygame.image.load('img/tutorial/arrow_DL.png'),
                pygame.image.load('img/tutorial/arrow_DR.png'),
                pygame.image.load('img/tutorial/arrow_UL.png'),
                pygame.image.load('img/tutorial/arrow_UR.png')
                ]


class Tutorial():
    def __init__(self):
        self.active = False
        self.bg = pygame.image.load('img/tutorial/bg.png')
        self.page_imgs = page_images
        self.arrows_imgs = arrow_images
        self.page = 0

    def draw(self, dest):
        dest.blit(self.bg, (0, 0))
        if self.page in range(1, 3):
            dest.blit(self.arrows_imgs[2], (154, 140))
            dest.blit(self.arrows_imgs[2], (586, 140))
            dest.blit(self.arrows_imgs[3], (945, 140))
            if self.page == 2:
                dest.blit(self.arrows_imgs[1], (520, 610))
        if self.page in range(3, 6):
            dest.blit(self.arrows_imgs[0], (145, 610))
            if self.page == 3:
                dest.blit(self.arrows_imgs[1], (520, 610))
        if self.page in range(6, 8):
            dest.blit(self.arrows_imgs[1], (820, 610))
        dest.blit(self.page_imgs[self.page], (328, 225))

    def reset_tutorial_page(self):
        if self.active == False:
            self.page = 0

tutorial = Tutorial()
