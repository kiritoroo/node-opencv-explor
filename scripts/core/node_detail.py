import pygame
from scripts.interface.inode_detail import INodeDetail

class NodeDetail(INodeDetail):
  def __init__(self) -> None:
    super().__init__()
    self.node = None

  def draw(self, surface: pygame.Surface) -> None:
    pass

  def update(self, delta_time: float) -> None:
    pass

  def events(self, event: pygame.event.Event) -> None:
    pass