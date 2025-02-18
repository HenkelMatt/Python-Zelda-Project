import pygame, sys
from settings import *
from level import Level
from debug import debug

class Game:
	def __init__(self):
		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Zelda Style game')
		self.clock = pygame.time.Clock()

		self.level = Level()

	def run(self):
		while True:
			for event in pygame.event.get():
				keys = pygame.key.get_pressed()

				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if keys[pygame.K_ESCAPE]:  # Schließen mit ESC
					pygame.quit()
					sys.exit()

				if keys[pygame.K_r]:  # Neustart mit R
					game = Game()
					game.run()

			self.screen.fill('black')
			#debug('HI')
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()	