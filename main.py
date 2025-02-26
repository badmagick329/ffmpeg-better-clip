import pyperclip

from src.ffmpeg_cmd import FFmpegCmd


def main():
    ffmpeg_strs = [
        f"ffmpeg {f.strip()}" for f in pyperclip.paste().split("ffmpeg ") if f.strip()
    ]
    cmd_strings = []
    for ffmpeg_str in ffmpeg_strs:
        cmd_strings.append(FFmpegCmd.create(ffmpeg_str).to_duration_cmd())
    pyperclip.copy("\n".join(cmd_strings))


if __name__ == "__main__":
    main()
