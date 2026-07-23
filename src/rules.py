import re

SQLI_PATTERNS = [
    r"(\%27)|(\')|(\-\-)|(\%23)|(#)",
    r"(\bOR\b|\bAND\b).*=.*",
    r"UNION\s+SELECT",
    r"SELECT\s+.*FROM",
    r"INSERT\s+INTO",
    r"DROP\s+TABLE",
    r"DELETE\s+FROM",
    r"UPDATE\s+.*SET",
]


def detect_sqli(text):

    if not text:
        return False

    text = text.upper()

    for pattern in SQLI_PATTERNS:
        if re.search(pattern, text):
            return True

    return False