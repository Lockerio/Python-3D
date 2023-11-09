import bpy
import json


class DataManager():
    @staticmethod
    def save_objects_parameters_to_json(objects_parameters, filename):
        with open(filename, 'w') as json_file:
            json.dump(objects_parameters, json_file, indent=4)