from abc import ABC, abstractmethod
import pygame
from scripts.core.node_data import NodeData
from scripts.handle.hd_nodes import NodesHandle
from scripts.handle.hd_nodes_detail import NodesDetailHandle
from scripts.structure.str_linked_list import LinkedList
from scripts.core.node import Node
from scripts.core.node_detail import NodeDetail

class ISolution(ABC):
  solution_name: str
  solution_path: str
  solution_dict: dict
  nodes_data: LinkedList
  node_data_count: int
  handle_nodes: NodesHandle
  handle_nodes_detail: NodesDetailHandle

  scale_ratio: float
  position_nodes: pygame.math.Vector2
  position_nodes_detail: pygame.math.Vector2 
  text_size: int
  font: pygame.font.Font
  color_bg: pygame.Color
  color_text: pygame.Color

  surf_solution_node: pygame.Surface
  surf_solution_node_detail: pygame.Surface
  surf_text: pygame.Surface
  rect_solution_node: pygame.Rect
  rect_solution_node_detail: pygame.Rect
  rect_text: pygame.Rect
  rect_container_node: pygame.Rect
  rect_container_node_detail: pygame.Rect

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
  def read_solution(self, solution_path: str) -> None:
    pass

  @abstractmethod
  def get_nodes(self) -> list[Node]:
    pass

  @abstractmethod
  def get_nodes_detail(self) -> list[NodeDetail]:
    pass

  @abstractmethod
  def add_node_data(self) -> None:
    pass

  @abstractmethod
  def remove_node_data(self) -> None:
    pass
  
  @abstractmethod
  def reset_position(self) -> None:
    pass