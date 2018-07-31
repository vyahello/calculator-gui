from lib.calculator import Calculator, Device
from lib.frame import CalculatorFrame
from lib.types import StringDisplay


if __name__ == '__main__':
    calculator: Device = Calculator(frame=CalculatorFrame("Calculator"), display=StringDisplay())
    calculator.run()
