# IPL-Project

[<ins>**LINK TO DEPLOYED HEROKU APPLICATION**</ins>](https://ipl-docker-ubuntu-07ba87a13732.herokuapp.com/)

Final project for DSAN 6700 ML App Deployment.

To run the app locally, clone the repo, `cd` into it and follow the steps below:

- `pip install -r requirements.txt`
- `flask run`

![](app_run.gif)

## Example feature vector #1 (in order) for app inputs

1. Select a Model (dropdown): Naive Bayes
2. Batting Team (dropdown): Chennai Super Kings
3. Bowling Team (dropdown): Mumbai Indians
4. Over #.Ball #: 4.2
5. Wickets Fallen: 1
6. Runs Scored: 35
7. Runs Left to Win: 0
8. Match Type: Round-Robin
9. Match Venue: Mumbai
10. Inning: 1
11. Batsman on Strike: Top-Order
12. Non-Striker Batsman: Top-Order
13. Bowler Type: Pacer
14. Ball Length: Good

Predicted Outcome: Extras (Wide, No Ball, Bye, Leg Bye)

## Example feature vector #2 (in order) for app inputs

1. Select a Model (dropdown): Decision Tree
2. Batting Team (dropdown): Chennai Super Kings
3. Bowling Team (dropdown): Mumbai Indians
4. Over #.Ball #: 4.2
5. Wickets Fallen: 1
6. Runs Scored: 35
7. Runs Left to Win: 0
8. Match Type: Round-Robin
9. Match Venue: Mumbai
10. Inning: 1
11. Batsman on Strike: Top-Order
12. Non-Striker Batsman: Top-Order
13. Bowler Type: Pacer
14. Ball Length: Good

Predicted Outcome: Runs from the bat!

## Example feature vector #3 (in order) for app inputs

1. Select a Model (dropdown): XGBoost
2. Batting Team (dropdown): Chennai Super Kings
3. Bowling Team (dropdown): Mumbai Indians
4. Over #.Ball #: 4.2
5. Wickets Fallen: 1
6. Runs Scored: 35
7. Runs Left to Win: 0
8. Match Type: Round-Robin
9. Match Venue: Mumbai
10. Inning: 1
11. Batsman on Strike: Top-Order
12. Non-Striker Batsman: Top-Order
13. Bowler Type: Pacer
14. Ball Length: Good

Predicted Outcome: Runs from the bat!

## Example feature vector #4 (in order) for app inputs

1. Select a Model (dropdown): Naive Bayes
2. Batting Team (dropdown): Delhi capitals
3. Bowling Team (dropdown): Kolkata Knight Riders
4. Over #.Ball #: 16.4
5. Wickets Fallen: 5
6. Runs Scored: 129
7. Runs Left to Win: 43
8. Match Type: Round-Robin
9. Match Venue: Delhi
10. Inning: 2
11. Batsman on Strike: Middle-Order
12. Non-Striker Batsman: Middle-Order
13. Bowler Type: Pacer
14. Ball Length: Full

Predicted Outcome: Runs from the bat!

## Example feature vector #5 (in order) for app inputs

1. Select a Model (dropdown): XGBoost
2. Batting Team (dropdown): Delhi capitals
3. Bowling Team (dropdown): Kolkata Knight Riders
4. Over #.Ball #: 16.4
5. Wickets Fallen: 5
6. Runs Scored: 129
7. Runs Left to Win: 43
8. Match Type: Round-Robin
9. Match Venue: Delhi
10. Inning: 2
11. Batsman on Strike: Middle-Order
12. Non-Striker Batsman: Middle-Order
13. Bowler Type: Pacer
14. Ball Length: Full

Predicted Outcome: WICKET!
