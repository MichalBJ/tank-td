import pygame
from config import consts
from src.projectile import Projectile


class PlayerUnit():
    def __init__(self, name, pos, img_path, training_time, iron_price, crystal_price, uran_price, speed_move, shoot_power,
                 shooting_speed, live, distance, already_moved, upgrade_life, upgrade_damage, upgrade_distance):
        self.name = name
        self.pos = pos
        self.img = pygame.image.load(img_path)
        self.img_path = img_path
        self.training_time = training_time
        self.iron_price = iron_price
        self.crystal_price = crystal_price
        self.uran_price = uran_price
        self.already_moved = already_moved
        self.live_max = live
        self.live = live
        self.shooting_distance = distance
        self.shoot_power = shoot_power
        self.shooting_speed = shooting_speed
        self.next_shoot = shooting_speed
        self.training_counter = 0
        self.load_line = 1
        self.speed_move = speed_move
        self.live_bar_w = 100
        self.live_bar_h = 12
        self.upgrade_life = upgrade_life
        self.upgrade_damage = upgrade_damage
        self.upgrade_distance = upgrade_distance


class PlayerRegiment():
    def __init__(self):
        self.player_regiment = []
        self.projectiles = []
        self.zeus_can_training = False
        self.thor_can_training = False
        self.odin_can_training = False
        self.zeus_training_counter = 0
        self.thor_training_counter = 0
        self.odin_training_counter = 0
        self.zeus_final_time = []
        self.thor_final_time = []
        self.odin_final_time = []
        self.zeus_training_bar = float(88 / consts.ZEUS_TRAINING_TIME)
        self.thor_training_bar = float(88 / consts.THOR_TRAINING_TIME)
        self.odin_training_bar = float(88 / consts.ODIN_TRAINING_TIME)
        self.projectile_remove = False


    def draw_regiment(self, dest):
        for soldier in self.player_regiment:
            dest.blit(soldier.img, (soldier.pos[0], soldier.pos[1] + 40))
            pygame.draw.rect(dest, 'green',
                             [soldier.pos[0] + 60, soldier.pos[1] + 20, soldier.live_bar_w, soldier.live_bar_h])

    def army_training(self, storage, time, dest, base, zeus, thor, odin):
        if self.zeus_can_training == True:
            if storage.iron_stock >= consts.ZEUS_IRON_PRICE and storage.crystal_stock >= consts.ZEUS_CRYSTAL_PRICE and storage.uran_stock >= consts.ZEUS_URAN_PRICE:
                storage.iron_stock -= consts.ZEUS_IRON_PRICE
                storage.crystal_stock -= consts.ZEUS_CRYSTAL_PRICE
                storage.uran_stock -= consts.ZEUS_URAN_PRICE
                self.zeus_can_training = False
                self.zeus_training_counter += 1
                if len(self.zeus_final_time) == 0:
                    self.zeus_final_time.append(time + consts.ZEUS_TRAINING_TIME)
            else:
                self.zeus_can_training = False

        if self.zeus_training_counter > 0:
            if len(self.zeus_final_time) == 0:
                self.zeus_final_time.append((time + consts.ZEUS_TRAINING_TIME))
            if time / self.zeus_final_time[0] == 1:
                x, y = base.position
                x -= 200
                self.player_regiment.append(PlayerUnit(zeus.name,
                                                       (x, y),
                                                       zeus.img_path,
                                                       zeus.training_time,
                                                       zeus.iron_price,
                                                       zeus.crystal_price,
                                                       zeus.uran_price,
                                                       zeus.speed_move,
                                                       zeus.shoot_power,
                                                       zeus.shooting_speed,
                                                       zeus.live,
                                                       zeus.shooting_distance,
                                                       zeus.already_moved,
                                                       zeus.upgrade_life,
                                                       zeus.upgrade_damage,
                                                       zeus.upgrade_distance
                                                       ))
                self.zeus_training_counter -= 1
                self.zeus_final_time.remove(self.zeus_final_time[0])
                self.zeus_training_bar = float(88 / consts.ZEUS_TRAINING_TIME)
            else:
                self.zeus_training_bar += float(88 / consts.ZEUS_TRAINING_TIME)
                pygame.draw.rect(dest, 'green', [49, 905, self.zeus_training_bar, 14])


        if self.thor_can_training == True:
            if storage.iron_stock >= consts.THOR_IRON_PRICE and storage.crystal_stock >= consts.THOR_CRYSTAL_PRICE and storage.uran_stock >= consts.THOR_URAN_PRICE:
                storage.iron_stock -= consts.THOR_IRON_PRICE
                storage.crystal_stock -= consts.THOR_CRYSTAL_PRICE
                storage.uran_stock -= consts.THOR_URAN_PRICE
                self.thor_can_training = False
                self.thor_training_counter += 1
                if len(self.thor_final_time) == 0:
                    self.thor_final_time.append(time + consts.THOR_TRAINING_TIME)

            else:
                self.thor_can_training = False

        if self.thor_training_counter > 0:
            if len(self.thor_final_time) == 0:
                self.thor_final_time.append((time + consts.THOR_TRAINING_TIME))
            if time / self.thor_final_time[0] == 1:
                x, y = base.position
                x -= 200
                self.player_regiment.append(PlayerUnit(thor.name,
                                                       (x, y),
                                                       thor.img_path,
                                                       thor.training_time,
                                                       thor.iron_price,
                                                       thor.crystal_price,
                                                       thor.uran_price,
                                                       thor.speed_move,
                                                       thor.shoot_power,
                                                       thor.shooting_speed,
                                                       thor.live,
                                                       thor.shooting_distance,
                                                       thor.already_moved,
                                                       thor.upgrade_life,
                                                       thor.upgrade_damage,
                                                       thor.upgrade_distance
                                                       ))
                self.thor_training_counter -= 1
                self.thor_final_time.remove(self.thor_final_time[0])
                self.thor_training_bar = float(88 / consts.THOR_TRAINING_TIME)
            else:
                self.thor_training_bar += float(88 / consts.THOR_TRAINING_TIME)
                pygame.draw.rect(dest, 'green', [177, 905, self.thor_training_bar, 14])


        if self.odin_can_training == True:
            if storage.iron_stock >= consts.ODIN_IRON_PRICE and storage.crystal_stock >= consts.ODIN_CRYSTAL_PRICE and storage.uran_stock >= consts.ODIN_URAN_PRICE:
                storage.iron_stock -= consts.ODIN_IRON_PRICE
                storage.crystal_stock -= consts.ODIN_CRYSTAL_PRICE
                storage.uran_stock -= consts.ODIN_URAN_PRICE
                self.odin_can_training = False
                self.odin_training_counter += 1
                if len(self.odin_final_time) == 0:
                    self.odin_final_time.append(time + consts.ODIN_TRAINING_TIME)

            else:
                self.odin_can_training = False

        if self.odin_training_counter > 0:
            if len(self.odin_final_time) == 0:
                self.odin_final_time.append((time + consts.ODIN_TRAINING_TIME))
            if time / self.odin_final_time[0] == 1:
                x, y = base.position
                x -= 200
                self.player_regiment.append(PlayerUnit(odin.name,
                                                       (x, y),
                                                       odin.img_path,
                                                       odin.training_time,
                                                       odin.iron_price,
                                                       odin.crystal_price,
                                                       odin.uran_price,
                                                       odin.speed_move,
                                                       odin.shoot_power,
                                                       odin.shooting_speed,
                                                       odin.live,
                                                       odin.shooting_distance,
                                                       odin.already_moved,
                                                       odin.upgrade_life,
                                                       odin.upgrade_damage,
                                                       odin.upgrade_distance
                                                       ))
                self.odin_training_counter -= 1
                self.odin_final_time.remove(self.odin_final_time[0])
                self.odin_training_bar = float(88 / consts.ODIN_TRAINING_TIME)
            else:
                self.odin_training_bar += float(88 / consts.ODIN_TRAINING_TIME)
                pygame.draw.rect(dest, 'green', [305, 905, self.odin_training_bar, 14])

        return storage.iron_stock, storage.crystal_stock, storage.uran_stock

    def move_or_shoot(self, base, enemy, time):
        e_x = base.position[0]
        if len(enemy.enemies) > 0:
            e_x = enemy.enemies[0].position[0]
        for soldier in self.player_regiment[:]:
            u_x, y = soldier.pos
            if u_x + soldier.shooting_distance < e_x and u_x <= base.position[0] - soldier.shooting_distance:
                u_x += soldier.speed_move
                soldier.pos = (u_x, y)
                soldier.next_shoot = time + 10
                soldier.already_moved = True
            elif soldier.already_moved == False:
                    soldier.next_shoot = time + 10
                    soldier.already_moved = True
            else:
                if time == soldier.next_shoot:
                    if soldier.name == 'zeus':
                        self.projectiles.append(Projectile((soldier.pos[0] + 200, soldier.pos[1] + 50),
                                                             consts.PROJECTILE_IMG_R, soldier.shoot_power))

                    if soldier.name == 'thor':
                        self.projectiles.append(Projectile((soldier.pos[0] + 200, soldier.pos[1] + 50),
                                                               consts.PROJECTILE_IMG_B, soldier.shoot_power))

                    if soldier.name == 'odin':
                        self.projectiles.append(Projectile((soldier.pos[0] + 200, soldier.pos[1] + 50),
                                                               consts.PROJECTILE_IMG_G, soldier.shoot_power))

                    soldier.next_shoot = time + soldier.shooting_speed

    def projectile_live(self, enemies, base):
        for projectile in self.projectiles[:]:
            p_x, y = projectile.position
            for enemy in enemies.enemies[:]:
                e_x = enemy.position[0]
                if p_x >= e_x - 20:
                    enemy.life -= projectile.power
                    enemy.live_bar_w -= float((projectile.power / enemy.live_max) * 100)
                    if enemy.life <= 0:
                        enemies.enemies.remove(enemy)
                    self.projectiles.remove(projectile)
                    self.projectile_remove = True
                    break
            if self.projectile_remove == True:
                self.projectile_remove = False
                continue
            if p_x >= base.position[0] - 20:
                base.live -= projectile.power
                base.bar_w_g -= float(((projectile.power/base.live_max)*100) * (base.bar_w / 100))
                self.projectiles.remove(projectile)

            else:
                p_x += 18
                projectile.position = (p_x, y)
        return base.live, base.bar_w_g, enemies

    def projectile_draw(self, dest):
        if len(self.projectiles) > 0:
            for projectile in self.projectiles:
                dest.blit(projectile.image, projectile.position)

    def army_info(self, mouse_position, dest, info_font, zeus, thor, odin):
        if mouse_position[0] in range(consts.CREAT_ZEUS_POS[0],
                                      consts.CREAT_ZEUS_POS[0] + (pygame.image.load(consts.CREAT_ZEUS_IMG).get_width())) \
                and mouse_position[1] in range(consts.CREAT_ZEUS_POS[1], consts.CREAT_ZEUS_POS[1] + (
        pygame.image.load(consts.CREAT_ZEUS_IMG).get_height())):
            zeus_info_iron = info_font.render(f'{consts.ZEUS_IRON_PRICE}', True, consts.INFO_FONT_COLOR)
            zeus_info_crystal = info_font.render(f'{consts.ZEUS_CRYSTAL_PRICE}', True, consts.INFO_FONT_COLOR)
            zeus_info_uran = info_font.render(f'{consts.ZEUS_URAN_PRICE}', True, consts.INFO_FONT_COLOR)
            zeus_info_live = info_font.render(f'{zeus.live}', True, consts.INFO_FONT_COLOR)
            zeus_info_damage = info_font.render(f'{zeus.shoot_power}', True, consts.INFO_FONT_COLOR)
            zeus_info_speed = info_font.render(f'{zeus.speed_move}', True, consts.INFO_FONT_COLOR)
            dest.blit(zeus_info_iron,
                      (consts.INFO_PANEL_POS[0] + 107 - zeus_info_iron.get_width(), consts.INFO_PANEL_POS[1] + 16))
            dest.blit(zeus_info_crystal,
                      (consts.INFO_PANEL_POS[0] + 107 - zeus_info_crystal.get_width(), consts.INFO_PANEL_POS[1] + 53))
            dest.blit(zeus_info_uran,
                      (consts.INFO_PANEL_POS[0] + 107 - zeus_info_uran.get_width(), consts.INFO_PANEL_POS[1] + 88))
            dest.blit(zeus_info_live,
                      (consts.INFO_PANEL_POS[0] + 288 - zeus_info_live.get_width(), consts.INFO_PANEL_POS[1] + 16))
            dest.blit(zeus_info_damage,
                      (consts.INFO_PANEL_POS[0] + 288 - zeus_info_damage.get_width(), consts.INFO_PANEL_POS[1] + 53))
            dest.blit(zeus_info_speed,
                      (consts.INFO_PANEL_POS[0] + 288 - zeus_info_speed.get_width(), consts.INFO_PANEL_POS[1] + 88))

        if mouse_position[0] in range(consts.CREAT_THOR_POS[0],
                                        consts.CREAT_THOR_POS[0] + (
                                        pygame.image.load(consts.CREAT_THOR_IMG).get_width())) \
                and mouse_position[1] in range(consts.CREAT_THOR_POS[1], consts.CREAT_THOR_POS[1] + (
                pygame.image.load(consts.CREAT_THOR_IMG).get_height())):
            thor_info_iron = info_font.render(f'{consts.THOR_IRON_PRICE}', True, consts.INFO_FONT_COLOR)
            thor_info_crystal = info_font.render(f'{consts.THOR_CRYSTAL_PRICE}', True, consts.INFO_FONT_COLOR)
            thor_info_uran = info_font.render(f'{consts.THOR_URAN_PRICE}', True, consts.INFO_FONT_COLOR)
            thor_info_live = info_font.render(f'{thor.live}', True, consts.INFO_FONT_COLOR)
            thor_info_damage = info_font.render(f'{thor.shoot_power}', True, consts.INFO_FONT_COLOR)
            thor_info_speed = info_font.render(f'{thor.speed_move}', True, consts.INFO_FONT_COLOR)
            dest.blit(thor_info_iron,
                        (consts.INFO_PANEL_POS[0] + 107 - thor_info_iron.get_width(), consts.INFO_PANEL_POS[1] + 16))
            dest.blit(thor_info_crystal,
                        (consts.INFO_PANEL_POS[0] + 107 - thor_info_crystal.get_width(),
                        consts.INFO_PANEL_POS[1] + 53))
            dest.blit(thor_info_uran,
                        (consts.INFO_PANEL_POS[0] + 107 - thor_info_uran.get_width(), consts.INFO_PANEL_POS[1] + 88))
            dest.blit(thor_info_live,
                        (consts.INFO_PANEL_POS[0] + 288 - thor_info_live.get_width(), consts.INFO_PANEL_POS[1] + 16))
            dest.blit(thor_info_damage,
                        (consts.INFO_PANEL_POS[0] + 288 - thor_info_damage.get_width(), consts.INFO_PANEL_POS[1] + 53))
            dest.blit(thor_info_speed,
                        (consts.INFO_PANEL_POS[0] + 288 - thor_info_speed.get_width(), consts.INFO_PANEL_POS[1] + 88))

        if mouse_position[0] in range(consts.CREAT_ODIN_POS[0],
                                        consts.CREAT_ODIN_POS[0] + (
                                        pygame.image.load(consts.CREAT_ODIN_IMG).get_width())) \
                and mouse_position[1] in range(consts.CREAT_ODIN_POS[1], consts.CREAT_ODIN_POS[1] + (
                pygame.image.load(consts.CREAT_ODIN_IMG).get_height())):
            odin_info_iron = info_font.render(f'{consts.ODIN_IRON_PRICE}', True, consts.INFO_FONT_COLOR)
            odin_info_crystal = info_font.render(f'{consts.ODIN_CRYSTAL_PRICE}', True, consts.INFO_FONT_COLOR)
            odin_info_uran = info_font.render(f'{consts.ODIN_URAN_PRICE}', True, consts.INFO_FONT_COLOR)
            odin_info_live = info_font.render(f'{odin.live}', True, consts.INFO_FONT_COLOR)
            odin_info_damage = info_font.render(f'{odin.shoot_power}', True, consts.INFO_FONT_COLOR)
            odin_info_speed = info_font.render(f'{odin.speed_move}', True, consts.INFO_FONT_COLOR)
            dest.blit(odin_info_iron,
                        (consts.INFO_PANEL_POS[0] + 107 - odin_info_iron.get_width(), consts.INFO_PANEL_POS[1] + 16))
            dest.blit(odin_info_crystal,
                        (consts.INFO_PANEL_POS[0] + 107 - odin_info_crystal.get_width(),consts.INFO_PANEL_POS[1] + 53))
            dest.blit(odin_info_uran,
                        (consts.INFO_PANEL_POS[0] + 107 - odin_info_uran.get_width(), consts.INFO_PANEL_POS[1] + 88))
            dest.blit(odin_info_live,
                        (consts.INFO_PANEL_POS[0] + 288 - odin_info_live.get_width(), consts.INFO_PANEL_POS[1] + 16))
            dest.blit(odin_info_damage,
                        (consts.INFO_PANEL_POS[0] + 288 - odin_info_damage.get_width(), consts.INFO_PANEL_POS[1] + 53))
            dest.blit(odin_info_speed,
                        (consts.INFO_PANEL_POS[0] + 288 - odin_info_speed.get_width(), consts.INFO_PANEL_POS[1] + 88))


player_regiment = PlayerRegiment()

zeus = PlayerUnit(consts.ZEUS_NAME,
                    consts.ZEUS_POS,
                    consts.ZEUS_IMG,
                    consts.ZEUS_TRAINING_TIME,
                    consts.ZEUS_IRON_PRICE,
                    consts.ZEUS_CRYSTAL_PRICE,
                    consts.ZEUS_URAN_PRICE,
                    consts.ZEUS_SPEED_MOVE,
                    consts.ZEUS_SHOOT_POWER,
                    consts.ZEUS_SHOOT_SPEED,
                    consts.ZEUS_LIVE,
                    consts.ZEUS_SHOOTING_DISTANCE,
                    consts.ZEUS_ALREADY_MOVED,
                    consts.ZEUS_UPGRADE_LIFE,
                    consts.ZEUS_UPGRADE_DAMAGE,
                    consts.ZEUS_UPGRADE_DISTANCE
                    )

thor = PlayerUnit(consts.THOR_NAME,
                    consts.THOR_POS,
                    consts.THOR_IMG,
                    consts.THOR_TRAINING_TIME,
                    consts.THOR_IRON_PRICE,
                    consts.THOR_CRYSTAL_PRICE,
                    consts.THOR_URAN_PRICE,
                    consts.THOR_SPEED_MOVE,
                    consts.THOR_SHOOT_POWER,
                    consts.THOR_SHOOT_SPEED,
                    consts.THOR_LIVE,
                    consts.THOR_SHOOTING_DISTANCE,
                    consts.THOR_ALREADY_MOVED,
                    consts.THOR_UPGRADE_LIFE,
                    consts.THOR_UPGRADE_DAMAGE,
                    consts.THOR_UPGRADE_DISTANCE
                    )

odin = PlayerUnit(consts.ODIN_NAME,
                    consts.ODIN_POS,
                    consts.ODIN_IMG,
                    consts.ODIN_TRAINING_TIME,
                    consts.ODIN_IRON_PRICE,
                    consts.ODIN_CRYSTAL_PRICE,
                    consts.ODIN_URAN_PRICE,
                    consts.ODIN_SPEED_MOVE,
                    consts.ODIN_SHOOT_POWER,
                    consts.ODIN_SHOOT_SPEED,
                    consts.ODIN_LIVE,
                    consts.ODIN_SHOOTING_DISTANCE,
                    consts.ODIN_ALREADY_MOVED,
                    consts.ODIN_UPGRADE_LIFE,
                    consts.ODIN_UPGRADE_DAMAGE,
                    consts.ODIN_UPGRADE_DISTANCE
                    )
