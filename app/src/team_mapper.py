from feature_mapper import FeatureMapper

class TeamMapper(FeatureMapper):
    def map_team(self, team, mapping_dict):
        self.map_feature(team, mapping_dict)