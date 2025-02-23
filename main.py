import pyperclip

from src.ffmpeg_cmd import FFmpegCmd


def main():
    ffmpeg_str = pyperclip.paste()
    ffmpeg_cmd = FFmpegCmd.create(ffmpeg_str)
    pyperclip.copy(ffmpeg_cmd.to_duration_cmd())


if __name__ == "__main__":
    main()
