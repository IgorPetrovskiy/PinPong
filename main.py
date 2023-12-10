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
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_hieght - 150:
            self.rect.y += self.speed

    def update_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_hieght - 150:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y > win_hieght - 50 or self.rect.y < 0:
            self.speed_y = -self.speed_y

        if sprite.collide_rect(self, rocket1) or sprite.collide_rect(self, rocket2):
            self.speed_x = -self.speed_x

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
win_width = 600
win_hieght = 500
color = (200, 255, 255)
font.init()
font = font.Font(None, 25)

win_left = font.render('LEFT WINNER!!!', True, (255, 0, 0))
win_right = font.render('RIGHT WINNER!!!', True,(255, 0, 0))
window = display.set_mode((win_width, win_hieght))
rocket1 = Player("ball.png", 10, 200, 4, 20, 150)
rocket2 = Player("ball.png", 570, 200, 4, 20, 150)
ball = Ball("ball.png", 200, 200, 4, 30, 50)
ball.speed_x = 4
ball.speed_y = 4
clock = time.Clock()
run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.fill(color)
        if ball.rect.x > 590:
            finish = True
            window.blit(win_left, (220, 10))
        if ball.rect.x < 0:
            finish = True
            window.blit(win_right, (220, 10))
        rocket1.update()
        rocket2.update_2()
        rocket1.reset()
        rocket2.reset()
        ball.update()
        ball.reset()
        display.update()
        clock.tick(60)