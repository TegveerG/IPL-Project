class FeatureMapper:
    def __init__(self):
        self.temp_array = []

    def map_feature(self, value, mapping_dict):
        if value in mapping_dict:
            self.temp_array.extend(mapping_dict[value])

    def get_temp_array(self):
        return self.temp_array