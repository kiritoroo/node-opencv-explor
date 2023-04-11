import pygame
from scripts.core.node_data import NodeData

class NodesDetailHandle:
  def __init__(self, nodes_data) -> None:
    self.scale_ratio = 1
    self.position = pygame.math.Vector2(0,0)
    self.nodes_data = nodes_data

  def draw_all(self, surface: pygame.Surface) -> None:
    pass

  def update_all(self, delta_time: float) -> None:
    pass

  def events_all(self, event: pygame.event.Event) -> None:
    pass

  def add_node_detail(self) -> None:
    pass

  def remove_node_detail(self) -> None:
    pass