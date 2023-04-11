import pygame
from scripts.handle.hd_solutions import SolutionsHandle
import assets.assets as ats

class Frame:
  def __init__(self, surface: pygame.Surface) -> None:
    self.surface = surface
    self.scale_ratio = 1
    self.handle_solutions = SolutionsHandle(ats.SOLUTION_FOLDER_PATH)

    self.start()

  def start(self):
    pass
  
  def render(self, surface: pygame.Surface) -> None:
    self.handle_solutions.draw_all(surface)

  def update(self, delta_time: str) -> None:
    pass

  def events(self, event: pygame.event.Event) -> None:
    pass