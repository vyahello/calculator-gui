from abc import ABC, abstractmethod
from typing import Iterable
from lib.calculator.button import (Button, One, Two, Three, Four,
                                   Five, Six, Seven, Eight,
                                   Nine, Zero, Add, Subtract,
                                   Multiply, Clear, Equals, Divide)
from lib.calculator.action import Action
from lib.calculator.frame import Frame


class Buttons(ABC):
    """Abstract interface a buttons."""

    @abstractmethod
    def render(self) -> None:
        pass


class CalculatorButtons(Buttons):
    """Represent calculator buttons facade."""

    def __init__(self, frame: Frame, action: Action) -> None:
        self._buttons: Iterable[Button] = (
            One(frame, action),
            Two(frame, action),
            Three(frame, action),
            Four(frame, action),
            Five(frame, action),
            Six(frame, action),
            Seven(frame, action),
            Eight(frame, action),
            Nine(frame, action),
            Zero(frame, action),
            Add(frame, action),
            Subtract(frame, action),
            Multiply(frame, action),
            Clear(frame, action),
            Equals(frame, action),
            Divide(frame, action),
        )

    def render(self) -> None:
        for button in self._buttons:
            button.grid()
