from abc import ABC, abstractmethod
import pygame

class INode(ABC):
  node_name: str
  size: pygame.Rect
  position: pygame.math.Vector2
  scale_ratio: float

  font: pygame.font.Font
  color_bg: pygame.Color
  color_text: pygame.Color

  surf_container: pygame.Surface
  rect_container: pygame.Rect
  surf_node: pygame.Surface
  rect_node: pygame.Rect
  surf_text: pygame.Surface
  rect_text: pygame.Rect

  @abstractmethod
  def draw(self, surface: pygame.Surface) -> None:
    pass

  @abstractmethod
  def update(self, delta_time: float) -> None:
    pass

  @abstractmethod
  def events(self, event: pygame.event.Event) -> None:
    pass