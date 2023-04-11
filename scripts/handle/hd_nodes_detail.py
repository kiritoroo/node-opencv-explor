import pygame
from scripts.core.node_detail import NodeDetail

class NodesDetailHandle:
  def __init__(self, list_node_detail: list[NodeDetail]) -> None:
    self.scale_ratio = 1
    self.position = pygame.math.Vector2(0,0)
    self.list_node_detail = list_node_detail
    self.node_detail_cout = len(self.list_node_detail)

  def draw_all(self, surface: pygame.Surface) -> None:
    for i in range(self.node_detail_cout):
      self.list_node_detail[i].draw(surface)

  def update_all(self, delta_time: float) -> None:
    pass

  def events_all(self, event: pygame.event.Event) -> None:
    pass

  def add_node_detail(self) -> None:
    pass

  def remove_node_detail(self) -> None:
    pass

  def reset_all_position(self) -> None:
    _padding_horizontal = self.list_node_detail[0].rect_container.width + 50
    _padding_vertical = 0
    _new_node_position = pygame.math.Vector2(
      self.position.x + _padding_horizontal,
      self.position.y + _padding_vertical)
    
    for i in range(self.node_detail_cout):
      self.list_node_detail[i].set_position(_new_node_position)
      _new_node_position.x = self.list_node_detail[i].position.x + _padding_horizontal
      _new_node_position.y = self.list_node_detail[i].position.y + _padding_vertical

  def set_position(self, position: pygame.math.Vector2) -> None:
    self.position = position
    self.reset_all_position()