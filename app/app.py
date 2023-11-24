# Importing essential libraries
from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os

# Import the FeatureProcessor class from the module where you define it
from src.feature_mapper import FeatureMapper
from src.feature_processor import FeatureProcessor
from src.inning_mapper import InningMapper
from src.match_type_mapper import MatchTypeMapper
from src.team_mapper import TeamMapper
from src.venue_mapper import VenueMapper


# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the file
filename = os.path.join(current_dir, './products/pickle_files/GNB_deploy.joblib')

with open(filename, "rb") as f:
    classifier = joblib.load(f)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Create an instance of the FeatureProcessor
        feature_processor = FeatureProcessor()

        # Process the features based on the incoming request
        temp_array = feature_processor.process_features(request)

        data = np.array([temp_array])
        my_prediction = int(classifier.predict(data)[0])

        if my_prediction == 0:
            my_prediction = "Extras (Wide, No Ball, Bye, Leg Bye)"
        elif my_prediction == 1:
            my_prediction = "Dot Ball"
        elif my_prediction == 2:
            my_prediction = "Runs from the bat!"
        elif my_prediction == 3:
            my_prediction = "WICKET!"

        return render_template(
            "result.html",
            my_prediction=my_prediction
        )

# New API route
@app.route("/api/predict", methods=["POST"])
def api_predict():
    try:
        data = request.json  # Assuming you send the data as JSON in the request body
        feature_processor = FeatureProcessor()

        # Process the features based on the incoming JSON data
        temp_array = feature_processor.process_features_json(data)

        data = np.array([temp_array])
        my_prediction = int(classifier.predict(data)[0])

        if my_prediction == 0:
            prediction_label = "Extras (Wide, No Ball, Bye, Leg Bye)"
        elif my_prediction == 1:
            prediction_label = "Dot Ball"
        elif my_prediction == 2:
            prediction_label = "Runs from the bat!"
        elif my_prediction == 3:
            prediction_label = "WICKET!"

        response_data = {
            "prediction": my_prediction,
            "prediction_label": prediction_label
        }
        return jsonify(response_data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port, debug=True)
