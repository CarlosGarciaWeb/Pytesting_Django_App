import fibonacci.naive as naive
import pytest
from ..cached import fibonacci_cached, fibonacci_lru_cached
from typing import Callable
@pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (2, 1), (20, 6765)])
def test_naive(n: int, expected: int) -> None:
    res = naive.fibonacci_naive(n=n)
    assert res == expected



@pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (2, 1), (20, 6765)])
def test_cached(n: int, expected: int) -> None:
    res = fibonacci_cached(n=n)
    assert res == expected


@pytest.mark.parametrize("fib_func", [naive.fibonacci_naive, fibonacci_cached, fibonacci_lru_cached])
@pytest.mark.parametrize("n, expected", [(0,0),(1,1),(2,1),(20, 6765)])
def test_fibonnaci_funcs(fib_func:Callable[[int], int], n: int, expected: int) -> None:
    res = fib_func(n)
    assert res == expected