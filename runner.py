import pygame, math, sys
import carSprite
from carSprite import CarSprite
from pygame.locals import *

screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()

rect = screen.get_rect()
car = CarSprite('car.png', rect.center)
car_group = pygame.sprite.RenderPlain(car)

while 1:
	deltat = clock.tick(60)
	for event in pygame.event.get():
		if not hasattr(event, 'key'): continue
		down = event.type == KEYDOWN
		if event.key == K_RIGHT: car.k_right = down * -5
		elif event.key == K_LEFT: car.k_left = down * 5
		elif event.key == K_UP: car.k_up = down * 2
		elif event.key == K_DOWN: car.k_down = down * -2
		elif event.key == K_ESCAPE: sys.exit(0)

	screen.fill((0,0,0))
	car_group.update(deltat)
	car_group.draw(screen)
	pygame.display.flip()
