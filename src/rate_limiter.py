from time import time

REQUEST_LIMIT = 10
TIME_WINDOW = 60

request_history = {}


def check_rate_limit(ip):

    current_time = time()

    if ip not in request_history:
        request_history[ip] = []

    request_history[ip] = [
        timestamp
        for timestamp in request_history[ip]
        if current_time - timestamp < TIME_WINDOW
    ]

    request_history[ip].append(current_time)

    print("=" * 40)
    print("IP:", ip)
    print("Current Request Count:", len(request_history[ip]))
    print("=" * 40)

    if len(request_history[ip]) > REQUEST_LIMIT:
        return True

    return False