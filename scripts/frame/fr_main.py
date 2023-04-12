import pygame
from scripts.handle.hd_solutions import SolutionsHandle
import assets.assets as ats
import scripts.stores as sts

class Frame:
  def __init__(self, surface: pygame.Surface) -> None:
    self.surface = surface
    self.scale_ratio = sts.scale_ratio
    self.handle_solutions = SolutionsHandle(ats.SOLUTION_FOLDER_PATH)
    self.is_move = False
    self.start()

  def start(self):
    pass
  
  def render(self, surface: pygame.Surface) -> None:
    self.handle_solutions.draw_all(surface)

  def update(self, delta_time: str) -> None:
    if not self.is_move:
      self.mouse_rel = pygame.mouse.get_rel()

    if pygame.mouse.get_pressed()[2]:
      self.is_move = True
      self.mouse_rel = pygame.mouse.get_rel()
      self.handle_solutions.move(pygame.math.Vector2(self.mouse_rel))
    else:
      self.is_move = False

  def events(self, event: pygame.event.Event) -> None:
    pass