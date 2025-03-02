import pytest

from src.exceptions import TimePeriodCreationError
from src.timecode_period import TimecodePeriod
from tests.test_time_period_cases import (
    EDGE_TIMECODE_CASES,
    INVALID_DURATION_CASES,
    INVALID_TIMECODE_CASES,
    TIMECODE_TO_SECONDS_TEST_CASES,
    VALID_DURATION_CASES,
)


@pytest.mark.parametrize("test_name,input,expected", TIMECODE_TO_SECONDS_TEST_CASES)
def test_timecode_duration_calculation(test_name, input, expected):
    start, end = input
    expected_start, expected_end = expected
    timecode_period = TimecodePeriod(start, end)
    assert timecode_period.start_seconds() == expected_start, f"{test_name} failed"
    assert timecode_period.end_seconds() == expected_end, f"{test_name} failed"


@pytest.mark.parametrize("test_name,invalid_input", INVALID_TIMECODE_CASES)
def test_invalid_timecode_inputs(test_name, invalid_input):
    with pytest.raises(TimePeriodCreationError):
        TimecodePeriod.create(invalid_input, "00:00:00.000")


@pytest.mark.parametrize(
    "test_name,start_input,end_input,expected_start_seconds,expected_end_seconds",
    EDGE_TIMECODE_CASES,
)
def test_edge_timecode_cases(
    test_name, start_input, end_input, expected_start_seconds, expected_end_seconds
):
    period = TimecodePeriod.create(start_input, end_input)
    assert period.start_seconds() == expected_start_seconds
    assert period.end_seconds() == expected_end_seconds


@pytest.mark.parametrize("test_name,start_input,end_input", INVALID_DURATION_CASES)
def test_invalid_timecode_durations(test_name, start_input, end_input):
    with pytest.raises(TimePeriodCreationError):
        TimecodePeriod.create(start_input, end_input)


@pytest.mark.parametrize(
    "test_name,start_input,end_input,expected_duration", VALID_DURATION_CASES
)
def test_valid_timecode_durations(test_name, start_input, end_input, expected_duration):
    period = TimecodePeriod.create(start_input, end_input)
    if expected_duration is None:
        assert period.duration() is None, f"{test_name} failed"
    else:
        assert period.duration() == expected_duration, f"{test_name} failed"
