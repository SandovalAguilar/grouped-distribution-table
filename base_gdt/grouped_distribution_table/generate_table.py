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
        self.array_intervals = self.generate_intervals()
        self.array_abs_freq = self.generate_abs_freq()
         
    def calculate_number_classes(self):
        self.number_classes = int(np.ceil(np.sqrt(self.length))) if self.length < 30 else int(np.ceil(1 + (3.322 * np.log10(self.length))))
        return self.number_classes

    def calculate_amplitude(self):
        self.amplitude = self.simple_range / self.number_classes
        return self.amplitude 
    
    def generate_intervals(self):
        array_intervals = np.empty((self.number_classes, 2), dtype=float)
        array_intervals[0][0] = self.df.min().iloc[0] 
        array_intervals[0][1] = self.df.min().iloc[0] + self.amplitude.iloc[0]
        aux_col1 = self.df.min().iloc[0]
        aux_col2 = self.df.min().iloc[0] + self.amplitude.iloc[0]

        for i in range(1,self.number_classes):
            aux_col1 += self.amplitude
            array_intervals[i][0] = aux_col1.iloc[0]
                
        for i in range(1,self.number_classes):
            aux_col2 += self.amplitude
            array_intervals[i][1] = aux_col2.iloc[0]
        
        '''
        array_intervals = [array_intervals[i][0] = (aux_col1 := aux_col1 + amplitud).iloc[0] for i in range(1, self.number_classes)]
        array_intervals = [array_intervals[i][1] = (aux_col2 := aux_col2 + amplitud).iloc[0] for i in range(1, self.number_classes)]
        '''    

        return self.array_intervals

    def count_range_in_list(array, interval):
        for i in array:
            if i != array[-1]:
                if interval[0] <= i < interval[1]:
                    counts += 1
            else:
                if interval[0] <= i <= interval[1]:
                    counts += 1
        
        return counts

    def generate_abs_freq(self):
        for i in range(self.number_classes):
	        self.array_abs_freq[i] = self.count_range_in_list(self.df[self.df.columns[0]].values, self.array_classes[i])