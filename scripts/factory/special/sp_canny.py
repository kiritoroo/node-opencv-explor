import pygame
import pygame_gui
import cv2 as cv
import numpy as np
from scripts.core.node_detail import NodeDetail

class SPCanny(NodeDetail):
  def __init__(self, color_bg: pygame.Color, image: np.matrix) -> None:
    self.node_name = "Canny"
    self.color_bg = color_bg
    self.size_panel_config = pygame.Rect(0, 0, 300, 150)

    self.param_t_lower = 100
    self.param_t_upper = 200
    self.param_aperture_size = 5

    self.param_dict = {
      "t_lower": self.param_t_lower,
      "t_upper": self.param_t_upper,
      "aperture_size": self.param_aperture_size
    }

    super().__init__(self.node_name, self.color_bg, image)
    self.__config_ui_elements()

  def __config_ui_elements(self) -> None:
    _rect = pygame.Rect(0, 0, 80, 20)
    self.ui_txt_param_1 = pygame_gui.elements.UIButton(relative_rect=_rect,
              text=f'tlower: {self.param_t_lower}', tool_tip_text="Threshold Lower là giá trị độ gradient tối thiểu để một điểm ảnh được coi là biên cạnh. Các điểm ảnh có độ gradient nhỏ hơn ngưỡng dưới sẽ bị loại bỏ và không được coi là biên cạnh.",
              manager=self.ui_manager, container=self.ui_panel_config,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_param",class_id="#btn"))
    _rect = pygame.Rect(0, 0, 150, 20)
    self.ui_slider_param_1 = pygame_gui.elements.UIHorizontalSlider(relative_rect=_rect,
              manager=self.ui_manager, container=self.ui_panel_config,
              start_value=100, value_range=(0,255),
              object_id=pygame_gui.core.ObjectID(class_id="#slider"))
    
    _rect = pygame.Rect(0, 0, 80, 20)
    self.ui_txt_param_2 = pygame_gui.elements.UIButton(relative_rect=_rect,
              text=f'tupper: {self.param_t_upper}', tool_tip_text="Threshold Upper: Ngưỡng trên, là giá trị độ gradient tối thiểu để một điểm ảnh được coi là biên cạnh chắc chắn. Các điểm ảnh có độ gradient lớn hơn ngưỡng trên sẽ được coi là biên cạnh chắc chắn.",
              manager=self.ui_manager, container=self.ui_panel_config,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_param",class_id="#btn"))
    _rect = pygame.Rect(0, 0, 150, 20)
    self.ui_slider_param_2 = pygame_gui.elements.UIHorizontalSlider(relative_rect=_rect,
              manager=self.ui_manager, container=self.ui_panel_config,
              start_value=100, value_range=(0,255),
              object_id=pygame_gui.core.ObjectID(class_id="#slider"))
    
    _rect = pygame.Rect(0, 0, 80, 20)
    self.ui_txt_param_3 = pygame_gui.elements.UIButton(relative_rect=_rect,
              text=f'aperture: {self.param_aperture_size}', tool_tip_text="Aperture: Kích thước của kernel được sử dụng trong quá trình tính toán độ gradient của điểm ảnh. Kích thước này cần là một số lẻ và được sử dụng để xác định hướng của độ gradient của điểm ảnh.",
              manager=self.ui_manager, container=self.ui_panel_config,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_param",class_id="#btn"))
    _rect = pygame.Rect(0, 0, 150, 20)
    self.ui_slider_param_3 = pygame_gui.elements.UIHorizontalSlider(relative_rect=_rect,
              manager=self.ui_manager, container=self.ui_panel_config,
              start_value=3, value_range=(3,7),
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

    self.ui_txt_param_2.set_position(pygame.math.Vector2(
      self.ui_panel_config.rect.left+15,
      _param_first_pos_y+_param_padding_y
    ))
    self.ui_slider_param_2.set_position(pygame.math.Vector2(
      self.ui_panel_config.rect.left+120,
      _param_first_pos_y+_param_padding_y
    ))

    self.ui_txt_param_3.set_position(pygame.math.Vector2(
      self.ui_panel_config.rect.left+15,
      _param_first_pos_y+_param_padding_y*2
    ))
    self.ui_slider_param_3.set_position(pygame.math.Vector2(
      self.ui_panel_config.rect.left+120,
      _param_first_pos_y+_param_padding_y*2
    ))

  def __hide_ui_params(self):
      self.ui_txt_param_1.set_position(pygame.math.Vector2(0,-100))
      self.ui_slider_param_1.set_position(pygame.math.Vector2(0,-100))
      self.ui_txt_param_2.set_position(pygame.math.Vector2(0,-100))
      self.ui_slider_param_2.set_position(pygame.math.Vector2(0,-100))
      self.ui_txt_param_3.set_position(pygame.math.Vector2(0,-100))
      self.ui_slider_param_3.set_position(pygame.math.Vector2(0,-100))

  def __apply_effect(self):
    self.image_apply = cv.Canny(self.image_apply, self.param_t_lower, self.param_t_upper, apertureSize=self.param_aperture_size)
    
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

  def set_params(self, tlower, tupper, aperture):
    if aperture % 2 == 0:
      aperture += 1

    self.param_t_lower = tlower
    self.param_t_upper= tupper
    self.param_aperture_size = aperture

    self.param_dict["tlower"] = self.param_t_lower
    self.param_dict["tupper"] = self.param_t_upper
    self.param_dict["aperture"] = self.param_aperture_size

    self.ui_txt_param_1.set_text(f'tlower: {self.param_t_lower}')
    self.ui_slider_param_1.set_current_value(self.param_t_lower)
    self.ui_txt_param_2.set_text(f'tupper: {self.param_t_upper}')
    self.ui_slider_param_2.set_current_value(self.param_t_upper)
    self.ui_txt_param_3.set_text(f'aperture: {self.param_aperture_size}')
    self.ui_slider_param_3.set_current_value(self.param_aperture_size)

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
          self.set_params(event.value, self.param_t_upper, self.param_aperture_size)
      if event.ui_element == self.ui_slider_param_2:
          self.set_params(self.param_t_lower, event.value, self.param_aperture_size)
      if event.ui_element == self.ui_slider_param_3:
          self.set_params(self.param_t_lower, self.param_t_upper, event.value)
