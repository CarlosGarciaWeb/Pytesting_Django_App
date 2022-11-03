from fibonacci.dynamic import fibonacci_dynamic_On
import pytest

@pytest.mark.performance
def test_performance():
    fibonacci_dynamic_On(1000)
