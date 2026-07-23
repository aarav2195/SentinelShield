from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>SentinelShield</h1>
    <h3>Advanced Intrusion Detection & Web Protection System</h3>
    <p>Project Initialized Successfully.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)