import joblib
import numpy as np
from flask import Flask, request, jsonify
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import threading

# Step 1: Load Pre-trained Models
pca_model = joblib.load("pca_model.pkl")
kmeans_model = joblib.load("kmeans_model.pkl")

# Step 2: Deploy API using Flask
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_data = np.array(data['input'])
        transformed_data = pca_model.transform(input_data)
        cluster = kmeans_model.predict(transformed_data)
        return jsonify({'predicted_cluster': cluster.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

# Step 3: Run Flask in a background thread
def run_flask():
    app.run(debug=False, port=5000, use_reloader=False)

thread = threading.Thread(target=run_flask)
thread.start()
