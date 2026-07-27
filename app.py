from flask import Flask, render_template

from src.utils import inspect_request
from src.logger import log_request
from src.detector import detect_attack
from src.dashboard import get_dashboard_data

app = Flask(__name__)


@app.route("/")
def home():

    request_info = inspect_request()

    attack = detect_attack(request_info)

    print("=" * 60)
    print("METHOD :", request_info["method"])
    print("PATH   :", request_info["path"])
    print("URL    :", request_info["url"])
    print("=" * 60)

    log_request(request_info, attack)

    if attack:
        return render_template("blocked.html",attack=attack,ip=request_info["ip"]),403

    return f"""
    <h1>SentinelShield</h1>

    <h3>HTTP Request Inspection</h3>

    <b>Attack Status:</b> {attack if attack else "No Attack Detected"}<br><br>

    <b>Client IP:</b> {request_info['ip']}<br><br>

    <b>Method:</b> {request_info['method']}<br><br>

    <b>URL:</b> {request_info['url']}<br><br>

    <b>Path:</b> {request_info['path']}<br><br>

    <b>Query Parameters:</b> {request_info['query_parameters']}<br><br>

    <b>Form Data:</b> {request_info['form_data']}<br><br>

    """

@app.route("/dashboard")
def dashboard():

    total_requests, blocked_requests, attack_counts, recent_logs = get_dashboard_data()

    return render_template(
        "dashboard.html",
        total_requests=total_requests,
        blocked_requests=blocked_requests,
        attack_counts=attack_counts,
        recent_logs=recent_logs
    )


if __name__ == "__main__":
    app.run(debug=True)