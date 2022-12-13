import math
import pygame
pygame.init()

window = pygame.display.set_mode((600,600))

def line(a,b,c,d,w):
	if c>a:
		width=c-a
	elif c<a:
		width=a-c
	else:
		width=c #c and a equal
		
	if d>b:
		height=d-b
	elif d<b:
		heigth=b-d
	else:
		height=d #d and b equal
	
	if width>height:
		steps=width
		for step in range(steps):
			x = step
			y = round(height/width*step)
			pygame.draw.rect(window,(255,255,255),pygame.Rect(x*w,y*w,w,w))
	elif width<height:
		steps=height
		for step in range(steps):
			y = step
			x = round(height/width*step)
			pygame.draw.rect(window,(255,255,255),pygame.Rect(x*w,y*w,w,w))
	else:
		steps=width #width height equal
		for step in range(steps):
			x = step
			y = step
			pygame.draw.rect(window,(255,255,255),pygame.Rect(x*w,y*w,w,w))
	
line(20,5,40,50,10)

while True:
	pygame.time.wait(1)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	if pygame.key.get_pressed()[pygame.key.key_code("x")]:
		pygame.quit()
		quit()	
	
	
	pygame.display.flip()
	
