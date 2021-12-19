import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 600))
    pygame.display.set_caption("Космические защитники")
    bg_color =(0,0,0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group() #передаем изображение где отображается наш пришелец
    controls.create_army(screen, inos) #вызываем функцию, которая вызывает экран и пришельцев
    stats = Stats()

    while True:

      controls.events(screen, gun, bullets)   # """функция ответственная за прослушивания события .events"""
      gun.update_gun()  # обновляем позицию пушки

      controls.update(bg_color, screen, gun, inos, bullets)
      controls.update_bullets(screen, inos, bullets)
      controls.update_inos(stats, screen, gun, inos, bullets)



run()

