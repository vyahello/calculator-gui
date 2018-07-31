from lib.calculator.calculator import Device, Calculator
from lib.calculator.frame import CalculatorFrame
from lib.calculator.types import StringDisplay


if __name__ == '__main__':
    calculator: Device = Calculator(frame=CalculatorFrame("Calculator"), display=StringDisplay())
    calculator.run()
