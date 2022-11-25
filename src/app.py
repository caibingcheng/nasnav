import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    host = os.getenv('NAV_HOST', '0.0.0.0')
    port = os.getenv('NAV_PORT', '8080')
    app.run(host=host, port=port)
