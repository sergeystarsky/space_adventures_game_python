import pygame

class Ino(pygame.sprite.Sprite):
    """класс одного пришельца"""

    def __init__(self,screen):   # в части документа передадим экран
        """инициализируем и задаем начальную позицию"""
        super(Ino,self).__init__() # подтягивает инфо из родительского класса sprite
        self.screen = screen # подтягиваем экран, то место где происходит действие
        self.image = pygame.image.load('images/ino.png') #загружаем инопланетянина
        self.rect = self.image.get_rect() # помещаем наш загруженный объект self.image в прямоугольник
        self.rect.x = self.rect.width  # по X отслеживаем ширину
        self.rect.y = self.rect.height # по y отслеживаем высоту
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """вывод пришельца на экрна"""
        self.screen.blit (self.image, self.rect)

    def update (self):
        """перемещает пришельцев"""
        self.y +=0.1
        self.rect.y = self.y




