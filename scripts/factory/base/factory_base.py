import numpy as np
from scripts.core.node_detail import NodeDetail
from scripts.factory.base.bs_original import BSOriginal
from scripts.factory.base.bs_grayscale import BSGrayscale
from scripts.factory.base.bs_invert import BSInvert
from scripts.factory.base.bs_logtranf import BSLogTranf
from scripts.factory.base.bs_gamma import BSGamma
import scripts.colors as cls

class FactoryBase:
  def __init__(self) -> None:
    self.color_bg = cls.NODE_BASE_BG_COLOR
  
  def create_node(self, node_type: str, image_cv: np.matrix) -> NodeDetail:
    if node_type == "original":
      return BSOriginal(self.color_bg, image_cv)
    elif node_type == "grayscale":
      return BSGrayscale(self.color_bg, image_cv)
    elif node_type == "invert":
      return BSInvert(self.color_bg, image_cv)
    elif node_type == "logtranf":
      return BSLogTranf(self.color_bg, image_cv)
    elif node_type == "gamma":
      return BSGamma(self.color_bg, image_cv)
    else:
      return None
