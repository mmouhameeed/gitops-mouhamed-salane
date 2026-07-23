from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)

NOM = os.environ.get("STUDENT_NAME", "Mouhamed-Salane")
VERSION = os.environ.get("APP_VERSION", "v1.0.0")

@app.route("/")
def home():
    return f"""
    <html>
      <head><title>{NOM}</title></head>
      <body style="font-family: sans-serif; text-align:center; margin-top:100px;">
        <h1>{NOM}</h1>
        <p>Projet GitOps Observable - Kubernetes</p>
        <p>Version: {VERSION}</p>
        <p>Pod: {socket.gethostname()}</p>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="ok", pod=socket.gethostname())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
