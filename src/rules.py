import re


# =========================
# SQL Injection Detection
# =========================

SQLI_PATTERNS = [
    r"\bOR\b.*=.*",
    r"\bAND\b.*=.*",
    r"UNION\s+SELECT",
    r"SELECT\s+.*\s+FROM",
    r"INSERT\s+INTO",
    r"UPDATE\s+.*\s+SET",
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


# =========================
# XSS Detection
# =========================

XSS_PATTERNS = [
    r"<script.*?>",
    r"javascript:",
    r"onerror\s*=",
    r"onload\s*=",
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


# =========================
# Path Traversal Detection
# =========================

TRAVERSAL_PATTERNS = [
    r"\.\./",
    r"\.\.\\",
]


def detect_traversal(text):
    if not text:
        return False

    for pattern in TRAVERSAL_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return True

    return False


# =========================
# Local File Inclusion (LFI)
# =========================

LFI_PATTERNS = [
    r"/etc/passwd",
    r"/etc/shadow",
    r"boot\.ini",
    r"win\.ini",
    r"php://",
    r"file://",
]


def detect_lfi(text):
    if not text:
        return False

    for pattern in LFI_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return True

    return False


# =========================
# Command Injection Detection
# =========================

COMMAND_PATTERNS = [
    r";\s*[\w.-]+",
    r"&&\s*[\w.-]+",
    r"\|\s*[\w.-]+",
    r"`[^`]+`",
    r"\$\([^)]+\)",
]


def detect_command_injection(text):
    if not text:
        return False

    for pattern in COMMAND_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return True

    return False

if __name__ == "__main__":
    tests = [
        ("' OR 1=1", detect_sqli),
        ("<script>alert(1)</script>", detect_xss),
        ("../../etc/passwd", detect_traversal),
        ("/etc/passwd", detect_lfi),
        ("; ls", detect_command_injection),
    ]

    for payload, detector in tests:
        print(payload, "->", detector(payload))