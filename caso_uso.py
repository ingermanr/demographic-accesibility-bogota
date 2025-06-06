import pandas as pd
import numpy as np
import geopandas as gpd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import plotly.express as px
import plotly.graph_objects as go
from geopy.distance import geodesic
import warnings
warnings.filterwarnings('ignore')

class CasosUsoEspecificos:
    def __init__(self, archivo_csv):
        """Inicializa con los datos sintéticos"""
        self.df = pd.read_csv(archivo_csv)
        print(f"Datos cargados: {len(self.df):,} registros")
    
    def segmentacion_demografica_avanzada(self):
        """Realiza segmentación demográfica usando clustering"""
        
        print("🎯 SEGMENTACIÓN DEMOGRÁFICA AVANZADA")
        print("="*50)
        
        # Preparar datos para clustering
        df_clustering = self.df.copy()
        
        # Codificar variables categóricas
        df_clustering['genero_num'] = df_clustering['genero'].map({'F': 1, 'M': 0})
        df_clustering['educacion_num'] = df_clustering['nivel_educativo'].map({
            'Primaria': 1, 'Secundaria': 2, 'Técnica': 3, 'Universitaria': 4
        })
        df_clustering['salud_num'] = df_clustering['afiliacion_salud'].map({
            'No_afiliado': 0, 'Subsidiado': 1, 'Contributivo': 2
        })
        
        # Seleccionar variables para clustering
        variables_clustering = ['edad', 'estrato', 'educacion_num', 'salud_num']
        X = df_clustering[variables_clustering]
        
        # Normalizar datos
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Aplicar K-means clustering
        n_clusters = 6
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        df_clustering['segmento'] = kmeans.fit_predict(X_scaled)
        
        # Analizar cada segmento
        print(f"\n📊 ANÁLISIS DE {n_clusters} SEGMENTOS IDENTIFICADOS:")
        print("-" * 60)
        
        segmentos_info = []
        for i in range(n_clusters):
            df_seg = df_clustering[df_clustering['segmento'] == i]
            
            info_segmento = {
                'Segmento': f"Segmento {i+1}",
                'Tamaño': len(df_seg),
                'Porcentaje': (len(df_seg) / len(df_clustering)) * 100,
                'Edad_Promedio': df_seg['edad'].mean(),
                'Estrato_Predominante': df_seg['estrato'].mode().iloc[0],
                'Educacion_Predominante': df_seg['nivel_educativo'].mode().iloc[0],
                'Salud_Predominante': df_seg['afiliacion_salud'].mode().iloc[0],
                'Genero_Predominante': 'Femenino' if df_seg['genero'].mode().iloc[0] == 'F' else 'Masculino',
                'Localidades_Top3': list(df_seg['localidad'].value_counts().head(3).index)
            }
            
            segmentos_info.append(info_segmento)
            
            print(f"\n🏷️ {info_segmento['Segmento']}:")
            print(f"   • Tamaño: {info_segmento['Tamaño']:,} personas ({info_segmento['Porcentaje']:.1f}%)")
            print(f"   • Edad promedio: {info_segmento['Edad_Promedio']:.1f} años")
            print(f"   • Estrato predominante: {info_segmento['Estrato_Predominante']}")
            print(f"   • Educación predominante: {info_segmento['Educacion_Predominante']}")
            print(f"   • Salud predominante: {info_segmento['Salud_Predominante']}")
            print(f"   • Género predominante: {info_segmento['Genero_Predominante']}")
            print(f"   • Top 3 localidades: {', '.join(info_segmento['Localidades_Top3'])}")
        
        # Visualizar segmentos geográficamente
        fig_segmentos = px.scatter_mapbox(
            df_clustering,
            lat='latitud',
            lon='longitud',
            color='segmento',
            hover_data=['localidad', 'edad', 'estrato', 'nivel_educativo'],
            title="Distribución Geográfica de Segmentos Demográficos",
            mapbox_style="open-street-map",
            zoom=9,
            height=600
        )
        
        fig_segmentos.show()
        
        return df_clustering, segmentos_info
    
    def analisis_accesibilidad_servicios(self):
        """Analiza accesibilidad a servicios por localidad"""
        
        print("\n🏥 ANÁLISIS DE ACCESIBILIDAD A SERVICIOS")
        print("="*50)
        
        # Definir centros de servicios importantes (coordenadas aproximadas)
        centros_servicios = {
            'Hospital_Kennedy': (4.6281, -74.1797),
            'Hospital_Suba': (4.7539, -74.0916),
            'Hospital_Engativa': (4.7045, -74.1247),
            'Universidad_Nacional': (4.6358, -74.0825),
            'Universidad_Javeriana': (4.6285, -74.0645),
            'Universidad_Andes': (4.6017, -74.0658),
            'Centro_Empleo_SENA': (4.6097, -74.0817),
            'Alcaldia_Mayor': (4.5981, -74.0759)
        }
        
        # Calcular distancias a servicios para cada persona
        df_accesibilidad = self.df.copy()
        
        for servicio, (lat_serv, lon_serv) in centros_servicios.items():
            distancias = []
            for _, row in df_accesibilidad.iterrows():
                punto_persona = (row['latitud'], row['longitud'])
                punto_servicio = (lat_serv, lon_serv)
                distancia = geodesic(punto_persona, punto_servicio).kilometers
                distancias.append(distancia)
            
            df_accesibilidad[f'dist_{servicio}'] = distancias
        
        # Calcular estadísticas de accesibilidad por localidad
        print("\n📍 DISTANCIA PROMEDIO A SERVICIOS CLAVE (KM):")
        print("-" * 60)
        
        accesibilidad_localidad = []
        for localidad in df_accesibilidad['localidad'].unique():
            df_loc = df_accesibilidad[df_accesibilidad['localidad'] == localidad]
            
            info_acc = {
                'Localidad': localidad,
                'Población': len(df_loc),
                'Hospital_más_cercano': min([
                    df_loc['dist_Hospital_Kennedy'].mean(),
                    df_loc['dist_Hospital_Suba'].mean(),
                    df_loc['dist_Hospital_Engativa'].mean()
                ]),
                'Universidad_más_cercana': min([
                    df_loc['dist_Universidad_Nacional'].mean(),
                    df_loc['dist_Universidad_Javeriana'].mean(),
                    df_loc['dist_Universidad_Andes'].mean()
                ]),
                'Centro_Empleo': df_loc['dist_Centro_Empleo_SENA'].mean(),
                'Alcaldía': df_loc['dist_Alcaldia_Mayor'].mean()
            }
            
            accesibilidad_localidad.append(info_acc)
            
            print(f"\n🏘️ {localidad}:")
            print(f"   • Hospital más cercano: {info_acc['Hospital_más_cercano']:.1f} km")
            print(f"   • Universidad más cercana: {info_acc['Universidad_más_cercana']:.1f} km")
            print(f"   • Centro de empleo: {info_acc['Centro_Empleo']:.1f} km")
            print(f"   • Alcaldía Mayor: {info_acc['Alcaldía']:.1f} km")
        
        df_accesibilidad_resumen = pd.DataFrame(accesibilidad_localidad)
        
        return df_accesibilidad, df_accesibilidad_resumen
    
    def identificar_zonas_vulnerabilidad(self):
        """Identifica zonas de vulnerabilidad social"""
        
        print("\n⚠️ IDENTIFICACIÓN DE ZONAS DE VULNERABILIDAD")
        print("="*50)
        
        # Crear índice de vulnerabilidad
        df_vulnerabilidad = self.df.copy()
        
        # Asignar puntajes de vulnerabilidad
        df_vulnerabilidad['puntaje_estrato'] = df_vulnerabilidad['estrato'].map({
            1: 5, 2: 4, 3: 3, 4: 2, 5: 1, 6: 0
        })
        
        df_vulnerabilidad['puntaje_educacion'] = df_vulnerabilidad['nivel_educativo'].map({
            'Primaria': 4, 'Secundaria': 3, 'Técnica': 2, 'Universitaria': 1
        })
        
        df_vulnerabilidad['puntaje_salud'] = df_vulnerabilidad['afiliacion_salud'].map({
            'No_afiliado': 5, 'Subsidiado': 3, 'Contributivo': 1
        })
        
        # Puntaje por edad (vulnerabilidad en extremos)
        df_vulnerabilidad['puntaje_edad'] = df_vulnerabilidad['edad'].apply(
            lambda x: 3 if x < 18 or x > 65 else 1
        )
        
        # Calcular índice de vulnerabilidad total
        df_vulnerabilidad['indice_vulnerabilidad'] = (
            df_vulnerabilidad['puntaje_estrato'] * 0.35 +
            df_vulnerabilidad['puntaje_educacion'] * 0.25 +
            df_vulnerabilidad['puntaje_salud'] * 0.25 +
            df_vulnerabilidad['puntaje_edad'] * 0.15
        )
        
        # Clasificar niveles de vulnerabilidad
        df_vulnerabilidad['nivel_vulnerabilidad'] = pd.cut(
            df_vulnerabilidad['indice_vulnerabilidad'],
            bins=[0, 2, 3, 4, 5],
            labels=['Baja', 'Media', 'Alta', 'Muy Alta']
        )
        
        # Análisis por localidad
        vulnerabilidad_localidad = df_vulnerabilidad.groupby('localidad').agg({
            'indice_vulnerabilidad': 'mean',
            'nivel_vulnerabilidad': lambda x: x.value_counts().index[0],  # Moda
            'id': 'count'
        }).rename(columns={'id': 'poblacion'}).round(2)
        
        vulnerabilidad_localidad = vulnerabilidad_localidad.sort_values(
            'indice_vulnerabilidad', ascending=False
        )
        
        print("\n📊 RANKING DE VULNERABILIDAD POR LOCALIDAD:")
        print("-" * 60)
        print(f"{'Posición':<3} {'Localidad':<20} {'Índice':<8} {'Nivel':<12} {'Población':<10}")
        print("-" * 60)
        
        for i, (localidad, datos) in enumerate(vulnerabilidad_localidad.iterrows(), 1):
            print(f"{i:<3} {localidad:<20} {datos['indice_vulnerabilidad']:<8} {datos['nivel_vulnerabilidad']:<12} {datos['poblacion']:<10,}")
        
        # Identificar hotspots de vulnerabilidad
        hotspots = df_vulnerabilidad[df_vulnerabilidad['indice_vulnerabilidad'] >= 4.0]
        
        print(f"\n🔥 HOTSPOTS DE ALTA VULNERABILIDAD:")
        print(f"   • Total de personas en alta vulnerabilidad: {len(hotspots):,}")
        print(f"   • Porcentaje de la población: {(len(hotspots)/len(df_vulnerabilidad))*100:.1f}%")
        
        hotspots_localidad = hotspots['localidad'].value_counts().head(10)
        print(f"\n📍 Localidades con más personas en alta vulnerabilidad:")
        for localidad, count in hotspots_localidad.items():
            porcentaje = (count / len(hotspots)) * 100
            print(f"   • {localidad}: {count:,} personas ({porcentaje:.1f}%)")
        
        # Mapa de vulnerabilidad
        fig_vulnerabilidad = px.scatter_mapbox(
            df_vulnerabilidad,
            lat='latitud',
            lon='longitud',
            color='indice_vulnerabilidad',
            hover_data=['localidad', 'nivel_vulnerabilidad', 'estrato'],
            title="Mapa de Vulnerabilidad Social - Bogotá",
            color_continuous_scale='Reds',
            mapbox_style="open-street-map",
            zoom=9,
            height=600
        )
        
        fig_vulnerabilidad.show()
        
        return df_vulnerabilidad, vulnerabilidad_localidad
    
    def simulacion_politicas_publicas(self):
        """Simula el impacto de diferentes políticas públicas"""
        
        print("\n🏛️ SIMULACIÓN DE POLÍTICAS PÚBLICAS")
        print("="*50)
        
        df_politicas = self.df.copy()
        
        # Escenario 1: Programa de educación superior gratuita
        print("\n📚 ESCENARIO 1: Educación Superior Gratuita")
        print("-" * 40)
        
        # Identificar beneficiarios potenciales
        beneficiarios_educacion = df_politicas[
            (df_politicas['estrato'].isin([1, 2, 3])) & 
            (df_politicas['edad'].between(17, 25)) &
            (df_politicas['nivel_educativo'].isin(['Secundaria', 'Técnica']))
        ]
        
        print(f"   • Beneficiarios potenciales: {len(beneficiarios_educacion):,}")
        print(f"   • Porcentaje de la población objetivo: {(len(beneficiarios_educacion)/len(df_politicas))*100:.1f}%")
        
        # Distribución por localidad
        beneficiarios_por_localidad = beneficiarios_educacion['localidad'].value_counts().head(10)
        print(f"\n   Top 10 localidades beneficiadas:")
        for localidad, count in beneficiarios_por_localidad.items():
            print(f"     • {localidad}: {count:,} beneficiarios")
        
        # Escenario 2: Ampliación cobertura salud contributiva
        print("\n🏥 ESCENARIO 2: Ampliación Cobertura Salud")
        print("-" * 40)
        
        # Identificar población objetivo
        objetivo_salud = df_politicas[
            (df_politicas['afiliacion_salud'] == 'Subsidiado') &
            (df_politicas['estrato'].isin([2, 3])) &
            (df_politicas['edad'].between(18, 60))
        ]
        
        print(f"   • Población objetivo: {len(objetivo_salud):,}")
        print(f"   • Costo estimado mensual: ${len(objetivo_salud) * 150000:,} COP")
        
        # Escenario 3: Programa de vivienda social
        print("\n🏠 ESCENARIO 3: Programa de Vivienda Social")
        print("-" * 40)
        
        # Identificar beneficiarios de vivienda
        beneficiarios_vivienda = df_politicas[
            (df_politicas['estrato'].isin([1, 2])) &
            (df_politicas['edad'].between(25, 50))
        ]
        
        # Estimar necesidad por localidad
        necesidad_vivienda = beneficiarios_vivienda.groupby('localidad').size().sort_values(ascending=False)
        
        print(f"   • Familias beneficiarias estimadas: {len(beneficiarios_vivienda):,}")
        print(f"\n   Priorización por localidad:")
        for localidad, familias in necesidad_vivienda.head(5).items():
            print(f"     • {localidad}: {familias:,} familias")
        
        # Escenario 4: Programa de empleo juvenil
        print("\n💼 ESCENARIO 4: Programa de Empleo Juvenil")
        print("-" * 40)
        
        jovenes_desempleo = df_politicas[
            (df_politicas['edad'].between(16, 28)) &
            (df_politicas['estrato'].isin([1, 2, 3])) &
            (df_politicas['nivel_educativo'].isin(['Secundaria', 'Técnica']))
        ]
        
        print(f"   • Jóvenes objetivo: {len(jovenes_desempleo):,}")
        
        # Análisis por género
        distribucion_genero = jovenes_desempleo['genero'].value_counts()
        print(f"   • Distribución por género:")
        for genero, count in distribucion_genero.items():
            genero_nombre = "Mujeres" if genero == 'F' else "Hombres"
            print(f"     • {genero_nombre}: {count:,}")
        
        return {
            'beneficiarios_educacion': beneficiarios_educacion,
            'objetivo_salud': objetivo_salud,
            'beneficiarios_vivienda': beneficiarios_vivienda,
            'jovenes_desempleo': jovenes_desempleo
        }
    
    def analisis_movilidad_urbana(self):
        """Analiza patrones de movilidad urbana simulados"""
        
        print("\n🚌 ANÁLISIS DE MOVILIDAD URBANA")
        print("="*50)
        
        df_movilidad = self.df.copy()
        
        # Simular patrones de movilidad basados en características demográficas
        np.random.seed(42)
        
        # Probabilidades de usar diferentes medios de transporte
        def asignar_transporte_principal(row):
            if row['estrato'] >= 4:
                return np.random.choice(['Automóvil', 'TransMilenio', 'Taxi/Uber'], 
                                      p=[0.6, 0.3, 0.1])
            elif row['estrato'] == 3:
                return np.random.choice(['TransMilenio', 'Bus', 'Automóvil'], 
                                      p=[0.5, 0.3, 0.2])
            else:
                return np.random.choice(['Bus', 'TransMilenio', 'Caminando'], 
                                      p=[0.5, 0.3, 0.2])
        
        df_movilidad['transporte_principal'] = df_movilidad.apply(asignar_transporte_principal, axis=1)
        
        # Simular tiempo de desplazamiento (minutos)
        def calcular_tiempo_desplazamiento(row):
            if row['transporte_principal'] == 'Automóvil':
                return np.random.normal(35, 15)
            elif row['transporte_principal'] == 'TransMilenio':
                return np.random.normal(50, 20)
            elif row['transporte_principal'] == 'Bus':
                return np.random.normal(65, 25)
            elif row['transporte_principal'] == 'Taxi/Uber':
                return np.random.normal(30, 12)
            else:  # Caminando
                return np.random.normal(25, 10)
        
        df_movilidad['tiempo_desplazamiento'] = df_movilidad.apply(
            calcular_tiempo_desplazamiento, axis=1
        ).clip(lower=5, upper=120)  # Entre 5 y 120 minutos
        
        # Análisis por localidad
        print("\n🚇 PATRONES DE MOVILIDAD POR LOCALIDAD:")
        print("-" * 50)
        
        movilidad_localidad = df_movilidad.groupby('localidad').agg({
            'tiempo_desplazamiento': 'mean',
            'transporte_principal': lambda x: x.mode().iloc[0]
        }).round(1)
        
        movilidad_localidad = movilidad_localidad.sort_values('tiempo_desplazamiento', ascending=False)
        
        print(f"{'Localidad':<20} {'Tiempo Prom (min)':<18} {'Transporte Principal':<20}")
        print("-" * 60)
        for localidad, datos in movilidad_localidad.head(10).iterrows():
            print(f"{localidad:<20} {datos['tiempo_desplazamiento']:<18} {datos['transporte_principal']:<20}")
        
        # Análisis de demanda de TransMilenio
        usuarios_transmilenio = df_movilidad[df_movilidad['transporte_principal'] == 'TransMilenio']
        
        print(f"\n🚌 ANÁLISIS TRANSMILENIO:")
        print(f"   • Usuarios estimados: {len(usuarios_transmilenio):,}")
        print(f"   • Porcentaje de la población: {(len(usuarios_transmilenio)/len(df_movilidad))*100:.1f}%")
        
        # Demanda por localidad
        demanda_tm = usuarios_transmilenio['localidad'].value_counts().head(10)
        print(f"\n   Localidades con mayor demanda:")
        for localidad, usuarios in demanda_tm.items():
            print(f"     • {localidad}: {usuarios:,} usuarios")
        
        return df_movilidad, movilidad_localidad
    
    def optimizacion_servicios_publicos(self):
        """Optimiza la ubicación de servicios públicos"""
        
        print("\n🎯 OPTIMIZACIÓN DE SERVICIOS PÚBLICOS")
        print("="*50)
        
        # Análisis de demanda por servicios
        df_servicios = self.df.copy()
        
        # 1. Centros de salud necesarios
        print("\n🏥 ANÁLISIS DE CENTROS DE SALUD:")
        print("-" * 40)
        
        # Población que requiere atención primaria (subsidiado + no afiliado)
        poblacion_atencion_publica = df_servicios[
            df_servicios['afiliacion_salud'].isin(['Subsidiado', 'No_afiliado'])
        ]
        
        print(f"   • Población objetivo: {len(poblacion_atencion_publica):,}")
        
        # Análisis por grupos vulnerables
        adultos_mayores = poblacion_atencion_publica[poblacion_atencion_publica['edad'] >= 60]
        menores = poblacion_atencion_publica[poblacion_atencion_publica['edad'] < 18]
        
        print(f"   • Adultos mayores: {len(adultos_mayores):,}")
        print(f"   • Menores de edad: {len(menores):,}")
        
        # Demanda por localidad
        demanda_salud = poblacion_atencion_publica.groupby('localidad').agg({
            'id': 'count',
            'edad': lambda x: (x >= 60).sum(),  # Adultos mayores
            'estrato': lambda x: (x <= 2).sum()  # Estratos más vulnerables
        }).rename(columns={'id': 'total', 'edad': 'adultos_mayores', 'estrato': 'vulnerables'})
        
        demanda_salud = demanda_salud.sort_values('total', ascending=False)
        
        print(f"\n   Priorización para nuevos centros de salud:")
        print(f"   {'Localidad':<20} {'Total':<8} {'A.Mayores':<12} {'Vulnerables':<12}")
        print("-" * 55)
        for localidad, datos in demanda_salud.head(8).iterrows():
            print(f"   {localidad:<20} {datos['total']:<8} {datos['adultos_mayores']:<12} {datos['vulnerables']:<12}")
        
        # 2. Bibliotecas públicas
        print("\n📚 ANÁLISIS DE BIBLIOTECAS PÚBLICAS:")
        print("-" * 40)
        
        # Población objetivo: menores de 25 años + adultos con educación básica
        poblacion_bibliotecas = df_servicios[
            (df_servicios['edad'] <= 25) |
            (df_servicios['nivel_educativo'].isin(['Primaria', 'Secundaria']))
        ]
        
        demanda_bibliotecas = poblacion_bibliotecas.groupby('localidad').size().sort_values(ascending=False)
        
        print(f"   • Población objetivo: {len(poblacion_bibliotecas):,}")
        print(f"\n   Localidades prioritarias:")
        for localidad, demanda in demanda_bibliotecas.head(8).items():
            print(f"     • {localidad}: {demanda:,} personas")
        
        # 3. Centros de empleo
        print("\n💼 ANÁLISIS DE CENTROS DE EMPLEO:")
        print("-" * 40)
        
        # Población en edad laboral, estratos bajos, educación técnica/secundaria
        poblacion_empleo = df_servicios[
            (df_servicios['edad'].between(18, 55)) &
            (df_servicios['estrato'].isin([1, 2, 3])) &
            (df_servicios['nivel_educativo'].isin(['Secundaria', 'Técnica']))
        ]
        
        demanda_empleo = poblacion_empleo.groupby('localidad').size().sort_values(ascending=False)
        
        print(f"   • Población objetivo: {len(poblacion_empleo):,}")
        print(f"\n   Localidades prioritarias:")
        for localidad, demanda in demanda_empleo.head(8).items():
            print(f"     • {localidad}: {demanda:,} personas")
        
        return {
            'demanda_salud': demanda_salud,
            'demanda_bibliotecas': demanda_bibliotecas,
            'demanda_empleo': demanda_empleo
        }
    
    def generar_dashboard_ejecutivo(self):
        """Genera un dashboard ejecutivo con métricas clave"""
        
        print("\n📊 DASHBOARD EJECUTIVO - MÉTRICAS CLAVE")
        print("="*60)
        
        # Métricas generales
        total_poblacion = len(self.df)
        edad_promedio = self.df['edad'].mean()
        
        # Métricas socioeconómicas
        estrato_promedio = self.df['estrato'].mean()
        poblacion_vulnerable = len(self.df[self.df['estrato'].isin([1, 2])])
        porcentaje_vulnerable = (poblacion_vulnerable / total_poblacion) * 100
        
        # Métricas educativas
        poblacion_universitaria = len(self.df[self.df['nivel_educativo'] == 'Universitaria'])
        porcentaje_universitaria = (poblacion_universitaria / total_poblacion) * 100
        
        poblacion_primaria = len(self.df[self.df['nivel_educativo'] == 'Primaria'])
        porcentaje_primaria = (poblacion_primaria / total_poblacion) * 100
        
        # Métricas de salud
        poblacion_contributivo = len(self.df[self.df['afiliacion_salud'] == 'Contributivo'])
        porcentaje_contributivo = (poblacion_contributivo / total_poblacion) * 100
        
        poblacion_sin_salud = len(self.df[self.df['afiliacion_salud'] == 'No_afiliado'])
        porcentaje_sin_salud = (poblacion_sin_salud / total_poblacion) * 100
        
        # Métricas demográficas
        poblacion_joven = len(self.df[self.df['edad'] < 30])
        porcentaje_joven = (poblacion_joven / total_poblacion) * 100
        
        poblacion_adulto_mayor = len(self.df[self.df['edad'] >= 60])
        porcentaje_adulto_mayor = (poblacion_adulto_mayor / total_poblacion) * 100
        
        # Localidades más pobladas
        top_localidades = self.df['localidad'].value_counts().head(5)
        
        print(f"\n🎯 INDICADORES CLAVE DE GESTIÓN:")
        print("-" * 50)
        print(f"   📈 Población Total: {total_poblacion:,} habitantes")
        print(f"   📊 Edad Promedio: {edad_promedio:.1f} años")
        print(f"   💰 Estrato Promedio: {estrato_promedio:.1f}")
        print(f"   ⚠️  Población Vulnerable (E1-E2): {poblacion_vulnerable:,} ({porcentaje_vulnerable:.1f}%)")
        print(f"   🎓 Educación Universitaria: {poblacion_universitaria:,} ({porcentaje_universitaria:.1f}%)")
        print(f"   📖 Solo Educación Primaria: {poblacion_primaria:,} ({porcentaje_primaria:.1f}%)")
        print(f"   🏥 Régimen Contributivo: {poblacion_contributivo:,} ({porcentaje_contributivo:.1f}%)")
        print(f"   ❌ Sin Afiliación a Salud: {poblacion_sin_salud:,} ({porcentaje_sin_salud:.1f}%)")
        print(f"   👦 Población Joven (<30): {poblacion_joven:,} ({porcentaje_joven:.1f}%)")
        print(f"   👴 Adultos Mayores (60+): {poblacion_adulto_mayor:,} ({porcentaje_adulto_mayor:.1f}%)")
        
        print(f"\n🏘️ TOP 5 LOCALIDADES MÁS POBLADAS:")
        print("-" * 40)
        for i, (localidad, poblacion) in enumerate(top_localidades.items(), 1):
            porcentaje = (poblacion / total_poblacion) * 100
            print(f"   {i}. {localidad}: {poblacion:,} ({porcentaje:.1f}%)")
        
        # Alertas y recomendaciones
        print(f"\n🚨 ALERTAS Y RECOMENDACIONES:")
        print("-" * 40)
        
        if porcentaje_vulnerable > 30:
            print(f"   ⚠️  ALTA VULNERABILIDAD: {porcentaje_vulnerable:.1f}% en estratos 1-2")
        
        if porcentaje_sin_salud > 8:
            print(f"   🏥 COBERTURA DE SALUD: {porcentaje_sin_salud:.1f}% sin afiliación")
        
        if porcentaje_primaria > 35:
            print(f"   📚 REZAGO EDUCATIVO: {porcentaje_primaria:.1f}% solo primaria")
        
        if porcentaje_adulto_mayor > 15:
            print(f"   👴 ENVEJECIMIENTO: {porcentaje_adulto_mayor:.1f}% adultos mayores")
        
        # Crear resumen ejecutivo
        resumen_ejecutivo = {
            'fecha_reporte': pd.Timestamp.now().strftime('%Y-%m-%d'),
            'poblacion_total': total_poblacion,
            'edad_promedio': round(edad_promedio, 1),
            'estrato_promedio': round(estrato_promedio, 1),
            'porcentaje_vulnerable': round(porcentaje_vulnerable, 1),
            'porcentaje_universitaria': round(porcentaje_universitaria, 1),
            'porcentaje_contributivo': round(porcentaje_contributivo, 1),
            'porcentaje_sin_salud': round(porcentaje_sin_salud, 1),
            'top_localidades': dict(top_localidades.head(3))
        }
        
        return resumen_ejecutivo

# Función principal para ejecutar todos los casos de uso
def ejecutar_casos_uso_completos(archivo_csv='./resultados_analisis_bogota/poblacion_sintetica_bogota.csv'):
    """Ejecuta todos los casos de uso específicos"""
    
    print("🚀 INICIANDO ANÁLISIS DE CASOS DE USO ESPECÍFICOS")
    print("="*70)
    
    casos_uso = CasosUsoEspecificos(archivo_csv)
    
    # Ejecutar todos los análisis
    print("\n1️⃣ Segmentación demográfica avanzada...")
    segmentos = casos_uso.segmentacion_demografica_avanzada()
    
    print("\n2️⃣ Análisis de accesibilidad a servicios...")
    accesibilidad = casos_uso.analisis_accesibilidad_servicios()
    
    print("\n3️⃣ Identificación de zonas de vulnerabilidad...")
    vulnerabilidad = casos_uso.identificar_zonas_vulnerabilidad()
    
    print("\n4️⃣ Simulación de políticas públicas...")
    politicas = casos_uso.simulacion_politicas_publicas()
    
    print("\n5️⃣ Análisis de movilidad urbana...")
    movilidad = casos_uso.analisis_movilidad_urbana()
    
    print("\n6️⃣ Optimización de servicios públicos...")
    servicios = casos_uso.optimizacion_servicios_publicos()
    
    print("\n7️⃣ Dashboard ejecutivo...")
    dashboard = casos_uso.generar_dashboard_ejecutivo()
    
    print(f"\n✅ ANÁLISIS COMPLETADO EXITOSAMENTE!")
    print(f"📊 Se han generado análisis para {len(casos_uso.df):,} registros sintéticos")
    
    return {
        'segmentos': segmentos,
        'accesibilidad': accesibilidad,
        'vulnerabilidad': vulnerabilidad,
        'politicas': politicas,
        'movilidad': movilidad,
        'servicios': servicios,
        'dashboard': dashboard
    }

# Ejemplo de uso
if __name__ == "__main__":
    resultados = ejecutar_casos_uso_completos('./resultados_analisis_bogota/poblacion_sintetica_bogota.csv')