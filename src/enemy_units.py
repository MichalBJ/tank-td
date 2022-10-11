import pygame
from config import consts
from src.projectile import Projectile


class Enemy:
    def __init__(self, position, img_path, life, shoot_power, speed_shooting):
        self.position = position
        self.image = pygame.image.load(img_path)
        self.image_path = img_path
        self.next_shoot = 0
        self.live_bar_w = 100
        self.live_bar_h = 12
        self.life = life
        self.live_max = life
        self.shoot_power = shoot_power
        self.speed_shooting = speed_shooting


class EnemyRegiment():
    def __init__(self):
        self.enemies = []
        self.projectiles = []
        self.when_start_m = consts.ENEM_LVL_ONE
        self.when_start_l = consts.ENEL_LVL_ONE
        self.when_start_x = consts.ENEX_LVL_ONE
        self.next_m = 0
        self.next_l = 0
        self.next_x = 0
        self.projectile_remove = False

    def create_enemy(self, timer, enemy_base, enem, enel, enex):
        if self.next_m < len(self.when_start_m):
            if timer / self.when_start_m[self.next_m] == 1:
                self.enemies.append(Enemy(enemy_base.position,
                                          enem.image_path,
                                          enem.life,
                                          enem.shoot_power,
                                          enem.speed_shooting))
                self.next_m += 1


        if self.next_l < len(self.when_start_l):
            if timer / self.when_start_l[self.next_l] == 1:
                self.enemies.append(Enemy(enemy_base.position,
                                          enel.image_path,
                                          enel.life,
                                          enel.shoot_power,
                                          enel.speed_shooting))
                self.next_l += 1


        if self.next_x < len(self.when_start_x):
            if timer / self.when_start_x[self.next_x] == 1:
                self.enemies.append(Enemy(enemy_base.position,
                                          enex.image_path,
                                          enex.life,
                                          enex.shoot_power,
                                          enex.speed_shooting))
                self.next_x += 1


    def move_or_shoot(self, soldier, base, timer):
        u_x = base.position[0]
        if len(soldier.player_regiment) > 0:
            u_x = soldier.player_regiment[0].pos[0]
        for enemy in self.enemies:
            e_x, y = enemy.position
            if e_x > u_x + 500 and e_x > base.position[0] + 500:
                e_x -= 20
                enemy.position = (e_x, y)
                enemy.next_shoot = timer + 10
            else:
                if timer / enemy.next_shoot == 1:
                    self.projectiles.append(Projectile((enemy.position[0] - 20, enemy.position[1] + 30),
                                                           consts.PROJECTILE_IMG_R, enemy.shoot_power))
                    enemy.next_shoot = timer + enemy.speed_shooting


    def enemie_projectile_live(self, soldiers, base):
        for projectile in self.projectiles[:]:
            p_x, y = projectile.position
            for soldier in soldiers.player_regiment[:]:
                s_x = soldier.pos[0]
                if p_x <= s_x + 190:
                    soldier.live -= projectile.power
                    soldier.live_bar_w -= float((projectile.power/soldier.live_max)*100)
                    if soldier.live <= 0:
                        soldiers.player_regiment.remove(soldier)
                    self.projectiles.remove(projectile)
                    self.projectile_remove = True
                    break
            if self.projectile_remove == True:
                self.projectile_remove = False
                continue

            if len(soldiers.player_regiment) < 1 and p_x in range(base.position[0] - 5, base.position[0] + 140):
                base.live -= projectile.power
                base.bar_w_g -= float(((projectile.power/base.live_max)*100) * (base.bar_w / 100))
                self.projectiles.remove(projectile)
            p_x -= 18
            projectile.position = (p_x, y)

        return base.live, base.bar_w_g, soldiers

    def projectile_draw(self, dest):
        if len(self.projectiles) > 0:
            for projectile in self.projectiles:
                dest.blit(projectile.image, projectile.position)


    def draw_enemies(self, dest):
        for enemy in self.enemies:
            dest.blit(enemy.image, enemy.position)
            pygame.draw.rect(dest, 'green',
                             [enemy.position[0], enemy.position[1] - 20, enemy.live_bar_w, enemy.live_bar_h])
        for projectile in self.projectiles:
            dest.blit(projectile.image, projectile.position)


enemy_regiment = EnemyRegiment()

enem = Enemy(consts.ENEM_POSITION,
             consts.ENEM_IMAGE_PATH,
             consts.ENEM_LIVE,
             consts.ENEM_SHOOT_POWER,
             consts.ENEM_SPEED_SHOOTING)

enel = Enemy(consts.ENEL_POSITION,
             consts.ENEL_IMAGE_PATH,
             consts.ENEL_LIVE,
             consts.ENEL_SHOOT_POWER,
             consts.ENEL_SPEED_SHOOTING)

enex = Enemy(consts.ENEX_POSITION,
             consts.ENEX_IMAGE_PATH,
             consts.ENEX_LIVE,
             consts.ENEX_SHOOT_POWER,
             consts.ENEX_SPEED_SHOOTING)