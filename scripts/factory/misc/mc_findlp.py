import pygame
import numpy as np
import pygame_gui
import cv2 as cv
import scripts.stores as sts  
from scripts.core.node_detail import NodeDetail

class MCFindlp(NodeDetail):
  def __init__(self, color_bg: pygame.Color, image: np.matrix) -> None:
    self.node_name = "Find L.P"
    self.color_bg = color_bg
    self.size_panel_config = pygame.Rect(0, 0, 100, 30)

    super().__init__(self.node_name, self.color_bg, image)
    self.__config_ui_elements()

  def __config_ui_elements(self) -> None:
    pass

  def __show_ui_params(self):
    pass

  def __hide_ui_params(self):
    pass

  def __apply_effect(self):
    if self.image_raw.ndim > 2:
      self.image_apply = cv.cvtColor(self.image_apply, cv.COLOR_RGB2GRAY)
      
    _binary = cv.threshold(self.image_apply, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
    _contours, _ = cv.findContours(_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    _contours_sort = sorted(_contours, key = cv.contourArea, reverse = True)

    for c in _contours_sort:
      contour_perimeter = cv.arcLength(c, True)
      approx = cv.approxPolyDP(c, 0.018 * contour_perimeter, True)

      if len(approx) > 3 and len(approx) < 6:
        screen_cut = approx
        x, y, w, h = cv.boundingRect(c)

        _image = cv.resize(sts.image_cv.copy(), (self.image_raw.shape[1], self.image_raw.shape[0]), interpolation=cv.INTER_LINEAR)[y: y + h, x: x + w]
        self.image_apply = _image
        self.image_display = cv.drawContours(cv.resize(sts.image_cv.copy(), (self.image_raw.shape[1], self.image_raw.shape[0]), interpolation=cv.INTER_LINEAR), [screen_cut], -1, (0, 255, 0), 3)

        return
      
    self.image_display = np.zeros((150, 50, 3)).astype(np.uint8)
    self.image_apply = np.zeros((150, 50, 3)).astype(np.uint8)

  def set_image(self, image_cv: np.matrix) -> None:
    self.image_raw = image_cv.copy()
    self.image_apply = image_cv.copy()
    self.image_display = image_cv.copy()
    self.__apply_effect()
    super().set_image(image_cv)

  def set_params(self):
    pass

  def update(self, delta_time: float) -> None:
    super().update(delta_time)
    if self.ui_panel_config.visible:
      self.__show_ui_params() 
    else:
      self.__hide_ui_params()

  def events(self, event: pygame.event.Event) -> None:
    super().events(event)
    pass
