from abc import abstractmethod
import pygame
import pygame_gui
import numpy as np
import assets.assets as ats
import scripts.utils as uts
import scripts.constants as cts
import scripts.colors as cls
import scripts.stores as sts
from scripts.core.node import Node

class NodeDetail():
  def __init__(self, node_name: str, color_node: pygame.Color, image: np.matrix) -> None:
    self.node_name = node_name
    self.color_node = color_node
    self.node: Node = Node(self.node_name, self.color_node)
    self.param_dict = {}

    self.image_raw = image.copy()
    self.image_apply = image.copy()
    self.image_display = image.copy()

    self._start()

  def __config_variables(self):
    self.scale_ratio = sts.scale_ratio
    self.position = pygame.math.Vector2(0, 0)
    self.default_image_width = 250
    self.image_width = int(self.default_image_width)
    self.is_show_ui = False
    self.is_update_image = False

    self.default_size_border = 1
    self.default_padding_container_image_horizontal = 50
    self.default_padding_container_image_vertical = 20

    self.current_size_border = int(self.default_size_border)
    self.current_padding_container_image_horizontal = float(self.default_padding_container_image_horizontal)
    self.current_padding_container_image_vertical = float(self.default_padding_container_image_vertical)

    self.color_node = self.color_node
    self.color_bg_image = cls.NODE_DETAIL_BG_COLOR
    self.color_border = cls.NODE_DETAIL_BORDER_COLOR

  def __config_ui_elements(self) -> None:
    self.ui_manager = pygame_gui.UIManager((cts.SCREEN_WIDTH, cts.SCREEN_HEIGHT), ats.THEME_PATH)

    _rect = pygame.Rect(0, 0, self.size_panel_config.width, self.size_panel_config.height)
    _rect.center = self.rect_container.center
    self.ui_panel_config = pygame_gui.elements.UIPanel(relative_rect=_rect,
              manager=self.ui_manager,
              object_id=pygame_gui.core.ObjectID(class_id="#panel"))
    self.ui_panel_config.visible = False
  
  def __config_ui_panel_config(self):
    _pos_x = self.rect_container.centerx-self.size_panel_config.width/2
    _pos_y = self.rect_image_container.centery-self.size_panel_config.height/3
    self.ui_panel_config.set_position(pygame.math.Vector2(_pos_x, _pos_y))

  def __config_surf_image(self):
    self.surf_image_default = pygame.surfarray.make_surface(self.image_display).convert_alpha()
    self.surf_image = self.surf_image_default.copy()

  def __config_rect_image(self):
    _image_scale_ratio = self.image_width / self.surf_image_default.get_width()
    self.image_height = int(self.surf_image_default.get_height() * _image_scale_ratio)
    self.surf_image = pygame.transform.smoothscale(self.surf_image_default, (self.image_width, self.image_height))
    self.rect_image = self.surf_image.get_rect(center=self.position)

  def __config_rect_container_image(self):
    _left = self.rect_image.left-self.current_padding_container_image_horizontal/2
    _top = self.rect_image.top-self.current_padding_container_image_vertical/2
    _width = self.rect_image.width+self.current_padding_container_image_horizontal
    _height = self.rect_image.height+self.current_padding_container_image_vertical
    self.rect_image_container = pygame.Rect(_left, _top, _width, _height)
  
  def __config_node(self):
    _node_position = pygame.math.Vector2(
      self.position.x,
      self.position.y-(self.rect_image_container.height/2))
    self.node.set_position(_node_position)
    self.node.set_scale_ratio(self.scale_ratio)

  def __config_rect_container(self):
    _left = self.rect_image_container.left
    _top = self.node.rect_container.top
    _width = self.rect_image_container.width
    _height = self.rect_image_container.height + self.node.rect_container.height/2
    self.rect_container = pygame.Rect(_left, _top, _width, _height)

  def __config_rect_area_bounding_box(self):
    _left = self.rect_image_container.left
    _top = self.node.rect_container.top-50/2
    _width = self.rect_image_container.width
    _height = self.rect_image_container.height + self.node.rect_container.height/2 + 50
    self.rect_area_bounding_box = pygame.Rect(_left, _top, _width, _height)

  def _start(self):
    self.__config_variables()
    self.__config_surf_image()
    self.__config_rect_image()
    self.__config_rect_container_image()
    self.__config_node()
    self.__config_rect_container()
    self.__config_rect_area_bounding_box()
    self.__config_ui_elements()
    self.__config_ui_panel_config()

  def draw(self, surface: pygame.Surface) -> None:
    uts.draw_rect_bordered_rounded(surface, self.rect_image_container, self.color_bg_image, self.color_border, 0, self.current_size_border)
    surface.blit(self.surf_image, self.rect_image)
    self.node.draw(surface)
    self.ui_manager.draw_ui(surface)

  def update(self, delta_time: float) -> None:
    self.node.update(delta_time)
    self.ui_manager.update(delta_time)

    _mouse_pos = pygame.mouse.get_pos()
    if self.rect_area_bounding_box.collidepoint(_mouse_pos):
      self.is_show_ui = True
      self.node.show_ui()
    else:
      self.is_show_ui = False
      self.node.hide_ui()
      if self.ui_panel_config.visible:
        self.ui_panel_config.visible = False

  def events(self, event: pygame.event.Event) -> None:
    self.ui_manager.process_events(event)
    self.node.events(event)

    if event.type == pygame_gui.UI_BUTTON_PRESSED:
      if event.ui_element == self.node.ui_btn_config:
        self.ui_panel_config.visible = True
        return

  def set_position(self, position: pygame.math.Vector2) -> None:
    self.position = position.copy()
    self.__config_rect_image()
    self.__config_rect_container_image()
    self.__config_node()
    self.__config_rect_container()
    self.__config_rect_area_bounding_box()
    self.__config_ui_panel_config()

  def set_scale_ratio(self, scale_ratio: float) -> None:
    self.scale_ratio = float(scale_ratio)
    self.image_width = int(self.default_image_width*self.scale_ratio)
    self.current_size_border = int(self.default_size_border*self.scale_ratio) if int(self.default_size_border*self.scale_ratio) > 0 else 1
    self.current_padding_container_image_horizontal = float(self.default_padding_container_image_horizontal*self.scale_ratio)
    self.current_padding_container_image_vertical = float(self.default_padding_container_image_vertical*self.scale_ratio)
    self.__config_rect_image()
    self.__config_rect_container_image()
    self.__config_node()
    self.__config_rect_container()
    self.__config_rect_area_bounding_box()
    self.__config_ui_panel_config()

  def set_image(self, image_cv: np.matrix) -> None:
    self.__config_surf_image()
    self.__config_rect_image()

  def set_params(self, *args, **kwargs):
    pass