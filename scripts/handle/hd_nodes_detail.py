import pygame
from scripts.core.node_detail import NodeDetail
import scripts.stores as sts
import scripts.utils as uts
import scripts.colors as cls

class NodesDetailHandle:
  def __init__(self, list_node_detail: list[NodeDetail]) -> None:
    self.list_node_detail = list_node_detail
    self.node_detail_cout = len(self.list_node_detail)

    self._start()

  def __config_variables(self):
    self.scale_ratio = sts.scale_ratio
    self.position = pygame.math.Vector2(0,0)

    self.default_padding_horizontal = 350
    self.default_padding_betwwen = 50
    self.default_padding_vertical = 0
    self.default_size_border_arrow = 2
    self.default_length_arrow = 0
    self.default_width_arrow = 6

    self.current_padding_horizontal = float(self.default_padding_horizontal)
    self.current_padding_betwwen = float(self.default_padding_betwwen)
    self.current_padding_vertical = float(self.default_padding_vertical)
    self.current_size_border_arrow= int(self.default_size_border_arrow)
    self.current_length_arrow = int(self.default_length_arrow)
    self.current_width_arrow = int(self.default_width_arrow)

    self.color_arrow = cls.ARROW_COLOR

  def _draw_arrow_node_detail(self, surface):
    for i in range(self.node_detail_cout-1):
      _arrow_start_pos = pygame.math.Vector2(
        self.list_node_detail[i].rect_container.right,
        self.list_node_detail[i].rect_container.y+self.list_node_detail[i].rect_container.height/2)
      _arrow_end_pos = pygame.math.Vector2(
        self.list_node_detail[i+1].rect_container.left,
        self.list_node_detail[i].rect_container.y+self.list_node_detail[i].rect_container.height/2)
      uts.draw_arrow(surface, _arrow_start_pos, _arrow_end_pos, self.current_width_arrow, self.current_length_arrow, self.color_arrow, self.current_size_border_arrow)

  def _start(self):
    self.__config_variables()

  def draw_all(self, surface: pygame.Surface) -> None:
    self._draw_arrow_node_detail(surface)
    for i in range(self.node_detail_cout):
      self.list_node_detail[i].draw(surface)

    for i in range(self.node_detail_cout):
      self.list_node_detail[i].ui_manager.draw_ui(surface)

  def update_all(self, delta_time: float) -> None:
    for i in range(self.node_detail_cout):
      self.list_node_detail[i].update(delta_time)

    for i in range(self.node_detail_cout):
      if self.list_node_detail[i].is_update_image:
        self.reset_image()
        self.list_node_detail[i].is_update_image = False
        return

  def events_all(self, event: pygame.event.Event) -> None:
    for i in range(self.node_detail_cout):
      self.list_node_detail[i].events(event)

  def add_node_detail(self) -> None:
    pass

  def remove_node_detail(self) -> None:
    pass

  def _reset_all_position(self) -> None:
    _new_position = self.position.copy()
    for i in range(self.node_detail_cout):
      self.list_node_detail[i].set_position(_new_position)
      _new_position.x = self.list_node_detail[i].position.x+self.current_padding_horizontal
      _new_position.y = self.list_node_detail[i].position.y+self.current_padding_vertical

  def set_position(self, position: pygame.math.Vector2) -> None:
    self.position = position.copy()
    self._reset_all_position()

  def _reset_all_scale_ratio(self) -> None:
    for i in range(self.node_detail_cout):
      self.list_node_detail[i].set_scale_ratio(self.scale_ratio)

  def set_scale_ratio(self, scale_ratio: float) -> None:
    self.scale_ratio = float(scale_ratio)
    self.current_padding_horizontal = float(self.default_padding_horizontal*self.scale_ratio)
    self.current_padding_betwwen = float(self.default_padding_betwwen*self.scale_ratio)
    self.current_padding_vertical = float(self.default_padding_vertical*self.scale_ratio)
    self.current_size_border_arrow = int(self.default_size_border_arrow*self.scale_ratio) if int(self.default_size_border_arrow*self.scale_ratio) > 0 else 1
    self.current_length_arrow = int(self.default_length_arrow*self.scale_ratio)
    self.current_width_arrow = int(self.default_width_arrow*self.scale_ratio)
    self._reset_all_scale_ratio()

  def reset_image(self):
    self.list_node_detail[0].set_image(sts.image_cv)
    for i in range(1, self.node_detail_cout):
      self.list_node_detail[i].set_image(self.list_node_detail[i-1].image_apply)