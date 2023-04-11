import pygame
import os
from scripts.core.solution import Solution

class SolutionsHandle:
  def __init__(self, solutons_folder_path: str) -> None:
    self.solutons_folder_path = solutons_folder_path
    self.solutions = list[Solution]()
    self.solutions_count = 0

    self.scale_ratio = 1
    self.position = pygame.math.Vector2(0,0)

    self.start()

  def start(self):
    self.read_solutions(self.solutons_folder_path)

  def draw_all(self, surface: pygame.Surface) -> None:
    pass

  def update_all(self, delta_time: float) -> None:
    pass

  def events_all(self, event: pygame.event.Event) -> None:
    pass

  def read_solutions(self, solutons_folder_path: str) -> None:
    self.solutons_folder_path = solutons_folder_path
    for _file_name in os.listdir(self.solutons_folder_path):
      if _file_name.endswith('.json'):
        self.solutions_count += 1
        _solution_path = os.path.join(self.solutons_folder_path, _file_name)
        _solution_name = f'Solution {self.solutions_count}'
        _solution = Solution(_solution_name, _solution_path)
        self.solutions.append(_solution)

  def write_solutions(self) -> None:
    pass

  def create_solution(self) -> None:
    pass

  def remove_solution(self) -> None:
    pass