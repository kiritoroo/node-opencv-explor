import pygame
from scripts.interface.inode import INode
import assets.assets as ats
import scripts.colors as cls
import scripts.utils as uts

class Node(INode):
  def __init__(self, node_name, color_bg) -> None:
    super().__init__()
    self.node_name = node_name

    self.scale_ratio = 1
    self.size = pygame.Rect(0, 0, 200, 40)
    self.position = pygame.math.Vector2(0, 0)
    self.text_size = 12
    self.font = pygame.font.Font(ats.FONT_POPPINS_REGULAR_PATH, self.text_size)
    self.color_bg = color_bg
    self.color_text = cls.NODE_TEXT_COLOR

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
    uts.draw_rect_rounded(surface, self.rect_node, self.color_bg, 8)
    surface.blit(self.surf_text, self.rect_text)

  def update(self, delta_time: float) -> None:
    pass

  def events(self, event: pygame.event.Event) -> None:
    pass
  
  def set_position(self, position: pygame.math.Vector2) -> None:
    self.position = position

    self.rect_node.left = self.position.x-self.size.width/2 
    self.rect_node.top = self.position.y-self.size.height/2
    self.rect_text = self.surf_text.get_rect(center=(self.position.x, self.position.y))
    self.rect_container = self.rect_node
