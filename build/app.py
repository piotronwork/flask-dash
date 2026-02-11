from flask import Flask, render_template
from datetime import datetime
import socket
import os
import psutil
import platform

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK", 200

@app.route("/")
def index():
    hostname = socket.gethostname();
    ip = socket.gethostbyname(hostname)
    port = os.environ.get("PORT", "5000")
    server_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # System info
    system_info = {
        "os": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "python": platform.python_version()
    }

    cpu_percent = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory()

    # Procesy
    process_count = len(psutil.pids())

    return render_template(
        "index.html",
        hostname=hostname,
        ip=ip,
        port=port,
        server_date=server_date,
        system_info=system_info,
        cpu_percent=cpu_percent,
        ram=ram,
        process_count=process_count
    )

