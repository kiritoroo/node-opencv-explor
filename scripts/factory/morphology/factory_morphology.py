import numpy as np
from scripts.core.node_detail import NodeDetail
from scripts.factory.morphology.mp_open import MPOpen 
from scripts.factory.morphology.mp_close import MPClose
from scripts.factory.morphology.mp_erode import MPErode
from scripts.factory.morphology.mp_dilate import MPDiale
from scripts.factory.morphology.mp_tophat import MPTopHat
from scripts.factory.morphology.mp_blackhat import MPBlackHat
import scripts.colors as cls

class FactoryMorphology:
  def __init__(self) -> None:
    self.color_bg = cls.NODE_MORPHOLOGY_BG_COLOR
  
  def create_node(self, node_type, image_cv: np.matrix) -> NodeDetail:
    if node_type == "open":
      return MPOpen(self.color_bg, image_cv)
    elif node_type == "close":
      return MPClose(self.color_bg, image_cv)
    elif node_type == "erode":
      return MPErode(self.color_bg, image_cv)
    elif node_type == "dilate":
      return MPDiale(self.color_bg, image_cv)
    elif node_type == "tophat":
      return MPTopHat(self.color_bg, image_cv)
    elif node_type == "blackhat":
      return MPBlackHat(self.color_bg, image_cv)
    else:
      return None    
