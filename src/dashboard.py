import os

LOG_FILE = "logs/requests.log"


def get_dashboard_data():

    total_requests = 0
    blocked_requests = 0
    attack_counts = {}
    recent_logs = []

    if not os.path.exists(LOG_FILE):
        return total_requests, blocked_requests, attack_counts, recent_logs

    with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()

        # Ignore empty lines
        if not line:
            continue

        # Only process actual request log lines
        if "IP=" not in line:
            continue

        total_requests += 1
        recent_logs.append(line)

        # Ignore malformed request lines
        if "Attack=" not in line:
            continue

        attack = line.split("Attack=")[1].split("|")[0].strip()

        if attack != "Normal":
            blocked_requests += 1
            attack_counts[attack] = attack_counts.get(attack, 0) + 1

    recent_logs = recent_logs[-10:]

    if total_requests == 0:
        threat_level = "LOW"

    else:
        percentage = (blocked_requests / total_requests) * 100

        if percentage < 20:
            threat_level = "LOW"
        elif percentage < 50:
            threat_level = "MEDIUM"
        else:
            threat_level = "HIGH"

    return (total_requests,blocked_requests,attack_counts,recent_logs,threat_level)