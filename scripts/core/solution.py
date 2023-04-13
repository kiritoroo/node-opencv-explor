import pygame
import json
import assets.assets as ats
import scripts.colors as cls
import scripts.stores as sts
import scripts.utils as uts
from scripts.structure.str_linked_list import LinkedList
from scripts.core.node_data import NodeData
from scripts.core.node import Node
from scripts.core.node_detail import NodeDetail
from scripts.core.node_data import NodeData
from scripts.handle.hd_nodes import NodesHandle
from scripts.handle.hd_nodes_detail import NodesDetailHandle

class Solution():
  def __init__(self, solution_name: str, solution_path: str) -> None:
    super().__init__()
    self.solution_name = solution_name
    self.solution_path = solution_path
    self.solution_dict = {}
    self.nodes_data = LinkedList()
    self.node_data_count = 0
    self.handle_nodes: NodesHandle = None
    self.handle_nodes_detail: NodesDetailHandle = None

    self._start()

  def __config_variables(self):
    self.scale_ratio = sts.scale_ratio

    self.position_nodes = pygame.math.Vector2(1600, 100)
    self.position_nodes_detail = pygame.math.Vector2(0, 0)

    self.default_size_text= 15
    self.default_size_label_node_detail = pygame.Rect(0,0,180,40)
    self.default_size_rounded_container = 10
    self.default_size_rounded_label  = 10
    self.default_padding_container_horizontal = 100
    self.default_padding_container_vertical = 50

    self.current_size_text = int(self.default_size_text)
    self.current_size_label_node_detail = self.default_size_label_node_detail.copy()
    self.current_size_rounded_container = int(self.default_size_rounded_container)
    self.current_size_rounded_label= int(self.default_size_rounded_label)
    self.current_padding_container_horizontal= float(self.default_padding_container_horizontal)
    self.current_padding_container_vertical= float(self.default_padding_container_vertical)
    
    self.font = pygame.font.Font(ats.FONT_POPPINS_MEDIUM_PATH, self.current_size_text)
    self.color_bg = cls.SOLUTION_BG_COLOR
    self.color_text = cls.SOLUTION_TEXT_COLOR
    self.color_arrow = cls.ARROW_COLOR
    self.color_bg_label_node_detail = cls.SOLUTION_LABEL_COLOR

  def __config_rect_container_node_detail(self):
    _left = self.handle_nodes_detail.list_node_detail[0].rect_container.left-self.current_padding_container_horizontal/2
    _top = self.handle_nodes_detail.list_node_detail[0].rect_container.top-self.current_padding_container_vertical/1.5
    _width = self.handle_nodes_detail.list_node_detail[self.handle_nodes_detail.node_detail_cout-1].rect_container.right-_left+self.current_padding_container_horizontal/2
    _height = self.handle_nodes_detail.list_node_detail[self.handle_nodes_detail.node_detail_cout-1].rect_container.bottom-_top+self.current_padding_container_vertical/2
    self.rect_container_node_detail = pygame.Rect(_left, _top, _width, _height)

  def __config_rect_label_node_detail(self):
    _left = self.rect_container_node_detail.left+self.current_size_label_node_detail.width/4
    _top = self.rect_container_node_detail.top-(self.current_size_label_node_detail.height/2)
    _width = self.current_size_label_node_detail.width
    _height = self.current_size_label_node_detail.height
    self.rect_label_node_detail = pygame.Rect(_left, _top, _width, _height)

  def __config_text_label_node_detail(self):
    self.surf_text_label_node_detail=self.font.render(self.solution_name, True, cls.SOLUTION_LABEL_TEXT_COLOR)
    self.rect_text_label_node_detail=self.surf_text_label_node_detail.get_rect(center=(self.rect_label_node_detail.center))

  def _start(self):
    self.read_solution(self.solution_path)
    self.__config_variables()
    self.__config_rect_container_node_detail()
    self.__config_rect_label_node_detail()
    self.__config_text_label_node_detail()
    self._reset_scale_ratio()

  def draw(self, surface: pygame.Surface) -> None:
    uts.draw_rect_rounded(surface, self.rect_container_node_detail, self.color_bg, self.current_size_rounded_container)
    self.handle_nodes_detail.draw_all(surface)
    self.handle_nodes.draw_all(surface)
    uts.draw_rect_rounded(surface, self.rect_label_node_detail, self.color_bg_label_node_detail, self.current_size_rounded_label)
    surface.blit(self.surf_text_label_node_detail, self.rect_text_label_node_detail)

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
    
    _list_node = self._get_nodes()
    _list_node_detail = self._get_nodes_detail() 
    self.handle_nodes = NodesHandle(_list_node)
    self.handle_nodes_detail = NodesDetailHandle(_list_node_detail)
        
  def _get_nodes(self) -> list[Node]:
    _list_node = list[Node]()
    for i in range(self.node_data_count):
      _node_data: NodeData = self.nodes_data.get(i)
      _node: Node = _node_data.node
      _list_node.append(_node)
    return _list_node

  def _get_nodes_detail(self) -> list[NodeDetail]:
    _list_node_detail = list[Node]()
    for i in range(self.node_data_count):
      _node_data: NodeData = self.nodes_data.get(i)
      _node_detail: NodeDetail = _node_data.node_detail
      _list_node_detail.append(_node_detail)
    return _list_node_detail

  def add_node_data(self) -> None:
    pass

  def remove_node_data(self) -> None:
    pass

  def _reset_position(self) -> None:
    self.handle_nodes.set_position(self.position_nodes.copy())
    self.handle_nodes_detail.set_position(self.position_nodes_detail.copy())

  def _reset_scale_ratio(self) -> None:
    self.handle_nodes_detail.set_scale_ratio(self.scale_ratio)

  def set_position_nodes_detail(self, position: pygame.math.Vector2) -> None:
    self.position_nodes_detail = position.copy()
    self._reset_position()
    self.__config_rect_container_node_detail()
    self.__config_rect_label_node_detail()
    self.__config_text_label_node_detail()

  def set_scale_ratio(self, scale_ratio: float) -> None:
    self.scale_ratio = float(scale_ratio)
    self.current_size_text = int(self.default_size_text*self.scale_ratio)
    self.current_size_label_node_detail.width = self.default_size_label_node_detail.width*self.scale_ratio
    self.current_size_label_node_detail.height = self.default_size_label_node_detail.height*self.scale_ratio
    self.current_size_rounded_container = int(self.default_size_rounded_container*self.scale_ratio)
    self.current_size_rounded_label = int(self.default_size_rounded_label*self.scale_ratio)
    self.current_padding_container_horizontal= float(self.default_padding_container_horizontal)
    self.current_padding_container_vertical= float(self.default_padding_container_vertical*self.scale_ratio)
    self.font = pygame.font.Font(ats.FONT_POPPINS_MEDIUM_PATH, self.current_size_text)
    self._reset_scale_ratio()
    self._reset_position()
    self.__config_rect_container_node_detail()
    self.__config_rect_label_node_detail()
    self.__config_text_label_node_detail()
