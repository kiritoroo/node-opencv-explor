from scripts.interface.inode import INode
from scripts.interface.inode_detail import INodeDetail

class NodeData:
  def __init__(self, node_catory: str, node_type: str, node_name: str, params: list) -> None:
    self.node_category = node_catory
    self.node_type = node_type
    self.node_name = node_name
    self.params = params
    self.node: INode = None
    self.node_detail: INodeDetail = None
    self.init()

  def init() -> None:
    pass