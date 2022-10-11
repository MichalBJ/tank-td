import pygame
from config import consts

class InfoPanels():
    def __init__(self, position, img):
        self.position = position
        self.image = pygame.image.load(img)

    def draw(self, dest):
        dest.blit(self.image, self.position)

class Timer():

    def __init__(self):
        self.time = 1
        self.mission_active = True

    def timer_count(self):
        if self.mission_active == True:
            self.time += 1

class MoveWorld():

    def move_world(self, keys, bg, enemy_base, player_base, soldiers, enemies, p_projectiles, e_projectiles):
        if keys[pygame.K_LEFT]:
            if player_base.position[0] < 10:
                p_x, p_y = bg.position
                p_x += consts.WORLD_MOVE
                bg.position = (p_x, p_y)
                p_x, p_y = player_base.position
                p_x += consts.WORLD_MOVE
                player_base.position = (p_x, p_y)
                e_x, e_y = enemy_base.position
                e_x += consts.WORLD_MOVE
                enemy_base.position = (e_x, e_y)
                for soldier in soldiers:
                    x, y = soldier.pos
                    x += consts.WORLD_MOVE
                    soldier.pos = (x, y)
                for enemy in enemies:
                    x, y = enemy.position
                    x += consts.WORLD_MOVE
                    enemy.position = (x, y)
                for projectile in p_projectiles:
                    x, y = projectile.position
                    x += consts.WORLD_MOVE
                    projectile.position = (x, y)
                for projectile in e_projectiles:
                    x, y = projectile.position
                    x += consts.WORLD_MOVE
                    projectile.position = (x, y)

                return player_base, enemy_base, soldiers, enemies, p_projectiles, e_projectiles

        if keys[pygame.K_RIGHT]:
            if enemy_base.position[0] > 1120:
                p_x, p_y = bg.position
                p_x -= consts.WORLD_MOVE
                bg.position = (p_x, p_y)
                p_x, p_y = player_base.position
                p_x -= consts.WORLD_MOVE
                player_base.position = (p_x, p_y)
                e_x, e_y = enemy_base.position
                e_x -= consts.WORLD_MOVE
                enemy_base.position = (e_x, e_y)
                for soldier in soldiers:
                    x, y = soldier.pos
                    x -= consts.WORLD_MOVE
                    soldier.pos = (x, y)
                for enemy in enemies:
                    x, y = enemy.position
                    x -= consts.WORLD_MOVE
                    enemy.position = (x, y)
                for projectile in p_projectiles:
                    x, y = projectile.position
                    x -= consts.WORLD_MOVE
                    projectile.position = (x, y)
                for projectile in e_projectiles:
                    x, y = projectile.position
                    x -= consts.WORLD_MOVE
                    projectile.position = (x, y)

                return player_base, enemy_base, soldiers, enemies, p_projectiles, e_projectiles

class StartLevel():
    def __init__(self):
        self.r = 159
        self.g = 93
        self.b = 17
        self.text = 'LEVEL'
        self.text_size = 30
        self.number_level = 1

    def animation(self, time, dest):
        if time < 30:
            self.text_size += 4
            self.r += 1
            self.g += 1
            self.b += 1
        if time < 45:
            text_font = pygame.font.SysFont('chiller', self.text_size, bold=True)
            text2 = text_font.render(f'{self.text} {self.number_level}', True, (20, 20, 20))
            text = text_font.render(f'{self.text} {self.number_level}', True, (self.r, self.g, self.b))
            dest.blit(text2, (
                (consts.GAME_RES[0] / 2 - (text.get_width() / 2) + 3), (consts.GAME_RES[0] / 2 - (text.get_height() / 2) - 147)))
            dest.blit(text, (consts.GAME_RES[0] / 2 - (text.get_width() / 2), (consts.GAME_RES[0] / 2 - (text.get_height() / 2) - 150)))

class Cash():
    def __init__(self):
        self.cash = 0

    def cash_in_pocket(self, font, dest):
        cash_text = font.render(f'$ {self.cash}', True, consts.CASH_FONT_COLOR)
        dest.blit(cash_text, (1057 - cash_text.get_width(), 183))

class GameEnd():
    def __init__(self):
        self.mision_complete_img = pygame.image.load('img/others/mission_complete.png')
        self.end_image = pygame.image.load('img/others/game_over.png')
        self.end_image_posx = (pygame.image.load(consts.GAME_IMG).get_width() / 2) - (self.end_image.get_width() / 2)
        self.end_image_posy = (pygame.image.load(consts.GAME_IMG).get_height() / 2) - (self.end_image.get_height() / 2) - 100
        self.again = False
        self.main_menu = False
        self.freeze = True
        self.tik = 0


    def positive_end(self, close, open, text, timer, resources, player_units, enemy_units, base, dest, enemy_base, cash, background, properties):
        if enemy_base.live <= 0:
            if self.freeze == True:
                timer.mission_active = False
                resources.iron_stock = 0
                resources.crystal_stock = 0
                resources.uran_stock = 0
                resources.iron_can_upgrade = False
                resources.crystal_can_upgrade = False
                resources.uran_can_upgrade = False
                resources.iron_upgrading = False
                resources.crystal_upgrading = False
                resources.uran_upgrading = False
                resources.iron_count_mining = 1
                resources.crystal_count_mining = 1
                resources.uran_count_mining = 1
                resources.iron_final_time = 1
                resources.crystal_final_time = 1
                resources.uran_final_time = 1
                resources.iron_mining_progres_bar = float(152 / consts.IRON_SPEED_MINIG)
                resources.crystal_mining_progres_bar = float(152 / consts.CRYSTAL_SPEED_MINIG)
                resources.uran_mining_progres_bar = float(152 / consts.URAN_SPEED_MINIG)
                resources.iron_upgrading_progres_bar = float(152 / consts.IRON_UPGRADING_TIME)
                resources.crystal_upgrading_progres_bar = float(152 / consts.CRYSTAL_UPGRADING_TIME)
                resources.uran_upgrading_progres_bar = float(152 / consts.URAN_UPGRADING_TIME)
                player_units.zeus_can_training = False
                player_units.thor_can_training = False
                player_units.odin_can_training = False
                player_units.zeus_training_bar = float(88 / consts.ZEUS_TRAINING_TIME)
                player_units.thor_training_bar = float(88 / consts.THOR_TRAINING_TIME)
                player_units.odin_training_bar = float(88 / consts.THOR_TRAINING_TIME)
                player_units.player_regiment = []
                player_units.projectiles = []
                enemy_units.projectiles = []
                enemy_units.enemies = []
                enemy_units.next_m = 0
                enemy_units.next_l = 0
                enemy_units.next_x = 0
                base.bar_w_g = consts.PLAYER_BASE_BAR_W
                base.position = consts.PLAYER_BASE_POS
                properties.loading_time = 300
                properties.actual_loading_time = 300

                properties.use_properties_healing = False
                properties.use_properties_speed = False
                properties.use_properties_damage = False
                properties.speed_active = False
                properties.damage_active = False
            if self.tik == 50:
                properties.loading_bar = float(88 / 300)
                player_units.zeus_training_counter = 0
                player_units.thor_training_counter = 0
                player_units.odin_training_counter = 0
                player_units.zeus_final_time = []
                player_units.thor_final_time = []
                player_units.odin_final_time = []
                start_level.r = 159
                start_level.g = 93
                start_level.b = 17
                start_level.text_size = 30
                cash.cash += 500
                background.position = consts.GAME_BG_POS
                base.live = base.live_max
                enemy_base.bar_w_g = consts.ENEMY_BASE_BAR_W
                enemy_base.position = consts.ENEMY_BASE_POS
                enemy_base.live = consts.ENEMY_BASE_LIVE_MAX
                timer.mission_active = True
                timer.time = 1
                self.tik = 0
                self.freeze = True
                close.active = False
                open.active = True
                print(enemy_base.live_max)
            else:
                self.tik += 1
                dest.blit(self.mision_complete_img, (self.end_image_posx, self.end_image_posy))






    def negative_end(self, close, open, base, timer, resources, player_units, enemy_units, text, dest,
                     main_menu, again, start_level, enemy_base, cash, background, enem, enel, enex, zeus, thor, odin, properties):
        if base.live <= 0:
            if self.freeze == True:
                timer.mission_active = False
                resources.iron_stock = 0
                resources.crystal_stock = 0
                resources.uran_stock = 0
                resources.iron_can_upgrade = False
                resources.crystal_can_upgrade = False
                resources.uran_can_upgrade = False
                resources.iron_upgrading = False
                resources.crystal_upgrading = False
                resources.uran_upgrading = False
                resources.iron_count_mining = 1
                resources.crystal_count_mining = 1
                resources.uran_count_mining = 1
                resources.iron_final_time = 1
                resources.crystal_final_time = 1
                resources.uran_final_time = 1
                resources.iron_mining_progres_bar = float(152 / consts.IRON_SPEED_MINIG)
                resources.crystal_mining_progres_bar = float(152 / consts.CRYSTAL_SPEED_MINIG)
                resources.uran_mining_progres_bar = float(152 / consts.URAN_SPEED_MINIG)
                resources.iron_upgrading_progres_bar = float(152 / consts.IRON_UPGRADING_TIME)
                resources.crystal_upgrading_progres_bar = float(152 / consts.CRYSTAL_UPGRADING_TIME)
                resources.uran_upgrading_progres_bar = float(152 / consts.URAN_UPGRADING_TIME)
                player_units.zeus_can_training = False
                player_units.thor_can_training = False
                player_units.odin_can_training = False
                player_units.zeus_training_counter = 0
                player_units.thor_training_counter = 0
                player_units.odin_training_counter = 0
                player_units.zeus_final_time = []
                player_units.thor_final_time = []
                player_units.odin_final_time = []
                player_units.player_regiment = []
                player_units.projectiles = []
                enemy_units.projectiles = []
                enemy_units.enemies = []
                enemy_units.next_m = 0
                enemy_units.next_l = 0
                enemy_units.next_x = 0
                text.text_size = 30
                start_level.r = 159
                start_level.g = 93
                start_level.b = 17
                enemy_base.bar_w_g = consts.ENEMY_BASE_BAR_W
                enemy_base.position = consts.ENEMY_BASE_POS
                cash.cash = 0
                self.freeze = False


            if self.main_menu == True:
                player_units.zeus_training_bar = float(88 / consts.ZEUS_TRAINING_TIME)
                player_units.thor_training_bar = float(88 / consts.THOR_TRAINING_TIME)
                player_units.odin_training_bar = float(88 / consts.THOR_TRAINING_TIME)
                zeus.live = consts.ZEUS_LIVE
                zeus.shoot_power = consts.ZEUS_SHOOT_POWER
                zeus.shooting_distance = consts.ZEUS_SHOOTING_DISTANCE
                thor.live = consts.THOR_LIVE
                thor.shoot_power = consts.THOR_SHOOT_POWER
                thor.shooting_distance = consts.THOR_SHOOTING_DISTANCE
                odin.live = consts.ODIN_LIVE
                odin.shoot_power = consts.ODIN_SHOOT_POWER
                odin.shooting_distance = consts.ODIN_SHOOTING_DISTANCE
                enem.life = consts.ENEM_LIVE
                enem.shoot_power = consts.ENEM_SHOOT_POWER
                enel.life = consts.ENEL_LIVE
                enel.shoot_power = consts.ENEL_SHOOT_POWER
                enex.life = consts.ENEX_LIVE
                enex.shoot_power = consts.ENEX_SHOOT_POWER
                enemy_units.when_start_m = consts.ENEM_LVL_ONE
                enemy_units.when_start_l = consts.ENEL_LVL_ONE
                enemy_units.when_start_x = consts.ENEX_LVL_ONE
                enemy_base.live = consts.ENEMY_BASE_LIVE
                start_level.number_level = 1
                timer.time = 1
                timer.mission_active = True
                self.main_menu = False
                base.live = consts.PLAYER_BASE_LIVE
                base.bar_w_g = consts.PLAYER_BASE_BAR_W
                base.position = consts.PLAYER_BASE_POS
                background.position = consts.GAME_BG_POS
                self.freeze = True
                close.active = False
                open.active = True
                properties.loading_time = 300
                properties.actual_loading_time = 300
                properties.loading_bar = float(88 / 300)
                properties.use_properties_healing = False
                properties.use_properties_speed = False
                properties.use_properties_damage = False
                properties.speed_active = False
                properties.damage_active = False

            elif self.again == True:
                player_units.zeus_training_bar = float(88 / consts.ZEUS_TRAINING_TIME)
                player_units.thor_training_bar = float(88 / consts.THOR_TRAINING_TIME)
                player_units.odin_training_bar = float(88 / consts.THOR_TRAINING_TIME)
                enemy_units.enemies = []
                self.again = False
                self.freeze = True
                timer.time = 1
                timer.mission_active = True
                base.live = base.live_max
                base.bar_w_g = consts.PLAYER_BASE_BAR_W
                base.position = consts.PLAYER_BASE_POS
                enemy_base.live = enemy_base.live_max
                background.position = consts.GAME_BG_POS
                properties.loading_time = 300
                properties.actual_loading_time = 300
                properties.loading_bar = float(88 / 300)
                properties.use_properties_healing = False
                properties.use_properties_speed = False
                properties.use_properties_damage = False
                properties.speed_active = False
                properties.damage_active = False

            print('time ', timer.time)

            dest.blit(self.end_image, (self.end_image_posx, self.end_image_posy))
            dest.blit(main_menu.tranform_image, main_menu.tranform_image_pos)
            dest.blit(again.tranform_image, again.tranform_image_pos)
            return base.live, base.bar_w_g, timer.time

pygame.init()

iron_panel = InfoPanels(consts.IRON_PANEL_POS, consts.IRON_PANEL_IMG)
crystal_panel = InfoPanels(consts.CRYSTAL_PANEL_POS, consts.CRYSTAL_PANEL_IMG)
uran_panel = InfoPanels(consts.URAN_PANEL_POS, consts.URAN_PANEL_IMG)
info_panel = InfoPanels(consts.INFO_PANEL_POS, consts.INFO_PANEL_IMG)

timer = Timer()
move_world = MoveWorld()
start_level = StartLevel()

cash = Cash()

game_end = GameEnd()