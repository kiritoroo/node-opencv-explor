import pygame
import pygame_gui
import os
import datetime
import json
import assets.assets as ats
import scripts.colors as cls
import scripts.stores as sts
import scripts.utils as uts
import scripts.constants as cts
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
    self.position = pygame.math.Vector2(600, 250)

    self.default_padding_horizontal = 0
    self.default_padding_vertical = 340

    self.current_padding_horizontal = float(self.default_padding_horizontal)
    self.current_padding_vertical = float(self.default_padding_vertical)

  def __config_ui_elements(self):
    self.ui_manager = pygame_gui.UIManager((cts.SCREEN_WIDTH, cts.SCREEN_HEIGHT), ats.THEME_PATH)

    _rect = pygame.Rect(0, 0, 120, 60)
    self.ui_btn_new_solution = pygame_gui.elements.UIButton(relative_rect=_rect,
              text='New Solution', manager=self.ui_manager,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_save", class_id="#btn"))
    
  def __config_rect_container(self):
    _left = self.solutions[0].rect_container_node_detail.left
    _top = self.solutions[0].rect_container_node_detail.top
    _width = 500
    _height = self.solutions[self.solution_count-1].rect_container_node_detail.bottom-_top
    self.rect_container = pygame.Rect(_left, _top, _width, _height)

  def __config_ui_btn_new_solution(self):
    _pos_x = self.rect_container.left+50
    _pos_y = self.rect_container.bottom+50
    self.ui_btn_new_solution.set_position(pygame.math.Vector2(_pos_x, _pos_y))

  def _start(self):
    self.read_solutions(self.solutons_folder_path)
    self.__config_variables()
    self.__config_rect_container()
    self.__config_ui_elements()
    self.__config_ui_btn_new_solution()

    self._reset_all_position()
    self._reset_all_scale_ratio()

  def draw_all(self, surface: pygame.Surface) -> None:
    self.ui_manager.draw_ui(surface)

    for i in range(self.solution_count):
      self.solutions[i].draw(surface)
    for i in range(self.solution_count):
      self.solutions[i].comp_node_store.draw(surface)

  def update_all(self, delta_time: float) -> None:
    self.ui_manager.update(delta_time)
    for i in range(self.solution_count):
      self.solutions[i].update(delta_time)

  def events_all(self, event: pygame.event.Event) -> None:
    self.ui_manager.process_events(event)
    for i in range(self.solution_count):
      self.solutions[i].events(event)
    
    if event.type == pygame_gui.UI_BUTTON_PRESSED:
      if event.ui_element == self.ui_btn_new_solution:
        self.create_solution()

      for i in range(self.solution_count):
        if event.ui_element == self.solutions[i].ui_btn_delete:
          if self.solution_count == 1: return
          self.solutions[i].remove_solution()
          del self.solutions[i]
          self.solution_count -= 1
          self.__config_rect_container()
          self.__config_ui_elements()
          self.__config_ui_btn_new_solution()

  def read_solutions(self, solutons_folder_path: str) -> None:
    self.solutons_folder_path = solutons_folder_path
    for _file_name in os.listdir(self.solutons_folder_path):
      if _file_name.endswith('.json'):
        self.solution_count += 1
        _solution_path = os.path.join(self.solutons_folder_path, _file_name)
        _solution_name = f'Solution {self.solution_count}'
        _solution = Solution(_solution_name, _solution_path)
        self.solutions.append(_solution)

  def create_solution(self) -> None:
    _default_solution_dict = {
      "0": {
        "category": "base",
        "type": "original",
        "name": "Original",
        "params": {}
      }
    }
    _solution_file_path = f'{ats.SOLUTION_FOLDER_PATH}/solution_{self.solution_count+1}_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    with open(_solution_file_path, "w") as f:
      json.dump(_default_solution_dict, f, indent=2)

    self.solution_count += 1
    _solution_path = os.path.join(_solution_file_path)
    _solution_name = f'Solution {self.solution_count}'
    _solution = Solution(_solution_name, _solution_path)
    self.solutions.append(_solution)
    self.__config_ui_btn_new_solution()

    self._reset_all_position()
    self._reset_all_scale_ratio()

  def _reset_all_position(self) -> None:
    _new_position = self.position.copy()
    for i in range(self.solution_count):
      self.solutions[i].set_position_nodes_detail(_new_position)
      _new_position.x = self.solutions[i].position_nodes_detail.x+self.current_padding_horizontal
      _new_position.y = self.solutions[i].position_nodes_detail.y+self.current_padding_vertical
    self.__config_rect_container()
    self.__config_ui_btn_new_solution()

  def _reset_all_scale_ratio(self) -> None:
    for i in range(self.solution_count):
      self.solutions[i].set_scale_ratio(self.scale_ratio)
    self.__config_rect_container()
    self.__config_ui_btn_new_solution()

  def move(self, offset: pygame.math.Vector2) -> None:
    self.position.x += offset.x
    self.position.y += offset.y
    self._reset_all_position()

  def zoom(self, scale_ratio) -> None:
    self.scale_ratio = float(scale_ratio)
    self.current_padding_horizontal = float(self.default_padding_horizontal*self.scale_ratio)
    self.current_padding_vertical = float(self.default_padding_vertical*self.scale_ratio)
    self._reset_all_scale_ratio()
    self._reset_all_position()

  def reset_image(self) -> None:
    for i in range(self.solution_count):
      self.solutions[i].handle_nodes_detail.reset_image()
    self._reset_all_scale_ratio()
    self._reset_all_position()

