import pygame
import numpy as np
import pygame_gui
import cv2 as cv
import scripts.stores as sts  
from scripts.core.node_detail import NodeDetail

class SPContours(NodeDetail):
  def __init__(self, color_bg: pygame.Color, image: np.matrix) -> None:
    self.node_name = "Contours"
    self.color_bg = color_bg
    self.size_panel_config = pygame.Rect(0, 0, 300, 120)

    self.param_top = 30

    self.param_dict = {
      "top": self.param_top
    }

    super().__init__(self.node_name, self.color_bg, image)
    self.image_draw = np.zeros((self.image_raw.shape[0], self.image_raw.shape[1], 3))
    self.__config_ui_elements()

  def __config_ui_elements(self) -> None:
    _rect = pygame.Rect(0, 0, 80, 20)
    self.ui_txt_param_1 = pygame_gui.elements.UIButton(relative_rect=_rect,
              text=f'top: {self.param_top}', tool_tip_text="Top các đường viền có diện tích lớn nhất",
              manager=self.ui_manager, container=self.ui_panel_config,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_param",class_id="#btn"))
    _rect = pygame.Rect(0, 0, 150, 20)
    self.ui_slider_param_1 = pygame_gui.elements.UIHorizontalSlider(relative_rect=_rect,
              manager=self.ui_manager, container=self.ui_panel_config,
              start_value=100, value_range=(0,255),
              object_id=pygame_gui.core.ObjectID(class_id="#slider"))
    
    _rect = pygame.Rect(0, 0, 80, 20)
    self.ui_txt_param_2 = pygame_gui.elements.UIButton(relative_rect=_rect,
              text='bg',tool_tip_text="Nền để vẽ các contours lên.",
              manager=self.ui_manager, container=self.ui_panel_config,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_param",class_id="#btn"))
    
    _rect = pygame.Rect(0, 0, 150, 25)
    _options = ['none', 'before', 'raw']
    self.ui_dropdown_param_2 = pygame_gui.elements.UIDropDownMenu(relative_rect = _rect,
              options_list = _options,
              starting_option = _options[0],
              manager = self.ui_manager,
              object_id=pygame_gui.core.ObjectID(class_id="#dropdown"))

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
    self.ui_dropdown_param_2.set_position(pygame.math.Vector2(
      self.ui_panel_config.rect.left+120,
      _param_first_pos_y+_param_padding_y
    ))

  def __hide_ui_params(self):
      self.ui_txt_param_1.set_position(pygame.math.Vector2(0,-100))
      self.ui_slider_param_1.set_position(pygame.math.Vector2(0,-100))
      self.ui_txt_param_2.set_position(pygame.math.Vector2(0,-100))
      self.ui_dropdown_param_2.set_position(pygame.math.Vector2(0,-100))

  def __apply_effect(self):
    if self.image_raw.ndim > 2:
      self.image_apply = cv.cvtColor(self.image_apply, cv.COLOR_RGB2GRAY)
      
    _binary = cv.threshold(self.image_apply, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
    _contours, _ = cv.findContours(_binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    _contours_sort = sorted(_contours, key = cv.contourArea, reverse = True)[:self.param_top]
    self.contours_cout = len(_contours)
    self.ui_slider_param_1.value_range = (0,self.contours_cout)
    self.image_apply = cv.drawContours(np.zeros((self.image_raw.shape[0], self.image_raw.shape[1], 3)), _contours_sort, -1, (0, 255, 0), 2).astype(np.uint8)

    self.image_display = cv.drawContours(self.image_draw, _contours_sort, -1, (0, 255, 0), 2)
      
  def set_image(self, image_cv: np.matrix) -> None:
    self.image_raw = image_cv.copy()
    self.image_apply = image_cv.copy()
    self.image_display = image_cv.copy()

    if self.ui_dropdown_param_2.selected_option == 'none':
      self.image_draw = np.zeros((self.image_raw.shape[0], self.image_raw.shape[1], 3))
    elif self.ui_dropdown_param_2.selected_option == 'before':
      if self.image_raw.ndim < 3:
        self.image_draw = cv.cvtColor(self.image_raw.copy(), cv.COLOR_GRAY2RGB)
      else:
        self.image_draw = self.image_raw.copy()
    elif self.ui_dropdown_param_2.selected_option == 'raw':
      self.image_draw = cv.resize(sts.image_cv.copy(), (self.image_raw.shape[1], self.image_raw.shape[0]), interpolation=cv.INTER_LINEAR)

    self.__apply_effect()
    super().set_image(image_cv)
  
  def set_params(self, top):
    self.param_top = top

    self.param_dict["top"] = self.param_top

    self.ui_txt_param_1.set_text(f'top: {self.param_top}')
    self.ui_slider_param_1.set_current_value(self.param_top)

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

    if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
      if event.ui_element == self.ui_dropdown_param_2:
        if event.text == 'none':
          self.image_draw = np.zeros((self.image_raw.shape[0], self.image_raw.shape[1], 3))
        elif event.text == 'before':
          if self.image_raw.ndim < 3:
            self.image_draw = cv.cvtColor(self.image_raw.copy(), cv.COLOR_GRAY2RGB)
          else:
            self.image_draw = self.image_raw.copy()
        elif event.text == 'raw':
          self.image_draw = cv.resize(sts.image_cv.copy(), (self.image_raw.shape[1], self.image_raw.shape[0]), interpolation=cv.INTER_LINEAR)
        self.set_params(self.param_top)

