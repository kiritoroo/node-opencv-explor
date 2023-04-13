import pygame
import pygame_gui
from scripts.handle.hd_solutions import SolutionsHandle
import assets.assets as ats
import scripts.stores as sts
import scripts.constants as cts

class Frame:
  def __init__(self, surface: pygame.Surface) -> None:
    self.surface = surface
    self.scale_ratio = sts.scale_ratio
    self.handle_solutions = SolutionsHandle(ats.SOLUTION_FOLDER_PATH)
    self.is_move = False

    self._start()

  def __config_ui_elements(self):
    self.ui_manager = pygame_gui.UIManager((cts.SCREEN_WIDTH, cts.SCREEN_HEIGHT), ats.THEME_PATH)

    _rect = pygame.Rect(0, 0, 50, 22)
    _rect.topright = (-80, 20)
    self.ui_txt_zoom_percent = pygame_gui.elements.ui_label.UILabel(relative_rect=_rect,
              text=f'{int(self.scale_ratio*100)}%', manager=self.ui_manager,
              object_id=pygame_gui.core.ObjectID(class_id="#txt"),
              anchors={'top': 'top',
                      'right': 'right'})

    _rect = pygame.Rect(0, 0, 22, 22)
    _rect.topright = (-50, 20)
    self.ui_btn_zoomin = pygame_gui.elements.UIButton(relative_rect=_rect,
              text='+', manager=self.ui_manager,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_zoom", class_id="#btn"),
              anchors={'top': 'top',
                      'right': 'right'})
    
    _rect = pygame.Rect(0, 0, 22, 22)
    _rect.topright = (-25, 20)
    self.ui_btn_zoomout = pygame_gui.elements.UIButton(relative_rect=_rect,
              text='-', manager=self.ui_manager,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_zoom", class_id="#btn"),
              anchors={'top': 'top',
                      'right': 'right'})

  def _start(self):
    self.__config_ui_elements()
  
  def render(self, surface: pygame.Surface) -> None:
    self.handle_solutions.draw_all(surface)
    self.ui_manager.draw_ui(surface)

  def update(self, delta_time: str) -> None:
    self.ui_manager.update(delta_time)
    self.handle_solutions.update_all(delta_time)

    if not self.is_move:
      self.mouse_rel = pygame.mouse.get_rel()

    if pygame.mouse.get_pressed()[2]:
      self.is_move = True
      self.mouse_rel = pygame.mouse.get_rel()
      self.handle_solutions.move(pygame.math.Vector2(self.mouse_rel))
    else:
      self.is_move = False

  def events(self, event: pygame.event.Event) -> None:
    self.ui_manager.process_events(event)
    self.handle_solutions.events_all(event)

    if event.type == pygame_gui.UI_BUTTON_PRESSED:
      if event.ui_element == self.ui_btn_zoomin:
        if self.scale_ratio < 5:
          self.scale_ratio += (0.2 * self.scale_ratio)
          self._zoom_handle()
      if event.ui_element == self.ui_btn_zoomout:
        if self.scale_ratio > 0.5:
          self.scale_ratio -= (0.2 * self.scale_ratio)
          self._zoom_handle()

    if event.type == pygame.MOUSEWHEEL:
      if event.y == 1 and self.scale_ratio < 5:
        self.scale_ratio += (0.2 * self.scale_ratio)
      if event.y == -1 and self.scale_ratio > 0.5:
        self.scale_ratio -= (0.2 * self.scale_ratio)
      self._zoom_handle()

  def _zoom_handle(self):
    sts.scale_ratio = float(self.scale_ratio)
    self.handle_solutions.zoom(self.scale_ratio)
    self.ui_txt_zoom_percent.set_text(f'{int(self.scale_ratio*100)}%')
