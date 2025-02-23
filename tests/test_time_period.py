import pytest
from src.timecode_period import TimecodePeriod

from tests.test_time_period_cases import (
    EDGE_TIMECODE_CASES,
    INVALID_DURATION_CASES,
    INVALID_TIMECODE_CASES,
    TIMECODE_SECONDS_TEST_CASES,
)


@pytest.mark.parametrize("test_name,input,expected", TIMECODE_SECONDS_TEST_CASES)
def test_timecode_duration_calculation(test_name, input, expected):
    start, end = input
    expected_start, expected_end = expected
    timecode_period = TimecodePeriod(start, end)
    assert timecode_period.start_seconds() == expected_start, f"{test_name} failed"
    assert timecode_period.end_seconds() == expected_end, f"{test_name} failed"


@pytest.mark.parametrize(
    "test_name,invalid_input,expected_error", INVALID_TIMECODE_CASES
)
def test_invalid_timecode_inputs(test_name, invalid_input, expected_error):
    with pytest.raises(ValueError) as exc_info:
        TimecodePeriod.create(invalid_input, "00:00:00.000")
    assert expected_error in str(exc_info.value)


@pytest.mark.parametrize(
    "test_name,start_input,end_input,expected_seconds", EDGE_TIMECODE_CASES
)
def test_edge_timecode_cases(test_name, start_input, end_input, expected_seconds):
    period = TimecodePeriod.create(start_input, end_input)
    assert period.start_seconds() == 0.0
    assert period.end_seconds() == expected_seconds


@pytest.mark.parametrize("test_name,start_input,end_input", INVALID_DURATION_CASES)
def test_invalid_timecode_durations(test_name, start_input, end_input):
    with pytest.raises(ValueError):
        TimecodePeriod.create(start_input, end_input)
