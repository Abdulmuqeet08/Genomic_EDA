# Genomic Data Analysis with PCA and KMeans Clustering

## Overview
This project focuses on genomic data analysis using Principal Component Analysis (PCA) for dimensionality reduction and KMeans clustering for classification. The trained model is deployed using Flask and an interactive visualization is developed using Jupyter Notebook.

## Features
- **Data Preprocessing**: Standardization and transformation of genomic data.
- **PCA for Dimensionality Reduction**: Reduces high-dimensional genomic data to key components.
- **KMeans Clustering**: Classifies genomic data into distinct clusters.
- **Visualization**: Scatter plot representation of clusters using Matplotlib.
- **Model Deployment**: Flask API to make predictions on new genomic data.
- **Interactive Jupyter Notebook**: Run the entire analysis and predictions in a single environment.

## Installation
### Prerequisites
Ensure you have Python 3.7+ and the following libraries installed:

```bash
pip install numpy pandas matplotlib seaborn sklearn flask joblib requests streamlit
```

## Usage
### 1. Running the Jupyter Notebook
Launch `Genomic.ipynb` to visualize and analyze the genomic dataset.

### 2. Running the Flask API
Run the Flask application to deploy the trained model:

```bash
python flask_app.py
```

Use Postman or cURL to send a JSON request:

```json
{
  "input": [[5.2, 10.4, 2.3, 7.1]]
}
```

### 3. Visualizing Clusters
The Jupyter Notebook includes code to generate a scatter plot showing clusters of genomic data.

## File Structure
```
📂 Genomic_EDA
├── 📄 Genomic.ipynb       # Jupyter Notebook for analysis
├── 📄 flask_app.py        # Flask API for model inference
├── 📄 kmeans_model.pkl    # Pre-trained KMeans model
├── 📄 pca_model.pkl       # Pre-trained PCA model
├── 📄 README.md           # Project documentation
```

## Future Enhancements
- Integrate real-time genomic dataset API.
- Deploy on cloud services like AWS/GCP.
- Extend analysis with deep learning models.

## License
This project is licensed under the MIT License.

