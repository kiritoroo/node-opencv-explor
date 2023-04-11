import pygame
import json
from scripts.interface.isolution import ISolution
from scripts.structure.str_linked_list import LinkedList
from scripts.core.node_data import NodeData
from scripts.handle.hd_nodes import NodesHandle
from scripts.handle.hd_nodes_detail import NodesDetailHandle

class Solution(ISolution):
  def __init__(self, solution_path: str, solution_name: str) -> None:
    super().__init__()
    self.solution_path = solution_path
    self.solution_name = solution_name
    self.solution_dict = {}
    self.nodes_data = LinkedList()
    self.nodes_data_count = 0
    self.handle_nodes = None
    self.handle_nodes_detail = None

    self.start()

  def start(self):
    self.read_solution(self.solution_path)

  def draw(self, surface: pygame.Surface) -> None:
    pass

  def update(self, delta_time: float) -> None:
    pass

  def events(self, event: pygame.event.Event) -> None:
    pass

  def read_solution(self, solution_path) -> None:
    self.solution_path = solution_path
    with open(self.solution_path, 'r') as _file:
      self.solution_dict: dict = json.load(_file)
      for _, _node_info in self.solution_dict.items():
        self.nodes_data_count += 1
        _node_category = _node_info["category"]
        _node_type = _node_info["type"]
        _node_params = []
        for _, _param_value in _node_info["params"].items():
          _node_params.append(_param_value)
        _node_data = NodeData(_node_category, _node_type, _node_params)
        self.nodes_data.add_last(_node_data)

    self.handle_nodes = NodesHandle(self.nodes_data)
    self.handle_nodes_detail = NodesDetailHandle(self.nodes_data)
  
  def add_node_data(self) -> None:
    pass

  def remove_node_data(self) -> None:
    pass