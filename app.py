from flask import Flask, render_template, request

from src.utils import inspect_request
from src.logger import log_request
from src.detector import detect_attack
from src.dashboard import get_dashboard_data
from src.rate_limiter import check_rate_limit

app = Flask(__name__)

last_request = None
last_attack = None

@app.route("/")
def home():

    global last_request, last_attack

    request_info = inspect_request()

    if check_rate_limit(request_info["ip"]):
        last_request = request_info.copy()
        last_attack = "Rate Limit Exceeded"

        if last_request["path"] not in ["/inspect", "/dashboard", "/favicon.ico"]:
            log_request(request_info, "Rate Limit Exceeded")

        return render_template("blocked.html",attack="Rate Limit Exceeded",ip=request_info["ip"]), 429

    attack = detect_attack(request_info)

    last_request = request_info.copy()
    last_attack = attack

    if request_info["path"] not in ["/inspect", "/dashboard", "/favicon.ico"]:
        log_request(request_info, attack)

    if attack:
        return render_template("blocked.html",attack=attack,ip=request_info["ip"]),403
    
    return render_template("home.html")

@app.route("/inspect")
def inspect():

    global last_request, last_attack

    if last_request is None:

        last_request = {
            "ip": "-",
            "method": "-",
            "path": "-",
            "url": "No requests inspected yet.",
            "query_parameters": "-",
            "form_data": "-"
        }

        last_attack = None

    return render_template("inspect.html",request_info=last_request,attack=last_attack)

@app.route("/demo/<attack_type>")
def demo_attack(attack_type):
    global last_request, last_attack

    demo_payloads = {
        "sqli": "' OR 1=1",
        "command": "; ls"
    }

    if attack_type not in demo_payloads:
        return "Invalid demo attack type", 400

    payload = demo_payloads[attack_type]

    request_info = {
        "ip": request.remote_addr,
        "method": "GET",
        "path": "/demo/" + attack_type,
        "url": request.url,
        "headers": dict(request.headers),
        "query_parameters": {
            "q": payload
        },
        "form_data": {}
    }

    attack = detect_attack(request_info)

    last_request = request_info.copy()
    last_attack = attack

    log_request(request_info, attack)

    if attack:
        return render_template(
            "blocked.html",
            attack=attack,
            ip=request_info["ip"]
        ), 403

    return "Demo request was not detected", 200

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
    app.run(host="0.0.0.0", port=5000, debug=True)