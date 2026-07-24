import re

SQLI_PATTERNS = [
    r"\bOR\b.*=.*",
    r"\bAND\b.*=.*",
    r"UNION\s+SELECT",
    r"SELECT\s+.*FROM",
    r"INSERT\s+INTO",
    r"UPDATE\s+.*SET",
    r"DELETE\s+FROM",
    r"DROP\s+TABLE",
]


def detect_sqli(text):

    if not text:
        return False

    text = text.upper()

    for pattern in SQLI_PATTERNS:
        if re.search(pattern, text):
            return True

    return False

XSS_PATTERNS = [
    r"<script.*?>.*?</script>",
    r"javascript:",
    r"onerror=",
    r"onload=",
    r"alert\s*\(",
    r"<img",
    r"<iframe",
]


def detect_xss(text):

    if not text:
        return False

    for pattern in XSS_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return True

    return False

TRAVERSAL_PATTERNS = [
    r"\.\./",
    r"\.\.//",
    r"/etc/passwd",
    r"boot.ini",
    r"win.ini"
]

def detect_traversal(text):
    if not text:
        return False

    for pattern in TRAVERSAL_PATTERNS:
        if re.search(pattern,text,re.IGNORECASE):
            return True

    return False