TIMECODE_TO_SECONDS_TEST_CASES = [
    ("test time with zeros", ("00:00:00.000", "00:00:00.000"), (0.0, 0.0)),
    (
        "test time with seconds difference",
        ("00:00:00.123", "00:00:10.123"),
        (0.123, 10.123),
    ),
    (
        "test time with minutes difference",
        ("00:01:00.123", "00:10:00.123"),
        (60.123, 600.123),
    ),
    (
        "test time with hours difference",
        ("01:00:00.123", "10:00:00.123"),
        (3600.123, 36000.123),
    ),
    (
        "test time with all differences",
        ("01:01:01.123", "10:10:10.123"),
        (3661.123, 36610.123),
    ),
]

INVALID_TIMECODE_CASES = [
    ("missing milliseconds", "01:00:00"),
    ("invalid hours", "99:00:00.000"),
    ("invalid minutes", "00:60:00.000"),
    ("invalid seconds", "00:00:60.000"),
    ("wrong format", "1:2:3.000"),
    ("letters in input", "aa:bb:cc.000"),
    ("empty string", ""),
]

EDGE_TIMECODE_CASES = [
    ("start and end edges", "00:00:00.000", "23:59:59.999", 0.0, 86399.999),
]

INVALID_DURATION_CASES = [
    ("duration of 0", "01:01:01.111", "01:01:01.111"),
    ("negative duration", "01:01:01.111", "01:01:00.111"),
]

VALID_DURATION_CASES = [
    ("duration of 1 second", "01:01:01.111", "01:01:02.111", 1.0),
    ("duration of 1 minute", "01:01:01.111", "01:02:01.111", 60.0),
    ("duration of 1 hour", "01:01:01.111", "02:01:01.111", 3600.0),
    ("duration of none when start is none", None, "01:01:01.111", None),
    ("duration of none when end is none", "01:01:01.111", None, None),
    ("duration of none when both are none", None, None, None),
]
