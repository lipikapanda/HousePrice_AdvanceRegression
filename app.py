from flask import Flask, jsonify,  request, render_template
from sklearn.externals import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)
model_load = joblib.load("./models/hp_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if (request.method == 'POST'):
        int_features = [x for x in request.form.values()]
        final_features = pd.DataFrame([np.array(int_features)])
        output = model_load.predict(final_features).tolist()
        return render_template('index.html', prediction_text='Predicted House Price is : {}'.format(output))
    else :
        return render_template('index.html')

@app.route("/predict_api", methods=['POST', 'GET'])
def predict_api():
    print(" request.method :",request.method)
    if (request.method == 'POST'):
        data = request.get_json()
        data_unseen = pd.DataFrame([data])
        return jsonify("hello")
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)