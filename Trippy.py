import pygame,time
import random
from math import pi
import numpy as np

CONST_W = 800
CONST_H = 800
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

def pol2cart(x,y,rho, phi):
	phi=(pi*phi/180)
	x1=x+rho*np.cos(phi)
	y1 = y + rho * np.sin(phi)
	return(int(x1), int(y1))    

def r_2(n1,angle1):
	return pi*(angle1%(360/n1) - (360/(2*n1)))/180

pygame.init()

size = [CONST_W, CONST_H]
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("screen2")

done = False
clock = pygame.time.Clock()
tick = 60
angle = []
dest = 70
dot_thick = 7
num_dot = 16
val = 0.4
colors = []

for i in range(1,100):
	colors.append((random.randint(0,127),random.randint(0,127),random.randint(0,127)))

screen.fill(WHITE)
angle.append(0)
angle.append(0)
angle.append(0)
lst = []
for i in range(3,num_dot+1):
	for j in range(0,i+1):
		lst.append(pol2cart(CONST_W/2,CONST_H/2,dest/(np.cos(pi/i)*np.tan(pi/i)),180/i+360*j/i+90))
	pygame.draw.polygon(screen, colors[i], lst, 2)
	lst.clear()
	angle.append(0)

sc1 = pygame.display.get_surface().copy()
ctr =0 
while not done:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True

	clock.tick(tick)
	screen.blit(sc1,(0,0))
	#pygame.draw.circle(screen, BLACK, (300,300), 5, 0)
	for i in range(3,num_dot+1):
		#angle[i]+= np.cos(r_2(i,angle[i]*(num_dot+1-i)-180/i))**2*np.tan(pi/i)*i/val
		pygame.draw.circle(screen, BLACK, pol2cart(CONST_W/2,CONST_H/2,dest/(np.cos(r_2(i,angle[i]*(num_dot+1-i)-180/i))*np.tan(pi/i)),angle[i]*(num_dot+1-i)+90), dot_thick, 0)
		angle[i]+= val
	pygame.display.flip()

	ctr+=1
	#pygame.image.save(pygame.display.get_surface(),"pic"+str(ctr))

pygame.display.flip()
pygame.quit()