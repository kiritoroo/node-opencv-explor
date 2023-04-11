from scripts.core.node_detail import NodeDetail
from scripts.factory.base.bs_original import BSOriginal
from scripts.factory.base.bs_grayscale import BSGrayscale
import scripts.colors as cls

class FactoryBase:
  def __init__(self) -> None:
    self.color_bg = cls.NODE_BASE_BG_COLOR
  
  def create_node(self, node_type) -> NodeDetail:
    if node_type == "original":
      return BSOriginal(self.color_bg)
    elif node_type == "grayscale":
      return BSGrayscale(self.color_bg)
    else:
      return None
