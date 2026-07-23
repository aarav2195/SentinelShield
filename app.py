from flask import Flask
from src.utils import inspect_request

app = Flask(__name__)


@app.route("/")
def home():

    request_info = inspect_request()

    return f"""
    <h1>SentinelShield</h1>

    <h3>HTTP Request Inspection</h3>

    <b>Client IP:</b> {request_info['ip']}<br><br>

    <b>Method:</b> {request_info['method']}<br><br>

    <b>URL:</b> {request_info['url']}<br><br>

    <b>Path:</b> {request_info['path']}<br><br>

    <b>Query Parameters:</b> {request_info['query_parameters']}<br><br>

    <b>Form Data:</b> {request_info['form_data']}<br><br>

    """


if __name__ == "__main__":
    app.run(debug=True)