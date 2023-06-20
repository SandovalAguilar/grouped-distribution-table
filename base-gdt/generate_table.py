import pandas as pd
import numpy as np 

class grouped_table:

    def __init__(self, name: str, source_file: str):
        self.name = name
        self.df = pd.read_csv(source_file)
        self.simple_range = self.df.max() - self.df.min()
        self.length = self.df.shape[0]
        self.column_name = self.df.columns[0]
         
    def calculate_number_classes(self, length):
        self.number_classes = int(np.ceil(np.sqrt(self.length))) if self.length < 30 else int(np.ceil(1 + (3.322 * np.log10(self.length))))
        return self.number_classes

    def calculate_amplitude(self, simple_range, number_classes):
        self.amplitude = simple_range / number_classes
        return self.amplitude
    
    def generate_intervals(self):
        pass

    def calculate_freq(self):
        pass