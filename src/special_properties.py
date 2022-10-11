import pygame
from config import consts

class SpecialProperties():
    def __init__(self):
        self.loading_time = 300
        self.actual_loading_time = 300
        self.can_use_properties = False
        self.use_properties_healing = False
        self.use_properties_speed = False
        self.use_properties_damage = False
        self.loading_bar = float(88 / 300)
        self.healing_number = 300
        self.time = 0
        self.bonus_speed = 10
        self.speed_active = False
        self.bonus_damage = 200
        self.damage_active = False

    def loading_properties(self, time):
        if time.time == self.actual_loading_time :
            self.can_use_properties = True
        elif self.can_use_properties == False:
            self.loading_bar += float(88 / 300)

    def loading_bar_render(self, dest):
        pygame.draw.rect(dest, 'yellow', [892, 905, self.loading_bar, 18])
        pygame.draw.rect(dest, 'yellow', [1020, 905, self.loading_bar, 18])
        pygame.draw.rect(dest, 'yellow', [1147, 905, self.loading_bar, 18])

    def healing_base(self, base, timer):
        if self.can_use_properties == True and self.use_properties_healing == True and base.live < base.live_max:
            if base.live + self.healing_number > base.live_max:
                base.live = base.live_max
                base.bar_w_g = consts.PLAYER_BASE_BAR_W

            else:
                base.live += self.healing_number
                base.bar_w_g += float((base.bar_w / base.live_max) * self.healing_number)
            self.can_use_properties = False
            self.use_properties_healing = False
            self.loading_bar = float(88 / 300)
            self.actual_loading_time = timer.time + self.loading_time
        else:
            self.use_properties_healing = False

    def speed_plus(self, timer, player_unit):
        if self.can_use_properties == True and self.use_properties_speed == True:
            self.time = timer.time + 60
            self.can_use_properties = False
            self.use_properties_speed = False
            self.speed_active = True
            self.loading_bar = float(88 / 300)
            self.actual_loading_time = timer.time + self.loading_time
            for unit in player_unit:
                unit.speed_move += self.bonus_speed
        else:
            self.use_properties_speed = False

        if self.speed_active == True:
            if timer.time == self.time:
                for unit in player_unit:
                    unit.speed_move -= self.bonus_speed
                self.speed_active = False

    def damage_plus(self, timer, player_unit):
        if self.can_use_properties == True and self.use_properties_damage == True:
            self.time = timer.time + 60
            self.can_use_properties = False
            self.use_properties_damage = False
            self.damage_active = True
            self.loading_bar = float(88 / 300)
            self.actual_loading_time = timer.time + self.loading_time
            for unit in player_unit:
                unit.shoot_power += self.bonus_damage
        else:
            self.use_properties_damage = False

        if self.damage_active == True:
            if timer.time == self.time:
                for unit in player_unit:
                    unit.shoot_power -= self.bonus_damage
                self.damage_active = False





special_properties = SpecialProperties()