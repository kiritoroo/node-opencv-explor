class StrNode:
  def __init__(self, prev: 'StrNode', item: any, next: 'StrNode') -> None:
    self.item: any = item
    self.prev: StrNode = prev
    self.next: StrNode = next

  def get_item(self) -> any:
    return self.item
  
  def get_node_prev(self) -> 'StrNode':
    return self.prev
   
  def get_node_next(self) -> 'StrNode':
    return self.next
  
  def set_item(self, item) -> None:
    self.item = item

  def set_node_prev(self, prev) -> None:
    self.prev = prev

  def set_node_next(self, next) -> None:
    self.next = next
