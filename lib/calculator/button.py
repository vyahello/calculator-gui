from abc import ABC, abstractmethod
from typing import Callable, Iterable
from lib.calculator.frame import Frame
from lib.calculator.types import TypeDisplay
import tkinter
from tkinter import Widget


class Button(ABC):
    """Abstract interface a button."""

    @abstractmethod
    def grid(self) -> None:
        pass


class Buttons(ABC):
    """Abstract interface a buttons."""

    @abstractmethod
    def render(self) -> None:
        pass


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


class CalculatorButton(Button):
    """Implementation of a button."""

    def __init__(self, row: int, column: int, text: str, frame: Frame, command: Callable) -> None:
        self._row = row
        self._column = column
        self._button: Widget = tkinter.Button(frame.element,
                                              padx=16,
                                              pady=16,
                                              bd=8,
                                              fg="black",
                                              font=('arial', 20, 'bold'),
                                              text=text,
                                              bg="sky blue",
                                              command=command)

    def grid(self) -> None:
        self._button.grid(row=self._row, column=self._column)


class One(Button):
    """Number ``one`` in a calculator."""

    def __init__(self, frame: Frame, action: Action) -> None:
        self._button: Button = CalculatorButton(row=3,
                                                column=0,
                                                text='1',
                                                frame=frame,
                                                command=lambda: action.click(number='1'))

    def grid(self) -> None:
        self._button.grid()


class Two(Button):
    """Number ``two`` in a calculator."""

    def __init__(self, frame: Frame, action: Action) -> None:
        self._button: Button = CalculatorButton(row=3,
                                                column=1,
                                                text='2',
                                                frame=frame,
                                                command=lambda: action.click(number='2'))

    def grid(self) -> None:
        self._button.grid()


class Three(Button):
    """Number ``three`` in a calculator."""

    def __init__(self, frame: Frame, action: Action) -> None:
        self._button: Button = CalculatorButton(row=3,
                                                column=2,
                                                text='3',
                                                frame=frame,
                                                command=lambda: action.click(number='3'))

    def grid(self) -> None:
        self._button.grid()


class Four(Button):
    """Number ``four`` in a calculator."""

    def __init__(self, frame: Frame, action: Action) -> None:
        self._button: Button = CalculatorButton(row=2,
                                                column=0,
                                                text='4',
                                                frame=frame,
                                                command=lambda: action.click(number='4'))

    def grid(self) -> None:
        self._button.grid()


class Five(Button):
    """Number ``five`` in a calculator."""

    def __init__(self, frame: Frame, action: Action) -> None:
        self._button: Button = CalculatorButton(row=2,
                                                column=1,
                                                text='5',
                                                frame=frame,
                                                command=lambda: action.click(number='5'))

    def grid(self) -> None:
        self._button.grid()


class Six(Button):
    """Number ``six`` in a calculator."""

    def __init__(self, frame: Frame, action: Action) -> None:
        self._button: Button = CalculatorButton(row=2,
                                                column=2,
                                                text='6',
                                                frame=frame,
                                                command=lambda: action.click(number='6'))

    def grid(self) -> None:
        self._button.grid()


class Seven(Button):
    """Number ``seven`` in a calculator."""

    def __init__(self, frame: Frame, action: Action) -> None:
        self._button: Button = CalculatorButton(row=1,
                                                column=0,
                                                text='7',
                                                frame=frame,
                                                command=lambda: action.click(number='7'))

    def grid(self) -> None:
        self._button.grid()


class Eight(Button):
    """Number ``eight`` in a calculator."""

    def __init__(self, frame: Frame, action: Action) -> None:
        self._button: Button = CalculatorButton(row=1,
                                                column=1,
                                                text='8',
                                                frame=frame,
                                                command=lambda: action.click(number='8'))

    def grid(self) -> None:
        self._button.grid()


class Nine(Button):
    """Number ``nine`` in a calculator."""

    def __init__(self, frame: Frame, action: Action) -> None:
        self._button: Button = CalculatorButton(row=1,
                                                column=2,
                                                text='9',
                                                frame=frame,
                                                command=lambda: action.click(number='9'))

    def grid(self) -> None:
        self._button.grid()


class Zero(Button):
    """Number ``zero`` in a calculator."""

    def __init__(self, frame: Frame, action: Action) -> None:
        self._button: Button = CalculatorButton(row=4,
                                                column=0,
                                                text='0',
                                                frame=frame,
                                                command=lambda: action.click(number='0'))

    def grid(self) -> None:
        self._button.grid()


class Add(Button):
    """``Addition`` operator button."""

    def __init__(self, frame: Frame, action: Action) -> None:
        self._button: Button = CalculatorButton(row=1,
                                                column=3,
                                                text='+',
                                                frame=frame,
                                                command=lambda: action.click(operator='+'))

    def grid(self) -> None:
        self._button.grid()


class Subtract(Button):
    """``Subtraction`` operator button."""

    def __init__(self, frame: Frame, action: Action) -> None:
        self._button: Button = CalculatorButton(row=2,
                                                column=3,
                                                text='-',
                                                frame=frame,
                                                command=lambda: action.click(operator='-'))

    def grid(self) -> None:
        self._button.grid()


class Multiply(Button):
    """``Multiplying`` operator button."""

    def __init__(self, frame: Frame, action: Action) -> None:
        self._button: Button = CalculatorButton(row=3,
                                                column=3,
                                                text='*',
                                                frame=frame,
                                                command=lambda: action.click(operator='*'))

    def grid(self) -> None:
        self._button.grid()


class Clear(Button):
    """``Clear`` operator button."""

    def __init__(self, frame: Frame, action: Action) -> None:
        self._button: Button = CalculatorButton(row=4,
                                                column=1,
                                                text='C',
                                                frame=frame,
                                                command=action.clear)

    def grid(self) -> None:
        self._button.grid()


class Equals(Button):
    """``Equals`` operator button."""

    def __init__(self, frame: Frame, action: Action) -> None:
        self._button: Button = CalculatorButton(row=4,
                                                column=2,
                                                text='=',
                                                frame=frame,
                                                command=action.equals)

    def grid(self) -> None:
        self._button.grid()


class Divide(Button):
    """``Division`` operator button."""

    def __init__(self, frame: Frame, action: Action) -> None:
        self._button: Button = CalculatorButton(row=4,
                                                column=3,
                                                text='/',
                                                frame=frame,
                                                command=lambda: action.click(operator='/'))

    def grid(self) -> None:
        self._button.grid()


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
