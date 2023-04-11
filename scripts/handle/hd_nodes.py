import pygame
from scripts.core.node import Node

class NodesHandle:
  def __init__(self, list_node: list[Node]) -> None:
    self.scale_ratio = 1
    self.position = pygame.math.Vector2(0,0)
    self.list_node = list_node
    self.node_count = len(self.list_node)
    
    self.start()

  def start(self):
    self.reset_all_position()

  def draw_all(self, surface: pygame.Surface) -> None:
    for i in range(self.node_count):
      self.list_node[i].draw(surface)

  def update_all(self, delta_time: float) -> None:
    pass

  def events_all(self, event: pygame.event.Event) -> None:
    pass

  def add_node(self) -> None:
    pass

  def remove_node(self) -> None:
    pass

  def reset_all_position(self) -> None:
    _padding_horizontal = 0
    _padding_vertical = self.list_node[0].rect_container.height + 10
    _new_node_position = pygame.math.Vector2(
      self.position.x + _padding_horizontal,
      self.position.y + _padding_vertical)
    
    for i in range(self.node_count):
      self.list_node[i].set_position(_new_node_position)
      _new_node_position.x = self.list_node[i].position.x + _padding_horizontal
      _new_node_position.y = self.list_node[i].position.y + _padding_vertical

  def set_position(self, position: pygame.math.Vector2) -> None:
    self.position = position
    self.reset_all_position()