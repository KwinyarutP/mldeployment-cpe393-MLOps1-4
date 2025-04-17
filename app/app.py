from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return "ML Model is Running"

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if "features" not in data:
        return jsonify({"error": "'features' key is missing"}), 400

    features = data["features"]

    # Helper function to check float type (not int)
    def is_strict_float(val):
        return isinstance(val, float)

    # Check if input is a single sample or list of samples
    if isinstance(features[0], float):
        # Validate single input
        if len(features) != 4:
            return jsonify({"error": "Each input must contain exactly 4 float values"}), 400
        if not all(is_strict_float(val) for val in features):
            return jsonify({"error": "All feature values must be float"}), 400
        input_features = np.array(features).reshape(1, -1)
    else:
        # Validate multiple inputs
        for i, sample in enumerate(features):
            if not isinstance(sample, list) or len(sample) != 4:
                return jsonify({"error": f"Input at index {i} must contain exactly 4 float values"}), 400
            if not all(is_strict_float(val) for val in sample):
                return jsonify({"error": f"All values in input at index {i} must be float"}), 400
        input_features = np.array(features)

    predictions = model.predict(input_features)
    return jsonify({
        "predictions": predictions.tolist()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000) #check your port number ( if it is in use, change the port number)
