import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar los datos
file_path = r"C:\Users\Aleja\OneDrive\Documentos\Proyecto BEDU Python\IDEFC_NM_jun24.csv"
data = pd.read_csv(file_path, delimiter=';', encoding='latin1')

# 2. Renombrar columnas para seguir la convención de snake_case
data.rename(columns={
    'Entidad': 'estado',
    'Año': 'anio',
    'Tipo de delito': 'tipo_delito',
    'Enero': 'enero',
    'Febrero': 'febrero',
    'Marzo': 'marzo',
    'Abril': 'abril',
    'Mayo': 'mayo',
    'Junio': 'junio',
    'Julio': 'julio',
    'Agosto': 'agosto',
    'Septiembre': 'septiembre',
    'Octubre': 'octubre',
    'Noviembre': 'noviembre',
    'Diciembre': 'diciembre',
}, inplace=True)

# 3. Convertir las columnas de meses a tipo numérico, manejando errores
meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
for mes in meses:
    data[mes] = pd.to_numeric(data[mes], errors='coerce')

# 4. Reemplazar valores faltantes con 0
data.fillna(0, inplace=True)

# 5. Convertir la columna 'anio' a tipo entero
data['anio'] = data['anio'].astype(int)

# 6. Crear columnas de total y promedio de delitos anuales
data['total_anual'] = data[meses].sum(axis=1)
data['promedio_mensual'] = data[meses].mean(axis=1)

# 7. Exploración y visualización de datos

# 7.1. Total de delitos por estado a lo largo de los años
total_delitos_por_estado = data.groupby('estado')['total_anual'].sum().reset_index()

# Visualizar los 10 estados con más delitos
top_10_estados = total_delitos_por_estado.sort_values(by='total_anual', ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(top_10_estados['estado'], top_10_estados['total_anual'])
plt.title('Top 10 Estados con Más Delitos (2015-2024)')
plt.xlabel('Estado')
plt.ylabel('Total de Delitos')
plt.xticks(rotation=45)
plt.show()

# 7.2. Tendencia mensual de delitos a lo largo de los años
tendencia_mensual = data.groupby('anio')[meses].sum().sum(axis=1).reset_index()
tendencia_mensual.columns = ['anio', 'total_delitos']

plt.figure(figsize=(10, 5))
plt.plot(tendencia_mensual['anio'], tendencia_mensual['total_delitos'], marker='o')
plt.title('Tendencia Anual de Delitos (2015-2024)')
plt.xlabel('Año')
plt.ylabel('Total de Delitos')
plt.grid(True)
plt.show()

# 8. Agrupación y análisis detallado

# 8.1. Agrupar por tipo de delito y estado
delitos_por_tipo_y_estado = data.groupby(['tipo_delito', 'estado'])['total_anual'].sum().reset_index()

# Visualizar los delitos más comunes por estado
for estado in top_10_estados['estado']:
    delitos_estado = delitos_por_tipo_y_estado[delitos_por_tipo_y_estado['estado'] == estado]
    top_delitos_estado = delitos_estado.sort_values(by='total_anual', ascending=False).head(5)

    plt.figure(figsize=(10, 5))
    plt.bar(top_delitos_estado['tipo_delito'], top_delitos_estado['total_anual'])
    plt.title(f'Top 5 Delitos en {estado} (2015-2024)')
    plt.xlabel('Tipo de Delito')
    plt.ylabel('Total de Delitos')
    plt.xticks(rotation=45)
    plt.show()

# 9. Propuestas de recomendaciones basadas en el análisis
# Ejemplo de recomendaciones basadas en los hallazgos del análisis:

recomendaciones = """
Recomendaciones:
1. Implementar programas de prevención del delito en los estados con mayor número de delitos.
2. Incrementar la presencia policial en las regiones y meses con mayor incidencia delictiva.
3. Fomentar la colaboración entre diferentes estados para compartir estrategias efectivas.
"""

print(recomendaciones)