from abc import ABC, abstractmethod


class TimePeriod(ABC):
    start_input: str | None
    end_input: str | None

    def __init__(self, start: str | None, end: str | None) -> None:
        self.start_input = start
        self.end_input = end

    @abstractmethod
    def start_seconds(self) -> float | None: ...

    @abstractmethod
    def end_seconds(self) -> float | None: ...

    def duration(self) -> float | None:
        end_seconds = self.end_seconds()
        start_seconds = self.start_seconds()
        if start_seconds is not None and end_seconds is not None:
            return round(end_seconds - start_seconds, 3)

        return None
