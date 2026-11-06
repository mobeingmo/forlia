import subprocess, sys
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    result = subprocess.run([sys.executable, "script.py"],
                            capture_output=True, text=True, timeout=30)
    return render_template("index.html", output=result.stdout or result.stderr)

app.run(debug=True)