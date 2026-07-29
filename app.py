from flask import Flask, render_template

from src.utils import inspect_request
from src.logger import log_request
from src.detector import detect_attack
from src.dashboard import get_dashboard_data
from src.rate_limiter import check_rate_limit

app = Flask(__name__)


@app.route("/")
def home():

    request_info = inspect_request()

    if check_rate_limit(request_info["ip"]):
        log_request(request_info, "Rate Limit Exceeded")

        return render_template("blocked.html",attack="Rate Limit Exceeded",ip=request_info["ip"]), 429

    attack = detect_attack(request_info)

    log_request(request_info, attack)

    if attack:
        return render_template("blocked.html",attack=attack,ip=request_info["ip"]),403

    return render_template("home.html")

@app.route("/inspect")
def inspect():

    request_info = inspect_request()

    if check_rate_limit(request_info["ip"]):
        log_request(request_info, "Rate Limit Exceeded")

        return render_template("blocked.html",attack="Rate Limit Exceeded",ip=request_info["ip"]),429

    attack = detect_attack(request_info)

    log_request(request_info, attack)

    if attack:
        return render_template("blocked.html",attack=attack,ip=request_info["ip"]),403

    return render_template("inspect.html",request_info=request_info,attack=attack)

@app.route("/dashboard")
def dashboard():

    total_requests, blocked_requests, attack_counts, recent_logs, threat_level = get_dashboard_data()

    return render_template(
        "dashboard.html",
        total_requests=total_requests,
        blocked_requests=blocked_requests,
        attack_counts=attack_counts,
        recent_logs=recent_logs,
        threat_level=threat_level
    )

if __name__ == "__main__":
    app.run(debug=True)