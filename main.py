import time

from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))  # разом 55,55 - параметри
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_hieght - 150:
            self.rect.y += self.speed

    def update_2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_hieght - 150:
            self.rect.y += self.speed
win_width = 600
win_hieght = 500
color = (200, 255, 255)
window = display.set_mode((win_width, win_hieght))
rocket1 = Player("ball.png", 10, 200, 4, 20, 150)
rocket2 = Player("ball.png", 570, 200, 4, 20, 150)
ball = GameSprite("ball.png", 200, 200, 4, 30, 50)

clock = time.Clock()
run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.fill(color)
        rocket1.update()
        rocket2.update_2()
        rocket1.reset()
        rocket2.reset()
        ball.reset()

        display.update()
        clock.tick(60)