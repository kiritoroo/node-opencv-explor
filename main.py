import pygame
import time, sys
import scripts.constants as cst
import scripts.colors as cls
import scripts.frame.fr_main as frame
from scripts.handle import hd_frame

class Canvas:
	def __init__(self) -> None:
		pygame.init()
		pygame.display.set_caption(cst.APP_CAPTION)
		self.clock = pygame.time.Clock()
		self.canvas = pygame.display.set_mode((
			cst.SCREEN_WIDTH, cst.SCREEN_HEIGHT
		))

		self.frame_handle = hd_frame.FrameHandle(self.canvas)

	def run(self):
		_last_time = time.time()
		while True:
			_delta_time = time.time() - _last_time
			_last_time = time.time()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				self.frame_handle.current_frame.events(event)

			self.canvas.fill(cls.WHITE)
			self.frame_handle.current_frame.update(_delta_time)
			self.frame_handle.current_frame.render(self.canvas)

			pygame.display.update()
			self.clock.tick(cst.FRAME_RATE)

if __name__ == '__main__':
	app = Canvas()
	app.run()