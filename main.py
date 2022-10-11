from src.game_section import *
from src.buttons import *
from src.others_elements import *
from src.resources import *
from src.base import *
from src.player_units import *
from src.enemy_units import *
from src.special_properties import *
from src.tutorial import *
import pygame
import sys
from config import consts


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode(consts.GAME_RES)

    resource_font = pygame.font.SysFont(consts.RES_FONT_TYPE, consts.RES_FONT_SIZE, bold=True)
    info_font = pygame.font.SysFont(consts.INFO_FONT_TYPE, consts.INFO_FONT_SIZE)
    cash_font = pygame.font.SysFont(consts.CASH_FONT_TYPE, consts.CASH_FONT_SIZE)


    while True:
        mouse_click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = pygame.mouse.get_pressed(num_buttons=3)[0]

        # Section Main menu
        if main_menu.active:
            #render
            main_menu.draw(window)
            new_game_button.draw(pygame.mouse.get_pos(), window)
            load_button.draw(pygame.mouse.get_pos(), window)
            tutorial_button.draw(pygame.mouse.get_pos(), window)
            credit_button.draw(pygame.mouse.get_pos(), window)

            #actions
            new_game_button.select_section(pygame.mouse.get_pos(), mouse_click, main_menu, game)
            tutorial_button.select_section(pygame.mouse.get_pos(), mouse_click, main_menu, tutorial)
            credit_button.select_section(pygame.mouse.get_pos(), mouse_click, main_menu, credit)

            tutorial.reset_tutorial_page()


        # Game
        if game.active:
            # rendering
            game_bg.draw(window)
            game.draw(window)
            storage.progres_bar_upgrade(window)
            storage.progres_bar_mining(window, timer)
            iron_panel.draw(window)
            crystal_panel.draw(window)
            uran_panel.draw(window)
            info_panel.draw(window)

            # Game over
            game_end.positive_end(game, between_level_upgrade, start_level, timer, storage, player_regiment,
                                  enemy_regiment, player_base, window, enemy_base, cash, game_bg,special_properties)

            game_end.negative_end(game, main_menu, player_base, timer, storage, player_regiment,
                                  enemy_regiment, start_level, window, b_main_menu, b_again, start_level, enemy_base,
                                  cash, game_bg, enem, enel, enex, zeus, thor, odin, special_properties)

            # player's soldiers
            player_regiment.army_training(storage, timer.time, window, player_base, zeus, thor, odin)
            player_regiment.move_or_shoot(enemy_base, enemy_regiment, timer.time)
            player_regiment.projectile_live(enemy_regiment, enemy_base)
            player_regiment.projectile_draw(window)

            special_properties.loading_bar_render(window)
            create_thor.draw(pygame.mouse.get_pos(), window)
            create_zeus.draw(pygame.mouse.get_pos(), window)
            create_odin.draw(pygame.mouse.get_pos(), window)
            recovery.draw(pygame.mouse.get_pos(), window)
            speed.draw(pygame.mouse.get_pos(), window)
            strong_missile.draw(pygame.mouse.get_pos(), window)
            iron_upgrade.draw(pygame.mouse.get_pos(), window)
            crystal_upgrade.draw(pygame.mouse.get_pos(), window)
            uran_upgrade.draw(pygame.mouse.get_pos(), window)
            player_base.render_base_and_live_bar(window)
            enemy_base.render_base_and_live_bar(window)
            player_regiment.draw_regiment(window)


            # enemies soldiers
            enemy_regiment.create_enemy(timer.time, enemy_base, enem, enel, enex)
            enemy_regiment.move_or_shoot(player_regiment, player_base, timer.time)
            enemy_regiment.enemie_projectile_live(player_regiment, player_base)
            enemy_regiment.draw_enemies(window)
            enemy_regiment.projectile_draw(window)

            # Buttons
            iron_upgrade.iron_up(pygame.mouse.get_pos(), mouse_click, storage)
            crystal_upgrade.crystal_up(pygame.mouse.get_pos(), mouse_click, storage)
            uran_upgrade.uran_up(pygame.mouse.get_pos(), mouse_click, storage)
            create_zeus.zeus_training(pygame.mouse.get_pos(), mouse_click, player_regiment)
            create_thor.thor_training(pygame.mouse.get_pos(), mouse_click, player_regiment)
            create_odin.odin_training(pygame.mouse.get_pos(), mouse_click, player_regiment)
            recovery.use_properties_healing(pygame.mouse.get_pos(), mouse_click, special_properties)
            speed.use_properties_speed(pygame.mouse.get_pos(), mouse_click, special_properties)
            strong_missile.use_properties_damage(pygame.mouse.get_pos(), mouse_click, special_properties)
            if player_base.live <= 0:
                b_again.select(pygame.mouse.get_pos())
                b_again.choose_again(pygame.mouse.get_pos(), mouse_click, game_end)
                b_main_menu.select(pygame.mouse.get_pos())
                b_main_menu.choose_main_menu(pygame.mouse.get_pos(), mouse_click, game_end)


            # text
            storage.render_resources(resource_font, window)
            storage.show_prize_upgrade(pygame.mouse.get_pos(), window, info_font)
            player_regiment.army_info(pygame.mouse.get_pos(), window, info_font, zeus, thor, odin)

            # timer
            timer.timer_count()

            # resources
            storage.mining(timer.time)
            storage.resource_upgrade(timer.time)

            # other function
            move_world.move_world((pygame.key.get_pressed()), game_bg, enemy_base, player_base,
                                  player_regiment.player_regiment, enemy_regiment.enemies, player_regiment.projectiles,
                                  enemy_regiment.projectiles)

            # Special properties
            special_properties.loading_properties(timer)
            special_properties.healing_base(player_base, timer)
            special_properties.speed_plus(timer, player_regiment.player_regiment)
            special_properties.damage_plus(timer, player_regiment.player_regiment)


            # text animation
            start_level.animation(timer.time, window)


        # Between level upgrade table
        if between_level_upgrade.active == True:
            # render
            between_level_upgrade.draw(window)
            b_zeus_upgrade_life.draw(pygame.mouse.get_pos(), window)
            b_zeus_upgrade_damage.draw(pygame.mouse.get_pos(), window)
            b_zeus_upgrade_distance.draw(pygame.mouse.get_pos(), window)
            b_thor_upgrade_life.draw(pygame.mouse.get_pos(), window)
            b_thor_upgrade_damage.draw(pygame.mouse.get_pos(), window)
            b_thor_upgrade_distance.draw(pygame.mouse.get_pos(), window)
            b_odin_upgrade_life.draw(pygame.mouse.get_pos(), window)
            b_odin_upgrade_damage.draw(pygame.mouse.get_pos(), window)
            b_odin_upgrade_distance.draw(pygame.mouse.get_pos(), window)
            b_base_upgrade_life.draw(pygame.mouse.get_pos(), window)
            b_sp_prop_healing.draw(pygame.mouse.get_pos(), window)
            b_sp_prop_plus_damage.draw(pygame.mouse.get_pos(), window)
            cash.cash_in_pocket(cash_font, window)
            b_main_menu_up_sec.draw(pygame.mouse.get_pos(), window)
            b_save_game.draw(pygame.mouse.get_pos(), window)
            b_next_mision.draw(pygame.mouse.get_pos(), window)

            #upgrading
            b_zeus_upgrade_life.upgrade_life(pygame.mouse.get_pos(), mouse_click, cash, zeus)
            b_zeus_upgrade_damage.upgrade_damage(pygame.mouse.get_pos(), mouse_click, cash, zeus)
            b_zeus_upgrade_distance.upgrade_distance(pygame.mouse.get_pos(), mouse_click, cash, zeus)
            b_thor_upgrade_life.upgrade_life(pygame.mouse.get_pos(), mouse_click, cash, thor)
            b_thor_upgrade_damage.upgrade_damage(pygame.mouse.get_pos(), mouse_click, cash, thor)
            b_thor_upgrade_distance.upgrade_distance(pygame.mouse.get_pos(), mouse_click, cash, thor)
            b_odin_upgrade_life.upgrade_life(pygame.mouse.get_pos(), mouse_click, cash, odin)
            b_odin_upgrade_damage.upgrade_damage(pygame.mouse.get_pos(), mouse_click, cash, odin)
            b_odin_upgrade_distance.upgrade_distance(pygame.mouse.get_pos(), mouse_click, cash, odin)


            #other funkcion
            b_main_menu_up_sec.main_menu(pygame.mouse.get_pos(), mouse_click, between_level_upgrade, main_menu,
                                         cash, zeus, thor, odin, consts)

            b_next_mision.next_mission(pygame.mouse.get_pos(), mouse_click, start_level, enemy_regiment, enem, enel,
                                       enex, enemy_base, between_level_upgrade, game)


        # Tutorial section
        if tutorial.active == True:
            tutorial.draw(window)
            b_back_main_menu.draw(pygame.mouse.get_pos(), window)
            b_back_main_menu.select_section(pygame.mouse.get_pos(), mouse_click, tutorial, main_menu)
            if tutorial.page < 10:
                page_plus.draw(pygame.mouse.get_pos(), window)
                page_plus.next_page(pygame.mouse.get_pos(), mouse_click, tutorial)
            if tutorial.page > 0:
                page_minus.draw(pygame.mouse.get_pos(), window)
                page_minus.back_page(pygame.mouse.get_pos(), mouse_click, tutorial)


        # Credit section
        if credit.active == True:
            credit.draw(window)
            b_back_main_menu.draw(pygame.mouse.get_pos(), window)
            b_back_main_menu.select_section(pygame.mouse.get_pos(), mouse_click, credit, main_menu)





        pygame.display.update()
        clock.tick(consts.GAME_FPS)






