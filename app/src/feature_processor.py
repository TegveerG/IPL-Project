
from flask import Flask, render_template, request, jsonify

from feature_mapper import FeatureMapper
from inning_mapper import InningMapper
from match_type_mapper import MatchTypeMapper
from team_mapper import TeamMapper
from venue_mapper import VenueMapper

class FeatureProcessor:
    def __init__(self):
        self.temp_array = []

    def process_features(self, request):
        match_type_mapper = MatchTypeMapper()
        match_type = request.form.get("Match-Type", "")
        match_type_mapper.map_match_type(match_type)

        venue_mapper = VenueMapper()
        venue = request.form.get("Venue", "")
        venue_mapper.map_venue(venue)

        inning_mapper = InningMapper()
        inning = int(request.form.get("Inning", 0))
        inning_mapper.map_inning(inning)

        batting_team_mapper = TeamMapper()
        batting_team_mapping = {
            # Define batting team mappings here
        }
        batting_team = request.form.get("batting-team", "")
        batting_team_mapper.map_team(batting_team, batting_team_mapping)

        bowling_team_mapper = TeamMapper()
        bowling_team_mapping = {
            # Define bowling team mappings here
        }
        bowling_team = request.form.get("bowling-team", "")
        bowling_team_mapper.map_team(bowling_team, bowling_team_mapping)

        batsman_type_mapper = FeatureMapper()
        batsman_type_mapping = {
            "Top": [1, 0, 0],
            "Middle": [0, 1, 0],
            "Tail": [0, 0, 1]
        }
        batsman_type = request.form.get("Batsman-Type", "")
        batsman_type_mapper.map_feature(batsman_type, batsman_type_mapping)

        nonstriker_type_mapper = FeatureMapper()
        nonstriker_type_mapping = {
            "Top": [1, 0, 0],
            "Middle": [0, 1, 0],
            "Tail": [0, 0, 1]
        }
        nonstriker_type = request.form.get("Nonstriker-Type", "")
        nonstriker_type_mapper.map_feature(nonstriker_type, nonstriker_type_mapping)

        bowler_type_mapper = FeatureMapper()
        bowler_type_mapping = {
            "Pacer": [1, 0],
            "Spinner": [0, 1]
        }
        bowler_type = request.form.get("Bowler-Type", "")
        bowler_type_mapper.map_feature(bowler_type, bowler_type_mapping)

        ball_length_mapper = FeatureMapper()
        ball_length_mapping = {
            "Random": [1, 0, 0, 0, 0, 0],
            "Full": [0, 1, 0, 0, 0, 0],
            "Full-Toss": [0, 0, 1, 0, 0, 0],
            "Good": [0, 0, 0, 1, 0, 0],
            "Short": [0, 0, 0, 0, 1, 0],
            "Yorker": [0, 0, 0, 0, 0, 1]
        }
        ball_length = request.form.get("Ball-Length", "")
        ball_length_mapper.map_feature(ball_length, ball_length_mapping)

        self.temp_array = (
            match_type_mapper.get_temp_array() +
            venue_mapper.get_temp_array() +
            inning_mapper.get_temp_array() +
            batting_team_mapper.get_temp_array() +
            bowling_team_mapper.get_temp_array() +
            batsman_type_mapper.get_temp_array() +
            nonstriker_type_mapper.get_temp_array() +
            bowler_type_mapper.get_temp_array() +
            ball_length_mapper.get_temp_array()
        )
        return self.temp_array


# Usage
feature_processor = FeatureProcessor()
temp_array = feature_processor.process_features(request)
