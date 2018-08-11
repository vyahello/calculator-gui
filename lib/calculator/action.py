from abc import ABC, abstractmethod
from typing import Tuple
from lib.calculator.operators import Operator, Add, Subtract, Divide, Multiply, Dot, Module, Power, Pi
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
        self._operators: Tuple[Operator] = (
            Add(), Subtract(), Divide(), Multiply(), Dot(), Module(), Power(), Pi()
        )
        self._input: str = ''
        self._data = data

    def click(self, number: str = None, operator: str = None) -> None:
        if number:
            self._input += str(number)
        else:
            for op in map(lambda _operator: str(_operator), self._operators):
                if op == operator and op not in self._input:
                    self._input += op
        self._data.set(self._input)

    def clear(self) -> None:
        self._input: str = ''
        self._data.set('')

    def equals(self) -> None:
        self._data.set(str(eval(self._input)))
        self._input: str = ''
