import re

from src.exceptions import TimePeriodCreationError
from src.time_period import TimePeriod


class TimecodePeriod(TimePeriod):
    def __init__(self, start: str, end: str) -> None:
        super().__init__(start, end)

    @classmethod
    def create(cls, start: str, end: str) -> "TimecodePeriod":
        cls._validate(start, end)
        created = cls(start, end)
        if created.duration() <= 0:
            raise TimePeriodCreationError("Invalid timecode duration")
        return created

    def start_seconds(self) -> float:
        return self._to_seconds(self.start_input)

    def end_seconds(self) -> float:
        return self._to_seconds(self.end_input)

    @staticmethod
    def _to_seconds(time_str: str) -> float:
        hours, minutes, seconds = [float(t) for t in time_str.split(":")]
        return hours * 3600 + minutes * 60 + seconds

    @classmethod
    def _validate(cls, start: str, end: str):
        if not isinstance(start, str) or not isinstance(end, str):
            raise TimePeriodCreationError("Invalid timecode format")

        time_regex = re.compile(r"^([0-9]{2}):([0-9]{2}):([0-9]{2})\.([0-9]{1,3})$")

        for time_str in [start, end]:
            match = time_regex.match(time_str)
            if not match:
                raise TimePeriodCreationError("Invalid timecode format")

            hours, minutes, seconds, _ = map(int, match.groups())

            if hours > 23:
                raise TimePeriodCreationError("Hours must be between 00-23")
            if minutes > 59:
                raise TimePeriodCreationError("Minutes must be between 00-59")
            if seconds > 59:
                raise TimePeriodCreationError("Seconds must be between 00-59")
