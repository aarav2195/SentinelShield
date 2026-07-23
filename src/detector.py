from src.rules import detect_sqli


def detect_attack(request_info):

    query = str(request_info["query_parameters"])

    if detect_sqli(query):
        return "SQL Injection"

    return None