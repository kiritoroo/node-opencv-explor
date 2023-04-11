import pygame
import json
from scripts.interface.isolution import ISolution
from scripts.structure.str_linked_list import LinkedList
from scripts.core.node_data import NodeData
from scripts.handle.hd_nodes import NodesHandle
from scripts.handle.hd_nodes_detail import NodesDetailHandle
from scripts.core.node import Node
from scripts.core.node_detail import NodeDetail
from scripts.core.node_data import NodeData
import assets.assets as ats
import scripts.colors as cls

class Solution(ISolution):
  def __init__(self, solution_name: str, solution_path: str) -> None:
    super().__init__()
    self.solution_name = solution_name
    self.solution_path = solution_path
    self.solution_dict = {}
    self.nodes_data = LinkedList()
    self.node_data_count = 0
    self.handle_nodes: NodesHandle = None
    self.handle_nodes_detail: NodesDetailHandle = None

    self.scale_ratio = 1
    self.position_nodes = pygame.math.Vector2(1600, 100)
    self.position_nodes_detail = pygame.math.Vector2(400, 100)
    self.text_size = 20
    self.font = pygame.font.Font(ats.FONT_POPPINS_MEDIUM_PATH, self.text_size)
    self.color_bg = cls.SOLUTION_BG_COLOR
    self.color_text = cls.SOLUTION_TEXT_COLOR

    self.start()

  def start(self):
    self.read_solution(self.solution_path)

  def draw(self, surface: pygame.Surface) -> None:
    self.handle_nodes.draw_all(surface)
    self.handle_nodes_detail.draw_all(surface)

  def update(self, delta_time: float) -> None:
    pass

  def events(self, event: pygame.event.Event) -> None:
    pass

  def read_solution(self, solution_path) -> None:
    self.solution_path = solution_path
    with open(self.solution_path, 'r') as _file:
      self.solution_dict: dict = json.load(_file)
      for _, _node_info in self.solution_dict.items():
        self.node_data_count += 1
        _node_category = _node_info["category"]
        _node_type = _node_info["type"]
        _node_name = _node_info["name"]
        _node_params = []
        for _, _param_value in _node_info["params"].items():
          _node_params.append(_param_value)
        _node_data = NodeData(_node_category, _node_type, _node_name, _node_params)
        self.nodes_data.add_last(_node_data)
    
    _list_node = self.get_nodes()
    _list_node_detail = self.get_nodes_detail() 
    self.handle_nodes = NodesHandle(_list_node)
    self.handle_nodes_detail = NodesDetailHandle(_list_node_detail)
    self.reset_position()

  def get_nodes(self) -> list[Node]:
    _list_node = list[Node]()
    for i in range(self.node_data_count):
      _node_data: NodeData = self.nodes_data.get(i)
      _node: Node = _node_data.node
      _list_node.append(_node)
    return _list_node

  def get_nodes_detail(self) -> list[NodeDetail]:
    _list_node_detail = list[Node]()
    for i in range(self.node_data_count):
      _node_data: NodeData = self.nodes_data.get(i)
      _node_detail: Node = _node_data.node_detail
      _list_node_detail.append(_node_detail)
    return _list_node_detail

  def add_node_data(self) -> None:
    pass

  def remove_node_data(self) -> None:
    pass

  def reset_position(self) -> None:
    self.handle_nodes.set_position(self.position_nodes)
    self.handle_nodes_detail.set_position(self.position_nodes_detail)