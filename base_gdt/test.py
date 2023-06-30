import grouped_distribution_table as gdt

def main():
    grouped_table = gdt.groupedTable('Tabla', 'mujeres.csv')
    #print(grouped_table.generate_intervals())
    print(grouped_table.calculate_grouped_mean())

if __name__ == '__main__':
    main()