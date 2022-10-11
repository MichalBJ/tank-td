import pygame
from config import consts


class Storage():

    def __init__(self):
        self.iron_stock = 1
        self.crystal_stock = 1
        self.uran_stock = 1
        self.iron_count_mining = 1
        self.crystal_count_mining = 1
        self.uran_count_mining = 1
        self.iron_can_upgrade = False
        self.crystal_can_upgrade = False
        self.uran_can_upgrade = False
        self.iron_upgrading = False
        self.crystal_upgrading = False
        self.uran_upgrading = False
        self.iron_final_time = 1
        self.crystal_final_time = 1
        self.uran_final_time = 1
        self.iron_mining_progres_bar = float(152 / consts.IRON_SPEED_MINIG)
        self.crystal_mining_progres_bar = float(152 / consts.CRYSTAL_SPEED_MINIG)
        self.uran_mining_progres_bar = float(152 / consts.URAN_SPEED_MINIG)
        self.iron_upgrading_progres_bar = float(152 / consts.IRON_UPGRADING_TIME)
        self.crystal_upgrading_progres_bar = float(152 / consts.CRYSTAL_UPGRADING_TIME)
        self.uran_upgrading_progres_bar = float(152 / consts.URAN_UPGRADING_TIME)

    def mining(self, timer):
        if timer % consts.IRON_SPEED_MINIG == 0:
            self.iron_stock += self.iron_count_mining
        if timer % consts.CRYSTAL_SPEED_MINIG == 0:
            self.crystal_stock += self.crystal_count_mining
        if timer % consts.URAN_SPEED_MINIG == 0:
            self.uran_stock += self.uran_count_mining

    def render_resources(self, font, dest):
        iron_text = font.render(f'{self.iron_stock}', True, consts.RES_FONT_COLOR)
        crystal_text = font.render(f'{self.crystal_stock}', True, consts.RES_FONT_COLOR)
        uran_text = font.render(f'{self.uran_stock}', True, consts.RES_FONT_COLOR)
        dest.blit(iron_text,
                    (consts.IRON_PANEL_POS[0] + 225 - iron_text.get_width() - 10, consts.IRON_PANEL_POS[1] + 7))
        dest.blit(crystal_text,
                    (
                    consts.CRYSTAL_PANEL_POS[0] + 225 - crystal_text.get_width() - 10, consts.CRYSTAL_PANEL_POS[1] + 7))
        dest.blit(uran_text,
                    (consts.URAN_PANEL_POS[0] + 225 - uran_text.get_width() - 10, consts.URAN_PANEL_POS[1] + 7))


    def resource_upgrade(self, time):
        if self.iron_can_upgrade == True:
            if self.iron_upgrading == False:
                if self.iron_stock >= consts.IRON_UP_PRICE_IRON and self.crystal_stock >= consts.IRON_UP_PRICE_CRYSTAL and self.uran_stock >= consts.IRON_UP_PRICE_URAN:
                    self.iron_stock = self.iron_stock - consts.IRON_UP_PRICE_IRON
                    self.crystal_stock = self.crystal_stock - consts.IRON_UP_PRICE_CRYSTAL
                    self.uran_stock = self.uran_stock - consts.IRON_UP_PRICE_URAN
                    self.iron_upgrading = True
                    self.iron_final_time = time + consts.IRON_UPGRADING_TIME


        if self.iron_upgrading == True:
            if time / self.iron_final_time == 1:
                self.iron_count_mining += 1
                self.iron_upgrading = False
                self.iron_can_upgrade = False


        if self.crystal_can_upgrade == True:
            if self.crystal_upgrading == False:
                if self.iron_stock >= consts.IRON_UP_PRICE_IRON and self.crystal_stock >= consts.IRON_UP_PRICE_CRYSTAL and self.uran_stock >= consts.IRON_UP_PRICE_URAN:
                    self.iron_stock = self.iron_stock - consts.IRON_UP_PRICE_IRON
                    self.crystal_stock = self.crystal_stock - consts.IRON_UP_PRICE_CRYSTAL
                    self.uran_stock = self.uran_stock - consts.IRON_UP_PRICE_URAN
                    self.crystal_upgrading = True
                    self.crystal_final_time = time + consts.CRYSTAL_UPGRADING_TIME

        if self.crystal_upgrading == True:
            if time / self.crystal_final_time == 1:
                self.crystal_count_mining += 1
                self.crystal_upgrading = False
                self.crystal_can_upgrade = False


        if self.uran_can_upgrade == True:
            if self.uran_upgrading == False:
                if self.iron_stock >= consts.IRON_UP_PRICE_IRON and self.crystal_stock >= consts.IRON_UP_PRICE_CRYSTAL and self.uran_stock >= consts.IRON_UP_PRICE_URAN:
                    self.iron_stock = self.iron_stock - consts.IRON_UP_PRICE_IRON
                    self.crystal_stock = self.crystal_stock - consts.IRON_UP_PRICE_CRYSTAL
                    self.uran_stock = self.uran_stock - consts.IRON_UP_PRICE_URAN
                    self.uran_upgrading = True
                    self.uran_final_time = time + consts.URAN_UPGRADING_TIME

        if self.uran_upgrading == True:
            if time / self.uran_final_time == 1:
                self.uran_count_mining += 1
                self.uran_upgrading = False
                self.uran_can_upgrade = False


    def show_prize_upgrade(self, mouse_position, dest, info_font):
        if mouse_position[0] in range(consts.IRON_PANEL_POS[0], consts.IRON_PANEL_POS[0] + (pygame.image.load(consts.IRON_PANEL_IMG).get_width())) \
                and mouse_position[1] in range(consts.IRON_PANEL_POS[1], consts.IRON_PANEL_POS[1] + (pygame.image.load(consts.IRON_PANEL_IMG).get_height())):
            iron_info_iron = info_font.render(f'{consts.IRON_UP_PRICE_IRON}', True, consts.INFO_FONT_COLOR)
            iron_info_crystal = info_font.render(f'{consts.IRON_UP_PRICE_CRYSTAL}', True, consts.INFO_FONT_COLOR)
            iron_info_uran = info_font.render(f'{consts.IRON_UP_PRICE_URAN}', True, consts.INFO_FONT_COLOR)
            dest.blit(iron_info_iron, (consts.INFO_PANEL_POS[0] + 107 - iron_info_iron.get_width(), consts.INFO_PANEL_POS[1] + 16))
            dest.blit(iron_info_crystal, (consts.INFO_PANEL_POS[0] + 107 - iron_info_crystal.get_width(), consts.INFO_PANEL_POS[1] + 53))
            dest.blit(iron_info_uran, (consts.INFO_PANEL_POS[0] + 107 - iron_info_uran.get_width(), consts.INFO_PANEL_POS[1] + 88))

        if mouse_position[0] in range(consts.CRYSTAL_PANEL_POS[0], consts.CRYSTAL_PANEL_POS[0] + (pygame.image.load(consts.CRYSTAL_PANEL_IMG).get_width())) \
                and mouse_position[1] in range(consts.CRYSTAL_PANEL_POS[1], consts.CRYSTAL_PANEL_POS[1] + (pygame.image.load(consts.CRYSTAL_PANEL_IMG).get_height())):
            crystal_info_iron = info_font.render(f'{consts.CRYSTAL_UP_PRICE_IRON}', True, consts.INFO_FONT_COLOR)
            crystal_info_crystal = info_font.render(f'{consts.CRYSTAL_UP_PRICE_CRYSTAL}', True, consts.INFO_FONT_COLOR)
            crystal_info_uran = info_font.render(f'{consts.CRYSTAL_UP_PRICE_URAN}', True, consts.INFO_FONT_COLOR)
            dest.blit(crystal_info_iron, (consts.INFO_PANEL_POS[0] + 107 - crystal_info_iron.get_width(), consts.INFO_PANEL_POS[1] + 16))
            dest.blit(crystal_info_crystal, (consts.INFO_PANEL_POS[0] + 107 - crystal_info_crystal.get_width(), consts.INFO_PANEL_POS[1] + 53))
            dest.blit(crystal_info_uran, (consts.INFO_PANEL_POS[0] + 107 - crystal_info_uran.get_width(), consts.INFO_PANEL_POS[1] + 88))

        if mouse_position[0] in range(consts.URAN_PANEL_POS[0], consts.URAN_PANEL_POS[0] + (pygame.image.load(consts.URAN_PANEL_IMG).get_width())) \
                and mouse_position[1] in range(consts.URAN_PANEL_POS[1], consts.URAN_PANEL_POS[1] + (pygame.image.load(consts.URAN_PANEL_IMG).get_height())):
            uran_info_iron = info_font.render(f'{consts.URAN_UP_PRICE_IRON}', True, consts.INFO_FONT_COLOR)
            uran_info_crystal = info_font.render(f'{consts.URAN_UP_PRICE_CRYSTAL}', True, consts.INFO_FONT_COLOR)
            uran_info_uran = info_font.render(f'{consts.URAN_UP_PRICE_URAN}', True, consts.INFO_FONT_COLOR)
            dest.blit(uran_info_iron, (consts.INFO_PANEL_POS[0] + 107 - uran_info_iron.get_width(), consts.INFO_PANEL_POS[1] + 16))
            dest.blit(uran_info_crystal, (consts.INFO_PANEL_POS[0] + 107 - uran_info_crystal.get_width(), consts.INFO_PANEL_POS[1] + 53))
            dest.blit(uran_info_uran, (consts.INFO_PANEL_POS[0] + 107 - uran_info_uran.get_width(), consts.INFO_PANEL_POS[1] + 88))

    def progres_bar_upgrade(self, dest):
        if self.iron_upgrading == True:
            self.iron_upgrading_progres_bar += float(152 / consts.IRON_UPGRADING_TIME)
            pygame.draw.rect(dest, 'blue', [216, 103, self.iron_upgrading_progres_bar, 14])
        else:
            self.iron_upgrading_progres_bar = float(152 / consts.IRON_UPGRADING_TIME)

        if self.crystal_upgrading == True:
            self.crystal_upgrading_progres_bar += float(152 / consts.CRYSTAL_UPGRADING_TIME)
            pygame.draw.rect(dest, 'blue', [623, 103, self.crystal_upgrading_progres_bar, 14])
        else:
            self.crystal_upgrading_progres_bar = float(152 / consts.CRYSTAL_UPGRADING_TIME)

        if self.uran_upgrading == True:
            self.uran_upgrading_progres_bar += float(152 / consts.URAN_UPGRADING_TIME)
            pygame.draw.rect(dest, 'blue', [1014, 103, self.uran_upgrading_progres_bar, 14])
        else:
            self.uran_upgrading_progres_bar = float(152 / consts.URAN_UPGRADING_TIME)

    def progres_bar_mining(self, dest, timer):
        if timer.mission_active == True:
            if timer.time % consts.IRON_SPEED_MINIG == 0:
                self.iron_mining_progres_bar = float(152 / consts.IRON_SPEED_MINIG)
            else:
                self.iron_mining_progres_bar += float(152 / consts.IRON_SPEED_MINIG)
                pygame.draw.rect(dest, 'green', [216, 53, self.iron_mining_progres_bar, 14])


            if timer.time % consts.CRYSTAL_SPEED_MINIG == 0:
                self.crystal_mining_progres_bar = float(152 / consts.CRYSTAL_SPEED_MINIG)
            else:
                self.crystal_mining_progres_bar += float(152 / consts.CRYSTAL_SPEED_MINIG)
                pygame.draw.rect(dest, 'green', [623, 53, self.crystal_mining_progres_bar, 14])

            if timer.time % consts.URAN_SPEED_MINIG == 0:
                self.uran_mining_progres_bar = float(152 / consts.URAN_SPEED_MINIG)
            else:
                self.uran_mining_progres_bar += float(152 / consts.URAN_SPEED_MINIG)
                pygame.draw.rect(dest, 'green', [1014, 53, self.uran_mining_progres_bar, 14])








storage = Storage()


