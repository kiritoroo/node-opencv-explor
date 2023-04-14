import pygame
import pygame_gui
import numpy as np
import cv2 as cv
from scripts.core.node_detail import NodeDetail

class MPErode(NodeDetail):
  def __init__(self, color_bg: pygame.Color, image: np.matrix) -> None:
    self.node_name = "Erode"
    self.color_bg = color_bg
    self.size_panel_config = pygame.Rect(0, 0, 250, 50)
    self.ksize = (5, 5)
    self.param_dict = {
      "ksize": self.ksize[0]
    }
    self.kernel = np.ones(self.ksize, np.uint8)
    super().__init__(self.node_name, self.color_bg, image)
    self.__config_ui_elements()

  def __config_ui_elements(self):
    _rect = pygame.Rect(0, 0, 60, 20)
    self.ui_txt_ksize= pygame_gui.elements.UIButton(relative_rect=_rect,
              text=f'ksize: {self.ksize[0]}', tool_tip_text="Kích thước của kernel (bộ lọc).",
              manager=self.ui_manager, container=self.ui_panel_config,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_param",class_id="#btn"))
    
    _rect = pygame.Rect(0, 0, 150, 20)
    self.ui_slider_ksize = pygame_gui.elements.UIHorizontalSlider(relative_rect=_rect,
              manager=self.ui_manager, container=self.ui_panel_config,
              start_value=3, value_range=(3,99),
              object_id=pygame_gui.core.ObjectID(class_id="#slider"))
    
  def __show_ui_params(self):
    self.ui_txt_ksize.set_position(pygame.math.Vector2(
      self.ui_panel_config.rect.left+15,
      self.ui_panel_config.rect.top+self.size_panel_config.height/2-10
    ))
    self.ui_slider_ksize.set_position(pygame.math.Vector2(
      self.ui_panel_config.rect.left+80,
      self.ui_panel_config.rect.top+self.size_panel_config.height/2-10
    ))

  def __hide_ui_params(self):
      self.ui_txt_ksize.set_position(pygame.math.Vector2(0,-100))
      self.ui_slider_ksize.set_position(pygame.math.Vector2(0,-100))

  def __apply_effect(self):
    self.image_apply = cv.erode(self.image_apply, self.kernel, iterations=1)
    
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
    self.param_dict["ksize"] = self.ksize[0]
    self.kernel = np.ones(self.ksize, np.uint8)
    self.ui_slider_ksize.set_current_value(self.ksize[0])
    self.ui_txt_ksize.set_text(f'ksize: {self.ksize[0]}')
    self.is_update_image = True
    self.set_image(self.image_raw)
    super().set_params()

  def update(self, delta_time: float) -> None:
    super().update(delta_time)
    if self.ui_panel_config.visible:
      self.__show_ui_params()
    else:
      self.__hide_ui_params()

  def events(self, event: pygame.event.Event) -> None:
    super().events(event)
    if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
      if event.ui_element == self.ui_slider_ksize:
          self.set_params(event.value)