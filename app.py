<<<<<<< HEAD
import logging
import joblib
import numpy as np 
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
model= joblib.load("rf_model.pkl")
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    """Handle predictions from user point"""
    try:
        float_features=[float(x) for x in request.form.values()]
        final_features=np.array([float_features])
    
        prediction = model.predict(final_features)[0]

        output="Loan Approval!!" if prediction == 1 else "Sorry! We can't approve your loan"

        return render_template('index.html',prediction_text=output)
    except ValueError:
        logging.error("Invalid input provided")
        return render_template('index.html',prediction_text="Error: Invalid input. Please enter valid numbers.")
@app.route('/predict_api',methods=['POST'])
def predict_api():
    """API Endpoint for JSON predictions."""
    try:
        data=request.get_json()
        features=np.array(data["features"]).reshape(1,-1)
        prediction=model.predict(features)[0]
        return jsonify({"prediction":int(prediction)})
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({"prediction":"Invalid input"}),400
if __name__ == "__main__":
=======
import logging
import joblib
import numpy as np 
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
model= joblib.load("rf_model.pkl")
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    """Handle predictions from user point"""
    try:
        float_features=[float(x) for x in request.form.values()]
        final_features=np.array([float_features])
    
        prediction = model.predict(final_features)[0]

        output="Loan Approval!!" if prediction == 1 else "Sorry! We can't approve your loan"

        return render_template('index.html',prediction_text=output)
    except ValueError:
        logging.error("Invalid input provided")
        return render_template('index.html',prediction_text="Error: Invalid input. Please enter valid numbers.")
@app.route('/predict_api',methods=['POST'])
def predict_api():
    """API Endpoint for JSON predictions."""
    try:
        data=request.get_json()
        features=np.array(data["features"]).reshape(1,-1)
        prediction=model.predict(features)[0]
        return jsonify({"prediction":int(prediction)})
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({"prediction":"Invalid input"}),400
if __name__ == "__main__":
>>>>>>> fa1fec0bf80be94998377a5c4e4729842aba559c
    app.run(debug=True)