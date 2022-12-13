from math import *
import pygame
pygame.init()

window = pygame.display.set_mode((600,600))

class circle:
	def __init__(self,x,y,radius,stroke_width=1,color=(255,255,255)):
		self.x = x-stroke_width/2
		self.y = y-stroke_width/2
		self.radiusx = radius-stroke_width/2
		self.radiusy = radius-stroke_width/2
		self.stroke_width = stroke_width
		self.color = pygame.Color(color)
	
	def strech(self,axis,value):
		if axis=="both":
			self.radiusx += value
			self.radiusy += value
		elif axis=="x" or axis=="h":
			self.radiusx += value
		elif axis=="y" or axis=="v":
			self.radiusy += value
		

deg = 0
speed = 5


def sine(x,y,z,user_wants_cosine=False):
	if user_wants_cosine:
		return int(cos(radians(x))*y)+z
	return int(sin(radians(x))*y)+z
	
def draw_circle(circle,deg,speed,trail=False,trail_length=0):
	pygame.draw.rect(
		window,
		circle.color,
		pygame.Rect(
			sine(
				deg*speed,
				circle.radiusx,
				circle.x
			),
			sine(
				deg*speed,
				circle.radiusy,
				circle.y,
				True
			),
			circle.stroke_width,
			circle.stroke_width
		)
	)
	if not trail:
		return 0
		
	traildeg = deg-trail_length
	pygame.draw.rect(
		window,
		(0,0,0),
		pygame.Rect(
			sine(
				traildeg*speed,
				circle.radiusx,
				circle.x
			),
			sine(
				traildeg*speed,
				circle.radiusy,
				circle.y,
				True
			),
			circle.stroke_width,
			circle.stroke_width
		)
	)

red = circle(300,300,295,10)


while True:
	
	pygame.time.wait(5)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	if pygame.key.get_pressed()[pygame.key.key_code("x")]:
		pygame.quit()
		quit()
	
	deg += 1
	#red.color.r = sine(deg,254/2,128)
	#red.color.g = sine(deg,254/2,128)
	#red.color.b = sine(deg,100/2,198,True)
	#window.fill((0,0,0))
	draw_circle(red,deg,1,True,10)
	pygame.display.flip()
	
