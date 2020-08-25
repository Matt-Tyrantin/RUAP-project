from modules.predict import predict_single

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict/', methods=['POST'])
def form_predict():
    return predict_single(request.form)

if __name__ == '__main__':
    app.run(debug=True)