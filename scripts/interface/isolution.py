from abc import ABC, abstractmethod
import pygame
from scripts.core.node_data import NodeData
from scripts.handle.hd_nodes import NodesHandle
from scripts.handle.hd_nodes_detail import NodesDetailHandle
from scripts.structure.str_linked_list import LinkedList

class ISolution(ABC):
  file_path: str
  nodes_data: LinkedList
  handle_nodes: NodesHandle
  handle_nodes_detail: NodesDetailHandle

  font: pygame.font.Font
  color_bg: pygame.Color
  color_text: pygame.Color

  surf_container: pygame.Surface
  rect_container: pygame.Rect
  surf_solution: pygame.Surface
  rect_solution: pygame.Rect
  surf_text: pygame.Surface
  rect_text: pygame.Rect

  def __init__(self, file_path) -> None:
    self.file_path = file_path

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
  def read_solution() -> None:
    pass

  @abstractmethod
  def add_node_data() -> None:
    pass

  @abstractmethod
  def remove_node_data() -> None:
    pass