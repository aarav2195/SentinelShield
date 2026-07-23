from src.rules import detect_sqli, detect_xss


def detect_attack(request_info):

    query = str(request_info["query_parameters"])

    if detect_xss(query):
        return "Cross-Site Scripting (XSS)"

    if detect_sqli(query):
        return "SQL Injection"

    return None