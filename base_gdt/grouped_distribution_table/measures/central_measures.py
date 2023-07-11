import pandas as pd
import numpy as np

import grouped_distribution_table as t

class centralMeasures(t.groupedTable):

    def __init__(self, name: str, source_file: str):
        super().__init__(name, source_file)
        self.grouped_mean = self.calculate_grouped_mean()
        self.mode_class = self.calculate_mode_class()
        self.grouped_mode = self.calculate_grouped_mode()
        self.median_class = self.calculate_median_class()
        self.grouped_meadian = self.calculate_grouped_median()

    def calculate_grouped_mean(self):
        self.table['x_i * f_i'] = self.table['Class mark'] * \
            self.table['Absolute frequency']
        sum_xifi = float(self.table['x_i * f_i'].sum())
        self.grouped_mean = sum_xifi / self.length

        return np.float32(self.grouped_mean)

    def calculate_mode_class(self):
        class_number = 0
        higher_freq = self.table['Absolute frequency'].max()

        for i in self.table['Absolute frequency']:
            class_number += 1
            if i == higher_freq:
                return class_number

    def calculate_grouped_mode(self):
        lower_limit = min(self.array_intervals[self.mode_class - 1])
        delta_1 = self.table['Absolute frecuency'].iloc[self.mode_class -
                                                        1] - self.table['Absolute frecuency'].iloc[self.mode_class - 2]
        delta_2 = self.table['Absolute frecuency'].iloc[self.mode_class -
                                                        1] - self.table['Absolute frecuency'].iloc[self.mode_class]
        self.grouped_mode = lower_limit + \
            ((delta_1) / (delta_1 + delta_2)) * self.amplitude
        return self.grouped_mode

    def calculate_median_class(self):
        position = (self.length + 1) / 2

        self.median_class = next((class_number + 1 for class_number, cumulative_freq in enumerate(
            self.table['Cumulative frequency']) if cumulative_freq >= position), None)

        return self.median_class

    def calculate_grouped_median(self):
        lower_limit = min(self.array_intervals[self.median_class - 1])
        prev_cum_freq = self.table['Cumulative frequency'].iloc[self.median_class - 2]
        absolute_freq = self.table['Absolute frequency'].iloc[self.median_class - 1]
        self.grouped_median = lower_limit + \
            (((self.length / 2) - prev_cum_freq) / absolute_freq) * self.amplitude

        return self.grouped_median.iloc[0]

'''
from grouped_distribution_table.table import groupedTable

def calculate_grouped_mean(gt: groupedTable):
    gt.table['x_i * f_i'] = gt.table['Class mark'] * gt.table['Absolute frequency']
    sum_xifi = float(gt.table['x_i * f_i'].sum())
    grouped_mean = sum_xifi / gt.length
    
    return grouped_mean

def calculate_mode_class(gt: groupedTable):
    class_number = 0
    higher_freq = gt.table['Absolute frecuency'].max()

    for i in gt.table['Absolute frecuency']:
            class_number += 1
            if i == higher_freq:
                return class_number
            
def calculate_grouped_mode(gt: groupedTable):
    lower_limit = min(gt.array_intervals[gt.class_mode - 1]) 
    delta_1 = gt.table['Absolute frequency'].iloc[gt.class_mode - 1] - gt.table['Absolute frecuency'].iloc[gt.class_mode - 2]
    delta_2 = gt.table['Absolute frecuency'].iloc[gt.class_mode - 1] - gt.table['Absolute frecuency'].iloc[gt.class_mode]
    gt.grouped_mode = lower_limit + ((delta_1) / (delta_1 + delta_2)) * gt.amplitude
    return gt.grouped_mode


def calculate_mode_class(gt: groupedTable):
    class_number = 0
    higher_freq = self.table['Absolute frecuency'].max()

    for i in self.table['Absolute frecuency']:
            class_number += 1
            if i == higher_freq:
                return class_number

def calculate_grouped_mode(gt: groupedTable):
    lower_limit = min(gt.array_intervals[gt.class_mode - 1]) 
    delta_1 = gt.table['Absolute frecuency'].iloc[gt.class_mode - 1] - gt.table['Absolute frecuency'].iloc[gt.class_mode - 2]
    delta_2 = gt.table['Absolute frecuency'].iloc[gt.class_mode - 1] - gt.table['Absolute frecuency'].iloc[gt.class_mode]
    gt.grouped_mode = lower_limit + ((delta_1) / (delta_1 + delta_2)) * gt.amplitude
    return gt.grouped_mode

def calculate_median_class(gt: groupedTable):
    position = (gt.length + 1) / 2

    gt.median_class = next((class_number + 1 for class_number, cumulative_freq in enumerate(gt.table['Cumulative frequency']) if cumulative_freq >= position), None)
    
    return gt.median_class

def calculate_grouped_median(gt: groupedTable):
    lower_limit = min(gt.array_intervals[gt.median_class - 1]) 
    prev_cum_freq = gt.table['Cumulative frequency'].iloc[gt.median_class - 2]
    absolute_freq = gt.table['Absolute frecuency'].iloc[gt.median_class - 1]
    gt.grouped_median = lower_limit + (((gt.length / 2) - prev_cum_freq) / absolute_freq ) * gt.amplitude

    return gt.grouped_median
'''
