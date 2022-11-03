import fibonacci.naive as naive


def test_naive() -> None:
    res = naive.fibonacci_naive(n=0)
    assert res == 0

    res = naive.fibonacci_naive(n=1)
    assert res == 1