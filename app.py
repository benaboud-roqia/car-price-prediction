from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model and encoders
model = joblib.load('car_price_model.pkl')
company_mapping = joblib.load('company_mapping.pkl')
fuel_mapping = joblib.load('fuel_mapping.pkl')

# Create reverse mappings for display
company_reverse_mapping = {v: k for k, v in company_mapping.items()}
fuel_reverse_mapping = {v: k for k, v in fuel_mapping.items()}

@app.route('/')
def home():
    return render_template('index.html', 
                         companies=list(company_mapping.keys()),
                         fuel_types=list(fuel_mapping.keys()))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        year = int(request.form['year'])
        kms = int(request.form['kms'])
        company = request.form['company']
        fuel_type = request.form['fuel_type']
        
        # Encode categorical variables
        company_encoded = company_mapping.get(company, 0)
        fuel_encoded = fuel_mapping.get(fuel_type, 0)
        
        # Create feature array
        features = np.array([[year, kms, company_encoded, fuel_encoded]])
        
        # Make prediction
        predicted_price = model.predict(features)[0]
        
        # Return result
        return jsonify({
            'success': True,
            'price': round(predicted_price, 2),
            'inputs': {
                'year': year,
                'kms': kms,
                'company': company,
                'fuel_type': fuel_type
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)