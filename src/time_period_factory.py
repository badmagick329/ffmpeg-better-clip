from src.exceptions import TimePeriodCreationError
from src.seconds_period import SecondsPeriod
from src.time_period import TimePeriod
from src.timecode_period import TimecodePeriod


class TimePeriodFactory:
    @staticmethod
    def create(start_input: str, end_input: str) -> TimePeriod:
        try:
            return TimecodePeriod.create(start_input, end_input)
        except TimePeriodCreationError:
            pass

        try:
            return SecondsPeriod.create(start_input, end_input)
        except TimePeriodCreationError:
            pass

        raise ValueError("Invalid time period format")
