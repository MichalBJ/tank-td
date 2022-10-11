import pygame
from config import consts
from src.others_elements import game_end


class Buttons():
    def __init__(self, pos, img):
        self.position = pos
        self.image = pygame.image.load(img)
        self.tranform_image = self.image
        self.tranform_image_pos = self.position
        self.action = True


    def draw(self, mouse_position, dest):
        if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()):
            self.tranform_image = pygame.transform.scale(self.image, (int(self.image.get_width() * 1.05), int(self.image.get_height() * 1.05)))
            x, y = self.position[0], self.position[1]
            x -= (int(self.image.get_width() * 1.05) - self.image.get_width()) / 2
            y -= (int(self.image.get_height() * 1.05) - self.image.get_height()) / 2
            self.tranform_image_pos = (x, y)
            dest.blit(self.tranform_image, self.tranform_image_pos)

        else:
            self.tranform_image = self.image
            self.tranform_image_pos = self.position
            dest.blit(self.tranform_image, self.tranform_image_pos)

    def select(self, mouse_position):
        if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()):
            self.tranform_image = pygame.transform.scale(self.image, (int(self.image.get_width() * 1.05), int(self.image.get_height() * 1.05)))
            x, y = self.position[0], self.position[1]
            x -= (int(self.image.get_width() * 1.05) - self.image.get_width()) / 2
            y -= (int(self.image.get_height() * 1.05) - self.image.get_height()) / 2
            self.tranform_image_pos = (x, y)
        else:
            self.tranform_image = self.image
            self.tranform_image_pos = self.position


    def select_section(self, mouse_position, click, close, open):
        if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()) and click:
            close.active = False
            open.active = True
            return close.active, open.active

    def iron_up(self, mouse_position, click, target):
        if target.iron_upgrading == False:
            if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                    and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()) and click:
                target.iron_can_upgrade = True
                return target.iron_can_upgrade

    def crystal_up(self, mouse_position, click, target):
        if target.crystal_upgrading == False:
            if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                    and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()) and click:
                target.crystal_can_upgrade = True
                return target.crystal_can_upgrade

    def uran_up(self, mouse_position, click, target):
        if target.uran_upgrading == False:
            if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                    and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()) and click:
                target.uran_can_upgrade = True
                return target.uran_can_upgrade

    def zeus_training(self, mouse_position, click, target):
        if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()) and click:
            target.zeus_can_training = True
            return target.zeus_can_training

    def thor_training(self, mouse_position, click, target):
        if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()) and click:
            target.thor_can_training = True
            return target.thor_can_training

    def odin_training(self, mouse_position, click, target):
        if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()) and click:
            target.odin_can_training = True
            return target.odin_can_training

    def choose_again(self, mouse_position, click, target):
        if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()) and click:
            target.again = True
            return target.again

    def choose_main_menu(self, mouse_position, click, target):
        if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()) and click:
            target.main_menu = True
            return target.main_menu

    def use_properties_healing(self, mouse_position, click, target):
        if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()) and click:
            if target.can_use_properties == True:
                target.use_properties_healing = True
            return target.use_properties_healing

    def use_properties_speed(self, mouse_position, click, target):
        if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()) and click:
            if target.can_use_properties == True:
                target.use_properties_speed = True
            return target.use_properties_speed

    def use_properties_damage(self, mouse_position, click, target):
        if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()) and click:
            if target.can_use_properties == True:
                target.use_properties_damage = True
            return target.use_properties_damage

    def next_page(self, mouse_position, click, target):
        if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()) and click:
            if target.page <= 10:
                target.page +=1

    def back_page(self, mouse_position, click, target):
        if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()) and click:
            if target.page >= 0:
                target.page -=1


class ButtonsUnitUpgrade(Buttons):
    def __init__(self,  pos, img):
        super().__init__( pos, img)

    def main_menu(self, mouse_position, click, close, open, cash, zeus, thor, odin, con):
        if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()) and click:
            close.active = False
            open.active = True
            cash.cash = 0
            zeus.live = con.ZEUS_LIVE
            zeus.shoot_power = con.ZEUS_SHOOT_POWER
            zeus.shooting_distance = con.ZEUS_SHOOTING_DISTANCE
            thor.live = con.THOR_LIVE
            thor.shoot_power = con.THOR_SHOOT_POWER
            thor.shooting_distance = con.THOR_SHOOTING_DISTANCE
            odin.live = con.ODIN_LIVE
            odin.shoot_power = con.ODIN_SHOOT_POWER
            odin.shooting_distance = con.ODIN_SHOOTING_DISTANCE


            return close.active, open.active

    def next_mission(self, mouse_position, click, mission, e_regiment, enem, enel, enex, e_base, closing, opening):
        if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()) and click:
            mission.number_level += 1
            enem.life += 50
            enem.shoot_power += 30
            enel.life += 50
            enel.shoot_power += 30
            enex.life += 50
            enex.shoot_power += 30
            e_base.live_max += 500
            e_base.live = e_base.live_max
            if mission.number_level == 2:
                e_regiment.when_start_m = [50, 150, 300, 600]
                e_regiment.when_start_l = []
                e_regiment.when_start_x = []
            elif mission.number_level == 3:
                e_regiment.when_start_m = []
                e_regiment.when_start_l = [50, 150, 300, 600]
                e_regiment.when_start_x = []
            elif mission.number_level == 4:
                e_regiment.when_start_m = []
                e_regiment.when_start_l = []
                e_regiment.when_start_x = [50, 150, 300, 600]
            closing.active = False
            opening.active = True

            return e_base.live


    def upgrade_life(self, mouse_position, click, cash, who):
        if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()) and click:
            if cash.cash - 300 >= 0:
                who.live += who.upgrade_life
                cash.cash -= 300

    def upgrade_damage(self, mouse_position, click, cash, who):
        if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()) and click:
            if cash.cash - 300 >= 0:
                who.shoot_power += who.upgrade_damage
                cash.cash -= 300

    def upgrade_distance(self, mouse_position, click, cash, who):
        if mouse_position[0] in range(self.position[0], self.position[0] + self.image.get_width()) \
                and mouse_position[1] in range(self.position[1], self.position[1] + self.image.get_height()) and click:
            if cash.cash - 300 >= 0:
                who.shooting_distance += who.upgrade_distance
                cash.cash -= 300



# game section
new_game_button = Buttons(consts.B_NEW_GAME_POS, consts.B_NEW_GAME_IMG)
load_button = Buttons(consts.B_LOAD_POS, consts.B_LOAD_IMG)
tutorial_button = Buttons(consts.B_TUTORIAL_POS, consts.B_TUTORIAL_IMG)
credit_button = Buttons(consts.B_CREDIT_POS, consts.B_CREDIT_IMG)

#resources
iron_upgrade = Buttons(consts.B_IRON_UPGRADE_POS, consts.B_IRON_UPGRADE_IMG)
crystal_upgrade = Buttons(consts.B_CRYSTAL_UPGRADE_POS, consts.B_CRYSTAL_UPGRADE_IMG)
uran_upgrade = Buttons(consts.B_URAN_UPGRADE_POS, consts.B_URAN_UPGRADE_IMG)

#soldiers
create_thor = Buttons(consts.CREAT_THOR_POS, consts.CREAT_THOR_IMG)
create_zeus = Buttons(consts.CREAT_ZEUS_POS, consts.CREAT_ZEUS_IMG)
create_odin = Buttons(consts.CREAT_ODIN_POS, consts.CREAT_ODIN_IMG)

#special action
recovery = Buttons(consts.RECOVERY_POS, consts.RECOVERY_IMG)
speed = Buttons(consts.SPEED_POS, consts.SPEED_IMG)
strong_missile = Buttons(consts.STRONG_MISSILE_POS, consts.STRONG_MISSILE_IMG)

#between game
b_again = Buttons((int(game_end.end_image_posx - ((pygame.image.load(consts.B_AGAIN_IMG).get_width()) / 2) + 65), int(game_end.end_image_posy + 120)), consts.B_AGAIN_IMG)
b_main_menu = Buttons((int(game_end.end_image_posx + pygame.image.load('img/others/game_over.png').get_width()
                           - ((pygame.image.load(consts.B_AGAIN_IMG).get_width()) / 2) - 55), int(game_end.end_image_posy + 120)),
                            consts.B_MAIN_MENU_IMG)

#Buttons for upgrade units properties
b_zeus_upgrade_life = ButtonsUnitUpgrade(consts.ZEUS_UPGRADE_LIFE_POS, consts.UNIVERSAL_IMG)
b_zeus_upgrade_damage = ButtonsUnitUpgrade(consts.ZEUS_UPGRADE_DAMAGE_POS, consts.UNIVERSAL_IMG)
b_zeus_upgrade_distance = ButtonsUnitUpgrade(consts.ZEUS_UPGRADE_DISTANCE_POS, consts.UNIVERSAL_IMG)
b_thor_upgrade_life = ButtonsUnitUpgrade(consts.THOR_UPGRADE_LIFE_POS, consts.UNIVERSAL_IMG)
b_thor_upgrade_damage = ButtonsUnitUpgrade(consts.THOR_UPGRADE_DAMAGE_POS, consts.UNIVERSAL_IMG)
b_thor_upgrade_distance = ButtonsUnitUpgrade(consts.THOR_UPGRADE_DISTANCE_POS, consts.UNIVERSAL_IMG)
b_odin_upgrade_life = ButtonsUnitUpgrade(consts.ODIN_UPGRADE_LIFE_POS, consts.UNIVERSAL_IMG)
b_odin_upgrade_damage = ButtonsUnitUpgrade(consts.ODIN_UPGRADE_DAMAGE_POS, consts.UNIVERSAL_IMG)
b_odin_upgrade_distance = ButtonsUnitUpgrade(consts.ODIN_UPGRADE_DISTANCE_POS, consts.UNIVERSAL_IMG)
b_base_upgrade_life = ButtonsUnitUpgrade(consts.BASE_UPGRADE_LIFE_POS, consts.UNIVERSAL_IMG)
b_sp_prop_healing = ButtonsUnitUpgrade(consts.SPEC_PROP_HEALING_POS, consts.UNIVERSAL_IMG)
b_sp_prop_plus_damage = ButtonsUnitUpgrade(consts.SPEC_PROP_PLUS_DAMAGE_POS, consts.UNIVERSAL_IMG)
b_main_menu_up_sec = ButtonsUnitUpgrade(consts.MAIN_MENU_UP_SC_POS, consts.B_MAIN_MENU_IMG)
b_save_game = ButtonsUnitUpgrade(consts.SAVE_GAME_POS, consts.SAVE_GAME_IMG)
b_next_mision = ButtonsUnitUpgrade(consts.NEXT_MISSION_POS, consts.NEXT_MISSION_IMG)

#tutorial button
page_plus = Buttons(consts.PAGE_PLUS_POS, consts.PAGE_PLUS_IMG)
page_minus = Buttons(consts.PAGE_MINUS_POS, consts.PAGE_MINUS_IMG)
b_back_main_menu = Buttons(consts.BACK_MAIN_MENU_POS, consts.BACK_MAIN_MENU_IMG)


