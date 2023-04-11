import scripts.stores as sts
from scripts.core.node import Node
from scripts.core.node_detail import NodeDetail
from scripts.factory.base.factory_base import FactoryBase
from scripts.factory.filtering.factory_filtering import FactoryFiltering
from scripts.factory.morphology.factory_morphology import FactoryMorphology

class NodeData:
  def __init__(self, node_catory: str, node_type: str, node_name: str, node_params: list) -> None:
    self.node_category = node_catory
    self.node_type = node_type
    self.node_name = node_name
    self.params = node_params
    self.node: Node = None
    self.node_detail: NodeDetail = None

    self.start()

  def start(self) -> None:
    _default_image_cv = sts.load_image_cv_default()

    _factory_base = FactoryBase()
    _factory_filtering = FactoryFiltering()
    _factory_morphology = FactoryMorphology()

    if self.node_category == "base":
      self.node_detail = _factory_base.create_node(self.node_type, _default_image_cv)
      self.node = Node(self.node_name, _factory_base.color_bg)
    elif self.node_category == "filtering":
      self.node_detail = _factory_filtering.create_node(self.node_type, _default_image_cv)
      self.node = Node(self.node_name, _factory_filtering.color_bg)
    elif self.node_category == "morphology":
      self.node_detail = _factory_morphology.create_node(self.node_type, _default_image_cv)
      self.node = Node(self.node_name, _factory_morphology.color_bg)
    else:
      self.node_detail = None
      self.node = None
