import re

from src.time_period_factory import TimePeriodFactory


class FFmpegCmd:
    cmd: str
    pattern: re.Pattern

    def __init__(self, cmd: str) -> None:
        self.cmd = cmd
        self.pattern = re.compile(
            r"^(?P<ffmpeg>ffmpeg)(?P<start>.+?)(?P<ss>-ss\s\S+)(?P<other>.+?)(?P<to>-to\s\S+)(?P<rest>.+)$"
        )

    @classmethod
    def create(cls, cmd: str) -> "FFmpegCmd":
        created = cls(cmd)
        match = created.pattern.match(created.cmd)
        if match is None:
            raise ValueError("Invalid FFmpeg command format")
        return created

    def start_input(self) -> str:
        match = self.pattern.match(self.cmd)
        assert match is not None
        parts = match.group("ss").split(" ")
        assert len(parts) > 1
        return parts[1]

    def end_input(self) -> str:
        match = self.pattern.match(self.cmd)
        assert match is not None
        parts = match.group("to").split(" ")
        assert len(parts) > 1
        return parts[1]

    def to_duration_cmd(self) -> str:
        start_input = self.start_input()
        end_input = self.end_input()
        period = TimePeriodFactory.create(start_input, end_input)
        ss = period.start_seconds()
        t = period.duration()
        match = self.pattern.match(self.cmd)
        if match is None:
            raise ValueError("Invalid FFmpeg command format")
        return self.pattern.sub(
            rf"\g<ffmpeg> -ss {ss}\g<start>\g<other>-t {t}\g<rest>", self.cmd
        )
