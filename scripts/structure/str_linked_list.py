from scripts.interface.ilinked_list import ILinkedList
from scripts.structure.str_node import StrNode

class LinkedList(ILinkedList):
  def __init__(self) -> None:
    super().__init__()
    self.size = 0
    self.first = None
    self.last = None

  def _is_empty(self) -> bool:
    return self.first == None and self.last == None and self.size == 0
  
  def _is_element_index(self, index: int) -> bool:
    return index >=0 and index < self.size
  
  def _is_position_index(self, index: int) -> bool:
    return index >= 0 and index <= self.size
    
  def _check_element_index(self, index: int) -> None:
    if not self._is_element_index(index):
      raise ValueError(f'[Out of Bound] Index: {index}')
    
  def _check_position_index(self, index: int) -> None:
    if not self._is_position_index(index):
      raise ValueError(f'[Out of Bound] Index: {index}')
    
  def _link(self, item: any, succ: StrNode) -> None:
    x = succ.get_node_prev()
    new_node = StrNode(x, item, succ)
    succ.prev = new_node
    if x is None:
      self.first = new_node
    else:
      x.set_node_next(new_node) 
    self.size += 1

  def _link_first(self, item: any) -> None:
    x = self.first
    new_node = StrNode(None, item, x)
    self.first = new_node
    if x is None:
      self.last = new_node
    else:
      x.set_node_prev(new_node)
    self.size += 1

  def _link_last(self, item: any) -> None:
    x = self.last
    new_node = StrNode(x, item, None)
    self.last = new_node
    if x is None:
      self.first = new_node
    else:
      x.set_node_next(new_node)
    self.size += 1

  def _unlink(self, x: StrNode) -> None:
    _prev = x.get_node_prev()
    _next = x.get_node_next()

    if _prev is None:
      self.first = _next
    else:
      _prev.set_node_next(_next)
      x.set_node_prev(None)

    if _next is None:
      self.last = _prev
    else:
      _next.set_node_prev(_prev)
      x.set_node_next(None)

    x.set_item(None)
    self.size -= 1

  def _unlink_fist(self) -> None:
    f = self.first
    next = f.get_node_next()
    f.set_item(None)
    self.first = next
    if next is None:
      self.last = None
    else:
      f.set_node_next(None)
      next.set_node_prev(None)
    self.size -= 1

  def _unlink_last(self) -> None:
    l = self.last
    prev = l.get_node_prev()
    l.set_item(None)
    self.last = prev
    if prev is None:
      self.first = None
    else:
      l.set_node_prev(None)
      prev.set_node_next(None)
    self.size -= 1

  def _node(self, index: int) -> StrNode:
    x = self.first
    for i in range(index):
      x = x.get_node_next()
    return x
  
  def get_size(self) -> int:
    return self.size
  
  def get(self, index: int) -> any:
    self._check_element_index(index)
    return self._node(index).get_item()
  
  def get_first(self) -> any:
    if self.first is None:
      return None
    return self.first.get_item()
  
  def get_last(self) -> any:
    if self.last is None:
      return None
    return self.last.get_item()
  
  def set(self, index: int, item: any) -> None:
    self._check_element_index()
    self._node(index).set_item(item)

  def set_fist(self, item: any) -> None:
    if self.first is None:
      return
    self.first.set_item(item)

  def set_last(self, item: any) -> None:
    if self.last is None:
      return
    self.last.set_item(item)

  def add(self, index: int, item: any) -> None:
    self._check_position_index(index)
    if index == self.size:
      self._link_last(item)
    else:
      self._link(item, self._node(index))

  def add_first(self, item: any) -> None:
    self._link_first(item)

  def add_last(self, item: any) -> None:
    self._link_last(item)

  def remove(self, index: int) -> None:
    self._check_element_index(index)
    self._unlink(self._node(index))

  def remove_first(self) -> None:
    if self.first is not None:
      self._unlink_fist()

  def remove_last(self) -> None:
    if self.last is not None:
      self._unlink_last()

  def find_item(self, index: int) -> any:
    self._check_element_index(index)
    return self._node(index).get_item()
  
  def find_index(self, item: any) -> int:
    x = self.first
    for i in range(self.size):
      if x.get_item() == item:
        return i
      x = x.get_node_next()
    return None
  
  def clear(self) -> None:
    x = self.first
    while x is not None:
      next_node = x.get_node_next()
      x.set_item(None)
      x.set_node_prev(None)
      x.set_node_next(None)
      x = next_node
    self.first = self.last = None
    self.size = 0
  
  def retrieve(self) -> None:
    if self.first is None:
      print("Linked list is empty")
    else:
      current_node = self.first
      while current_node is not None:
        prev_node = current_node.get_node_prev()
        prev_hex = hex(id(prev_node)) if prev_node is not None else None
        current_hex = hex(id(current_node))
        next_node = current_node.get_node_next()
        next_hex = hex(id(next_node)) if next_node is not None else None
        print(f'[{prev_hex} -> {current_hex} -> {next_hex}]\n')
        current_node = current_node.next