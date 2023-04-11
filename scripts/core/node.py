import pygame
from scripts.interface.inode import INode

class Node(INode):
  def __init__(self, node_name, color_bg) -> None:
    super().__init__()
    self.node_name = node_name
    self.color_bg = color_bg

  def draw(self, surface: pygame.Surface) -> None:
    pass

  def update(self, delta_time: float) -> None:
    pass

  def events(self, event: pygame.event.Event) -> None:
    pass
  