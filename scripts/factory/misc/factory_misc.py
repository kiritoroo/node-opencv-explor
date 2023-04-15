import numpy as np
from scripts.core.node_detail import NodeDetail
from scripts.factory.misc.mc_rescale import MCRescale
from scripts.factory.misc.mc_findlp import MCFindlp
import scripts.colors as cls

class FactoryMisc:
  def __init__(self) -> None:
    self.color_bg = cls.NODE_MISC_COLOR
  
  def create_node(self, node_type, image_cv: np.matrix) -> NodeDetail:
    if node_type == "rescale":
      return MCRescale(self.color_bg, image_cv)
    elif node_type == "findlp":
      return MCFindlp(self.color_bg, image_cv)
    else:
      return None    
