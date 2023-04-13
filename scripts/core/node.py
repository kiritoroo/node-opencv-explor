import pygame
import assets.assets as ats
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
    self.__config_rect_node()
    self.__config_text_node()
    self.__config_rect_container()

  def draw(self, surface: pygame.Surface) -> None:
    uts.draw_rect_rounded(surface, self.rect_node, self.color_node, self.current_size_rounded)
    surface.blit(self.surf_text_node, self.rect_text_node)

  def update(self, delta_time: float) -> None:
    pass

  def events(self, event: pygame.event.Event) -> None:
    pass
  
  def set_position(self, position: pygame.math.Vector2) -> None:
    self.position = position.copy()
    self.__config_rect_node()
    self.__config_text_node()
    self.__config_rect_container()

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