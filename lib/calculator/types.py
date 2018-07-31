from abc import ABC, abstractmethod
from tkinter import StringVar, Variable


class TypeDisplay(ABC):
    """Abstract interface for a screen."""

    @abstractmethod
    def var(self) -> Variable:
        pass

    @abstractmethod
    def set(self, value: str) -> None:
        pass


class StringDisplay(TypeDisplay):
    """Represent `StringDisplay` type variable."""

    def __init__(self) -> None:
        self._string: Variable = StringVar()

    @property
    def var(self) -> Variable:
        return self._string

    def set(self, value: str) -> None:
        self._string.set(value)
