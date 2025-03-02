import pytest

from src.exceptions import TimePeriodCreationError
from src.seconds_period import SecondsPeriod
from tests.test_seconds_period_cases import (
    INVALID_SECONDS_CASES,
    VALID_SECONDS_CASES,
    VALID_SECONDS_DURATION_CASES,
)


@pytest.mark.parametrize("test_name,start,end", INVALID_SECONDS_CASES)
def test_invalid_seconds_inputs(test_name, start, end):
    with pytest.raises(TimePeriodCreationError):
        SecondsPeriod.create(start, end)


@pytest.mark.parametrize("test_name,start,end", VALID_SECONDS_CASES)
def test_valid_seconds_inputs(test_name, start, end):
    period = SecondsPeriod.create(start, end)
    if start is None:
        assert period.start_seconds() is None
    else:
        assert period.start_seconds() == float(start)
    if end is None:
        assert period.end_seconds() is None
    else:
        assert period.end_seconds() == float(end)


@pytest.mark.parametrize("test_name,start,end,duration", VALID_SECONDS_DURATION_CASES)
def test_valid_seconds_duration(test_name, start, end, duration):
    period = SecondsPeriod.create(start, end)
    if duration is None:
        assert period.duration() is None, (
            f"test_name: {test_name} failed. Expected None"
        )
    else:
        assert period.duration() == duration, (
            f"test_name: {test_name} failed. Expected {duration}"
        )
