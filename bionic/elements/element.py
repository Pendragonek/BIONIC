"""Element"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Type


@dataclass
class Element(ABC):
    """Element class"""
    mass: float = 0
    temperature: float = 0

    @property
    @abstractmethod
    def name(self) -> str:
        """Return name of element"""
        pass

    @property
    @abstractmethod
    def shc(self) -> float:
        """Return SHC of element"""
        pass

    @property
    def heat(self) -> float:
        """Return heat amount"""
        return self.shc * self.mass * self.temperature

    def __add__(self, other: 'Element') -> 'Element':
        element_type: Type[Element] = type(self)
        if not isinstance(other, element_type):
            raise TypeError
        mass = self.mass + other.mass
        temperature = (self.mass * self.temperature + other.mass * other.temperature) / mass
        return element_type(mass, temperature)
