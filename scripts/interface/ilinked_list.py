from abc import ABC, abstractmethod
from scripts.structure.str_node import StrNode

class ILinkedList(ABC):
  size: int
  first: StrNode
  last: StrNode

  @abstractmethod
  def get(self, index: int) -> any:
    pass

  @abstractmethod
  def get_first(self) -> any:
    pass

  @abstractmethod
  def get_last(self) -> any:
    pass

  @abstractmethod
  def add(self, index: int, item: any):
    pass

  @abstractmethod
  def add_first(self, item: any) -> None:
    pass

  @abstractmethod
  def add_last(self, item: any) -> None:
    pass

  @abstractmethod
  def remove(self, index: int) -> None:
    pass

  @abstractmethod
  def remove_first(self) -> None:
    pass

  @abstractmethod
  def remove_last(self) -> None:
    pass

  @abstractmethod
  def find_item(self, index: int) -> any:
    pass

  @abstractmethod
  def find_index(self, item: any) -> int:
    pass

  @abstractmethod
  def clear(self) -> None:
    pass

  @abstractmethod
  def retrieve(self) -> None:
    pass