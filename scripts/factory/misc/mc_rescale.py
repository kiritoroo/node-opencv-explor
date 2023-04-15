import pygame
import pygame_gui
import cv2 as cv
import numpy as np
from scripts.core.node_detail import NodeDetail

class MCRescale(NodeDetail):
  def __init__(self, color_bg: pygame.Color, image: np.matrix) -> None:
    self.node_name = "Rescale"
    self.color_bg = color_bg
    self.size_panel_config = pygame.Rect(0, 0, 300, 50)

    self.param_w = 100

    self.param_dict = {
      "w": self.param_w
    }

    self.param_dict = {
      "w": self.param_w,
    }

    super().__init__(self.node_name, self.color_bg, image)
    self.param_w = self.image_raw.shape[0]
    self.__config_ui_elements()

  def __config_ui_elements(self) -> None:
    _rect = pygame.Rect(0, 0, 80, 20)
    self.ui_txt_param_1 = pygame_gui.elements.UIButton(relative_rect=_rect,
              text=f'w: {self.param_w}', tool_tip_text="Chiều rộng (pixel)",
              manager=self.ui_manager, container=self.ui_panel_config,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_param",class_id="#btn"))
    _rect = pygame.Rect(0, 0, 150, 20)
    self.ui_slider_param_1 = pygame_gui.elements.UIHorizontalSlider(relative_rect=_rect,
              manager=self.ui_manager, container=self.ui_panel_config,
              start_value=self.param_w, value_range=(100,1200),
              object_id=pygame_gui.core.ObjectID(class_id="#slider"))
    
  def __show_ui_params(self):
    _param_first_pos_y = self.ui_panel_config.rect.top+20
    _param_padding_y = 40
    self.ui_txt_param_1.set_position(pygame.math.Vector2(
      self.ui_panel_config.rect.left+15,
      _param_first_pos_y
    ))
    self.ui_slider_param_1.set_position(pygame.math.Vector2(
      self.ui_panel_config.rect.left+120,
      _param_first_pos_y
    ))

  def __hide_ui_params(self):
      self.ui_txt_param_1.set_position(pygame.math.Vector2(0,-100))
      self.ui_slider_param_1.set_position(pygame.math.Vector2(0,-100))

  def __apply_effect(self):
    _img_width = self.param_w
    _image_scale_ratio = _img_width / self.image_raw.shape[0]
    _image_height =  int(self.image_raw.shape[1] * _image_scale_ratio)
    self.image_apply = cv.resize(self.image_raw.copy(), (_image_height, _img_width), interpolation=cv.INTER_LINEAR)

    self.image_display = self.image_apply.copy()

  def set_image(self, image_cv: np.matrix) -> None:
    self.image_raw = image_cv.copy()
    self.image_apply = image_cv.copy()
    self.image_display = image_cv.copy()
    self.__apply_effect()
    super().set_image(image_cv)

  def set_params(self, w):
    self.param_w = w
    self.param_dict["w"] = self.param_w

    self.ui_txt_param_1.set_text(f'w: {self.param_w}')
    self.ui_slider_param_1.set_current_value(self.param_w)

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
      if event.ui_element == self.ui_slider_param_1:
          self.set_params(event.value)