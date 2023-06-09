import scripts.stores as sts
from scripts.core.node import Node
from scripts.core.node_detail import NodeDetail
from scripts.factory.base.factory_base import FactoryBase
from scripts.factory.filtering.factory_filtering import FactoryFiltering
from scripts.factory.morphology.factory_morphology import FactoryMorphology
from scripts.factory.special.factory_special import FactorySpecial
from scripts.factory.misc.factory_misc import FactoryMisc

class NodeData:
  def __init__(self, node_catory: str, node_type: str, node_name: str, node_params: list) -> None:
    self.node_category = node_catory
    self.node_type = node_type
    self.node_name = node_name
    self.params = node_params
    self.node: Node = None
    self.node_detail: NodeDetail = None

    self._start()

  def _start(self) -> None:
    _default_image_cv = sts.image_cv

    _factory_base = FactoryBase()
    _factory_filtering = FactoryFiltering()
    _factory_morphology = FactoryMorphology()
    _factory_special = FactorySpecial()
    _factory_misc = FactoryMisc()

    if self.node_category == "base":
      self.node_detail = _factory_base.create_node(self.node_type, _default_image_cv)
      self.node = Node(self.node_name, _factory_base.color_bg)
    elif self.node_category == "filtering":
      self.node_detail = _factory_filtering.create_node(self.node_type, _default_image_cv)
      self.node = Node(self.node_name, _factory_filtering.color_bg)
    elif self.node_category == "morphology":
      self.node_detail = _factory_morphology.create_node(self.node_type, _default_image_cv)
      self.node = Node(self.node_name, _factory_morphology.color_bg)
    elif self.node_category == "special":
      self.node_detail = _factory_special.create_node(self.node_type, _default_image_cv)
      self.node = Node(self.node_name, _factory_special.color_bg)
    elif self.node_category == "misc":
      self.node_detail = _factory_misc.create_node(self.node_type, _default_image_cv)
      self.node = Node(self.node_name, _factory_misc.color_bg)
    else:
      self.node_detail = None
      self.node = None

    self.node_detail.set_params(*self.params)

  def export_data_dict(self) -> dict:
    _category = self.node_category
    _node_type = self.node_type
    _node_name = self.node_name
    _node_params = self.node_detail.param_dict

    _data_dict = {
      "category": _category,
      "type": _node_type,
      "name": _node_name,
      "params": _node_params
    }

    return _data_dict
