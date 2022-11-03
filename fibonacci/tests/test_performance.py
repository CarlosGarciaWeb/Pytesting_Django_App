from fibonacci.dynamic import fibonacci_dynamic_On
import pytest
from fixtures import track_performance
from time import sleep

@pytest.mark.performance
@track_performance
def test_performance():
    fibonacci_dynamic_On(1000)
