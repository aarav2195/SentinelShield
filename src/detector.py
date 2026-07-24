from src.rules import detect_sqli, detect_xss, detect_traversal, detect_lfi, detect_command_injection


def detect_attack(request_info):

    query = " ".join(request_info["query_parameters"].values())

    if detect_xss(query):
        return "Cross-Site Scripting (XSS)"

    if detect_sqli(query):
        return "SQL Injection"

    if detect_traversal(query):
        return "Directory Traversal"

    if detect_lfi(query):
        return "Local File Inclusion (LFI)"

    if detect_command_injection(query):
        return "Command Injection"

    return None