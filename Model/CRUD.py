from abc import ABC, abstractmethod


class ICrud (ABC):
   
  @abstractmethod
  def create (self, **kwargs):
    raise NotImplementedError
  
  @abstractmethod
  def search_by (self, **kwargs):
    raise NotImplementedError

  @staticmethod
  def has_many (one, many):
    for item in many:
      one.associated_to(item)