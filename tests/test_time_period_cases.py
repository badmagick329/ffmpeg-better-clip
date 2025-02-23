TIMECODE_SECONDS_TEST_CASES = [
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
    ("missing milliseconds", "01:00:00", "Invalid timecode format"),
    ("invalid hours", "99:00:00.000", "Hours must be between 00-23"),
    ("invalid minutes", "00:60:00.000", "Minutes must be between 00-59"),
    ("invalid seconds", "00:00:60.000", "Seconds must be between 00-59"),
    ("wrong format", "1:2:3.000", "Invalid timecode format"),
    ("letters in input", "aa:bb:cc.000", "Invalid timecode format"),
    ("empty string", "", "Invalid timecode format"),
    ("none value", None, "Invalid timecode format"),
]

EDGE_TIMECODE_CASES = [
    ("start and end edges", "00:00:00.000", "23:59:59.999", 86399.999),
]

INVALID_DURATION_CASES = [
    ("duration of 0", "01:01:01.111", "01:01:01.111"),
    ("negative duration", "01:01:01.111", "01:01:00.111"),
]
