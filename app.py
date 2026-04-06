from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/status')
def status():
    return jsonify(status="Running", version="1.0.0")

@app.route('/about')
def about():
    return jsonify(message="This project demonstrates CI/CD pipeline with Docker.")

# (Optional) keep API version if you want
@app.route('/api/status')
def api_status():
    return jsonify(status="Running", version="1.0.0")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)