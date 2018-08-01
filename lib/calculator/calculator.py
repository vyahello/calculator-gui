from abc import ABC, abstractmethod
from lib.calculator.button import ButtonAction, Buttons, CalculatorButtons
from lib.calculator.frame import Frame, CalculatorFrame
from lib.calculator.screen import Screen, CalculatorScreen
from lib.calculator.types import TypeDisplay, StringDisplay


class Device(ABC):
    """Abstraction of some device."""

    @abstractmethod
    def run(self) -> None:
        pass


class _Calculator(Device):
    """Represent calculator device."""

    def __init__(self, frame: Frame, display: TypeDisplay) -> None:
        self._frame = frame
        self._screen: Screen = CalculatorScreen(frame, display)
        self._buttons: Buttons = CalculatorButtons(frame, ButtonAction(display))

    def run(self) -> None:
        self._frame.title()
        self._screen.grid()
        self._buttons.render()
        self._frame.run()


class GUICalculator(Device):
    """Represent GUI calculator device."""

    def __init__(self, name: str = 'Calculator') -> None:
        self._calculator: Device = _Calculator(CalculatorFrame(name), StringDisplay())

    def run(self) -> None:
        self._calculator.run()
