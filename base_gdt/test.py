import grouped_distribution_table as gdt

def main():
    grouped_table = gdt.groupedTable('Tabla', 'hombres.csv')
    #print(grouped_table.generate_intervals())
    print(grouped_table.generate_abs_freq())

if __name__ == '__main__':
    main()