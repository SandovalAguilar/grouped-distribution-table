import pandas as pd
import numpy as np 

class groupedTable:

    def __init__(self, name: str, source_file: str):
        self.name = name
        self.df = pd.read_csv(source_file)
        self.simple_range = self.df.max() - self.df.min()
        self.length = self.df.shape[0]
        self.column_name = self.df.columns[0]
        self.number_classes = self.calculate_number_classes()
        self.amplitude = self.calculate_amplitude()
         
    def calculate_number_classes(self):
        self.number_classes = int(np.ceil(np.sqrt(self.length))) if self.length < 30 else int(np.ceil(1 + (3.322 * np.log10(self.length))))
        return self.number_classes

    def calculate_amplitude(self):
        self.amplitude = self.simple_range / self.number_classes
        return self.amplitude 
    
    def generate_intervals(self):
        pass

    def calculate_freq(self):
        pass