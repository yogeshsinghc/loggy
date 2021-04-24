import json
import pickle
class Applications:
    all_apps = []
    def __init__(self,app_name,max_data,max_time):
        self.app_name = app_name
        self.max_data = max_data
        self.max_time = max_time

    def __str__(self):
        return f"app_name:{self.app_name}, max_date:{self.max_data}, max_time:{self.max_time}"

    @staticmethod
    def save():
        with open(f'Applications.config', 'wb') as file:
            pickle.dump(Applications.all_apps, file)

    @staticmethod
    def load():
        # load it
        with open(f'Applications.config', 'rb') as file:
            Applications.all_apps = pickle.load(file)
