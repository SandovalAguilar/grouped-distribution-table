import grouped_distribution_table as gdt

def main():
    grouped_table = gdt.groupedTable('Tabla', 'hombres.csv')
    print(grouped_table.calculate_amplitude())

if __name__ == '__main__':
    main()