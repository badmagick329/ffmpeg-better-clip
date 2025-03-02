import re

from src.exceptions import TimePeriodCreationError
from src.time_period import TimePeriod


class TimecodePeriod(TimePeriod):
    def __init__(self, start: str | None, end: str | None) -> None:
        super().__init__(start, end)

    @classmethod
    def create(cls, start: str | None, end: str | None) -> "TimecodePeriod":
        cls._validate(start, end)
        created = cls(start, end)
        duration = created.duration()

        if duration is not None and duration <= 0:
            raise TimePeriodCreationError("Invalid timecode duration")
        return created

    def start_seconds(self) -> float | None:
        return None if self.start_input is None else self._to_seconds(self.start_input)

    def end_seconds(self) -> float | None:
        return None if self.end_input is None else self._to_seconds(self.end_input)

    @staticmethod
    def _to_seconds(time_str: str) -> float:
        hours, minutes, seconds = [float(t) for t in time_str.split(":")]
        return hours * 3600 + minutes * 60 + seconds

    @classmethod
    def _validate(cls, start: str | None, end: str | None):
        start_is_valid = start is None or isinstance(start, str)
        end_is_valid = end is None or isinstance(end, str)
        if not start_is_valid or not end_is_valid:
            raise TimePeriodCreationError(f"Invalid timecode format - {start} {end}")

        time_regex = re.compile(r"^([0-9]{2}):([0-9]{2}):([0-9]{2})\.([0-9]{1,3})$")

        time_strs = []
        if start is not None:
            time_strs.append(start)
        if end is not None:
            time_strs.append(end)

        for time_str in time_strs:
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
