from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

model_path = os.path.join(os.path.dirname(__file__), "iris_model.pkl")
model = joblib.load(model_path)
# model = joblib.load("iris_model.pkl")  # Load your trained model


# Predict (POST + GET)
@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        # Handle JSON input from Postman or curl
        data = request.get_json(force=True)
        preds = model.predict([data["features"]])
        return jsonify({"prediction": int(preds[0])})

    elif request.method == "GET":
        # Handle query params for browser use
        # Example: /predict?f1=5.1&f2=3.5&f3=1.4&f4=0.2
        try:
            f1 = float(request.args.get("f1"))
            f2 = float(request.args.get("f2"))
            f3 = float(request.args.get("f3"))
            f4 = float(request.args.get("f4"))
        except (TypeError, ValueError):
            return (
                jsonify(
                    {
                        "error": "Please provide all 4 features as query parameters (f1,f2,f3,f4)"
                    }
                ),
                400,
            )

        preds = model.predict([[f1, f2, f3, f4]])
        return jsonify({"prediction": int(preds[0]), "features": [f1, f2, f3, f4]})


# Health check
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "running"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


# from flask import Flask, request, jsonify
# import joblib
# app = Flask(__name__)
# model = joblib.load("iris_model.pkl")  # load your trained model

# @app.route("/predict", methods=["POST"])
# def predict():
#     data = request.get_json(force=True)
#     # Assuming input is a JSON with feature values
#     preds = model.predict([data["features"]])
#     return jsonify({"prediction": int(preds[0])})

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)


# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # Health check (GET)
# @app.route("/health", methods=["GET"])
# def health():
#     return jsonify({"status": "running"}), 200

# # Predict (POST + GET)
# @app.route("/predict", methods=["POST", "GET"])
# def predict():
#     if request.method == "POST":
#         # Handle JSON input (from Postman or curl)
#         data = request.get_json()
#         features = data.get("features", [])
#         # Dummy prediction logic
#         prediction = "Predicted class based on POST data"
#         return jsonify({"prediction": prediction, "features": features})

#     elif request.method == "GET":
#         # Handle browser GET requests (no JSON)
#         # Optionally use query params like /predict?f1=5.1&f2=3.5&f3=1.4&f4=0.2
#         f1 = request.args.get("f1", type=float)
#         f2 = request.args.get("f2", type=float)
#         f3 = request.args.get("f3", type=float)
#         f4 = request.args.get("f4", type=float)
#         features = [f1, f2, f3, f4]
#         # Dummy prediction logic
#         prediction = "Predicted class based on GET data"
#         return jsonify({"prediction": prediction, "features": features})
