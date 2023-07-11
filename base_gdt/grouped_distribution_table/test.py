import grouped_distribution_table as gdt

grouped_table = gdt.groupedTable('Tabla', 'mujeres.csv')

#grouped_table.generate_table()

print('Grouped mean:', grouped_table.calculate_grouped_mean())
print('Mode class:', grouped_table.calculate_mode_class())

try:
    print('Grouped mode', grouped_table.calculate_grouped_mode())
except Exception as error:
    print('Grouped mode error:', error)

print('Median class:', grouped_table.calculate_median_class())
print('Grouped median', grouped_table.calculate_grouped_median())