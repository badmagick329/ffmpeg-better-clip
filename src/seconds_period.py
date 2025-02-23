import re

from src.exceptions import TimePeriodCreationError
from src.time_period import TimePeriod


class SecondsPeriod(TimePeriod):
    def __init__(self, start: str, end: str) -> None:
        super().__init__(start, end)

    @classmethod
    def create(cls, start: str, end: str) -> "SecondsPeriod":
        cls._validate(start, end)
        created = cls(start, end)
        if created.duration() <= 0:
            raise TimePeriodCreationError("Invalid timecode duration")
        return created

    def start_seconds(self) -> float:
        return float(self.start_input)

    def end_seconds(self) -> float:
        return float(self.end_input)

    def duration(self) -> float:
        return self.end_seconds() - self.start_seconds()

    @classmethod
    def _validate(cls, start: str, end: str):
        if not isinstance(start, str) or not isinstance(end, str):
            raise TimePeriodCreationError("Invalid timecode format")

        try:
            start_seconds = float(start)
            end_seconds = float(end)
            if start_seconds < 0 or end_seconds < 0:
                raise TimePeriodCreationError("Timecode must be positive")
        except ValueError:
            raise TimePeriodCreationError("Invalid timecode format")
