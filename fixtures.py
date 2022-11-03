from datetime import datetime, timedelta
import pytest
from typing import Callable

@pytest.fixture
def time_tracker():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    time_delta = end_time - start_time
    print(f"\nruntime: {time_delta.total_seconds()}s")


class PerformanceException(Exception):
    def __init__(self, runtime: timedelta, limit: timedelta):
        self.runtime = runtime
        self.limit = limit

    def __str__(self) -> str:
        return f"Performance test failed, runtime: {self.runtime.total_seconds()}, limit: {self.limit.total_seconds()}"



def track_performance(method: Callable, runtime_limit=timedelta(seconds=2)):
    def run_function_and_validate_runtime(*args, **kw):
        start_time = datetime.now()
        result = method(*args, **kw)
        end_time = datetime.now()
        time_delta = end_time - start_time
        print(f"\nruntime: {time_delta.total_seconds()}s")

        if time_delta > runtime_limit:
            raise PerformanceException(runtime=time_delta, limit=runtime_limit)

        return result

    return run_function_and_validate_runtime
