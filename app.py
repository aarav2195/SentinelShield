from flask import Flask, render_template

from src.utils import inspect_request
from src.logger import log_request
from src.detector import detect_attack

app = Flask(__name__)


@app.route("/")
def home():

    request_info = inspect_request()

    attack = detect_attack(request_info)

    log_request(request_info, attack)

    if attack:
        return render_template("blocked.html"),403

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


if __name__ == "__main__":
    app.run(debug=True)