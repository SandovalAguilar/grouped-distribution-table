class dispersionMeasures:
    
    def grouped_variance(tabla_frecuencias, n, media_agrupada):
        tabla_frecuencias['(x_i - \mu)^2'] = ((tabla_frecuencias['Marca de clase'] - media_agrupada) ** 2)
        tabla_frecuencias['(x_i - \mu)^2 * f_i'] = tabla_frecuencias['(x_i - \mu)^2'] * tabla_frecuencias['Frecuencia absoluta']
        sumatoria = tabla_frecuencias['(x_i - \mu)^2 * f_i'].sum()
        varianza_agrupada = (sumatoria) / (n - 1)
        return varianza_agrupada
    
    def grouped_range(tabla_frecuencias):
        rango = tabla_frecuencias['Marca de clase'].max() - tabla_frecuencias['Marca de clase'].min()
        return rango