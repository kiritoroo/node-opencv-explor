import pygame
import os
from scripts.core.solution import Solution
import scripts.stores as sts

class SolutionsHandle:
  def __init__(self, solutons_folder_path: str) -> None:
    self.solutons_folder_path = solutons_folder_path
    self.solutions = list[Solution]()
    self.solution_count = 0

    self._start()

  def __config_variables(self):
    self.scale_ratio = sts.scale_ratio
    self.position = pygame.math.Vector2(300, 250)

  def _start(self):
    self.__config_variables()
    self.read_solutions(self.solutons_folder_path)

  def draw_all(self, surface: pygame.Surface) -> None:
    for i in range(self.solution_count):
      self.solutions[i].draw(surface)

  def update_all(self, delta_time: float) -> None:
    pass

  def events_all(self, event: pygame.event.Event) -> None:
    pass

  def read_solutions(self, solutons_folder_path: str) -> None:
    self.solutons_folder_path = solutons_folder_path
    for _file_name in os.listdir(self.solutons_folder_path):
      if _file_name.endswith('.json'):
        self.solution_count += 1
        _solution_path = os.path.join(self.solutons_folder_path, _file_name)
        _solution_name = f'Solution {self.solution_count}'
        _solution = Solution(_solution_name, _solution_path)
        self.solutions.append(_solution)

    self._reset_all_position()
    self._reset_all_scale_ratio()

  def write_solutions(self) -> None:
    pass

  def create_solution(self) -> None:
    pass

  def remove_solution(self) -> None:
    pass

  def _reset_all_position(self) -> None:
    _padding_horizontal = 0
    _padding_vertical = self.solutions[0].rect_container_node_detail.height + 50
    _new_position = self.position.copy()
    
    for i in range(self.solution_count):
      self.solutions[i].set_position_nodes_detail(_new_position)
      _new_position.x = self.solutions[i].position_nodes_detail.x + _padding_horizontal
      _new_position.y = self.solutions[i].position_nodes_detail.y + _padding_vertical

  def _reset_all_scale_ratio(self) -> None:
    for i in range(self.solution_count):
      self.solutions[i].set_scale_ratio(self.scale_ratio)

  def move(self, offset: pygame.math.Vector2) -> None:
    self.position.x += offset.x
    self.position.y += offset.y
    self._reset_all_position()

  def zoom(self, scale_ratio) -> None:
    self.scale_ratio = float(scale_ratio)
    self._reset_all_scale_ratio()
    self._reset_all_position()
    