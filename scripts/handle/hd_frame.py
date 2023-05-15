from scripts.frame import fr_intro
from scripts.frame import fr_main

class FrameHandle:
  def __init__(self, surface) -> None:
    self.surface = surface
    self.current_frame = fr_intro.Frame(self, self.surface)

  def set_frame(self, frname):
    if frname == 'frame_intro':
      self.current_frame = fr_intro.Frame(self, self.surface)
    elif frname == 'frame_main':
      self.current_frame = fr_main.Frame(self, self.surface)
    else:
      return