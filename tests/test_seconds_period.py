import pytest

from src.exceptions import TimePeriodCreationError
from src.seconds_period import SecondsPeriod
from tests.test_seconds_period_cases import INVALID_TIMECODE_CASES


@pytest.mark.parametrize("test_name,start,end", INVALID_TIMECODE_CASES)
def test_invalid_seconds_inputs(test_name, start, end):
    with pytest.raises(TimePeriodCreationError):
        SecondsPeriod.create(start, end)
