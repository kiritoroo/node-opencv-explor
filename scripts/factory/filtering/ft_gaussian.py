import pygame
import numpy as np
from scripts.core.node_detail import NodeDetail

class FLGaussian(NodeDetail):
  def __init__(self, color_bg: pygame.Color, image: np.matrix) -> None:
    self.node_name = "Gaussian"
    self.color_bg = color_bg
    super().__init__(self.node_name, self.color_bg, image)
