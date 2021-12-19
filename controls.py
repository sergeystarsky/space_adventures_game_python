import pygame, sys
from bullet import Bullet
from ino import Ino
import time

def events(screen,gun, bullets):  #цикл использует экран, пушку, контейнер bullets
   # """обработка событий"""
    for event in pygame.event.get(): # метод event.get() прослушивает все события на экране
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: # если клавиша нажата (KEYDOWN)
            #вправо
            if event.key == pygame.K_d:
                gun.mright = True   #переменная движения вправо
            #влево
            elif event.key == pygame.K_a:
                gun.mleft = True  #переменная движения влево
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet (screen,gun)  # на нашем текущем экране, где находится наша пушка
                bullets.add(new_bullet) #в контейнер bullet добавляем new_bullet
        elif event.type == pygame.KEYUP:
            #вправо
            if event.key == pygame.K_d:
                gun.mright = False #переменная движения вправо
            #влево
            elif event.key == pygame.K_a:
                gun.mleft = False  #переменная движения влево


def update(bg_color, screen, gun, inos,  bullets):
    """обновление экрана"""
    screen.fill(bg_color)
    for bullet in bullets.sprites(): #до отрисовки пушки, выводим пульки, что бы было красиво
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(screen, inos,bullets):
    """обновлять позиции пуль"""
    bullets.update()  # помещаем в цикл наши пули
    for bullet in bullets.copy(): # копируем содержимое контейнера
        if bullet.rect.bottom <=0: #пуля должна исчезать когда ее низ перешел предел экрана
            bullets.remove(bullet) # удаляем из нашего контейнера bullets пулю bullet
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True) #groupcollide - метод  проверяте пересечение двух объектов
    # и если они соприкосунулись уничтожает их пуля и ино, аргумент true говорит о том что объект уничтожается
    if len(inos) == 0: # если длина пришельцев  = 0
        bullets.empty() # очищаем всю группу с пулями
        create_army(screen, inos) # вызываем нашу функцию create army передаем ей screen, inos


def gun_kill(stats,screen, gun ,inos,bullets):
    """столкновение пушки и армии"""
    stats.guns_left -= 1 # при столкновении пришельца с пусшкой убираем в статистике 1 жизнь
    inos.empty() #очищаем от пришельцев
    bullets.empty() # очищаем от пуль
    create_army(screen, inos)
    gun.create_gun() #  метод восстанавливает пушку после уничтожения
    time.sleep(2)

def update_inos(stats, screen, gun, inos, bullets):
    """обновляет позицию инопришельцев"""
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, gun, inos, bullets)
    inos_check(stats, screen, gun, inos, bullets)

def inos_check (stats, screen, gun, inos, bullets):
    """проверка добралась ли армия до края экрана"""
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >=screen_rect.bottom:
            gun_kill(stats, screen, gun, inos, bullets)
            break




def create_army(screen, inos):
    """создание армии пришельцев"""
    ino = Ino(screen)
    ino_width =ino.rect.width  #ширина прямоугольника
    number_ino_x =int((700-2*ino_width)/ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((700-16-2*ino_height)/ino_height)

    for row_number in range(number_ino_y-2): # цикл создаем пришельцев в столбик
        for ino_number in range (number_ino_x): # цикл создаем пришельцев в ряд
            ino =Ino(screen) # создаем одного пришельца
            ino.x =ino_width + (ino_width*ino_number)
            ino.y = ino_height + (ino_height*row_number)
            ino.rect.x =ino.x # расстояние между пришельцами
            ino.rect.y = ino.rect.height + (ino.rect.height *  row_number)
            inos.add(ino) # добавляем в группу inos



