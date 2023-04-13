import pygame
import pygame_gui
import assets.assets as ats
import scripts.constants as cts
import scripts.colors as cls

class ComponentNodeStore:
  def __init__(self) -> None:

    self._start()

  def __config_variables(self) -> None:
    self.is_show = False
    self.size_text = 15
    self.font = pygame.font.Font(ats.FONT_POPPINS_MEDIUM_PATH, self.size_text)
    self.selected_category_index = 0

    self.category_count = 5
    self.category_name = ["Base", "Filtering", "Morphology", "Special", "Misc"]

    self.node_base_info_dict = {
      "1": {
        "category": "base",
        "type": "original",
        "name": "Original",
        "tooltip": "Original Node đại diện cho hình ảnh đầu vào ban đầu mà không có bất kỳ sửa đổi nào",
        "params": {}
      },
      "2": {
        "category": "base",
        "type": "grayscale",
        "name": "Grayscale",
        "tooltip": "Grayscale Node chuyển đổi hình ảnh thành thang độ xám, chỉ chứa các sắc thái xám từ đen sang trắng",
        "params": {}
      }
    }
    self.node_base_info_list = [
      {"category": v["category"],
       "type": v["type"],
       "name": v["name"],
       "tooltip": v["tooltip"],
       "params": v["params"]} 
      for v in self.node_base_info_dict.values()]
    self.node_base_info_count = len(self.node_base_info_list)
    
    self.size_btn_category = pygame.Rect(0, 0, 130, 35)
    self.size_btn_node = pygame.Rect(0, 0, 180, 40)

  def __config_ui_elements(self) -> None:
    self.ui_manager = pygame_gui.UIManager((cts.SCREEN_WIDTH, cts.SCREEN_HEIGHT), ats.THEME_PATH)

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
  
    self.ui_btn_node_base_list = list[pygame_gui.elements.UIButton]()
    _rect = pygame.Rect(0, 0, self.size_btn_node.width, self.size_btn_node.height)
    for i in range(self.node_base_info_count):
      _ui_btn_node_base = pygame_gui.elements.UIButton(relative_rect=_rect,
              text=f'{self.node_base_info_list[i].get("name")}', tool_tip_text=f'{self.node_base_info_list[i].get("tooltip")}',
              manager=self.ui_manager, container=self.ui_panel_container,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_node_base", class_id="#btn"))
      self.ui_btn_node_base_list.append(_ui_btn_node_base)

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

  def __config_ui_btn_node_base_list(self):
    _start_pos_x = self.ui_panel_container.rect.left+70
    _start_pos_y = self.ui_panel_container.rect.top+50
    for i in range(len(self.ui_btn_node_base_list)):
      _pos_x = _start_pos_x + (i%3)*(self.ui_btn_node_base_list[i].rect.width+70)
      _pos_y = _start_pos_y + (i//3)*(self.ui_btn_node_base_list[i].rect.height+30)
      self.ui_btn_node_base_list[i].set_position(pygame.math.Vector2(_pos_x, _pos_y))
    
  def _start(self) -> None:
    self.__config_variables()
    self.__config_ui_elements()
    self.__config_ui_btn_close_panel()
    self.__config_ui_btn_category_list()
    self.__config_ui_btn_node_base_list()
  
  def draw(self, surface: pygame.Surface) -> None:
    if self.is_show:
      self.ui_manager.draw_ui(surface)

  def update(self, delta_time: float) -> None:
    self.ui_manager.update(delta_time)

  def events(self, event: pygame.event.Event) -> None:
    self.ui_manager.process_events(event)

    if event.type == pygame_gui.UI_BUTTON_PRESSED:
      if event.ui_element == self.ui_btn_close_panel:
        self.is_show = False
          
      for i, _btn_category in enumerate(self.ui_btn_category_list):
        if event.ui_element == _btn_category:
          self.selected_category_index = i
          self._select_category_handle()

  def _select_category_handle(self):
    pass