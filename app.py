# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = "./products/pickle_files/XGB_deploy.pkl"
classifier = pickle.load(open(filename, "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    temp_array = list()

    if request.method == "POST":
        overs = float(request.form["Overs"])
        temp_array = temp_array + [overs]

        wickets = int(request.form["Wickets-Fallen"])
        temp_array = temp_array + [wickets]

        runs = int(request.form["Runs-Scored"])
        temp_array = temp_array + [runs]

        runs_left = int(request.form["Runs-Left"])
        temp_array = temp_array + [runs_left]

        match_type = request.form["Match-Type"]
        if match_type == "playoffs":
            temp_array = temp_array + [1, 0]
        elif match_type == "round-robin":
            temp_array = temp_array + [0, 1]

        venue = request.form["Venue"]
        if venue == "Ahmedabad":
            temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif venue == "Bangalore":
            temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif venue == "Chennai":
            temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif venue == "Cuttack":
            temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif venue == "Delhi":
            temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif venue == "Dharamsala":
            temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif venue == "Hyderabad":
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif venue == "Indore":
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        elif venue == "Kolkata":
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        elif venue == "Mohali":
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        elif venue == "Mumbai":
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        elif venue == "Nagpur":
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        elif venue == "Pune":
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        elif venue == "Raipur":
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        elif venue == "Rajasthan":
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        elif venue == "Ranchi":
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        elif venue == "Visakhapatnam":
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

        inning = int(request.form["Inning"])
        if inning == 1:
            temp_array = temp_array + [1, 0]
        elif inning == 2:
            temp_array = temp_array + [0, 1]

        batting_team = request.form["batting-team"]
        if batting_team == "Chennai Super Kings":
            temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0]
        elif batting_team == "Delhi Daredevils":
            temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0]
        elif batting_team == "Kings XI Punjab":
            temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0]
        elif batting_team == "Kolkata Knight Riders":
            temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0]
        elif batting_team == "Mumbai Indians":
            temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0]
        elif batting_team == "Rajasthan Royals":
            temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0]
        elif batting_team == "Royal Challengers Bangalore":
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0]
        elif batting_team == "Sunrisers Hyderabad":
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1]

        bowling_team = request.form["bowling-team"]
        if bowling_team == "Chennai Super Kings":
            temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0]
        elif bowling_team == "Delhi Daredevils":
            temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0]
        elif bowling_team == "Kings XI Punjab":
            temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0]
        elif bowling_team == "Kolkata Knight Riders":
            temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0]
        elif bowling_team == "Mumbai Indians":
            temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0]
        elif bowling_team == "Rajasthan Royals":
            temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0]
        elif bowling_team == "Royal Challengers Bangalore":
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0]
        elif bowling_team == "Sunrisers Hyderabad":
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1]

        batsman_type = request.form["Batsman-Type"]
        if batsman_type == "Top":
            temp_array = temp_array + [1, 0, 0]
        elif batsman_type == "Middle":
            temp_array = temp_array + [0, 1, 0]
        elif batsman_type == "Tail":
            temp_array = temp_array + [0, 0, 1]

        nonstriker_type = request.form["Nonstriker-Type"]
        if nonstriker_type == "Top":
            temp_array = temp_array + [1, 0, 0]
        elif nonstriker_type == "Middle":
            temp_array = temp_array + [0, 1, 0]
        elif nonstriker_type == "Tail":
            temp_array = temp_array + [0, 0, 1]

        bowler_type = request.form["Bowler-Type"]
        if bowler_type == "Pacer":
            temp_array = temp_array + [1, 0]
        elif bowler_type == "Spinner":
            temp_array = temp_array + [0, 1]

        ball_length = request.form["Ball-Length"]
        if ball_length == "Random":
            temp_array = temp_array + [1, 0, 0, 0, 0, 0]
        elif ball_length == "Full":
            temp_array = temp_array + [0, 1, 0, 0, 0, 0]
        elif ball_length == "Full-Toss":
            temp_array = temp_array + [0, 0, 1, 0, 0, 0]
        elif ball_length == "Good":
            temp_array = temp_array + [0, 0, 0, 1, 0, 0]
        elif ball_length == "Short":
            temp_array = temp_array + [0, 0, 0, 0, 1, 0]
        elif ball_length == "Yorker":
            temp_array = temp_array + [0, 0, 0, 0, 0, 1]

        data = np.array([temp_array])
        my_prediction = int(classifier.predict(data)[0]) # classifier.predict_proba(data)

        # map my_prediction to string value

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

if __name__ == "__main__":
    app.run(debug=True)
