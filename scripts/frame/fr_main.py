import pygame
import pygame_gui
import os
import pytesseract
import cv2 as cv
from scripts.handle.hd_solutions import SolutionsHandle
import assets.assets as ats
import scripts.stores as sts
import scripts.constants as cts

pytesseract.pytesseract.tesseract_cmd = ats.TESSERACT_ENGINE_PATH

class Frame:
  def __init__(self, surface: pygame.Surface) -> None:
    self.image_cv = sts.image_cv
    self.surface = surface
    self.scale_ratio = sts.scale_ratio
    self.handle_solutions = SolutionsHandle(ats.SOLUTION_FOLDER_PATH)
    self.is_move = False
    self.is_select_image = False
    self.ui_image_license_plate = None

    self._start()

  def __config_ui_elements(self):
    self.ui_manager = pygame_gui.UIManager((cts.SCREEN_WIDTH, cts.SCREEN_HEIGHT), ats.THEME_PATH)
    self.file_dialog = None
    
    _rect = pygame.Rect(0, 0, 50, 22)
    _rect.topright = (-80, 20)
    self.ui_txt_zoom_percent = pygame_gui.elements.UILabel(relative_rect=_rect,
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
    
    _rect = pygame.Rect(0, 0, 35, 25)
    self.ui_btn_close_panel_main = pygame_gui.elements.UIButton(relative_rect=_rect,
              text='-', manager=self.ui_manager,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_close_panel", class_id="#btn"))
    
    _rect = pygame.Rect(-5, 100, 30, 40)
    self.ui_btn_open_panel_main = pygame_gui.elements.UIButton(relative_rect=_rect,
              text='>', manager=self.ui_manager, visible=False,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_close_panel", class_id="#btn"))

    _rect = pygame.Rect(0, 0, 300, 650)
    _rect.topleft = pygame.math.Vector2(25, 50)
    self.ui_panel_main_container = pygame_gui.elements.UIPanel(relative_rect=_rect,
              manager=self.ui_manager,
              object_id=pygame_gui.core.ObjectID(object_id="@panel_main", class_id="#panel"),
              anchors={'top': 'top',
                      'left': 'left'})
    
    self.ui_btn_close_panel_main.set_position(pygame.math.Vector2(
      self.ui_panel_main_container.rect.right-50,
      self.ui_panel_main_container.rect.top-20))

    _rect = pygame.Rect(0, 0, 250, 250)
    _rect.center = pygame.math.Vector2(self.ui_panel_main_container.rect.centerx, self.ui_panel_main_container.rect.top+150)
    self.ui_panel_image = pygame_gui.elements.UIPanel(relative_rect=_rect,
              manager=self.ui_manager,
              object_id=pygame_gui.core.ObjectID(object_id="@panel_image", class_id="#panel"))
    
    _surf_image_default = pygame.surfarray.make_surface(self.image_cv).convert_alpha()
    _img_width = 220
    _image_scale_ratio = _img_width / _surf_image_default.get_width()
    _image_height = int(_surf_image_default.get_height() * _image_scale_ratio)
    _surf_image = pygame.transform.smoothscale(_surf_image_default, (_img_width, _image_height))
    _rect = pygame.Rect(0, 0, _img_width, _image_height)
    self.ui_image_cv = pygame_gui.elements.UIImage(
            relative_rect = _rect, 
            image_surface = _surf_image,
            manager = self.ui_manager)
    self.ui_image_cv.set_position(pygame.math.Vector2(
      self.ui_panel_image._rect.left+15,
      self.ui_panel_image.rect.top+15))
    
    self.ui_panel_image.set_dimensions(pygame.math.Vector2(
      250, _image_height + 80
    ))

    _rect = pygame.Rect(0, 0, 150, 30)
    _rect.bottomleft = (self.ui_panel_image.rect.width/2-150/2, -20)
    self.ui_txt_image_size = pygame_gui.elements.UILabel(relative_rect=_rect,
              text=f'{_surf_image_default.get_width()} x {_surf_image_default.get_height()} pixel', 
              manager=self.ui_manager, container=self.ui_panel_image,
              object_id=pygame_gui.core.ObjectID(object_id="@txt_image_size", class_id="#txt"),
              anchors={'bottom': 'bottom',
                      'left': 'left'})
    
    _rect = pygame.Rect(0, 0, 120, 40)
    self.ui_btn_load_image = pygame_gui.elements.UIButton(relative_rect=_rect,
              text='Load image', 
              manager=self.ui_manager, container=self.ui_panel_main_container,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_load_image", class_id="#btn"))
    self.ui_btn_load_image.set_position(pygame.math.Vector2(
      self.ui_panel_image.rect.left+70, self.ui_panel_image.rect.bottom + 20
    ))


    _rect = pygame.Rect(0, 0, 250, 200)
    _rect.center = pygame.math.Vector2(self.ui_panel_main_container.rect.centerx, self.ui_panel_main_container.rect.bottom-220)
    self.ui_panel_recognition = pygame_gui.elements.UIPanel(relative_rect=_rect,
              manager=self.ui_manager,
              object_id=pygame_gui.core.ObjectID(object_id="@panel_image", class_id="#panel"))
    
    _rect = pygame.Rect(0, 0, 150, 30)
    _rect.bottomleft = (self.ui_panel_recognition.rect.width/2-150/2, -20)
    self.ui_txt_image_license_plate = pygame_gui.elements.UILabel(relative_rect=_rect,
              text=f'License Plate is: ...', 
              manager=self.ui_manager, container=self.ui_panel_recognition,
              object_id=pygame_gui.core.ObjectID(object_id="@txt_image_size", class_id="#txt"),
              anchors={'bottom': 'bottom',
                      'left': 'left'})
    
    _rect = pygame.Rect(0, 0, 120, 40)
    self.ui_btn_recognition = pygame_gui.elements.UIButton(relative_rect=_rect,
              text='Recognition', 
              manager=self.ui_manager, container=self.ui_panel_main_container,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_load_image", class_id="#btn"))
    self.ui_btn_recognition.set_position(pygame.math.Vector2(
      self.ui_panel_recognition.rect.left+70, self.ui_panel_recognition.rect.bottom + 20
    ))
    
  def __config_ui_image(self):
    self.ui_manager.ui_group.remove(self.ui_image_cv)
    _surf_image_default = pygame.surfarray.make_surface(self.image_cv).convert_alpha()
    _img_width = 220
    _image_scale_ratio = _img_width / _surf_image_default.get_width()
    _image_height = int(_surf_image_default.get_height() * _image_scale_ratio)
    _surf_image = pygame.transform.smoothscale(_surf_image_default, (_img_width, _image_height))
    _rect = pygame.Rect(0, 0, _img_width, _image_height)
    self.ui_image_cv = pygame_gui.elements.UIImage(
            relative_rect = _rect, 
            image_surface = _surf_image,
            manager = self.ui_manager)
    self.ui_image_cv.set_position(pygame.math.Vector2(
      self.ui_panel_image._rect.left+15,
      self.ui_panel_image.rect.top+15))
    
    self.ui_panel_image.set_dimensions(pygame.math.Vector2(
      250, _image_height + 80
    ))

    self.ui_txt_image_size.set_text(f'{_surf_image_default.get_width()} x {_surf_image_default.get_height()} pixel')
  
    self.ui_btn_load_image.set_position(pygame.math.Vector2(
      self.ui_panel_image.rect.left+70, self.ui_panel_image.rect.bottom + 20
    ))

    if self.ui_image_license_plate is not None:
      self.ui_manager.ui_group.remove(self.ui_image_license_plate)
    self.ui_txt_image_license_plate.set_text("Nothing...")

  def _start(self):
    self.__config_ui_elements()
  
  def render(self, surface: pygame.Surface) -> None:
    self.handle_solutions.draw_all(surface)
    self.ui_manager.draw_ui(surface)

  def update(self, delta_time: float) -> None:
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
      if not self.is_select_image:
        if event.ui_element == self.ui_btn_zoomin:
          if self.scale_ratio < 5:
            self.scale_ratio += (0.2 * self.scale_ratio)
            self._zoom_handle()
        if event.ui_element == self.ui_btn_zoomout:
          if self.scale_ratio > 0.5:
            self.scale_ratio -= (0.2 * self.scale_ratio)
            self._zoom_handle()
      if event.ui_element == self.ui_btn_load_image:
        self.__open_file_dialog()
      if event.ui_element == self.ui_btn_close_panel_main:
        self.__hide_panel_main()
      if event.ui_element == self.ui_btn_open_panel_main:
        self.__show_panel_main()
      if event.ui_element == self.ui_btn_recognition:
        self.__recognition_license_plate()

    if event.type == pygame.MOUSEWHEEL:
      if not self.is_select_image:
        if event.y == 1 and self.scale_ratio < 5:
          self.scale_ratio += (0.2 * self.scale_ratio)
        if event.y == -1 and self.scale_ratio > 0.5:
          self.scale_ratio -= (0.2 * self.scale_ratio)
        self._zoom_handle()

    if event.type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED:
      if event.ui_element == self.file_dialog:
        self.__change_image_handle(event.text)

    if event.type == pygame_gui.UI_WINDOW_CLOSE:
      if self.file_dialog != None and event.ui_element == self.file_dialog:
        self.is_select_image = False

  def _zoom_handle(self):
    sts.scale_ratio = float(self.scale_ratio)
    self.handle_solutions.zoom(self.scale_ratio)
    self.ui_txt_zoom_percent.set_text(f'{int(self.scale_ratio*100)}%')

  def __open_file_dialog(self):
    self.is_select_image = True
    _init_path = os.path.dirname(ats.IMAGE_DEFAULT_PATH)
    # _os_name = platform.system()
    # if _os_name == "Windows":
    #   _init_path = 'C:/Users/{}/Downloads'.format(getpass.getuser())
    # else:
    #   _init_path = '/home/{}/Downloads'.format(getpass.getuser())

    _rect = pygame.Rect(0, 0, 650, 450)
    _rect.center = pygame.math.Vector2(cts.SCREEN_WIDTH//2, cts.SCREEN_HEIGHT//2)
    self.file_dialog = pygame_gui.windows.UIFileDialog(rect = _rect,
              window_title = 'Choose image (●''◡''●)',
              initial_file_path = _init_path,
              manager = self.ui_manager,
              object_id=pygame_gui.core.ObjectID(class_id="#file_dialog"))
    
  def __change_image_handle(self, img_path):
    self.is_select_image = False
    sts.image_cv = sts.load_image_cv(img_path)
    self.image_cv = sts.image_cv
    self.handle_solutions.reset_image()
    self.__config_ui_image()

  def __hide_panel_main(self) -> None:
    self.ui_panel_main_container.visible = False
    self.ui_panel_image.visible = False
    self.ui_btn_close_panel_main.visible = False
    self.ui_image_cv.visible = False
    self.ui_txt_image_size.visible = False
    self.ui_btn_load_image.visible = False
    self.ui_btn_open_panel_main.visible = True

  def __show_panel_main(self) -> None:
    self.ui_panel_main_container.visible = True
    self.ui_panel_image.visible = True
    self.ui_btn_close_panel_main.visible = True
    self.ui_image_cv.visible = True
    self.ui_txt_image_size.visible = True
    self.ui_btn_load_image.visible = True
    self.ui_btn_open_panel_main.visible = False


  def __recognition_license_plate(self) -> None:
    _list_candidates = self.handle_solutions.get_image_candidates_list()
    for i in range(len(_list_candidates)):
      _image = _list_candidates[i]
      _image_flip = cv.flip(_image.copy(), 0)
      _image_rotate = cv.rotate(_image_flip, cv.ROTATE_90_CLOCKWISE)

      predicted_result = pytesseract.image_to_string(_image_rotate, lang ='eng', config ='--oem 3 -l eng --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
      filter_predicted_result = "".join(predicted_result.split()).replace(":", "").replace("-", "")
      
      if self.ui_image_license_plate is not None:
        self.ui_manager.ui_group.remove(self.ui_image_license_plate)

      if len(filter_predicted_result) > 2:
        self.ui_txt_image_license_plate.set_text(filter_predicted_result)

        _surf_image_default = pygame.surfarray.make_surface(_image).convert_alpha()
        _img_width = 220
        _image_scale_ratio = _img_width / _surf_image_default.get_width()
        _image_height = int(_surf_image_default.get_height() * _image_scale_ratio)
        _surf_image = pygame.transform.smoothscale(_surf_image_default, (_img_width, _image_height))
        _rect = pygame.Rect(0, 0, _img_width, _image_height)
        self.ui_image_license_plate = pygame_gui.elements.UIImage(
                relative_rect = _rect, 
                image_surface = _surf_image,
                manager = self.ui_manager)
        self.ui_image_license_plate.set_position(pygame.math.Vector2(
          self.ui_panel_recognition._rect.left+15,
          self.ui_panel_recognition.rect.top+15))
        return  
      else:
        self.ui_txt_image_license_plate.set_text("Nothing...")
    