INVALID_TIMECODE_CASES = [
    ("negative end", "0", "-12"),
    ("mixed format", "0", "00:00:01.000"),
    ("letters in end input", "0", "aa"),
    ("empty end string", "0", ""),
    ("none end value", "0", None),
]
