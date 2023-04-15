import pygame
import numpy as np
from scripts.core.node_detail import NodeDetail

class BSOriginal(NodeDetail):
  def __init__(self, color_bg: pygame.Color, image: np.matrix) -> None:
    self.node_name = "Original"
    self.color_bg = color_bg
    self.size_panel_config = pygame.Rect(0, 0, 100, 30)
    super().__init__(self.node_name, self.color_bg, image)

  def set_image(self, image_cv: np.matrix) -> None:
    self.image_raw = image_cv.copy()
    self.image_apply = image_cv.copy()
    self.image_display = image_cv.copy()
    super().set_image(image_cv)
  
  def set_params(self):
    pass