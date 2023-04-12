from abc import ABC, abstractmethod
import pygame

class INode(ABC):
  node_name: str

  scale_ratio: float
  size_default: pygame.Rect
  size: pygame.Rect
  position: pygame.math.Vector2
  text_size: int
  font: pygame.font.Font
  color_bg: pygame.Color
  color_text: pygame.Color
  rounded_size: int

  surf_text: pygame.Surface
  rect_node: pygame.Rect
  rect_text: pygame.Rect
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

  @abstractmethod
  def set_scale_ratio(self, scale_ratio: float) -> None:
    pass
