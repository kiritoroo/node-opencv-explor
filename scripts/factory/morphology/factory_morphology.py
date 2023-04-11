from scripts.core.node_detail import NodeDetail
from scripts.factory.morphology.mp_open import MPOpen 
from scripts.factory.morphology.mp_close import MPClose
import scripts.colors as cls

class FactoryMorphology:
  def __init__(self) -> None:
    self.color_bg = cls.NODE_MORPHOLOGY_BG_COLOR
  
  def create_node(self, node_type) -> NodeDetail:
    if node_type == "open":
      return MPOpen(self.color_bg)
    elif node_type == "close":
      return MPClose(self.color_bg)
    else:
      return None    
