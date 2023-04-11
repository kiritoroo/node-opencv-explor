import pygame
from scripts.core.node_detail import NodeDetail

class BSOriginal(NodeDetail):
  def __init__(self, color_bg: pygame.Color) -> None:
    super().__init__()
    self.node_name = "Original"
    self.color_bg = color_bg