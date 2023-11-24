from feature_mapper import FeatureMapper
class InningMapper(FeatureMapper):
    def map_inning(self, inning):
        if inning == 1:
            self.temp_array.extend([1, 0])
        elif inning == 2:
            self.temp_array.extend([0, 1])