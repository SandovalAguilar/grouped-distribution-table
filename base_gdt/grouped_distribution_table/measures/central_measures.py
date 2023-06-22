class centralMeasures():
    
    def grouped_mean(tabla_frecuencias, n):
        tabla_frecuencias['x_i * f_i'] = tabla_frecuencias['Marca de clase'] * tabla_frecuencias['Frecuencia absoluta']
        sum_xifi = float(tabla_frecuencias['x_i * f_i'].sum())
        media_agrupada = sum_xifi / n
        return media_agrupada
    
    def mode_class(tabla_frecuencias):
        clase = 0
        frecuencia_mayor = tabla_frecuencias['Frecuencia absoluta'].max()

        for i in tabla_frecuencias['Frecuencia absoluta']:
                clase += 1
                if i == frecuencia_mayor:
                    return clase

    def grouped_mode(moda_clase, amplitud, tabla_frecuencias, intervalos_float):
        limite_inferior = min(intervalos_float[moda_clase - 1]) 
        delta_1 = tabla_frecuencias['Frecuencia absoluta'].iloc[moda_clase - 1] - tabla_frecuencias['Frecuencia absoluta'].iloc[moda_clase - 2]
        delta_2 = tabla_frecuencias['Frecuencia absoluta'].iloc[moda_clase - 1] - tabla_frecuencias['Frecuencia absoluta'].iloc[moda_clase]
        moda_agrupada = limite_inferior + ((delta_1) / (delta_1 + delta_2)) * amplitud
        return moda_agrupada
    
    def median_class(n, tabla_frecuencias):
        posicion = (n + 1) / 2
        clase = 0

        posicion_clase = next((clase + 1 for clase, frecuencia_acumulada in enumerate(tabla_frecuencias['Frecuencia acumulada']) if frecuencia_acumulada>=posicion), None)
        
        return posicion_clase

    def grouped_median(mediana_clase, amplitud, tabla_frecuencias, intervalos_float):
        limite_inferior = min(intervalos_float[mediana_clase - 1]) 
        frec_acum_anterior = tabla_frecuencias['Frecuencia acumulada'].iloc[mediana_clase - 2]
        frec_absoluta = tabla_frecuencias['Frecuencia absoluta'].iloc[mediana_clase -1]
        mediana_agrupada = limite_inferior + (((n / 2) - frec_acum_anterior) / frec_absoluta ) * amplitud

        return mediana_agrupada