import pygame
import numpy as np
from scripts.interface.inode_detail import INodeDetail
from scripts.core.node import Node
import scripts.utils as uts
import scripts.colors as cls

class NodeDetail(INodeDetail):
  def __init__(self, node_name: str, color_bg: pygame.Color, image: np.matrix) -> None:
    super().__init__()
    self.node_name = node_name
    self.image_raw = image.copy()
    self.image_apply = image.copy()
    self.image_display = image.copy()

    self.scale_ratio = 1  
    self.position = pygame.math.Vector2(0, 0)
    self.image_width = 300
    self.color_bg = color_bg
    self.color_bg_image = cls.NODE_DETAIL_BG_COLOR
    self.color_border = cls.NODE_DETAIL_BORDER_COLOR
    self.border_thickness = 2

    self.node: Node = Node(self.node_name, self.color_bg)

    self.surf_image = pygame.surfarray.make_surface(self.image_display).convert_alpha()
    _image_scale_ratio = self.image_width / self.surf_image.get_width()
    self.image_height = int(self.surf_image.get_height() * _image_scale_ratio)
    self.surf_image = pygame.transform.smoothscale(self.surf_image, (self.image_width, self.image_height))
    self.rect_image = self.surf_image.get_rect(center=self.position)

    _image_padding_horizontal = 50
    _image_padding_vertical = 20
    self.rect_image_container = pygame.Rect(
      self.rect_image.left-_image_padding_horizontal/2,
      self.rect_image.top-_image_padding_vertical/2,
      self.rect_image.width+_image_padding_horizontal,
      self.rect_image.height+_image_padding_vertical)
    
    self.rect_container = pygame.Rect(
      self.rect_image_container.left,
      self.node.rect_container.top,
      self.rect_image_container.width,
      self.rect_image_container.height + self.node.rect_container.height/2)

    self.start()

  def start(self):
    pass

  def draw(self, surface: pygame.Surface) -> None:
    uts.draw_rect_bordered_rounded(surface, self.rect_image_container, self.color_bg_image, self.color_border, 0, self.border_thickness)
    surface.blit(self.surf_image, self.rect_image)
    self.node.draw(surface)

  def update(self, delta_time: float) -> None:
    pass

  def events(self, event: pygame.event.Event) -> None:
    pass

  def set_position(self, position: pygame.math.Vector2) -> None:
    self.position = position

    self.node.set_position(self.position)

    self.rect_image = self.surf_image.get_rect(center=self.position)

    _image_padding_horizontal = 50
    _image_padding_vertical = 20
    self.rect_image_container = pygame.Rect(
      self.rect_image.left-_image_padding_horizontal/2,
      self.rect_image.top-_image_padding_vertical/2,
      self.rect_image.width+_image_padding_horizontal,
      self.rect_image.height+_image_padding_vertical)
    
    self.rect_container = pygame.Rect(
      self.rect_image_container.left,
      self.node.rect_container.top,
      self.rect_image_container.width,
      self.rect_image_container.height + self.node.rect_container.height/2)