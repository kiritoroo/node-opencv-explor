import pygame
import pygame_gui
import assets.assets as ats
import scripts.constants as cts
import scripts.colors as cls
import scripts.utils as uts
import scripts.stores as sts

class Node():
  def __init__(self, node_name, color_node) -> None:
    super().__init__()
    self.node_name = node_name
    self.color_node = color_node

    self._start()
    
  def __config_variables(self):
    self.scale_ratio = sts.scale_ratio

    self.position = pygame.math.Vector2(0, 0)

    self.default_size_node = pygame.Rect(0, 0, 180, 35)
    self.default_size_text = 12
    self.default_size_rounded = 8

    self.current_size_node = self.default_size_node.copy()
    self.current_size_text = int(self.default_size_text)
    self.current_size_rounded = int(self.default_size_rounded)

    self.font = pygame.font.Font(ats.FONT_POPPINS_REGULAR_PATH, self.current_size_text)
    self.color_node = self.color_node
    self.color_text = cls.NODE_TEXT_COLOR

  def __config_ui_elements(self) -> None:
    self.ui_manager = pygame_gui.UIManager((cts.SCREEN_WIDTH, cts.SCREEN_HEIGHT), ats.THEME_PATH)

    _rect = pygame.Rect(0, 0, 40, 20)
    self.ui_btn_config = pygame_gui.elements.UIButton(relative_rect=_rect,
              text='edit', manager=self.ui_manager,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_config", class_id="#btn"))

    _rect = pygame.Rect(0, 0, 30, 30)
    self.ui_btn_remove = pygame_gui.elements.UIButton(relative_rect=_rect,
              text='-', manager=self.ui_manager,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_remove", class_id="#btn"))

  def __config_ui_btn_config(self):
    _pos_x = self.rect_container.left+20
    _pos_y = self.rect_container.top-10
    self.ui_btn_config.set_position(pygame.math.Vector2(_pos_x, _pos_y))

  def __config_ui_btn_remove(self):
    _pos_x = self.rect_container.right-self.rect_container.width/4
    _pos_y = self.rect_container.centery-(30/2)
    self.ui_btn_remove.set_position(pygame.math.Vector2(_pos_x, _pos_y))

  def __config_rect_node(self):
    self.rect_node = pygame.Rect(
      self.position.x-self.current_size_node.width/2,
      self.position.y-self.current_size_node.height/2,
      self.current_size_node.width,
      self.current_size_node.height)
    
  def __config_text_node(self):
    self.surf_text_node = self.font.render(self.node_name, True, self.color_text)
    self.rect_text_node = self.surf_text_node.get_rect(center=(self.position.x, self.position.y))
    
  def __config_rect_container(self):
    self.rect_container = self.rect_node

  def _start(self):
    self.__config_variables()
    self.__config_ui_elements()
    self.__config_rect_node()
    self.__config_text_node()
    self.__config_rect_container()
    self.__config_ui_btn_config()
    self.__config_ui_btn_remove()

  def draw(self, surface: pygame.Surface) -> None:
    uts.draw_rect_rounded(surface, self.rect_node, self.color_node, self.current_size_rounded)
    surface.blit(self.surf_text_node, self.rect_text_node)
    self.ui_manager.draw_ui(surface)

  def update(self, delta_time: float) -> None:
    self.ui_manager.update(delta_time)

  def events(self, event: pygame.event.Event) -> None:
    self.ui_manager.process_events(event)
  
  def set_position(self, position: pygame.math.Vector2) -> None:
    self.position = position.copy()
    self.__config_rect_node()
    self.__config_text_node()
    self.__config_rect_container()
    self.__config_ui_btn_config()
    self.__config_ui_btn_remove()

  def set_scale_ratio(self, scale_ratio: float) -> None:
    self.scale_ratio = float(scale_ratio)
    self.current_size_node.width = self.default_size_node.width*self.scale_ratio
    self.current_size_node.height = self.default_size_node.height*self.scale_ratio
    self.current_size_text = int(self.default_size_text*self.scale_ratio)
    self.current_size_rounded = int(self.default_size_rounded*self.scale_ratio)
    self.font = pygame.font.Font(ats.FONT_POPPINS_REGULAR_PATH, self.current_size_text)
    self.__config_rect_node()
    self.__config_text_node()
    self.__config_rect_container()
    self.__config_ui_btn_config()
    self.__config_ui_btn_remove()

  def show_ui(self):
    if self.node_name != 'Original':
      self.ui_btn_config.visible = True
      self.ui_btn_remove.visible = True
  
  def hide_ui(self):
    self.ui_btn_config.visible = False
    self.ui_btn_remove.visible = False