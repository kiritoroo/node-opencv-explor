import pygame
import numpy as np
import cv2 as cv
from scripts.core.node_detail import NodeDetail

class MPOpen(NodeDetail):
  def __init__(self, color_bg: pygame.Color, image: np.matrix) -> None:
    self.node_name = "Open"
    self.color_bg = color_bg
    super().__init__(self.node_name, self.color_bg, image)
    self.ksize = (3,3)
    self.kernel = np.ones(self.ksize, np.uint8)

  def __apply_effect(self):
    if self.image_raw.ndim > 2:
      self.image_apply = cv.cvtColor(self.image_apply, cv.COLOR_RGB2GRAY)
      
    _binary_img = cv.threshold(self.image_apply, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)[1]
    self.image_apply = cv.morphologyEx(_binary_img, cv.MORPH_OPEN, self.kernel, iterations=1)
    
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

  def set_params(self, ksize):
    if ksize % 2 == 0:
      ksize += 1
    self.ksize = (int(ksize), int(ksize))
    self.__apply_effect()