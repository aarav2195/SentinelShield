from src.rules import detect_sqli, detect_xss, detect_traversal


def detect_attack(request_info):

    query = " ".join(request_info["query_parameters"].values())

    if detect_xss(query):
        return "Cross-Site Scripting (XSS)"

    if detect_sqli(query):
        return "SQL Injection"

    if detect_traversal(query):
        return "Directory Traversal"

    return None