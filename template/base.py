import json


class ConfigurationsApp:
    def __init__(self, config_json_file_path):
        with open(config_json_file_path) as f:
            data = json.load(f)

        self.height = data['image_height']
        self.width = data['image_width']
        self.bounds = data['bounds']
        self.classes = data['classes']
        self.classes_names = data['classes_names']
        self.image_name = data['image_name'].split(".")[0]
