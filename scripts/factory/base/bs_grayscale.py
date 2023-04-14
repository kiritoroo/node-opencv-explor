import pygame
import numpy as np
import cv2 as cv
from scripts.core.node_detail import NodeDetail

class BSGrayscale(NodeDetail):
  def __init__(self, color_bg: pygame.Color, image: np.matrix) -> None:
    self.node_name = "Graysale"
    self.color_bg = color_bg
    super().__init__(self.node_name, self.color_bg, image)

  def __apply_effect(self):
    if self.image_raw.ndim > 2:
      self.image_apply = cv.cvtColor(self.image_apply, cv.COLOR_RGB2GRAY)
    
    if self.image_apply.ndim < 3:
      self.image_display = cv.cvtColor(self.image_apply.copy(), cv.COLOR_GRAY2RGB)
    else:
      self.image_display = self.image_apply.copy()
      
  def set_image(self, image_cv: np.matrix) -> None:
    self.image_raw = image_cv.copy()
    self.image_apply = image_cv.copy()
    self.image_display = image_cv.copy()

    self.__apply_effect()

    super().set_image(image_cv)
  
  def set_params(self):
    pass