# Demographic Accessibility Bogotá 🏙️🚑

**Comprehensive Demographic Analysis and Healthcare Accessibility Assessment for Bogotá D.C.**

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

## 📋 Project Overview

**Demographic Accessibility Bogotá** is a comprehensive analytical system that generates synthetic demographic data for Bogotá D.C. and evaluates healthcare accessibility across the city's 20 localities. This tool supports urban planning, public health policy development, and accessibility research by providing detailed insights into population distribution and healthcare service coverage.

### 🎯 **Core Functionality**
- **Synthetic Population Generation**: Creates realistic demographic datasets for Bogotá
- **Healthcare Accessibility Analysis**: Calculates distance and accessibility metrics to health centers
- **Vulnerability Assessment**: Identifies underserved populations and geographic gaps
- **Interactive Visualizations**: Generates maps and charts for policy decision-making
- **Automated Reporting**: Produces comprehensive reports for stakeholders

---

## ✨ Key Features

### 🏥 **Healthcare Accessibility Analysis**
- ✅ Real health center data processing for Bogotá D.C.
- ✅ Automated geocoding by locality
- ✅ Haversine distance calculations between population and health centers
- ✅ Accessibility metrics and coverage analysis
- ✅ Vulnerable population group analysis
- ✅ Geospatial accessibility visualizations
- ✅ Capacity vs demand analysis

### 📊 **Demographic Intelligence**
- ✅ Synthetic population generation based on real demographic patterns
- ✅ 20 Bogotá localities representation
- ✅ Socioeconomic stratification (levels 1-6)
- ✅ Age, gender, and education level distributions
- ✅ Healthcare affiliation modeling
- ✅ Geographic coordinate assignment

### 🗺️ **Geospatial Integration**
- ✅ Interactive map generation with health center locations
- ✅ Population density heat maps
- ✅ Accessibility corridor visualization
- ✅ Multi-layer map controls for different data views
- ✅ Export capabilities for GIS applications

### 📈 **Advanced Analytics**
- ✅ Statistical correlation analysis
- ✅ Vulnerability scoring algorithms
- ✅ Distance-based accessibility rankings
- ✅ Demographic segmentation analysis
- ✅ Automated alert systems for policy recommendations

---

## 🚀 Quick Start

### **Prerequisites**
```bash
# Minimum requirements
Python 3.7+
pip package manager
```

### **Installation**
```bash
# 1. Clone the repository
git clone https://github.com/ingermanr/demographic-accessibility-bogota.git
cd demographic-accessibility-bogota

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the complete analysis
python main_corregido.py
```

### **Alternative: Specific Analysis**
```bash
# Healthcare accessibility analysis only
python analizador_centros_salud.py

# Interactive map integration
python ejecutar_integracion.py

# System testing
python test_sistema.py
```

---

## 📁 Project Structure

```
demographic-accessibility-bogota/
├── 📄 main_corregido.py                     # ⭐ MAIN EXECUTION FILE
├── 📄 generador_datos_sinteticos_bogota.py  # Synthetic population generator
├── 📄 validador_datos_sinteticos.py         # Demographic analysis engine
├── 📄 analizador_centros_salud.py           # 🏥 Healthcare accessibility analyzer
├── 📄 integrador_centros_salud_v2.py        # Interactive map generator
├── 📄 ejecutar_integracion.py               # Map integration executor
├── 📄 demo_integracion.py                   # Integration demonstration
├── 📄 caso_uso.py                           # Use case implementations
├── 📄 test_sistema.py                       # 🧪 System testing suite
├── 📄 test_caso_uso.py                      # 🧪 Use case testing
├── 📄 centros_salud.csv                     # 🏥 Health centers database
├── 📄 requirements.txt                      # 📦 Dependencies
├── 📄 .gitignore                           # Git ignore rules
├── 📄 LICENSE                              # MIT License
├── 📄 README.md                            # This documentation
├── 📄 README_integracion_centros.md        # Map integration guide
└── 📂 resultados_analisis_bogota/          # 📊 OUTPUT DIRECTORY
    ├── poblacion_sintetica_bogota.csv      # Generated synthetic population
    ├── poblacion_sintetica_bogota.json     # Population data (JSON format)
    ├── analisis_demografico_bogota.png     # Demographic visualizations
    ├── analisis_accesibilidad_centros_salud.png # Accessibility charts
    ├── matriz_correlacion.png             # Correlation analysis
    ├── reporte_datos_sinteticos.txt       # Demographic report
    ├── reporte_accesibilidad_salud.txt    # Healthcare accessibility report
    ├── analisis_accesibilidad_poblacion.csv # Population accessibility data
    ├── centros_salud_procesados.csv       # Processed health centers
    └── resumen_ejecutivo.txt              # Executive summary
```

---

## 💻 Programming Interface

### **Complete Analysis Pipeline**
```python
from main_corregido import SistemaDatosSinteticosBogota

# Initialize the system
sistema = SistemaDatosSinteticosBogota()

# Execute complete demographic and accessibility analysis
success = sistema.ejecutar_pipeline_completo(tamaño_muestra=5000)

if success:
    print("✅ Analysis completed successfully!")
    print("📊 Check results in: resultados_analisis_bogota/")
```

### **Healthcare Accessibility Analysis**
```python
from analizador_centros_salud import SistemaAccesibilidadSalud

# Create accessibility analysis system
accessibility_system = SistemaAccesibilidadSalud(
    population_file='poblacion_sintetica_bogota.csv', 
    health_centers_file='centros_salud.csv'
)

# Execute comprehensive accessibility analysis
results = accessibility_system.ejecutar_analisis_completo(muestra_poblacion=3000)

# Access key metrics
if results and 'metricas' in results:
    metrics = results['metricas']
    print(f"Average distance to nearest health center: {metrics['distancia_promedio']:.2f} km")
    print(f"Population with local health center: {metrics['pct_misma_localidad']:.1f}%")
```

### **Interactive Map Generation**
```python
from integrador_centros_salud_v2 import IntegradorCentrosSaludBogota

# Create map integrator
integrator = IntegradorCentrosSaludBogota()

# Generate interactive map with health centers and population data
map_obj, processed_data = integrator.ejecutar_integracion(
    archivo_centros_csv="centros_salud.csv",
    archivo_poblacion_csv="resultados_analisis_bogota/poblacion_sintetica_bogota.csv",
    archivo_salida="interactive_accessibility_map.html"
)
```

---

## 📊 Generated Data Schema

### **Synthetic Population Dataset**
| Field | Description | Example |
|-------|-------------|---------|
| `id` | Unique identifier | "KEN123456" |
| `nombre` | Synthetic first name | "María" |
| `apellido1` | First surname | "García" |
| `apellido2` | Second surname | "López" |
| `genero` | Gender (F/M) | "F" |
| `edad` | Age in years | 34 |
| `localidad` | Bogotá locality (1-20) | "Kennedy" |
| `estrato` | Socioeconomic stratum (1-6) | 3 |
| `nivel_educativo` | Education level | "Universitaria" |
| `afiliacion_salud` | Health insurance type | "Contributivo" |
| `latitud` | Geographic latitude | 4.6281 |
| `longitud` | Geographic longitude | -74.1597 |

### **Health Centers Database**
| Field | Description | Example |
|-------|-------------|---------|
| `centro_salud` | Health center name | "Hospital Kennedy" |
| `barrio` | Specific neighborhood | "Kennedy Central" |
| `localidad` | Bogotá locality | "Kennedy" |
| `capacidad_ambulancias` | Number of ambulances | 5 |
| `capacidad_camas` | Number of beds | 120 |
| `capacidad_camillas` | Number of stretchers | 15 |
| `capacidad_consultorios` | Number of consultation rooms | 25 |
| `capacidad_salas` | Number of operating rooms | 8 |
| `latitud` | Health center latitude | 4.6285 |
| `longitud` | Health center longitude | -74.1605 |

### **Accessibility Analysis Dataset**
| Field | Description | Example |
|-------|-------------|---------|
| `persona_id` | Person identifier | "KEN123456" |
| `persona_localidad` | Residence locality | "Kennedy" |
| `centro_cercano` | Nearest health center | "Hospital Kennedy" |
| `distancia_km` | Distance in kilometers | 2.3 |
| `misma_localidad` | Same locality flag | True |
| `capacidad_centro` | Center total capacity | 173 |

---

## 📈 Analysis Outputs

### **Demographic Analysis Visualizations**
- Age distribution histograms
- Gender composition pie charts
- Socioeconomic stratum distribution
- Top 10 localities by population
- Education level breakdown
- Health insurance affiliation patterns

### **Healthcare Accessibility Visualizations**
- Distance distribution to nearest health centers
- Average distance by locality
- Local health center coverage percentages
- Capacity vs demand analysis by center
- Vulnerable population accessibility maps

### **Correlation Analysis**
- Demographic variable correlation matrices
- Accessibility correlation with socioeconomic factors
- Geographic accessibility patterns

---

## 📋 Generated Reports

### **Demographic Intelligence Report** (`reporte_datos_sinteticos.txt`)
- Complete descriptive statistics
- Variable distribution analysis
- Population representativeness assessment
- Demographic trend identification

### **Healthcare Accessibility Report** (`reporte_accesibilidad_salud.txt`)
- General accessibility metrics
- Locality-specific analysis
- Vulnerable population assessment
- Most/least accessible areas identification
- Policy recommendations for healthcare planning

### **Executive Summary** (`resumen_ejecutivo.txt`)
- Key findings overview
- Critical accessibility gaps
- Priority intervention areas
- Actionable insights for decision-makers

---

## 🎯 Use Cases

### **🏛️ Urban Planning**
- **Service Location Optimization**: Identify optimal locations for new health centers
- **Population Growth Planning**: Predict future healthcare needs based on demographic trends
- **Resource Allocation**: Guide budget allocation for healthcare infrastructure
- **Accessibility Gap Analysis**: Identify underserved geographic areas

### **🏥 Public Health Policy**
- **Healthcare Access Equity**: Measure and improve healthcare accessibility equity
- **Vulnerable Population Support**: Target interventions for elderly, low-income, and uninsured populations
- **Emergency Response Planning**: Optimize ambulance and emergency service coverage
- **Health System Capacity Planning**: Balance demand and supply across localities

### **📊 Research Applications**
- **Academic Studies**: Provide synthetic datasets for demographic and accessibility research
- **Algorithm Development**: Test geospatial algorithms with realistic synthetic data
- **Policy Impact Modeling**: Simulate the impact of new health centers or policy changes
- **Accessibility Methodology Validation**: Test new accessibility measurement approaches

### **💻 Software Development**
- **Application Testing**: Realistic synthetic data for healthcare app development
- **GIS System Validation**: Test geographic information systems with comprehensive datasets
- **API Development**: Mock data for healthcare accessibility APIs
- **Machine Learning Training**: Synthetic datasets for accessibility prediction models

---

## 🔍 Calculated Accessibility Metrics

### **General Accessibility Metrics**
- Average distance to nearest health center
- Median and maximum distances
- Percentage of population with local health center access
- Distance range distribution (0-2km, 2-5km, 5-10km, >10km)

### **Locality-Specific Analysis**
- Average distance by locality ranking
- Local healthcare coverage percentages
- Accessibility inequality measures
- Geographic accessibility hotspots

### **Vulnerable Population Analysis**
- **Elderly Population (60+)**: Accessibility metrics for senior citizens
- **Pediatric Population (0-17)**: Child healthcare accessibility
- **Low Socioeconomic Status (Strata 1-2)**: Healthcare access for low-income populations
- **Uninsured Population**: Access analysis for those without health insurance
- **Subsidized Healthcare Recipients**: Analysis of public healthcare accessibility

### **Health Center Performance Metrics**
- Most demanded health centers
- Capacity utilization analysis
- Geographic demand distribution
- Service area coverage analysis

---

## 🚨 Automated Alerts and Recommendations

The system automatically generates:
- **Accessibility Alerts**: Localities with average distances > 5km to nearest health center
- **Location Recommendations**: Priority areas for new health center placement
- **Capacity Analysis**: Health centers with high demand vs. capacity ratios
- **Risk Group Identification**: Vulnerable populations with poor healthcare accessibility
- **Policy Recommendations**: Actionable insights for public health decision-makers

---

## ⚠️ Data Limitations and Considerations

### **Synthetic Data Limitations**
- Population data is completely synthetic and not representative of real individuals
- Health center coordinates are locality-approximated, not exact addresses
- Demographic distributions based on 2021-2024 public data sources
- No real-time economic or employment data included

### **Accessibility Analysis Limitations**
- Distances calculated as straight-line (haversine), not actual travel routes
- No consideration of geographic barriers (rivers, mountains, infrastructure)
- Public transportation routes and schedules not included
- Health center operating hours not considered
- Emergency vs. routine care accessibility not differentiated

### **Recommended Validation**
- Always validate findings with real DANE (National Statistics) data
- Cross-reference with Bogotá Health Secretary official databases
- Consider real transportation networks for practical accessibility
- Validate health center locations with Google Maps or official sources
- Include real demographic data for official policy decisions

---

## 🛠️ Technical Requirements

### **Minimum System Requirements**
- **Python**: 3.7 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 1GB available space
- **OS**: Windows 10+, macOS 10.14+, Ubuntu 18.04+

### **Required Dependencies**
```bash
pandas>=1.3.0        # Data manipulation and analysis
numpy>=1.20.0         # Numerical computing
matplotlib>=3.3.0     # Static plotting
seaborn>=0.11.0       # Statistical visualization
```

### **Optional Dependencies**
```bash
folium>=0.12.0        # Interactive mapping (recommended)
geopandas>=0.9.0      # Geospatial analysis
geopy>=2.1.0          # Geographic calculations
plotly>=5.0.0         # Interactive plots
scikit-learn>=1.0.0   # Machine learning algorithms
```

---

## 🔧 Troubleshooting

### **Common Installation Issues**
```bash
# Missing dependencies error
pip install --upgrade pip
pip install -r requirements.txt

# Data file not found
python main_corregido.py  # Generates required data files

# Memory issues with large samples
# Reduce sample size in configuration files
```

### **Performance Optimization**
- **Large Datasets**: Use sample sizes ≤ 10,000 for initial analysis
- **Memory Management**: Close other applications when processing large datasets
- **Geographic Processing**: Consider using geographic subsets for detailed analysis

---

## 📊 Performance Benchmarks

| Sample Size | Processing Time | Memory Usage | Output Size |
|-------------|----------------|--------------|-------------|
| 1,000 | ~30 seconds | ~200MB | ~5MB |
| 5,000 | ~2 minutes | ~500MB | ~25MB |
| 10,000 | ~4 minutes | ~1GB | ~50MB |
| 25,000 | ~10 minutes | ~2.5GB | ~125MB |

*Benchmarks based on Intel i5 processor, 8GB RAM*

---

## 🤝 Contributing

We welcome contributions to improve the demographic accessibility analysis capabilities:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/accessibility-improvement`)
3. **Commit changes** (`git commit -am 'Add new accessibility metric'`)
4. **Push to branch** (`git push origin feature/accessibility-improvement`)
5. **Create Pull Request**

### **Contribution Areas**
- New accessibility metrics implementation
- Additional visualization types
- Performance optimizations
- Documentation improvements
- Test coverage expansion

---

## 📞 Support

### **Documentation**
- 📖 **Main Documentation**: This README
- 🗺️ **Map Integration Guide**: `README_integracion_centros.md`
- 📊 **API Reference**: Check docstrings in main modules

### **Getting Help**
1. Check existing documentation and troubleshooting sections
2. Review the issues section for similar problems
3. Create a new issue with detailed error information
4. Include your system configuration and sample data when reporting bugs

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Academic and Research Use**: This tool is designed for educational, research, and non-commercial policy analysis purposes. Generated synthetic data should not be used as a substitute for official demographic or health statistics.

---

## 🏆 Acknowledgments

- **Bogotá Health Secretary**: Health center data based on public information
- **DANE**: Demographic distributions based on national statistics
- **OpenStreetMap Community**: Geographic coordinate references
- **Python Community**: Open-source libraries that make this analysis possible

---

## 🔗 Related Projects

- [Bogotá Open Data](https://datosabiertos.bogota.gov.co/): Official Bogotá open data portal
- [DANE Colombia](https://www.dane.gov.co/): National statistics department
- [WHO Health Facility Assessments](https://www.who.int/): Global health accessibility frameworks

---

## 📈 Roadmap

### **Version 2.0 Planning**
- [ ] Real-time public transportation integration
- [ ] Multi-city analysis capabilities  
- [ ] Advanced machine learning accessibility predictions
- [ ] Web-based dashboard interface
- [ ] API development for external integrations
- [ ] Real-time health center capacity monitoring

### **Current Version: 1.5**
- [x] ✅ Complete demographic synthesis
- [x] ✅ Healthcare accessibility analysis
- [x] ✅ Interactive map generation
- [x] ✅ Vulnerability assessment
- [x] ✅ Automated reporting pipeline
- [x] ✅ Comprehensive documentation

---

**🎯 Ready to analyze demographic accessibility in Bogotá? Run `python main_corregido.py` to start your comprehensive analysis!**

---

*This project provides valuable insights for urban planning and public health policy development in Bogotá D.C., supporting evidence-based decision-making for improved healthcare accessibility across all socioeconomic levels and geographic areas.*
