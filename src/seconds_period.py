import re

from src.exceptions import TimePeriodCreationError
from src.time_period import TimePeriod


class SecondsPeriod(TimePeriod):
    def __init__(self, start: str | None, end: str | None) -> None:
        super().__init__(start, end)

    @classmethod
    def create(cls, start: str | None, end: str | None) -> "SecondsPeriod":
        cls._validate(start, end)
        created = cls(start, end)
        duration = created.duration()

        if duration and duration <= 0:
            raise TimePeriodCreationError("Invalid timecode duration")
        return created

    def start_seconds(self) -> float | None:
        return None if self.start_input is None else float(self.start_input)

    def end_seconds(self) -> float | None:
        return None if self.end_input is None else float(self.end_input)

    @classmethod
    def _validate(cls, start: str | None, end: str | None):
        start_is_valid = start is None or isinstance(start, str)
        if not start_is_valid:
            raise TimePeriodCreationError(f"Invalid start timecode format - {start}")
        end_is_valid = end is None or isinstance(end, str)
        if not end_is_valid:
            raise TimePeriodCreationError(f"Invalid end timecode format - {end}")

        try:
            start_seconds = float(start) if start is not None else None
            end_seconds = float(end) if end is not None else None
            if start_seconds is None or end_seconds is None:
                return

            if start_seconds < 0 or end_seconds < min(start_seconds, 0):
                raise TimePeriodCreationError(
                    "Timecode must be positive and end time must be greater than start time"
                )
        except ValueError:
            raise TimePeriodCreationError("Invalid timecode format")
