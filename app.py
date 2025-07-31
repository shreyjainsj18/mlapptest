from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load model dynamically
model_path = os.path.join(os.path.dirname(__file__), "iris_model.pkl")
model = joblib.load(model_path)


@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        data = request.get_json(force=True)
        preds = model.predict([data["features"]])
        return jsonify({"prediction": int(preds[0])})

    elif request.method == "GET":
        try:
            f1 = float(request.args.get("f1"))
            f2 = float(request.args.get("f2"))
            f3 = float(request.args.get("f3"))
            f4 = float(request.args.get("f4"))
        except (TypeError, ValueError):
            return jsonify(
                {
                    "error": "Please provide all 4 features as query parameters (f1,f2,f3,f4)"
                }
            ), 400

        preds = model.predict([[f1, f2, f3, f4]])
        return jsonify({"prediction": int(preds[0]), "features": [f1, f2, f3, f4]})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "running"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
