from lib.calculator.action import ButtonAction
from lib.calculator.buttons import CalculatorButtons
from lib.calculator.frame import CalculatorFrame
from lib.calculator.types import StringDisplay

_name: str = 'calculator'
_buttons: int = 16


def test_calculator_buttons() -> None:
    assert len(CalculatorButtons(CalculatorFrame(_name), ButtonAction(StringDisplay()))) == _buttons
