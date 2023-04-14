import numpy as np
from scripts.core.node_detail import NodeDetail
from scripts.factory.special.sp_canny import SPCanny 
from scripts.factory.special.sp_contours import SPContours 
import scripts.colors as cls

class FactorySpecial:
  def __init__(self) -> None:
    self.color_bg = cls.NODE_SPECIAL_COLOR
  
  def create_node(self, node_type, image_cv: np.matrix) -> NodeDetail:
    if node_type == "canny":
      return SPCanny(self.color_bg, image_cv)
    elif node_type == "contours":
      return SPContours(self.color_bg, image_cv)
    else:
      return None    
