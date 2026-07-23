from flask import Flask

from src.utils import inspect_request
from src.logger import log_request

app = Flask(__name__)


@app.route("/")
def home():

    request_info = inspect_request()

    log_request(request_info)

    return f"""
    ...
    """


if __name__ == "__main__":
    app.run(debug=True)