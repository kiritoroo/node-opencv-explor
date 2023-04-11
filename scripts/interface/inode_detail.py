from abc import ABC, abstractmethod
import numpy as np
import pygame
from scripts.interface.inode import INode

class INodeDetail(ABC):
  node_name: str
  image_raw: np.matrix
  image_apply: np.matrix
  image_display: np.matrix

  scale_ratio: float
  position: pygame.math.Vector2
  image_width: int
  image_height: int
  color_bg: pygame.Color
  color_bg_image: pygame.color
  color_border: pygame.Color
  border_thickness: int

  node: INode

  surf_image: pygame.Surface
  rect_image: pygame.Rect
  rect_image_container: pygame.Rect
  rect_container: pygame.Rect

  @abstractmethod
  def start(self):
    pass

  @abstractmethod
  def draw(self, surface: pygame.Surface) -> None:
    pass

  @abstractmethod
  def update(self, delta_time: float) -> None:
    pass

  @abstractmethod
  def events(self, event: pygame.event.Event) -> None:
    pass

  @abstractmethod
  def set_position(self, position: pygame.math.Vector2) -> None:
    pass
