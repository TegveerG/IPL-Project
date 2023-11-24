from feature_mapper import FeatureMapper

class MatchTypeMapper(FeatureMapper):
    def map_match_type(self, match_type):
        match_type_mapping = {
            "playoffs": [1, 0],
            "round-robin": [0, 1]
        }
        self.map_feature(match_type, match_type_mapping)