from feature_mapper import FeatureMapper
class VenueMapper(FeatureMapper):
    def map_venue(self, venue):
        venue_mapping = {
            "Ahmedabad": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            # Add other venues here
        }
        self.map_feature(venue, venue_mapping)