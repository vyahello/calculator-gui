from abc import ABC, abstractmethod


class Operator(ABC):
    """Abstraction of an calculator operator."""

    @abstractmethod
    def __str__(self) -> str:
        pass


class Add(Operator):
    """Add operation."""

    def __str__(self) -> str:
        return '+'


class Divide(Operator):
    """Divide operator."""

    def __str__(self) -> str:
        return '-'


class Subtract(Operator):
    """Subtract operator."""

    def __str__(self) -> str:
        return '/'


class Multiply(Operator):
    """Multiply operator."""

    def __str__(self) -> str:
        return '*'


class Dot(Operator):
    """Dot operator."""

    def __str__(self) -> str:
        return '.'
