import pytest

from src.ffmpeg_cmd import FFmpegCmd
from tests.test_ffmpeg_cmd_cases import BETTER_CMD_CASES, VALID_CMD_CASES


@pytest.mark.parametrize("cmd", VALID_CMD_CASES)
def test_ffmpeg_cmd_ctor(cmd):
    assert FFmpegCmd.create(cmd) is not None


@pytest.mark.parametrize("test_name,cmd,expected_duration", BETTER_CMD_CASES)
def test_ffmpeg_better_cmd(test_name, cmd, expected_duration):
    ffmpeg_cmd = FFmpegCmd.create(cmd)
    assert ffmpeg_cmd.to_better_cmd() == expected_duration, f"{test_name} failed"
