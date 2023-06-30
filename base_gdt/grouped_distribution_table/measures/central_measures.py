import pandas as pd
import numpy as np
import table as t

class centralMeasures(t.groupedTable):
    
    def __init__(self, name: str, source_file: str):
         super().__init__(name, source_file)
         self.grouped_mean = self.calculate_grouped_mean()
         self.mode_class = self.calculate_mode_class()
         self.grouped_mode = self.calculate_grouped_mode()
         self.median_class = self.calculate_median_class()

    def calculate_grouped_mean(self):
        self.table['x_i * f_i'] = self.table['Mark class'] * self.table['Absolute frequency']
        sum_xifi = float(self.table['x_i * f_i'].sum())
        self.grouped_mean = sum_xifi / self.length
        
        return self.grouped_mean
    
    def calculate_mode_class(self):
        class_number = 0
        higher_freq = self.table['Absolute frecuency'].max()

        for i in self.table['Absolute frecuency']:
                class_number += 1
                if i == higher_freq:
                    return class_number

    def calculate_grouped_mode(self):
        lower_limit = min(self.array_intervals[self.class_mode - 1]) 
        delta_1 = self.table['Absolute frecuency'].iloc[self.class_mode - 1] - self.table['Absolute frecuency'].iloc[self.class_mode - 2]
        delta_2 = self.table['Absolute frecuency'].iloc[self.class_mode - 1] - self.table['Absolute frecuency'].iloc[self.class_mode]
        self.grouped_mode = lower_limit + ((delta_1) / (delta_1 + delta_2)) * self.amplitude
        return self.grouped_mode
    
    def calculate_median_class(self):
        position = (self.length + 1) / 2

        self.median_class = next((class_number + 1 for class_number, cumulative_freq in enumerate(self.table['Cumulative frequency']) if cumulative_freq >= position), None)
        
        return self.median_class

    def calculate_grouped_median(self):
        lower_limit = min(self.array_intervals[self.median_class - 1]) 
        prev_cum_freq = self.table['Cumulative frequency'].iloc[self.median_class - 2]
        absolute_freq = self.table['Absolute frecuency'].iloc[self.median_class - 1]
        self.grouped_median = lower_limit + (((self.length / 2) - prev_cum_freq) / absolute_freq ) * self.amplitude

        return self.grouped_median