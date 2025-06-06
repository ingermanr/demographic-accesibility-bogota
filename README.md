---

## 🔧 Solución: Ejecución Sin Entrada Manual

**Problema Común**: "No puedo ingresar manualmente el tamaño de muestra"

**Solución**: Usa los scripts automáticos incluidos:

### **Método 1: Scripts Automáticos (Más Fácil)**
```bash
# Windows - Un solo clic
ejecutar.bat

# Linux/Mac  
./ejecutar.sh
```

### **Método 2: Python Directo**
```bash
# Ejecución completamente automática
python ejecutar_automatico.py
```

### **Método 3: Modificar Configuración**
Si quieres cambiar el tamaño de muestra, edita el archivo `ejecutar_automatico.py`:
```python
# Línea 67 - Cambiar el valor
tamaño_muestra = 3000  # Cambia este número
```

**Configuraciones Recomendadas:**
- `tamaño_muestra = 1000` → Prueba rápida (~30 segundos)
- `tamaño_muestra = 5000` → Análisis estándar (~2 minutos) **[Por defecto]**
- `tamaño_muestra = 10000` → Análisis completo (~4 minutos)

# BOG_SINTE - Sistema de Datos Sintéticos de Bogotá 🏙️

## 🚀 Versión Mejorada - Con Análisis de Centros de Salud

Este proyecto genera y analiza datos sintéticos de la población de Bogotá D.C. para análisis demográfico y planificación urbana, **ahora con análisis completo de accesibilidad a centros de salud**.

---

## ✨ NUEVAS FUNCIONALIDADES

### 🏥 **Análisis de Centros de Salud**
- ✅ Procesamiento de datos de centros de salud de Bogotá
- ✅ Geocodificación automática de centros por localidad
- ✅ Cálculo de distancias entre población y centros de salud
- ✅ Métricas de accesibilidad y cobertura sanitaria
- ✅ Análisis de grupos vulnerables
- ✅ Visualizaciones de accesibilidad geoespacial
- ✅ Reportes de capacidad vs demanda

### 🔧 **Mejoras Técnicas**
- ✅ Código completamente reorganizado y modularizado
- ✅ Eliminación de archivos duplicados y obsoletos
- ✅ Integración fluida entre análisis demográfico y sanitario
- ✅ Pipeline automatizado con manejo de errores
- ✅ Documentación actualizada y completa

---

## 🚀 Instalación y Uso Rápido

### **Opción 1: Ejecución Completa (Recomendada)**

```bash
# 1. Instalar dependencias básicas
pip install pandas numpy matplotlib seaborn

# 2. Ejecutar sistema completo mejorado
python main_corregido.py
```

### **Opción 2: Solo Análisis de Centros de Salud**

```bash
# Si ya tienes datos de población generados
python analizador_centros_salud.py
```

---

## 📁 Estructura de Archivos Actualizada

```
bog_sinte/
├── 📄 main_corregido.py                     # ⭐ ARCHIVO PRINCIPAL
├── 📄 ejecutar_automatico.py                # 🆕 EJECUCIÓN AUTOMÁTICA
├── 📄 ejecutar.bat                          # 🆕 SCRIPT WINDOWS
├── 📄 ejecutar.sh                           # 🆕 SCRIPT LINUX/MAC
├── 📄 generador_datos_sinteticos_bogota.py  # Generador de datos
├── 📄 validador_datos_sinteticos.py         # Análisis demográfico
├── 📄 analizador_centros_salud.py           # 🆕 Análisis centros salud
├── 📄 test_sistema.py                       # 🆕 Script de prueba
├── 📄 centros_salud.csv                     # 🆕 Datos de centros
├── 📄 requirements.txt                      # Dependencias
├── 📄 README.md                            # Esta documentación
├── 📂 resultados_analisis_bogota/          # 📊 RESULTADOS
│   ├── poblacion_sintetica_bogota.csv      # Datos sintéticos
│   ├── poblacion_sintetica_bogota.json     # Datos en JSON
│   ├── analisis_demografico_bogota.png     # Gráficos demográficos
│   ├── analisis_accesibilidad_centros_salud.png # 🆕 Gráficos accesibilidad
│   ├── matriz_correlacion.png             # Análisis correlaciones
│   ├── reporte_datos_sinteticos.txt       # Reporte demográfico
│   ├── reporte_accesibilidad_salud.txt    # 🆕 Reporte centros salud
│   ├── analisis_accesibilidad_poblacion.csv # 🆕 Datos accesibilidad
│   ├── centros_salud_procesados.csv       # 🆕 Centros geocodificados
│   └── resumen_ejecutivo.txt               # Resumen del proceso
└── 📄 archivos_eliminados.log             # Log de limpieza
```

---

## 💻 Uso Programático

### Pipeline Completo Automático 🆕
```python
# Ejecución completamente automática (sin entrada del usuario)
from ejecutar_automatico import main_automatico

# Ejecutar con configuración predeterminada
exito = main_automatico()  # 5000 registros, ~2-3 minutos

if exito:
    print("✅ Análisis completado!")
```

### Pipeline Completo Manual
```python
from main_corregido import SistemaDatosSinteticosBogota

# Crear instancia
sistema = SistemaDatosSinteticosBogota()

# Ejecutar pipeline completo (demografía + centros de salud)
exito = sistema.ejecutar_pipeline_completo(tamaño_muestra=5000)

if exito:
    print("✅ Análisis completado exitosamente!")
```

### Solo Análisis de Centros de Salud
```python
from analizador_centros_salud import SistemaAccesibilidadSalud

# Crear sistema de accesibilidad
sistema_acceso = SistemaAccesibilidadSalud(
    'poblacion_sintetica_bogota.csv', 
    'centros_salud.csv'
)

# Ejecutar análisis
resultados = sistema_acceso.ejecutar_analisis_completo(muestra_poblacion=3000)
```

### Análisis de Componentes Individuales
```python
# Procesar centros de salud
from analizador_centros_salud import ProcesadorCentrosSalud

procesador = ProcesadorCentrosSalud('centros_salud.csv')
centros = procesador.procesar_centros_completo()

# Calcular distancias
from analizador_centros_salud import CalculadorDistancias

calculador = CalculadorDistancias(df_poblacion, centros)
accesibilidad = calculador.analizar_accesibilidad_poblacion(muestra_max=1000)

# Analizar accesibilidad
from analizador_centros_salud import AnalizadorAccesibilidad

analizador = AnalizadorAccesibilidad(accesibilidad, centros)
metricas = analizador.generar_metricas_accesibilidad()
```

---

## 📊 Datos y Análisis Generados

### **Datos de Población Sintética**
| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `id` | Identificador único | "KEN123456" |
| `nombre` | Nombre sintético | "María" |
| `apellido1` | Primer apellido | "García" |
| `apellido2` | Segundo apellido | "López" |
| `genero` | F (Femenino) / M (Masculino) | "F" |
| `edad` | Edad en años | 34 |
| `localidad` | Una de las 20 localidades | "Kennedy" |
| `estrato` | Estrato socioeconómico (1-6) | 3 |
| `nivel_educativo` | Nivel educativo | "Universitaria" |
| `afiliacion_salud` | Tipo de afiliación | "Contributivo" |
| `latitud` | Coordenada geográfica | 4.6281 |
| `longitud` | Coordenada geográfica | -74.1597 |

### **🆕 Datos de Centros de Salud**
| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `centro_salud` | Nombre del centro | "Hospital Kennedy" |
| `barrio` | Barrio específico | "Kennedy Central" |
| `localidad` | Localidad de Bogotá | "Kennedy" |
| `capacidad_ambulancias` | Número de ambulancias | 5 |
| `capacidad_camas` | Número de camas | 120 |
| `capacidad_camillas` | Número de camillas | 15 |
| `capacidad_consultorios` | Número de consultorios | 25 |
| `capacidad_salas` | Número de salas | 8 |
| `latitud` | Coordenada del centro | 4.6285 |
| `longitud` | Coordenada del centro | -74.1605 |

### **🆕 Datos de Accesibilidad**
| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `persona_id` | ID de la persona | "KEN123456" |
| `persona_localidad` | Localidad de residencia | "Kennedy" |
| `centro_cercano` | Centro más cercano | "Hospital Kennedy" |
| `distancia_km` | Distancia en kilómetros | 2.3 |
| `misma_localidad` | Centro en misma localidad | True |
| `capacidad_centro` | Capacidad del centro | 173 |

---

## 📈 Visualizaciones Generadas

### **Análisis Demográfico** (`analisis_demografico_bogota.png`)
- Distribución por edad (histograma)
- Distribución por género (pie chart)
- Distribución por estrato (barras)
- Top 10 localidades (barras horizontales)
- Nivel educativo (pie chart)
- Afiliación a salud (barras)

### **🆕 Análisis de Accesibilidad** (`analisis_accesibilidad_centros_salud.png`)
- Distribución de distancias al centro más cercano
- Distancia promedio por localidad
- Porcentaje con centro en su localidad
- Relación capacidad vs demanda de centros

### **Análisis de Correlaciones** (`matriz_correlacion.png`)
- Heatmap de correlaciones entre variables numéricas

---

## 📋 Reportes Generados

### **Reporte Demográfico** (`reporte_datos_sinteticos.txt`)
- Estadísticas descriptivas completas
- Distribuciones por variables
- Análisis de representatividad

### **🆕 Reporte de Accesibilidad** (`reporte_accesibilidad_salud.txt`)
- Métricas de accesibilidad general
- Análisis por localidad
- Grupos vulnerables
- Centros más demandados
- Recomendaciones para políticas públicas

---

## 🎯 Casos de Uso

### **Planificación Urbana**
- Simulación de políticas públicas
- Optimización de ubicación de servicios
- Análisis de cobertura sanitaria

### **Análisis Demográfico**
- Estudios de población por localidad
- Segmentación demográfica
- Identificación de grupos vulnerables

### **Gestión Sanitaria**
- Evaluación de accesibilidad a centros de salud
- Análisis de capacidad vs demanda
- Planificación de nuevos centros
- Optimización de recursos sanitarios

### **Desarrollo de Software**
- Datos de prueba para aplicaciones
- Testing de sistemas geoespaciales
- Validación de algoritmos de proximidad

### **Investigación Académica**
- Análisis estadístico sin datos sensibles
- Estudios de accesibilidad urbana
- Modelado de servicios públicos

---

## 🔍 Métricas de Accesibilidad Calculadas

### **Métricas Generales**
- Distancia promedio al centro más cercano
- Distancia mediana y máxima
- Porcentaje con centro en su localidad
- Distribución por rangos de distancia (0-2km, 2-5km, 5-10km, >10km)

### **Análisis por Localidad**
- Distancia promedio por localidad
- Porcentaje de cobertura local
- Ranking de accesibilidad

### **Grupos Vulnerables**
- Adultos mayores (60+)
- Menores de edad (0-17)
- Estratos socioeconómicos bajos (1-2)
- Población sin afiliación a salud
- Régimen subsidiado

### **Análisis de Centros**
- Centros más demandados
- Relación capacidad-demanda
- Distribución geográfica de la demanda

---

## 🚨 Alertas y Recomendaciones Automáticas

El sistema genera automáticamente:
- **Alertas de accesibilidad**: Localidades con distancias promedio > 5km
- **Recomendaciones de ubicación**: Zonas prioritarias para nuevos centros
- **Análisis de capacidad**: Centros con alta demanda vs capacidad
- **Grupos de riesgo**: Poblaciones vulnerables con baja accesibilidad

---

## ⚠️ Limitaciones y Consideraciones

### **Limitaciones de los Datos**
- Los datos de población son completamente sintéticos
- Las coordenadas de centros son aproximadas por localidad
- Las distribuciones se basan en fuentes públicas de 2021-2024
- No incluye información económica específica detallada

### **Limitaciones del Análisis**
- Las distancias son calculadas en línea recta (haversine)
- No considera barreras geográficas específicas (ríos, montañas)
- No incluye análisis de transporte público
- No considera horarios de atención de centros
- No incluye tiempos de desplazamiento reales

### **Uso Recomendado**
- Para análisis oficial, usar siempre datos reales del DANE y Secretaría de Salud
- Los resultados son indicativos para planificación preliminar
- Validar hallazgos con datos reales antes de tomar decisiones

### **🆕 Nota sobre Entrada Manual**
- **Problema**: Los scripts originales requerían entrada manual del usuario
- **Solución**: Se crearon versiones automáticas que no requieren interacción
- **Recomendación**: Usa `ejecutar_automatico.py` o los scripts `.bat/.sh`

---

## 🆘 Solución de Problemas

### Error: "ModuleNotFoundError"
```bash
pip install pandas numpy matplotlib seaborn
```

### Error: "No se encontró el archivo CSV"
```bash
# Ejecutar primero el generador
python main_corregido.py
```

### Error: "centros_salud.csv no encontrado"
```bash
# Verificar que el archivo está en el directorio del proyecto
# El análisis de centros se saltará automáticamente
```

### Problemas de memoria con muestras grandes
```bash
# Reducir el tamaño de muestra
# El sistema maneja automáticamente muestras grandes
```

---

## 📞 Comparación: Versión Anterior vs Mejorada

| Aspecto | ❌ Versión Anterior | ✅ Versión Mejorada |
|---------|---------------------|---------------------|
| **Funcionalidad** | Solo análisis demográfico | Demografía + Centros de salud |
| **Estructura** | Archivos duplicados | Modular y organizada |
| **Accesibilidad** | No incluida | Análisis completo |
| **Visualizaciones** | Básicas | Avanzadas con accesibilidad |
| **Reportes** | 1 reporte básico | 2 reportes especializados |
| **Limpieza** | Archivos obsoletos | Solo archivos necesarios |
| **Documentación** | Básica | Completa y detallada |
| **Casos de uso** | Limitados | Múltiples sectores |

---

## 🏃‍♂️ Inicio Rápido (5 minutos)

```bash
# Paso 1: Instalar dependencias
pip install pandas numpy matplotlib seaborn

# Paso 2: Ejecutar sistema completo
python main_corregido.py

# Paso 3: Seguir las instrucciones en pantalla
# Elegir tamaño de muestra (recomendado: 5000)

# Paso 4: Ver resultados
# Archivos generados en: resultados_analisis_bogota/
```

---

## 🎯 Próximos Pasos Recomendados

1. **Ejecutar el sistema mejorado** con `python main_corregido.py`
2. **Revisar los reportes** en `resultados_analisis_bogota/`
3. **Analizar visualizaciones** de accesibilidad sanitaria
4. **Adaptar el código** para tus necesidades específicas
5. **Integrar con datos reales** para validación

---

## 📋 Lista de Verificación de Mejoras

- [x] ✅ Archivos duplicados eliminados
- [x] ✅ Módulo de centros de salud creado
- [x] ✅ Cálculo de distancias implementado
- [x] ✅ Métricas de accesibilidad desarrolladas
- [x] ✅ Visualizaciones de accesibilidad creadas
- [x] ✅ Pipeline integrado y automatizado
- [x] ✅ Reportes especializados generados
- [x] ✅ Documentación completa actualizada
- [x] ✅ Manejo de errores mejorado
- [x] ✅ Limpieza de código realizada

---

## 🤝 Contribuciones y Feedback

Si encuentras problemas o tienes sugerencias:

1. Verifica que tienes las dependencias básicas instaladas
2. Ejecuta `python main_corregido.py` para la versión estable
3. Revisa este README para soluciones comunes
4. Consulta los archivos de log para diagnósticos

---

## 📜 Licencia

Este proyecto está diseñado para uso educativo y de investigación. Los datos generados son completamente sintéticos y no representan información real de personas.

---

## 🏆 Créditos

- **Datos de centros de salud**: Basados en información pública de la Secretaría de Salud de Bogotá
- **Distribuciones demográficas**: Basadas en datos del DANE y estudios demográficos
- **Geocodificación**: Aproximada usando coordenadas conocidas de localidades

---

Ejecuta `python main_corregido.py` para comenzar a generar y analizar datos sintéticos de la población de Bogotá con análisis completo de accesibilidad a centros de salud.

**🆕 Nueva funcionalidad**: El sistema ahora calcula automáticamente la cercanía entre cada persona registrada y los centros de salud disponibles, proporcionando métricas de accesibilidad y cobertura sanitaria para apoyar la toma de decisiones en salud pública.
