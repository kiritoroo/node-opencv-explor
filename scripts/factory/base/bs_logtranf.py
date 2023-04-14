import pygame
import pygame_gui
import numpy as np
import cv2 as cv
from scripts.core.node_detail import NodeDetail

class BSLogTranf(NodeDetail):
  def __init__(self, color_bg: pygame.Color, image: np.matrix) -> None:
    self.node_name = "Log Transform"
    self.color_bg = color_bg
    self.size_panel_config = pygame.Rect(0, 0, 250, 50)
    self.c = 5
    self.param_dict = {
      "c": self.c
    }
    super().__init__(self.node_name, self.color_bg, image)
    self.__config_ui_elements()

  def __config_ui_elements(self):
    _rect = pygame.Rect(0, 0, 50, 20)
    self.ui_txt_c = pygame_gui.elements.UIButton(relative_rect=_rect,
              text=f'c: {self.c}', tool_tip_text="c là một hằng...",
              manager=self.ui_manager, container=self.ui_panel_config,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_param",class_id="#btn"))
    
    _rect = pygame.Rect(0, 0, 150, 20)
    self.ui_slider_c = pygame_gui.elements.UIHorizontalSlider(relative_rect=_rect,
              manager=self.ui_manager, container=self.ui_panel_config,
              start_value=1, value_range=(3,101),
              object_id=pygame_gui.core.ObjectID(class_id="#slider"))

  def __show_ui_params(self):
    self.ui_txt_c.set_position(pygame.math.Vector2(
      self.ui_panel_config.rect.left+15,
      self.ui_panel_config.rect.top+self.size_panel_config.height/2-10
    ))
    self.ui_slider_c.set_position(pygame.math.Vector2(
      self.ui_panel_config.rect.left+80,
      self.ui_panel_config.rect.top+self.size_panel_config.height/2-10
    ))

  def __hide_ui_params(self):
      self.ui_txt_c.set_position(pygame.math.Vector2(0,-100))
      self.ui_slider_c.set_position(pygame.math.Vector2(0,-100))

  def __apply_effect(self):
    if 0 in self.image_apply:
      self.image_apply[self.image_apply == 0] = 1

    _log_image = self.c * (np.log(self.image_apply + 1))
    self.image_apply = np.array(_log_image, dtype = np.uint8)
    
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
  
  def set_params(self, c):
    self.c = c
    self.param_dict["c"] = self.c
    self.ui_slider_c.set_current_value(self.c)
    self.ui_txt_c.set_text(f'c: {self.c}')
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
      if event.ui_element == self.ui_slider_c:
          self.set_params(event.value)
