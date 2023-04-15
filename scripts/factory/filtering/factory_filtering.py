import numpy as np
from scripts.core.node_detail import NodeDetail
from scripts.factory.filtering.ft_gaussian import FLGaussian 
from scripts.factory.filtering.ft_median import FLMedian
from scripts.factory.filtering.ft_max import FTMax 
from scripts.factory.filtering.ft_min import FTMin
import scripts.colors as cls

class FactoryFiltering:
  def __init__(self) -> None:
    self.color_bg = cls.NODE_FILTERING_BG_COLOR
  
  def create_node(self, node_type: str, image_cv: np.matrix) -> NodeDetail:
    if node_type == "gaussian":
      return FLGaussian(self.color_bg, image_cv)
    elif node_type == "median":
      return FLMedian(self.color_bg, image_cv)
    elif node_type == "max":
      return FTMax(self.color_bg, image_cv)
    elif node_type == "min":
      return FTMin(self.color_bg, image_cv)
    else:
      return None    
