from abc import ABC, abstractmethod

class ICrud (ABC):
   
  @abstractmethod
  def create (self, **kwargs):
    pass
  
  @abstractmethod
  def search_by (self, **kwargs):
    pass