from abc import ABC, abstractmethod
import numpy as np
import pygame
from scripts.interface.inode import INode

class INodeDetail(ABC):
  node_name: str
  node: INode
  image_raw: np.matrix
  image_apply: np.matrix
  size: pygame.Rect
  size_current: pygame.Rect
  position: pygame.math.Vector2
  scale_ratio: float

  color_bg: pygame.Color
  color_border: pygame.Color

  surf_container: pygame.Surface
  rect_container: pygame.Rect
  surf_image: pygame.Surface
  rect_image: pygame.Rect
  surf_image_container: pygame.Surface
  rect_image_container: pygame.Rect

  @abstractmethod
  def draw(self, surface: pygame.Surface) -> None:
    pass

  @abstractmethod
  def update(self, delta_time: float) -> None:
    pass

  @abstractmethod
  def events(self, event: pygame.event.Event) -> None:
    pass