import os
from flask import Flask, render_template, request, redirect
from solve_captchas_with_model import predict

app = Flask(__name__)


@app.route('/predict', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.files:
            captcha = request.files['image']
            fileName = captcha.filename
            if fileName.split('.')[1] != 'png':
                return ''
            captcha.save(os.path.join('testing', fileName))
            return predict(fileName)
            


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
