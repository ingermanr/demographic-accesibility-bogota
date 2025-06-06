# Archivo principal del generador de datos sintéticos de Bogotá
# Este archivo resuelve los problemas de imports del proyecto

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import json

# Configuración de semilla para reproducibilidad
np.random.seed(42)
random.seed(42)

class GeneradorDatosSinteticosBogota:
    def __init__(self):
        # Coordenadas aproximadas de cada localidad (centro geográfico)
        self.coordenadas_localidades = {
            'Usaquén': {'lat': 4.7017, 'lon': -74.0307, 'radio_km': 8},
            'Chapinero': {'lat': 4.6357, 'lon': -74.0675, 'radio_km': 4},
            'Santa Fe': {'lat': 4.6097, 'lon': -74.0817, 'radio_km': 5},
            'San Cristóbal': {'lat': 4.5647, 'lon': -74.0889, 'radio_km': 7},
            'Usme': {'lat': 4.4793, 'lon': -74.1361, 'radio_km': 12},
            'Tunjuelito': {'lat': 4.5739, 'lon': -74.1329, 'radio_km': 4},
            'Bosa': {'lat': 4.6189, 'lon': -74.1798, 'radio_km': 8},
            'Kennedy': {'lat': 4.6281, 'lon': -74.1597, 'radio_km': 10},
            'Fontibón': {'lat': 4.6711, 'lon': -74.1453, 'radio_km': 6},
            'Engativá': {'lat': 4.7045, 'lon': -74.1147, 'radio_km': 7},
            'Suba': {'lat': 4.7539, 'lon': -74.0816, 'radio_km': 12},
            'Barrios Unidos': {'lat': 4.6759, 'lon': -74.0697, 'radio_km': 3},
            'Teusaquillo': {'lat': 4.6409, 'lon': -74.0889, 'radio_km': 3},
            'Los Mártires': {'lat': 4.6097, 'lon': -74.0999, 'radio_km': 2},
            'Antonio Nariño': {'lat': 4.5889, 'lon': -74.1069, 'radio_km': 2},
            'Puente Aranda': {'lat': 4.6259, 'lon': -74.1169, 'radio_km': 4},
            'La Candelaria': {'lat': 4.5981, 'lon': -74.0759, 'radio_km': 1.5},
            'Rafael Uribe Uribe': {'lat': 4.5497, 'lon': -74.1169, 'radio_km': 5},
            'Ciudad Bolívar': {'lat': 4.4859, 'lon': -74.1589, 'radio_km': 15},
            'Sumapaz': {'lat': 4.2059, 'lon': -74.3589, 'radio_km': 25}
        }
        
        # Distribuciones demográficas por localidad
        self.distribuciones = {
            'Usaquén': {
                'poblacion': 460000,
                'estratos': {1: 0, 2: 0, 3: 25, 4: 35, 5: 25, 6: 15},
                'genero': {'F': 52.3, 'M': 47.7},
                'educacion': {'Primaria': 20, 'Secundaria': 28, 'Técnica': 30, 'Universitaria': 22},
                'salud': {'Contributivo': 75, 'Subsidiado': 20, 'No_afiliado': 5},
                'edad': {'0-17': 18, '18-59': 68, '60+': 14}
            },
            'Chapinero': {
                'poblacion': 140000,
                'estratos': {1: 0, 2: 0, 3: 15, 4: 30, 5: 35, 6: 20},
                'genero': {'F': 53, 'M': 47},
                'educacion': {'Primaria': 15, 'Secundaria': 25, 'Técnica': 31, 'Universitaria': 29},
                'salud': {'Contributivo': 80, 'Subsidiado': 15, 'No_afiliado': 5},
                'edad': {'0-17': 15, '18-59': 72, '60+': 13}
            },
            'Santa Fe': {
                'poblacion': 110000,
                'estratos': {1: 20, 2: 35, 3: 30, 4: 15, 5: 0, 6: 0},
                'genero': {'F': 51, 'M': 49},
                'educacion': {'Primaria': 40, 'Secundaria': 30, 'Técnica': 15, 'Universitaria': 15},
                'salud': {'Contributivo': 45, 'Subsidiado': 50, 'No_afiliado': 5},
                'edad': {'0-17': 22, '18-59': 65, '60+': 13}
            },
            'San Cristóbal': {
                'poblacion': 404000,
                'estratos': {1: 25, 2: 45, 3: 25, 4: 5, 5: 0, 6: 0},
                'genero': {'F': 52, 'M': 48},
                'educacion': {'Primaria': 45, 'Secundaria': 32, 'Técnica': 11, 'Universitaria': 12},
                'salud': {'Contributivo': 40, 'Subsidiado': 55, 'No_afiliado': 5},
                'edad': {'0-17': 25, '18-59': 63, '60+': 12}
            },
            'Usme': {
                'poblacion': 350000,
                'estratos': {1: 35, 2: 45, 3: 20, 4: 0, 5: 0, 6: 0},
                'genero': {'F': 51.5, 'M': 48.5},
                'educacion': {'Primaria': 50, 'Secundaria': 30, 'Técnica': 10, 'Universitaria': 10},
                'salud': {'Contributivo': 35, 'Subsidiado': 60, 'No_afiliado': 5},
                'edad': {'0-17': 28, '18-59': 62, '60+': 10}
            },
            'Tunjuelito': {
                'poblacion': 200000,
                'estratos': {1: 0, 2: 70, 3: 25, 4: 5, 5: 0, 6: 0},
                'genero': {'F': 52, 'M': 48},
                'educacion': {'Primaria': 40, 'Secundaria': 35, 'Técnica': 11, 'Universitaria': 14},
                'salud': {'Contributivo': 50, 'Subsidiado': 45, 'No_afiliado': 5},
                'edad': {'0-17': 23, '18-59': 65, '60+': 12}
            },
            'Bosa': {
                'poblacion': 750000,
                'estratos': {1: 30, 2: 50, 3: 20, 4: 0, 5: 0, 6: 0},
                'genero': {'F': 51.5, 'M': 48.5},
                'educacion': {'Primaria': 45, 'Secundaria': 35, 'Técnica': 8, 'Universitaria': 12},
                'salud': {'Contributivo': 40, 'Subsidiado': 55, 'No_afiliado': 5},
                'edad': {'0-17': 26, '18-59': 64, '60+': 10}
            },
            'Kennedy': {
                'poblacion': 1200000,
                'estratos': {1: 0, 2: 45, 3: 40, 4: 15, 5: 0, 6: 0},
                'genero': {'F': 52, 'M': 48},
                'educacion': {'Primaria': 35, 'Secundaria': 38, 'Técnica': 11, 'Universitaria': 16},
                'salud': {'Contributivo': 55, 'Subsidiado': 40, 'No_afiliado': 5},
                'edad': {'0-17': 24, '18-59': 66, '60+': 10}
            },
            'Fontibón': {
                'poblacion': 380000,
                'estratos': {1: 0, 2: 35, 3: 45, 4: 20, 5: 0, 6: 0},
                'genero': {'F': 51, 'M': 49},
                'educacion': {'Primaria': 32, 'Secundaria': 40, 'Técnica': 10, 'Universitaria': 18},
                'salud': {'Contributivo': 60, 'Subsidiado': 35, 'No_afiliado': 5},
                'edad': {'0-17': 22, '18-59': 68, '60+': 10}
            },
            'Engativá': {
                'poblacion': 850000,
                'estratos': {1: 0, 2: 40, 3: 45, 4: 15, 5: 0, 6: 0},
                'genero': {'F': 52, 'M': 48},
                'educacion': {'Primaria': 33, 'Secundaria': 40, 'Técnica': 10, 'Universitaria': 17},
                'salud': {'Contributivo': 58, 'Subsidiado': 37, 'No_afiliado': 5},
                'edad': {'0-17': 23, '18-59': 67, '60+': 10}
            },
            'Suba': {
                'poblacion': 1300000,
                'estratos': {1: 0, 2: 35, 3: 40, 4: 20, 5: 5, 6: 0},
                'genero': {'F': 52.5, 'M': 47.5},
                'educacion': {'Primaria': 30, 'Secundaria': 42, 'Técnica': 9, 'Universitaria': 19},
                'salud': {'Contributivo': 62, 'Subsidiado': 33, 'No_afiliado': 5},
                'edad': {'0-17': 22, '18-59': 68, '60+': 10}
            },
            'Barrios Unidos': {
                'poblacion': 240000,
                'estratos': {1: 0, 2: 0, 3: 60, 4: 30, 5: 10, 6: 0},
                'genero': {'F': 53, 'M': 47},
                'educacion': {'Primaria': 25, 'Secundaria': 40, 'Técnica': 10, 'Universitaria': 25},
                'salud': {'Contributivo': 70, 'Subsidiado': 25, 'No_afiliado': 5},
                'edad': {'0-17': 18, '18-59': 70, '60+': 12}
            },
            'Teusaquillo': {
                'poblacion': 143000,
                'estratos': {1: 0, 2: 0, 3: 0, 4: 60, 5: 30, 6: 10},
                'genero': {'F': 55, 'M': 45},
                'educacion': {'Primaria': 20, 'Secundaria': 30, 'Técnica': 15, 'Universitaria': 35},
                'salud': {'Contributivo': 85, 'Subsidiado': 10, 'No_afiliado': 5},
                'edad': {'0-17': 15, '18-59': 70, '60+': 15}
            },
            'Los Mártires': {
                'poblacion': 95000,
                'estratos': {1: 0, 2: 50, 3: 35, 4: 15, 5: 0, 6: 0},
                'genero': {'F': 51, 'M': 49},
                'educacion': {'Primaria': 35, 'Secundaria': 35, 'Técnica': 10, 'Universitaria': 20},
                'salud': {'Contributivo': 55, 'Subsidiado': 40, 'No_afiliado': 5},
                'edad': {'0-17': 20, '18-59': 68, '60+': 12}
            },
            'Antonio Nariño': {
                'poblacion': 110000,
                'estratos': {1: 0, 2: 45, 3: 40, 4: 15, 5: 0, 6: 0},
                'genero': {'F': 52, 'M': 48},
                'educacion': {'Primaria': 35, 'Secundaria': 38, 'Técnica': 9, 'Universitaria': 18},
                'salud': {'Contributivo': 58, 'Subsidiado': 37, 'No_afiliado': 5},
                'edad': {'0-17': 21, '18-59': 67, '60+': 12}
            },
            'Puente Aranda': {
                'poblacion': 250000,
                'estratos': {1: 0, 2: 40, 3: 45, 4: 15, 5: 0, 6: 0},
                'genero': {'F': 51, 'M': 49},
                'educacion': {'Primaria': 33, 'Secundaria': 40, 'Técnica': 10, 'Universitaria': 17},
                'salud': {'Contributivo': 60, 'Subsidiado': 35, 'No_afiliado': 5},
                'edad': {'0-17': 22, '18-59': 68, '60+': 10}
            },
            'La Candelaria': {
                'poblacion': 24000,
                'estratos': {1: 30, 2: 40, 3: 25, 4: 5, 5: 0, 6: 0},
                'genero': {'F': 50, 'M': 50},
                'educacion': {'Primaria': 35, 'Secundaria': 30, 'Técnica': 10, 'Universitaria': 25},
                'salud': {'Contributivo': 45, 'Subsidiado': 50, 'No_afiliado': 5},
                'edad': {'0-17': 18, '18-59': 70, '60+': 12}
            },
            'Rafael Uribe Uribe': {
                'poblacion': 380000,
                'estratos': {1: 20, 2: 50, 3: 25, 4: 5, 5: 0, 6: 0},
                'genero': {'F': 52, 'M': 48},
                'educacion': {'Primaria': 42, 'Secundaria': 35, 'Técnica': 10, 'Universitaria': 13},
                'salud': {'Contributivo': 45, 'Subsidiado': 50, 'No_afiliado': 5},
                'edad': {'0-17': 24, '18-59': 65, '60+': 11}
            },
            'Ciudad Bolívar': {
                'poblacion': 760000,
                'estratos': {1: 45, 2: 40, 3: 15, 4: 0, 5: 0, 6: 0},
                'genero': {'F': 51, 'M': 49},
                'educacion': {'Primaria': 52, 'Secundaria': 30, 'Técnica': 10, 'Universitaria': 8},
                'salud': {'Contributivo': 30, 'Subsidiado': 65, 'No_afiliado': 5},
                'edad': {'0-17': 30, '18-59': 60, '60+': 10}
            },
            'Sumapaz': {
                'poblacion': 7000,
                'estratos': {1: 60, 2: 35, 3: 5, 4: 0, 5: 0, 6: 0},
                'genero': {'F': 49, 'M': 51},
                'educacion': {'Primaria': 60, 'Secundaria': 25, 'Técnica': 10, 'Universitaria': 5},
                'salud': {'Contributivo': 15, 'Subsidiado': 80, 'No_afiliado': 5},
                'edad': {'0-17': 32, '18-59': 58, '60+': 10}
            }
        }
        
        # Nombres comunes en Colombia
        self.nombres_femeninos = [
            'María', 'Ana', 'Carmen', 'Luz', 'Rosa', 'Gloria', 'Esperanza', 'Patricia',
            'Martha', 'Sandra', 'Jenny', 'Diana', 'Carolina', 'Andrea', 'Paola', 'Claudia',
            'Marcela', 'Adriana', 'Mónica', 'Alejandra', 'Natalia', 'Catalina', 'Valentina',
            'Sofía', 'Isabella', 'Camila', 'Juliana', 'Daniela', 'Gabriela', 'Fernanda'
        ]
        
        self.nombres_masculinos = [
            'José', 'Carlos', 'Luis', 'Juan', 'Diego', 'Andrés', 'Fernando', 'Jorge',
            'Miguel', 'David', 'Daniel', 'Alejandro', 'Oscar', 'Mauricio', 'Ricardo',
            'Sergio', 'Roberto', 'Francisco', 'Rafael', 'Eduardo', 'Gonzalo', 'Jairo',
            'Felipe', 'Sebastián', 'Santiago', 'Nicolás', 'Mateo', 'Samuel', 'Emilio'
        ]
        
        self.apellidos = [
            'García', 'Rodríguez', 'López', 'Martínez', 'González', 'Pérez', 'Sánchez',
            'Ramírez', 'Cruz', 'Flores', 'Gómez', 'Díaz', 'Reyes', 'Morales', 'Jiménez',
            'Herrera', 'Medina', 'Castro', 'Vargas', 'Ortiz', 'Ramos', 'Delgado',
            'Torres', 'Vega', 'Mendoza', 'Rojas', 'Aguilar', 'Moreno', 'Gutiérrez', 'Silva'
        ]

    def generar_coordenadas_aleatorias(self, localidad):
        """Genera coordenadas aleatorias dentro del área de una localidad"""
        coords = self.coordenadas_localidades[localidad]
        centro_lat, centro_lon = coords['lat'], coords['lon']
        radio_km = coords['radio_km']
        
        # Convertir radio a grados (aproximadamente 1° = 111 km)
        radio_grados = radio_km / 111.0
        
        # Generar punto aleatorio en círculo
        angle = random.uniform(0, 2 * np.pi)
        radius = random.uniform(0, radio_grados) * np.sqrt(random.random())
        
        lat = centro_lat + radius * np.cos(angle)
        lon = centro_lon + radius * np.sin(angle)
        
        return round(lat, 6), round(lon, 6)

    def seleccionar_por_distribucion(self, distribucion):
        """Selecciona un valor basado en una distribución de probabilidades"""
        opciones = list(distribucion.keys())
        probabilidades = [distribucion[k] / 100.0 for k in opciones]
        return np.random.choice(opciones, p=probabilidades)

    def generar_edad_por_grupo(self, grupo_edad):
        """Genera una edad específica dentro del grupo"""
        if grupo_edad == '0-17':
            return random.randint(0, 17)
        elif grupo_edad == '18-59':
            return random.randint(18, 59)
        else:  # 60+
            return random.randint(60, 95)

    def generar_persona_sintetica(self, localidad):
        """Genera los datos de una persona sintética"""
        dist = self.distribuciones[localidad]
        
        # Generar características demográficas
        genero = self.seleccionar_por_distribucion(dist['genero'])
        grupo_edad = self.seleccionar_por_distribucion(dist['edad'])
        edad = self.generar_edad_por_grupo(grupo_edad)
        estrato = int(self.seleccionar_por_distribucion({k: v for k, v in dist['estratos'].items() if v > 0}))
        educacion = self.seleccionar_por_distribucion(dist['educacion'])
        afiliacion_salud = self.seleccionar_por_distribucion(dist['salud'])
        
        # Generar nombre
        if genero == 'F':
            nombre = random.choice(self.nombres_femeninos)
        else:
            nombre = random.choice(self.nombres_masculinos)
        
        apellido1 = random.choice(self.apellidos)
        apellido2 = random.choice(self.apellidos)
        
        # Generar coordenadas
        latitud, longitud = self.generar_coordenadas_aleatorias(localidad)
        
        # Generar ID único
        id_persona = f"{localidad[:3].upper()}{random.randint(100000, 999999)}"
        
        return {
            'id': id_persona,
            'nombre': nombre,
            'apellido1': apellido1,
            'apellido2': apellido2,
            'genero': genero,
            'edad': edad,
            'grupo_edad': grupo_edad,
            'localidad': localidad,
            'estrato': estrato,
            'nivel_educativo': educacion,
            'afiliacion_salud': afiliacion_salud,
            'latitud': latitud,
            'longitud': longitud,
            'fecha_generacion': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

    def generar_dataset(self, muestra_total=100000, proporcional=True):
        """
        Genera un dataset completo de personas sintéticas
        
        Args:
            muestra_total: Número total de registros a generar
            proporcional: Si True, respeta las proporciones reales de población por localidad
        """
        datos = []
        
        if proporcional:
            # Calcular población total real
            poblacion_total = sum(self.distribuciones[loc]['poblacion'] for loc in self.distribuciones)
            
            # Generar registros proporcionalmente
            for localidad, dist in self.distribuciones.items():
                proporcion = dist['poblacion'] / poblacion_total
                n_registros = int(muestra_total * proporcion)
                
                print(f"Generando {n_registros} registros para {localidad}...")
                
                for _ in range(n_registros):
                    persona = self.generar_persona_sintetica(localidad)
                    datos.append(persona)
        else:
            # Distribución uniforme entre localidades
            registros_por_localidad = muestra_total // len(self.distribuciones)
            
            for localidad in self.distribuciones:
                print(f"Generando {registros_por_localidad} registros para {localidad}...")
                
                for _ in range(registros_por_localidad):
                    persona = self.generar_persona_sintetica(localidad)
                    datos.append(persona)
        
        return pd.DataFrame(datos)

# Ejemplo de uso
if __name__ == "__main__":
    generador = GeneradorDatosSinteticosBogota()
    
    # Generar dataset de muestra (10,000 registros)
    print("Iniciando generación de datos sintéticos...")
    df_poblacion = generador.generar_dataset(muestra_total=10000, proporcional=True)
    
    # Mostrar estadísticas del dataset generado
    print(f"\nDataset generado con {len(df_poblacion)} registros")
    print("\nDistribución por localidad:")
    print(df_poblacion['localidad'].value_counts().sort_index())
    
    print("\nDistribución por género:")
    print(df_poblacion['genero'].value_counts(normalize=True) * 100)
    
    print("\nDistribución por estrato:")
    print(df_poblacion['estrato'].value_counts().sort_index())
    
    print("\nPrimeros 5 registros:")
    print(df_poblacion.head())
    
    # Guardar dataset
    df_poblacion.to_csv('poblacion_sintetica_bogota.csv', index=False, encoding='utf-8')
    df_poblacion.to_json('poblacion_sintetica_bogota.json', orient='records', indent=2)
    
    print(f"\nDataset guardado como 'poblacion_sintetica_bogota.csv' y 'poblacion_sintetica_bogota.json'")
