import pygame
import  pygame_gui
import assets.assets as ats
import scripts.stores as sts
import scripts.constants as cts
import scripts.colors as cls
import cv2 as cv
import html

class Frame:
  def __init__(self, handler, surface: pygame.Surface) -> None:
    self.surface = surface
    self.handler = handler
    self._start()

  def _start(self):
    self.__config_ui_elements()

  def __config_ui_elements(self):
    self.ui_manager = pygame_gui.UIManager((cts.SCREEN_WIDTH, cts.SCREEN_HEIGHT), ats.THEME_PATH)

    _rect = pygame.Rect(0, 0, 600, 80)
    _rect.center = pygame.math.Vector2(cts.SCREEN_WIDTH//2, 100)
    self.ui_txt_project_title = pygame_gui.elements.UILabel(relative_rect=_rect,
              manager=self.ui_manager,
              text=f'License Plate Recognition',
              object_id=pygame_gui.core.ObjectID(object_id="@txt_project_title", class_id="#txt"))

    _rect = pygame.Rect(0, 0, 600, 80)
    _rect.center = pygame.math.Vector2(
      cts.SCREEN_WIDTH//2,
      self.ui_txt_project_title.get_relative_rect().bottom+10)
    self.ui_txt_project_advisor= pygame_gui.elements.UILabel(relative_rect=_rect,
              manager=self.ui_manager,
              text=f'{html.unescape("&#x47;&#x56;&#x48;&#x44;&#x3A;&#x20;&#x54;&#x68;&#x1EA7;&#x79;&#x20;&#x48;&#x6F;&#xE0;&#x6E;&#x67;&#x20;&#x56;&#x103;&#x6E;&#x20;&#x44;&#x169;&#x6E;&#x67;")}',
              object_id=pygame_gui.core.ObjectID(object_id="@txt_project_advisor", class_id="#txt"))

    ## Member - Minh Chau
    _avatar_cv = cv.imread(ats.AVATAR_CHAU_PATH)
    _avatar_cv = cv.transpose(_avatar_cv)
    _surf_image_default = pygame.surfarray.make_surface(_avatar_cv).convert_alpha()
    _img_width = 100
    _image_scale_ratio = _img_width / _surf_image_default.get_width()
    _image_height = int(_surf_image_default.get_height() * _image_scale_ratio)
    _surf_image = pygame.transform.smoothscale(_surf_image_default, (_img_width, _image_height))
    _rect = pygame.Rect(450, 200, _img_width, _image_height)
    self.ui_image_cv = pygame_gui.elements.UIImage(
            relative_rect = _rect, 
            image_surface = _surf_image,
            manager = self.ui_manager)

    _rect = pygame.Rect(0, 0, _img_width, _image_height)
    _rect = pygame.Rect(0, 0, 350, 180)
    _rect.center = pygame.math.Vector2(
      self.ui_image_cv.get_relative_rect().left+self.ui_image_cv.get_relative_rect().width//2,
      self.ui_image_cv.get_relative_rect().top+250)
    self.ui_panel_member = pygame_gui.elements.UIPanel(relative_rect=_rect,
              manager=self.ui_manager,
              object_id=pygame_gui.core.ObjectID(object_id="@panel_main", class_id="#panel"))
    
    _rect = pygame.Rect(0, 0, 200, 50)
    _rect.center = pygame.math.Vector2(
      self.ui_panel_member.get_relative_rect().left+self.ui_panel_member.get_relative_rect().width//2,
      self.ui_panel_member.get_relative_rect().top+50)
    self.ui_member_name = pygame_gui.elements.UILabel(relative_rect=_rect,
              manager=self.ui_manager,
              text=f'{html.unescape("&#x4D;&#x69;&#x6E;&#x68;&#x20;&#x43;&#x68;&#xE2;&#x75;")}',
              object_id=pygame_gui.core.ObjectID(object_id="@txt_member_name", class_id="#txt"))

    _rect = pygame.Rect(0, 0, 300, 35)
    _rect.center = pygame.math.Vector2(
      self.ui_panel_member.get_relative_rect().left+self.ui_panel_member.get_relative_rect().width//2,
      self.ui_member_name.get_relative_rect().bottom+20)
    self.ui_member_id = pygame_gui.elements.UILabel(relative_rect=_rect,
              manager=self.ui_manager,
              text=f'{html.unescape("&#x32;&#x30;&#x31;&#x31;&#x30;&#x31;&#x38;&#x38;")}',
              object_id=pygame_gui.core.ObjectID(object_id="@txt_member_id", class_id="#txt"))

    _rect = pygame.Rect(0, 0, 300, 30)
    _rect.center = pygame.math.Vector2(
      self.ui_panel_member.get_relative_rect().left+self.ui_panel_member.get_relative_rect().width//2,
      self.ui_member_id.get_relative_rect().bottom+15)
    self.ui_member_email = pygame_gui.elements.UILabel(relative_rect=_rect,
              manager=self.ui_manager,
              text=f'{html.unescape("&#x32;&#x30;&#x31;&#x31;&#x30;&#x31;&#x38;&#x38;&#x40;&#x73;&#x74;&#x75;&#x64;&#x65;&#x6E;&#x74;&#x2E;&#x68;&#x63;&#x6D;&#x75;&#x74;&#x65;&#x2E;&#x65;&#x64;&#x75;&#x2E;&#x76;&#x6E;")}',
              object_id=pygame_gui.core.ObjectID(object_id="@txt_member_email", class_id="#txt"))
    
    ## Member - Thuy Trang
    _avatar_cv = cv.imread(ats.AVATAR_TRANG_PATH)
    _avatar_cv = cv.transpose(_avatar_cv)
    _surf_image_default = pygame.surfarray.make_surface(_avatar_cv).convert_alpha()
    _img_width = 100
    _image_scale_ratio = _img_width / _surf_image_default.get_width()
    _image_height = int(_surf_image_default.get_height() * _image_scale_ratio)
    _surf_image = pygame.transform.smoothscale(_surf_image_default, (_img_width, _image_height))
    _rect = pygame.Rect(850, 200, _img_width, _image_height)
    self.ui_image_cv = pygame_gui.elements.UIImage(
            relative_rect = _rect, 
            image_surface = _surf_image,
            manager = self.ui_manager)

    _rect = pygame.Rect(0, 0, _img_width, _image_height)
    _rect = pygame.Rect(0, 0, 350, 180)
    _rect.center = pygame.math.Vector2(
      self.ui_image_cv.get_relative_rect().left+self.ui_image_cv.get_relative_rect().width//2,
      self.ui_image_cv.get_relative_rect().top+250)
    self.ui_panel_member = pygame_gui.elements.UIPanel(relative_rect=_rect,
              manager=self.ui_manager,
              object_id=pygame_gui.core.ObjectID(object_id="@panel_main", class_id="#panel"))
    
    _rect = pygame.Rect(0, 0, 200, 50)
    _rect.center = pygame.math.Vector2(
      self.ui_panel_member.get_relative_rect().left+self.ui_panel_member.get_relative_rect().width//2,
      self.ui_panel_member.get_relative_rect().top+50)
    self.ui_member_name = pygame_gui.elements.UILabel(relative_rect=_rect,
              manager=self.ui_manager,
              text=f'{html.unescape("&#x54;&#x68;&#xF9;&#x79;&#x20;&#x54;&#x72;&#x61;&#x6E;&#x67;")}',
              object_id=pygame_gui.core.ObjectID(object_id="@txt_member_name", class_id="#txt"))

    _rect = pygame.Rect(0, 0, 300, 35)
    _rect.center = pygame.math.Vector2(
      self.ui_panel_member.get_relative_rect().left+self.ui_panel_member.get_relative_rect().width//2,
      self.ui_member_name.get_relative_rect().bottom+20)
    self.ui_member_id = pygame_gui.elements.UILabel(relative_rect=_rect,
              manager=self.ui_manager,
              text=f'{html.unescape("&#x32;&#x30;&#x31;&#x31;&#x30;&#x35;&#x38;&#x30;")}',
              object_id=pygame_gui.core.ObjectID(object_id="@txt_member_id", class_id="#txt"))

    _rect = pygame.Rect(0, 0, 300, 30)
    _rect.center = pygame.math.Vector2(
      self.ui_panel_member.get_relative_rect().left+self.ui_panel_member.get_relative_rect().width//2,
      self.ui_member_id.get_relative_rect().bottom+15)
    self.ui_member_email = pygame_gui.elements.UILabel(relative_rect=_rect,
              manager=self.ui_manager,
              text=f'{html.unescape("&#x32;&#x30;&#x31;&#x31;&#x30;&#x35;&#x38;&#x30;&#x40;&#x73;&#x74;&#x75;&#x64;&#x65;&#x6E;&#x74;&#x2E;&#x68;&#x63;&#x6D;&#x75;&#x74;&#x65;&#x2E;&#x65;&#x64;&#x75;&#x2E;&#x76;&#x6E;")}',
              object_id=pygame_gui.core.ObjectID(object_id="@txt_member_email", class_id="#txt"))
    
    ## Member - Kim Hanh
    _avatar_cv = cv.imread(ats.AVATAR_HANH_PATH)
    _avatar_cv = cv.transpose(_avatar_cv)
    _surf_image_default = pygame.surfarray.make_surface(_avatar_cv).convert_alpha()
    _img_width = 100
    _image_scale_ratio = _img_width / _surf_image_default.get_width()
    _image_height = int(_surf_image_default.get_height() * _image_scale_ratio)
    _surf_image = pygame.transform.smoothscale(_surf_image_default, (_img_width, _image_height))
    _rect = pygame.Rect(1250, 200, _img_width, _image_height)
    self.ui_image_cv = pygame_gui.elements.UIImage(
            relative_rect = _rect, 
            image_surface = _surf_image,
            manager = self.ui_manager)

    _rect = pygame.Rect(0, 0, _img_width, _image_height)
    _rect = pygame.Rect(0, 0, 350, 180)
    _rect.center = pygame.math.Vector2(
      self.ui_image_cv.get_relative_rect().left+self.ui_image_cv.get_relative_rect().width//2,
      self.ui_image_cv.get_relative_rect().top+250)
    self.ui_panel_member = pygame_gui.elements.UIPanel(relative_rect=_rect,
              manager=self.ui_manager,
              object_id=pygame_gui.core.ObjectID(object_id="@panel_main", class_id="#panel"))
    
    _rect = pygame.Rect(0, 0, 200, 50)
    _rect.center = pygame.math.Vector2(
      self.ui_panel_member.get_relative_rect().left+self.ui_panel_member.get_relative_rect().width//2,
      self.ui_panel_member.get_relative_rect().top+50)
    self.ui_member_name = pygame_gui.elements.UILabel(relative_rect=_rect,
              manager=self.ui_manager,
              text=f'{html.unescape("&#x4B;&#x69;&#x6D;&#x20;&#x48;&#x1EA1;&#x6E;&#x68;")}',
              object_id=pygame_gui.core.ObjectID(object_id="@txt_member_name", class_id="#txt"))

    _rect = pygame.Rect(0, 0, 300, 35)
    _rect.center = pygame.math.Vector2(
      self.ui_panel_member.get_relative_rect().left+self.ui_panel_member.get_relative_rect().width//2,
      self.ui_member_name.get_relative_rect().bottom+20)
    self.ui_member_id = pygame_gui.elements.UILabel(relative_rect=_rect,
              manager=self.ui_manager,
              text=f'{html.unescape("&#x32;&#x30;&#x31;&#x31;&#x30;&#x34;&#x36;&#x38;")}',
              object_id=pygame_gui.core.ObjectID(object_id="@txt_member_id", class_id="#txt"))

    _rect = pygame.Rect(0, 0, 300, 30)
    _rect.center = pygame.math.Vector2(
      self.ui_panel_member.get_relative_rect().left+self.ui_panel_member.get_relative_rect().width//2,
      self.ui_member_id.get_relative_rect().bottom+15)
    self.ui_member_email = pygame_gui.elements.UILabel(relative_rect=_rect,
              manager=self.ui_manager,
              text=f'{html.unescape("&#x32;&#x30;&#x31;&#x31;&#x30;&#x34;&#x36;&#x38;&#x40;&#x73;&#x74;&#x75;&#x64;&#x65;&#x6E;&#x74;&#x2E;&#x68;&#x63;&#x6D;&#x75;&#x74;&#x65;&#x2E;&#x65;&#x64;&#x75;&#x2E;&#x76;&#x6E;")}',
              object_id=pygame_gui.core.ObjectID(object_id="@txt_member_email", class_id="#txt"))

    ## Our team
    _rect = pygame.Rect(0, 0, 150, 50)
    _rect.center = pygame.math.Vector2(
      cts.SCREEN_WIDTH//2,
      self.ui_panel_member.get_relative_rect().bottom+30)
    self.ui_txt_ourteam = pygame_gui.elements.UILabel(relative_rect=_rect,
              manager=self.ui_manager,
              text=f'Our team',
              object_id=pygame_gui.core.ObjectID(object_id="@txt_project_advisor", class_id="#txt"))
    
    ## Let's get started
    _rect = pygame.Rect(0, 0, 200, 80)
    _rect.center = pygame.math.Vector2(cts.SCREEN_WIDTH//2, cts.SCREEN_HEIGHT-100)
    self.ui_btn_start = pygame_gui.elements.UIButton(relative_rect=_rect,
              text="Let's get started", manager=self.ui_manager,
              object_id=pygame_gui.core.ObjectID(object_id="@btn_start", class_id="#btn"))

  def render(self, surface: pygame.Surface) -> None:
    self.ui_manager.draw_ui(surface)
    pygame.draw.line(surface, cls.ARROW_COLOR, 
      (600, self.ui_panel_member.get_relative_rect().bottom+30),
      (self.ui_txt_ourteam.get_relative_rect().left-5, self.ui_panel_member.get_relative_rect().bottom+30), 2)
    pygame.draw.line(surface, cls.ARROW_COLOR, 
      (self.ui_txt_ourteam.get_relative_rect().right+5, self.ui_panel_member.get_relative_rect().bottom+30),
      (1200, self.ui_panel_member.get_relative_rect().bottom+30), 2)

  def update(self, delta_time: float) -> None:
    self.ui_manager.update(delta_time)

  def events(self, event: pygame.event.Event) -> None:
    self.ui_manager.process_events(event)
    if event.type == pygame_gui.UI_BUTTON_PRESSED:
      if event.ui_element == self.ui_btn_start:
        self.handler.set_frame('frame_main')
      else:
        return