VALID_CMD_CASES = [
    "ffmpeg -i input.mp4 -c:v libx264 -c:a aac -strict experimental -b:a 192k -b:v 400k -r 24 -s 1280x720 output.mp4",
    "ffmpeg -i input.mp4 -c:v libx264 -c:a aac -strict experimental -b:a 192k -b:v 400k -r 24 -s 1280x720 -ss 00:00:00.000 -to 00:00:10.000 output.mp4",
    r'ffmpeg -y -i "D:\Source\2011-07-24(일)CADTV6-1-HD 여름방학특집 SBS 인기가요(15세).tp" -c:v libsvtav1 -b:v 10M -c:a copy -fps_mode vfr -vf bwdif=mode=1:parity=0:deint=0 -ss 01:00:11.439 -to 01:03:56.196 "D:\Destination\110724 Miss A - Goodbye Baby (HD Live).mp4"',
    r'ffmpeg -y -i "D:\Source\2011-07-24(일)CADTV6-1-HD 여름방학특집 SBS 인기가요(15세).tp" -ss 30 -c copy "D:\Destination\110724 Miss A - Goodbye Baby (HD Live).mp4"',
    r'ffmpeg -y -i "/Source/2011-07-24(일)CADTV6-1-HD 여름방학특집 SBS 인기가요(15세).tp" -ss 01:00:11.439 -c copy "/Destination/110724 Miss A - Goodbye Baby (HD Live).mp4"',
    r'ffmpeg -n -i "D:\Source\2011-07-24(일)CADTV6-1-HD 여름방학특집 SBS 인기가요(15세).tp" -to 30 -c copy "D:\Destination\110724 Miss A - Goodbye Baby (HD Live).mp4"',
    r'ffmpeg -n -i "D:\Source\2011-07-24(일)CADTV6-1-HD 여름방학특집 SBS 인기가요(15세).tp" -to 01:03:56.196 -c copy "D:\Destination\110724 Miss A - Goodbye Baby (HD Live).mp4"',
]

BETTER_CMD_CASES = [
    (
        "Leave original command alone",
        "ffmpeg -i input.mp4 -c:v libx264 -c:a aac -strict experimental -b:a 192k -b:v 400k -r 24 -s 1280x720 output.mp4",
        "ffmpeg -i input.mp4 -c:v libx264 -c:a aac -strict experimental -b:a 192k -b:v 400k -r 24 -s 1280x720 output.mp4",
    ),
    (
        "Format start and end times",
        "ffmpeg -i input.mp4 -c:v libx264 -c:a aac -strict experimental -b:a 192k -b:v 400k -r 24 -s 1280x720 -ss 00:00:00.000 -to 00:00:10.000 output.mp4",
        "ffmpeg -ss 0.0 -i input.mp4 -c:v libx264 -c:a aac -strict experimental -b:a 192k -b:v 400k -r 24 -s 1280x720  -t 10.0 output.mp4",
    ),
    (
        "Format start and end times with timecodes",
        r'ffmpeg -y -i "D:\Source\2011-07-24(일)CADTV6-1-HD 여름방학특집 SBS 인기가요(15세).tp" -c:v libsvtav1 -b:v 10M -c:a copy -fps_mode vfr -vf bwdif=mode=1:parity=0:deint=0 -ss 01:00:11.439 -to 01:03:56.196 "D:\Destination\110724 Miss A - Goodbye Baby (HD Live).mp4"',
        r'ffmpeg -ss 3611.439 -y -i "D:\Source\2011-07-24(일)CADTV6-1-HD 여름방학특집 SBS 인기가요(15세).tp" -c:v libsvtav1 -b:v 10M -c:a copy -fps_mode vfr -vf bwdif=mode=1:parity=0:deint=0  -t 224.757 "D:\Destination\110724 Miss A - Goodbye Baby (HD Live).mp4"',
    ),
    (
        "Format start time with seconds",
        r'ffmpeg -y -i "D:\Source\2011-07-24(일)CADTV6-1-HD 여름방학특집 SBS 인기가요(15세).tp" -ss 30 -c copy "D:\Destination\110724 Miss A - Goodbye Baby (HD Live).mp4"',
        r'ffmpeg -ss 30.0 -y -i "D:\Source\2011-07-24(일)CADTV6-1-HD 여름방학특집 SBS 인기가요(15세).tp"  -c copy "D:\Destination\110724 Miss A - Goodbye Baby (HD Live).mp4"',
    ),
    (
        "Format start time with timecode",
        r'ffmpeg -y -i "/Source/2011-07-24(일)CADTV6-1-HD 여름방학특집 SBS 인기가요(15세).tp" -ss 01:00:11.439 -c copy "/Destination/110724 Miss A - Goodbye Baby (HD Live).mp4"',
        r'ffmpeg -ss 3611.439 -y -i "/Source/2011-07-24(일)CADTV6-1-HD 여름방학특집 SBS 인기가요(15세).tp"  -c copy "/Destination/110724 Miss A - Goodbye Baby (HD Live).mp4"',
    ),
    (
        "Format end time with seconds",
        r'ffmpeg -n -i "D:\Source\2011-07-24(일)CADTV6-1-HD 여름방학특집 SBS 인기가요(15세).tp" -to 30 -c copy "D:\Destination\110724 Miss A - Goodbye Baby (HD Live).mp4"',
        r'ffmpeg -n -i "D:\Source\2011-07-24(일)CADTV6-1-HD 여름방학특집 SBS 인기가요(15세).tp" -to 30 -c copy "D:\Destination\110724 Miss A - Goodbye Baby (HD Live).mp4"',
    ),
    (
        "Format end time with timecode",
        r'ffmpeg -n -i "D:\Source\2011-07-24(일)CADTV6-1-HD 여름방학특집 SBS 인기가요(15세).tp" -to 01:03:56.196 -c copy "D:\Destination\110724 Miss A - Goodbye Baby (HD Live).mp4"',
        r'ffmpeg -n -i "D:\Source\2011-07-24(일)CADTV6-1-HD 여름방학특집 SBS 인기가요(15세).tp" -to 01:03:56.196 -c copy "D:\Destination\110724 Miss A - Goodbye Baby (HD Live).mp4"',
    ),
]
