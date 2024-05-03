import pickle

class DataHandler:
    """A class for handling reading and writing data using pickle"""

    def __init__(self, file_path):
        """Initialize the DataHandler"""
        self.file_path = file_path

    def write_data(self, data):
        """Write data to the data file using pickle"""
        with open(self.file_path, 'wb') as file:
            pickle.dump(data, file)

    def read_data(self):
        """Read data from the data file using pickle"""
        try:
            with open(self.file_path, 'rb') as file:
                data = pickle.load(file)
            return data
        except FileNotFoundError:
            return None
