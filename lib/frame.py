from abc import ABC, abstractmethod
from tkinter import Tk


class Frame(ABC):
    """Abstract interface for a frame."""

    @abstractmethod
    def element(self) -> Tk:
        pass

    @abstractmethod
    def title(self) -> None:
        pass

    @abstractmethod
    def run(self, number: int = 0) -> None:
        pass


class CalculatorFrame(Frame):
    """Calculator frame."""

    def __init__(self, name: str) -> None:
        self._frame: Tk = Tk()
        self._name = name

    @property
    def element(self) -> Tk:
        return self._frame

    def title(self) -> None:
        self._frame.title(self._name)

    def run(self, number: int = 0) -> None:
        self._frame.mainloop(number)
