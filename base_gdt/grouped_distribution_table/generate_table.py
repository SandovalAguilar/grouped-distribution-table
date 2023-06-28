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
        self.array_intervals = np.empty((self.number_classes, 2), dtype=float)
        self.array_intervals[0][0] = self.df.min().iloc[0] 
        self.array_intervals[0][1] = self.df.min().iloc[0] + self.amplitude.iloc[0]
        aux_col1 = self.df.min().iloc[0]
        aux_col2 = self.df.min().iloc[0] + self.amplitude.iloc[0]

        for i in range(1, self.number_classes):
            aux_col1 += self.amplitude
            self.array_intervals[i][0] = aux_col1.iloc[0]
                
        for i in range(1, self.number_classes):
            aux_col2 += self.amplitude
            self.array_intervals[i][1] = aux_col2.iloc[0]

        return self.array_intervals

    def generate_abs_freq(self):
        self.array_abs_freq = np.empty((self.number_classes), dtype = int)

        def count_range_in_list(array, interval):
            counts = 0

            for i in array:
                print(i)
                if np.float32(i) != np.float32(array[-1]):
                    if np.float32(interval[0]) <= np.float32(i) < np.float32(interval[1]):
                        counts += 1
                    else:
                        if np.float32(interval[0]) <= np.float32(i) <= np.float32(interval[1]):
                            counts += 1

                return counts
  
        for i in range(self.number_classes):
            self.array_abs_freq[i] = count_range_in_list(self.df[self.column_name].values, self.array_intervals[i])
                
        return self.array_abs_freq


