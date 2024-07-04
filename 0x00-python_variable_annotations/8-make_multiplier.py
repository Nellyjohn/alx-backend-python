#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier that takes a float...
...multiplier as argument and returns a function that multiplies...
...a float by multiplier."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies its input by the given multiplier."""
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
