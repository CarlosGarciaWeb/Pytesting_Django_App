from datetime import datetime
import pytest

@pytest.fixture
def time_tracker():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    time_delta = end_time - start_time
    print(f"\nruntime: {time_delta.total_seconds()}s")
