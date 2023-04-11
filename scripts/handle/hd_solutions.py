import pygame
from scripts.interface.isolution import ISolution

class SolutionsHandle:
  def __init__(self) -> None:
    self.scale_ratio = 1
    self.position = pygame.math.Vector2(0,0)
    self.solutions = list[ISolution]

  def draw_all(self, surface: pygame.Surface) -> None:
    pass

  def update_all(self, delta_time: float) -> None:
    pass

  def events_all(self, event: pygame.event.Event) -> None:
    pass

  def read_solutions(self) -> None:
    pass

  def write_solutions(self) -> None:
    pass

  def create_solution(self) -> None:
    pass

  def remove_solution(self) -> None:
    pass