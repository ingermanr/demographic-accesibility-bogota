# Integrador de Centros de Salud - Bogotá

## 📋 Descripción

Este proyecto integra los centros de salud de Bogotá con los datos de población sintética en un mapa interactivo. Permite visualizar la ubicación de hospitales, centros de salud y unidades de servicios junto con la densidad poblacional de la ciudad.

## 🏥 Características

- **Mapeo automático** de centros de salud por localidad
- **Geocodificación inteligente** basada en coordenadas por localidad
- **Integración con datos de población** sintética existentes
- **Mapa interactivo** con capas organizadas por tipo de servicio
- **Información detallada** de capacidades por centro
- **Estadísticas en tiempo real** mostradas en el mapa

## 🚀 Instalación

### Prerrequisitos

```bash
pip install pandas folium geopy numpy
```

### Archivos necesarios

**Requerido:**
- `centros_salud.csv` - Archivo con los centros de salud

**Opcionales:**
- `resultados_analisis_bogota/poblacion_sintetica_bogota.csv` - Datos de población sintética
- `mapa_poblacion_bogota.html` - Mapa de población existente

## 🎯 Uso Rápido

### Opción 1: Script Automático
```bash
python ejecutar_integracion.py
```

### Opción 2: Uso Programático
```python
from integrador_centros_salud import IntegradorCentrosSaludBogota

integrador = IntegradorCentrosSaludBogota()
mapa, datos = integrador.ejecutar_integracion(
    archivo_centros_csv="centros_salud.csv",
    archivo_poblacion_csv="resultados_analisis_bogota/poblacion_sintetica_bogota.csv",
    archivo_salida="mi_mapa_personalizado.html"
)
```

## 📊 Formato del Archivo CSV

El archivo `centros_salud.csv` debe tener esta estructura:

```csv
centro_salud;barrio;localidad;capacidad_ambulancias;capacidad_camas;capacidad_camillas;capacidad_consultorios;capacidad_salas
HOSPITAL EJEMPLO;BARRIO EJEMPLO;Kennedy;5;100;20;15;8
CENTRO DE SALUD EJEMPLO;OTRO BARRIO;Suba;0;0;5;10;2
```

### Columnas requeridas:
- `centro_salud`: Nombre del centro de salud
- `barrio`: Barrio donde se ubica
- `localidad`: Localidad de Bogotá
- `capacidad_*`: Diferentes capacidades del centro (opcional)

## 🗺️ Funcionalidades del Mapa

### Capas Disponibles
- 🔴 **Hospitales** - Marcadores rojos para hospitales
- 🔵 **Centros de Salud** - Marcadores azules para centros
- 🟢 **Unidades de Servicios** - Marcadores verdes para unidades
- 🌡️ **Densidad Poblacional** - Mapa de calor (si hay datos disponibles)

### Interacción
- **Click en marcadores**: Muestra información detallada del centro
- **Control de capas**: Activa/desactiva elementos del mapa
- **Zoom y navegación**: Explora diferentes áreas de Bogotá
- **Tooltips**: Información rápida al pasar el mouse

## 📈 Estadísticas Integradas

El mapa incluye:
- **Resumen general** con conteo por tipo de centro
- **Top localidades** con mayor número de centros
- **Información de capacidades** por centro
- **Densidad poblacional** si hay datos disponibles

## 🔧 Personalización

### Modificar Coordenadas por Localidad
```python
integrador.coordenadas_localidades['Nueva Localidad'] = [-74.1234, 4.5678]
```

### Cambiar Colores y Estilos
```python
# En el método crear_mapa_integrado()
if 'HOSPITAL' in nombre_upper:
    color = 'red'      # Cambiar color
    icon = 'heart'     # Cambiar ícono
```

### Agregar Nuevas Capacidades
```python
# Agregar en la lista de capacidades a procesar
capacidades = ['capacidad_ambulancias', 'capacidad_camas', 'capacidad_nueva']
```

## 📁 Archivos Generados

Después de ejecutar el script, se crean:

1. **`mapa_integrado_centros_salud_bogota.html`**
   - Mapa interactivo principal
   - Abrir en cualquier navegador web

2. **`mapa_integrado_centros_salud_bogota_datos.csv`**
   - Datos procesados con coordenadas
   - Útil para análisis posterior

## 🛠️ Solución de Problemas

### Error: Archivo no encontrado
```
❌ Error: No se encontró el archivo centros_salud.csv
```
**Solución**: Verifica que el archivo esté en el directorio del proyecto.

### Error: Dependencias
```
❌ Error: No module named 'folium'
```
**Solución**: Instala las dependencias:
```bash
pip install pandas folium geopy numpy
```

### Error: Codificación
```
❌ Error: 'utf-8' codec can't decode
```
**Solución**: Verifica la codificación del archivo CSV o usa:
```python
df = pd.read_csv(archivo, encoding='latin-1')
```

### Sin datos de población
```
⚠️ No se pudieron cargar los datos de población
```
**Solución**: El script funciona sin datos de población, pero no mostrará el mapa de calor.

## 📊 Análisis Adicional

### Exportar datos para análisis
```python
# Los datos procesados incluyen coordenadas
datos.to_excel('centros_salud_con_coordenadas.xlsx')

# Análisis por localidad
resumen = datos.groupby('localidad').agg({
    'centro_salud': 'count',
    'capacidad_camas': 'sum',
    'capacidad_consultorios': 'sum'
}).round(2)
```

### Calcular distancias
```python
from geopy.distance import geodesic

def calcular_distancia(lat1, lon1, lat2, lon2):
    return geodesic((lat1, lon1), (lat2, lon2)).kilometers
```

## 🎨 Ejemplos de Visualización

### Mapa básico solo con centros
```python
integrador.ejecutar_integracion(
    archivo_centros_csv="centros_salud.csv",
    archivo_salida="mapa_solo_centros.html"
)
```

### Mapa completo con población
```python
integrador.ejecutar_integracion(
    archivo_centros_csv="centros_salud.csv",
    archivo_poblacion_csv="poblacion_sintetica_bogota.csv",
    archivo_salida="mapa_completo.html"
)
```

## 📞 Soporte

Si encuentras problemas:

1. **Verifica los archivos**: Asegúrate de que `centros_salud.csv` existe
2. **Revisa las dependencias**: Instala pandas, folium, geopy
3. **Consulta los logs**: El script muestra información detallada de errores
4. **Revisa el formato**: El CSV debe usar `;` como separador

## 🔄 Actualizaciones

Para actualizar los datos:
1. Reemplaza `centros_salud.csv` con datos nuevos
2. Ejecuta nuevamente el script
3. El mapa se actualizará automáticamente

## 📝 Notas Técnicas

- **Geocodificación**: Usa coordenadas aproximadas por localidad + variación aleatoria
- **Rendimiento**: Procesa ~100 centros en menos de 30 segundos
- **Memoria**: Requiere ~50MB RAM para 10,000 puntos de población
- **Compatibilidad**: Funciona en Windows, macOS y Linux

## 🎯 Casos de Uso

1. **Planificación urbana**: Identificar áreas con baja cobertura de salud
2. **Análisis de accesibilidad**: Distancias entre población y centros
3. **Gestión de recursos**: Distribución de capacidades por localidad
4. **Investigación**: Correlación entre densidad poblacional y servicios

---

## 🚀 ¡Empezar Ahora!

```bash
# 1. Asegúrate de tener el archivo de centros de salud
ls centros_salud.csv

# 2. Instala dependencias
pip install pandas folium geopy

# 3. Ejecuta la integración
python ejecutar_integracion.py

# 4. Abre el mapa generado
# Archivo: mapa_integrado_centros_salud_bogota.html
```

¡Tu mapa integrado estará listo en minutos! 🎉
