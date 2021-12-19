import pygame

class Bullet(pygame.sprite.Sprite): #
    def __init__(self, screen,gun):
        """создаем пулю в позиции пушки"""
        super (Bullet, self).__init__()
        self.screen = screen #подзакгружаю экран где будут отрисовываться пули
        self.rect = pygame.Rect(0, 0, 2, 12) #рисуем прямоугольник rect, кординаты (0.0) ширина и высота
        self.color = 204, 220, 57 # цвет пули
        self.speed = 4.5 # скрость пули
        self.rect.centerx = gun.rect.centerx # положение пушки
        self.rect.top = gun.rect.top # пуля вылетатет из верха пушки
        self.y = float(self.rect.y) # движение пушки по координате y

    def update(self):
        """перемещение пули вверх"""
        self.y -= self.speed # координата y будет уменьшатьс на скорость которую мы задали
        self.rect.y = self.y

    def draw_bullet(self):
        """рисум пулю на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect) # рисуем пушку на нашем экране, с прописанном ранее цветом,размером



