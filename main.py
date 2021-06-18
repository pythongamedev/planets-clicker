#importing pygame
import pygame
from pygame.locals import *
#intializing pygame
pygame.init()
#creating surface
surface = pygame.display.set_mode((480, 640))
#setting an game title
pygame.display.set_caption("planet clicker")
#creating variable named 'score', loading font and creating text
score = 0
pygame.font.init()
font = pygame.font.Font("ARCADECLASSIC.ttf", 64)
scoretext = font.render(str(score), False, (255, 255, 255))
#making class 'Planet'
class Planet:
	def __init__(self, name, power):
		self.name = name
		self.power = power
		self.planetimg = pygame.image.load(self.name + ".png")
		self.planet = self.planetimg.get_rect().move((160, 220))
#creating object of class 'Planet'
planet = Planet("earth", 1)
#creating clock
clock = pygame.time.Clock()
#mainloop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		elif event.type == pygame.MOUSEBUTTONUP:
			if planet.planet.collidepoint(event.pos):
				score += planet.power
	#Framelimiter
	clock.tick(20)
	surface.fill((0, 0, 39))
	surface.blit(planet.planetimg, planet.planet)
	surface.blit(scoretext, (240, 50))
	scoretext = font.render(str(score), False, (255, 255, 255))
	pygame.display.flip()