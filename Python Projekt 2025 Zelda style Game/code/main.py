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

		# sound
		main_sound = pygame.mixer.Sound('../audio/main.ogg')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)

	def run(self):
		while True:
			for event in pygame.event.get():
				keys = pygame.key.get_pressed()

				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						self.level.toggle_menu()

					if keys[pygame.K_ESCAPE]:  # Schließen mit ESC
						pygame.quit()
						sys.exit()

					if keys[pygame.K_r]:  # Neustart mit R
						pygame.mixer.stop()
						game = Game()
						game.run()

			self.screen.fill(WATER_COLOR)
			#debug('HI')
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)
			self.check_death()

	def check_death(self):
		if self.level.player.health <= 0:
			self.level.player.kill()
			pygame.mixer.stop()
			self.level.player.death_sound.play()
			pygame.time.wait(5000)
			game = Game()
			game.run()

if __name__ == '__main__':
	game = Game()
	game.run()	