import os
import psutil
import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get the server time in IST
    ist_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
    ist_time = ist_time.strftime('%Y-%m-%d %H:%M:%S')

    # Get system info
    user = os.getlogin()
    name = "Kammila Venkata Vamsi"  # Replace with your full name

    # Get the top command output (simulate with psutil)
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    top_output = f"CPU Usage: {cpu_percent}% | Memory Usage: {memory.percent}%"

    return f"""
    <h1>Server Info</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {user}</p>
    <p><strong>Server Time (IST):</strong> {ist_time}</p>
    <p><strong>Top Output:</strong> {top_output}</p>
    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
