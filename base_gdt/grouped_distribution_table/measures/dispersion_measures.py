import pandas as pd
import numpy as np
import central_measures as cm

class dispersionMeasures(cm.centralMeasures):
    def __init__(self, name: str, source_file: str):
        super().__init__(name, source_file)
        self.grouped_variance = self.calculate_grouped_variance()
        self.grouped_range = self.calculate_grouped_range()
    
    def calculate_grouped_variance(self):
        self.table['(x_i - \mu)^2'] = ((self.table['Mark class'] - self.grouped_mean) ** 2)
        self.table['(x_i - \mu)^2 * f_i'] = self.table['(x_i - \mu)^2'] * self.table['Absolute frequency']
        sum = self.table['(x_i - \mu)^2 * f_i'].sum()
        self.grouped_variance = (sum) / (self.length - 1)
        
        return self.grouped_variance
    
    def calculate_grouped_range(self):
        self.grouped_range = self.table['Class mark'].max() - self.table['Class mark'].min()
        
        return self.grouped_range