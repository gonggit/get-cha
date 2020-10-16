import os
from flask import Flask, request
from prediction import solve_captcha
import json

app = Flask(__name__)

@app.route('/captcha', methods=['POST'])
def index():
    if request.files:
        captcha = request.files['image']
        return solve_captcha(captcha)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
