import pygame
import pygame_gui
import json
import assets.assets as ats
import scripts.constants as cts

class ComponentNodesFilteringe:
  def __init__(self, ui_manager: pygame_gui.UIManager) -> None:
    self.ui_manager = ui_manager
    self._start()

  def __config_variables(self) -> None:
    self.nodes_filtering_info_path = ats.NODES_FILTERING_INFO_PATH
    self.size_btn_node = pygame.Rect(0, 0, 180, 40)

    with open(self.nodes_filtering_info_path, 'r', encoding='utf-8') as _file:
      self.nodes_filtering_info_dict: dict = json.load(_file)

      self.nodes_info_list = [
        {"category": v["category"],
        "type": v["type"],
        "name": v["name"],
        "tooltip": v["tooltip"],
        "params": v["params"]}
        for v in self.nodes_filtering_info_dict.values()]
      
      self.nodes_info_count = len(self.nodes_info_list)

  def __config_ui_elements(self) -> None:
    _rect = pygame.Rect(0, 0, 800, 400)
    _rect.center = pygame.math.Vector2(cts.SCREEN_WIDTH//2, cts.SCREEN_HEIGHT//2)
    self.ui_panel_container = pygame_gui.elements.UIPanel(relative_rect=_rect,
              manager=self.ui_manager,
              object_id=pygame_gui.core.ObjectID(class_id="#panel"))
    self.ui_panel_container.visible = False
    
    self.ui_btn_node_list = list[pygame_gui.elements.UIButton]()
    _rect = pygame.Rect(0, 0, self.size_btn_node.width, self.size_btn_node.height)
    for i in range(self.nodes_info_count):
      _ui_btn_node_base = pygame_gui.elements.UIButton(relative_rect=_rect,
              text=f'{self.nodes_info_list[i].get("name")}', tool_tip_text=f'{self.nodes_info_list[i].get("tooltip")}',
              manager=self.ui_manager, container=self.ui_panel_container,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_node_filtering", class_id="#btn"))
      self.ui_btn_node_list.append(_ui_btn_node_base)

  def __config_ui_btn_node_base_list(self):
    _start_pos_x = self.ui_panel_container.rect.left+70
    _start_pos_y = self.ui_panel_container.rect.top+50
    for i in range(len(self.ui_btn_node_list)):
      _pos_x = _start_pos_x + (i%3)*(self.ui_btn_node_list[i].rect.width+70)
      _pos_y = _start_pos_y + (i//3)*(self.ui_btn_node_list[i].rect.height+30)
      self.ui_btn_node_list[i].set_position(pygame.math.Vector2(_pos_x, _pos_y))
    
  def _start(self):
    self.__config_variables()
    self.__config_ui_elements()
    self.__config_ui_btn_node_base_list()

  def show(self):
    for i in range(self.nodes_info_count):
      self.ui_btn_node_list[i].visible = True

  def hide(self):
    for i in range(self.nodes_info_count):
      self.ui_btn_node_list[i].visible = False