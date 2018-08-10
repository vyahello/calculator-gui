from abc import ABC, abstractmethod
from tkinter import Entry, StringVar
from lib.calculator.types import TypeDisplay
from lib.calculator.frame import Frame


class Screen(ABC):
    """Abstract interface for a screen."""

    @abstractmethod
    def grid(self, column_span: int = 4) -> StringVar:
        pass


class CalculatorScreen(Screen):
    """Calculator screen."""

    def __init__(self, frame: Frame, enter: TypeDisplay) -> None:
        self._screen: Entry = Entry(frame.element,
                                    font=('arial', 20, 'bold'),
                                    textvariable=enter.var,
                                    bd=30,
                                    insertwidth=4,
                                    bg="sky blue",
                                    justify='right')

    def grid(self, column_span: int = 4) -> StringVar:
        return self._screen.grid(columnspan=column_span)
