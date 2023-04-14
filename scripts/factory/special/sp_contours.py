import pygame
import numpy as np
import cv2 as cv
from scripts.core.node_detail import NodeDetail

class SPContours(NodeDetail):
  def __init__(self, color_bg: pygame.Color, image: np.matrix) -> None:
    self.node_name = "Contours"
    self.color_bg = color_bg
    self.size_panel_config = pygame.Rect(0, 0, 100, 30)
    super().__init__(self.node_name, self.color_bg, image)

  def __apply_effect(self):
    if self.image_raw.ndim > 2:
      self.image_apply = cv.cvtColor(self.image_apply, cv.COLOR_RGB2GRAY)
      
    _binary = cv.threshold(self.image_apply, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
    _contours, _ = cv.findContours(_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    _contours_sort = sorted(_contours, key = cv.contourArea, reverse = True)
    self.image_apply = cv.drawContours(np.zeros((self.image_raw.shape[0], self.image_raw.shape[1], 3), dtype=np.uint8), _contours_sort, -1, (0, 255, 0), 2)

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