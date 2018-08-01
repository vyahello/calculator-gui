from abc import ABC, abstractmethod
from lib.calculator.types import TypeDisplay


class Action(ABC):
    """Abstract interfaces for button actions."""

    @abstractmethod
    def click(self, number: str = None, operator: str = None) -> None:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def equals(self) -> None:
        pass


class ButtonAction(Action):
    """Concrete button action."""

    def __init__(self, data: TypeDisplay) -> None:
        self._operator: str = ''
        self._data = data

    def click(self, number: str = None, operator: str = None) -> None:
        self._operator += str(number if number else operator)
        self._data.set(self._operator)

    def clear(self) -> None:
        self._operator: str = ''
        self._data.set('')

    def equals(self) -> None:
        self._data.set(str(eval(self._operator)))
        self._operator: str = ''
