from math import *
import pygame
pygame.init()

window = pygame.display.set_mode((600,600))
unitsize = 30

class entity:
	def __init__(self, x=0, y=0, r=255, g=255, b=255):
		self.x = x
		self.y = y
		self.color = (r,g,b)

	def moverel(self, x, y):
		self.x += x
		self.y += y
	
def render(entity):
	global unitsize
	pygame.draw.rect(window,entity.color,pygame.Rect(entity.x*unitsize, entity.y*unitsize,unitsize,unitsize))

steve = entity(4,4,100,100,255)

def on_close():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	
def move(object):
	
	pressed = pygame.key.get_pressed()
	
	if pressed[pygame.key.key_code("up")]:
		object.moverel(0,-1)
	if pressed[pygame.key.key_code("left")]:
		object.moverel(-1,0)
	if pressed[pygame.key.key_code("down")]:
		object.moverel(0,1)
	if pressed[pygame.key.key_code("right")]:
		object.moverel(1,0)


def tick():
	pygame.time.wait(100)
	on_close()
	global steve
	move(steve)
	
	
def draw():
	window.fill((0,0,0))
	render(steve)
	pygame.display.flip()

while True:

	tick()
	draw()
