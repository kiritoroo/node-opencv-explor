import pygame
import pygame_gui
import assets.assets as ats
import scripts.constants as cts
import scripts.colors as cls
from scripts.frame.components.comp_nodes_base import ComponentNodesBase
from scripts.frame.components.comp_nodes_filterring import ComponentNodesFilteringe

class ComponentNodeStore:
  def __init__(self, solution) -> None:
    self.solution = solution

    self._start()

  def __config_variables(self) -> None:
    self.is_show = False
    self.size_text = 15
    self.font = pygame.font.Font(ats.FONT_POPPINS_MEDIUM_PATH, self.size_text)

    self.size_btn_category = pygame.Rect(0, 0, 130, 35)
    self.category_count = 5
    self.category_name = ["Base", "Filtering", "Morphology", "Special", "Misc"]

  def __config_ui_elements(self) -> None:
    self.ui_manager = pygame_gui.UIManager((cts.SCREEN_WIDTH, cts.SCREEN_HEIGHT), ats.THEME_PATH)

    self.comp_nodes_base = ComponentNodesBase(self.ui_manager)
    self.comp_nodes_filtering = ComponentNodesFilteringe(self.ui_manager)
    self.comp_nodes_list = [self.comp_nodes_base, self.comp_nodes_filtering]
    self.selected_category_index = 0
    self.selected_comp_node = self.comp_nodes_list[self.selected_category_index]

    self.ui_btn_category_list = list[pygame_gui.elements.UIButton]()
    _rect = pygame.Rect(0, 0, self.size_btn_category.width, self.size_btn_category.height)
    for i in range(self.category_count):
      _ui_btn_category = pygame_gui.elements.UIButton(relative_rect=_rect,
              text=f'{self.category_name[i]}',
              manager=self.ui_manager,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_category", class_id="#btn"))
      self.ui_btn_category_list.append(_ui_btn_category)

    _rect = pygame.Rect(0, 0, 25, 25)
    self.ui_btn_close_panel = pygame_gui.elements.UIButton(relative_rect=_rect,
              text='x', manager=self.ui_manager,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_close_panel", class_id="#btn"))

    _rect = pygame.Rect(0, 0, 800, 400)
    _rect.center = pygame.math.Vector2(cts.SCREEN_WIDTH//2, cts.SCREEN_HEIGHT//2)
    self.ui_panel_container = pygame_gui.elements.UIPanel(relative_rect=_rect,
              manager=self.ui_manager,
              object_id=pygame_gui.core.ObjectID(class_id="#panel"))
  
  def __config_ui_btn_close_panel(self):
    _pos_x = self.ui_panel_container.rect.right-38
    _pos_y = self.ui_panel_container.rect.top-22
    self.ui_btn_close_panel.set_position(pygame.math.Vector2(_pos_x, _pos_y))

  def __config_ui_btn_category_list(self):
    _pos_x = self.ui_panel_container.rect.left+50
    _pos_y = self.ui_panel_container.rect.top-30
    for i in range(len(self.ui_btn_category_list)):
      self.ui_btn_category_list[i].set_position(pygame.math.Vector2(_pos_x, _pos_y))
      _pos_x += self.ui_btn_category_list[i].rect.width+10

  def _start(self) -> None:
    self.__config_variables()
    self.__config_ui_elements()
    self.__config_ui_btn_close_panel()
    self.__config_ui_btn_category_list()
    self._select_category_handle()
  
  def draw(self, surface: pygame.Surface) -> None:
    if self.is_show:
      self.ui_manager.draw_ui(surface)

  def update(self, delta_time: float) -> None:
    self.ui_manager.update(delta_time)

  def events(self, event: pygame.event.Event) -> None:
    self.ui_manager.process_events(event)
    if not self.is_show:
      return
    
    if event.type == pygame_gui.UI_BUTTON_PRESSED:
      if event.ui_element == self.ui_btn_close_panel:
        self.is_show = False
          
      for i, _btn_category in enumerate(self.ui_btn_category_list):
        if event.ui_element == _btn_category:
          self.selected_category_index = i
          self._select_category_handle()
          return

      for i, _btn_node in enumerate(self.selected_comp_node.ui_btn_node_list):
        if event.ui_element == _btn_node:
          self.add_node_handle(self.selected_comp_node.nodes_info_list[i])
          self.hide()
          return

  def _select_category_handle(self):
    self._hide_all_comp_nodes()
    self.selected_comp_node = self.comp_nodes_list[self.selected_category_index]
    self.selected_comp_node.show()

  def _hide_all_comp_nodes(self):
    for i in range(len(self.comp_nodes_list)):
      self.comp_nodes_list[i].hide()

  def show(self):
    self._hide_all_comp_nodes()
    self.is_show = True
    self.selected_category_index = 0
    self.selected_comp_node = self.comp_nodes_list[0]
    self.selected_comp_node.show()

  def hide(self):
    self._hide_all_comp_nodes()
    self.is_show = False
    self.selected_category_index = 0
    self.selected_comp_node = self.comp_nodes_list[0]

  def add_node_handle(self, node_info_dict):
    _node_category = node_info_dict["category"]
    _node_type = node_info_dict["type"]
    _node_name = node_info_dict["name"]
    _node_params = []
    for _, _param_value in node_info_dict["params"].items():
      _node_params.append(_param_value)

    self.solution.add_node_data(_node_category, _node_type, _node_name, _node_params)