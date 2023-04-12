import pygame
from scripts.interface.inode import INode
import assets.assets as ats
import scripts.colors as cls
import scripts.utils as uts
import scripts.stores as sts

class Node(INode):
  def __init__(self, node_name, color_bg) -> None:
    super().__init__()
    self.node_name = node_name

    self.scale_ratio = sts.scale_ratio
    self.size_default = pygame.Rect(0, 0, 180, 35)
    self.size = self.size_default.copy()
    self.position = pygame.math.Vector2(0, 0)
    self.text_size = 12
    self.font = pygame.font.Font(ats.FONT_POPPINS_REGULAR_PATH, self.text_size)
    self.color_bg = color_bg
    self.color_text = cls.NODE_TEXT_COLOR
    self.rounded_size = 8

    self.surf_text = self.font.render(self.node_name, True, self.color_text)
    self.rect_node = pygame.Rect(
      self.position.x-self.size.width/2,
      self.position.y-self.size.height/2,
      self.size.width,
      self.size.height)
    self.rect_text = self.surf_text.get_rect(center=(self.position.x, self.position.y))
    self.rect_container = self.rect_node

    self.start()
    
  def start(self):
    pass

  def draw(self, surface: pygame.Surface) -> None:
    uts.draw_rect_rounded(surface, self.rect_node, self.color_bg, self.rounded_size)
    surface.blit(self.surf_text, self.rect_text)

  def update(self, delta_time: float) -> None:
    pass

  def events(self, event: pygame.event.Event) -> None:
    pass
  
  def set_position(self, position: pygame.math.Vector2) -> None:
    self.position = position.copy()

    self.rect_node.left = self.position.x-self.size.width/2 
    self.rect_node.top = self.position.y-self.size.height/2
    self.rect_text = self.surf_text.get_rect(center=(self.position.x, self.position.y))
    self.rect_container = self.rect_node

  def set_scale_ratio(self, scale_ratio: float) -> None:
    self.scale_ratio = scale_ratio
    self.size.width = self.size_default.width*self.scale_ratio
    self.size.height = self.size_default.height*self.scale_ratio
    
    self.rounded_size = int(self.rounded_size*self.scale_ratio)
    self.rect_node.left = self.position.x-self.size.width/2
    self.rect_node.top = self.position.y-self.size.height/2
    self.rect_node.width =  self.size.width
    self.rect_node.height =  self.size.height
    self.rect_text = self.surf_text.get_rect(center=(self.position.x, self.position.y))
    self.rect_container = self.rect_node