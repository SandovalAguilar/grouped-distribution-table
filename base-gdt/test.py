import generate_table as gt

def main():
    grouped_table = gt.grouped_table('Tabla', 'hombres.csv')
    print(grouped_table.calculate_amplitude())
    print(grouped_table.calculate_number_classes())
    

if __name__ == '__main__':
    main()