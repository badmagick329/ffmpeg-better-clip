from abc import ABC, abstractmethod


class TimePeriod(ABC):
    start_input: str
    end_input: str

    def __init__(self, start: str, end: str) -> None:
        self.start_input = start
        self.end_input = end

    @abstractmethod
    def start_seconds(self) -> float: ...

    @abstractmethod
    def end_seconds(self) -> float: ...

    def duration(self) -> float:
        return round(self.end_seconds() - self.start_seconds(), 3)
