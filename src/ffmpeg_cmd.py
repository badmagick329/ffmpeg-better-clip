import re

from src.time_period_factory import TimePeriodFactory


class FFmpegCmd:
    cmd: str
    pattern: re.Pattern
    matched: re.Match

    def __init__(self, cmd: str) -> None:
        self.cmd = cmd
        # self.patternv0 = re.compile(
        #     r"^(?P<ffmpeg>ffmpeg)(?P<start>.+?)(?P<ss>-ss\s\S+)(?P<other>.+?)(?P<to>-to\s\S+)(?P<rest>.+)$"
        # )
        self.pattern = re.compile(
            r"^(?P<ffmpeg>ffmpeg)(?P<start>(?:(?!-ss|-to).)*)(?P<ss>-ss\s+\S+)?(?P<mid>(?:(?!-ss|-to).)*)(?P<to>-to\s+\S+)?(?P<rest>.*)$"
        )
        match = self.pattern.match(self.cmd)
        if match is None:
            raise ValueError("Invalid FFmpeg command format")
        self.matched = match

    @classmethod
    def create(cls, cmd: str) -> "FFmpegCmd":
        created = cls(cmd)
        match = created.pattern.match(created.cmd)
        if match is None:
            raise ValueError("Invalid FFmpeg command format")
        return created

    def start_input(self) -> str | None:
        ss = self.matched.group("ss")
        if ss is None:
            return None
        parts = ss.split(" ")
        assert len(parts) > 1
        return parts[1]

    def end_input(self) -> str | None:
        to = self.matched.group("to")
        if to is None:
            return None
        parts = to.split(" ")
        assert len(parts) > 1
        return parts[1]

    def to_better_cmd(self) -> str:
        start_input = self.start_input()
        end_input = self.end_input()
        period = TimePeriodFactory.create(start_input, end_input)
        ss = period.start_seconds()
        t = period.duration()
        if ss is not None and t is None:
            return self.pattern.sub(
                rf"\g<ffmpeg> -ss {ss}\g<start>\g<mid>\g<rest>", self.cmd
            )

        if ss is not None and t is not None:
            return self.pattern.sub(
                rf"\g<ffmpeg> -ss {ss}\g<start>\g<mid>-t {t}\g<rest>", self.cmd
            )

        return self.cmd
