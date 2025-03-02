INVALID_SECONDS_CASES = [
    ("negative end", "0", "-12"),
    ("mixed format", "0", "00:00:01.000"),
    ("letters in end input", "0", "aa"),
    ("empty end string", "0", ""),
    ("none end value", "", "123"),
]

VALID_SECONDS_CASES = [
    ("positive end", "0", "12"),
    ("positive float end", "0", "12.5"),
    ("positive float start", "0.5", "12"),
    ("positive start", "0.5", "12"),
    ("None start", None, "12"),
    ("None end", "0.5", None),
    ("None both", None, None),
]

VALID_SECONDS_DURATION_CASES = [
    ("positive end", "0", "12", 12),
    ("positive float end", "0", "12.5", 12.5),
    ("positive float start", "0.5", "12", 11.5),
    ("positive start", "0.5", "12", 11.5),
    ("None start", None, "12", None),
    ("None end", "0.5", None, None),
    ("None both", None, None, None),
]
