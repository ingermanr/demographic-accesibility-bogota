#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sistema de Análisis de Accesibilidad a Centros de Salud
Bogotá D.C. - Análisis basado en datos sintéticos

Este módulo analiza la accesibilidad geográfica de la población
a los centros de salud en Bogotá.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import radians, cos, sin, asin, sqrt
from datetime import datetime
import os
import warnings
warnings.filterwarnings('ignore')

class SistemaAccesibilidadSalud:
    """
    Sistema completo para analizar la accesibilidad geográfica
    a centros de salud en Bogotá
    """
    
    def __init__(self, archivo_poblacion, archivo_centros):
        """Inicializa el sistema con archivos de datos"""
        self.archivo_poblacion = archivo_poblacion
        self.archivo_centros = archivo_centros
        self.df_poblacion = None
        self.df_centros = None
        self.df_accesibilidad = None
        
        # Configuración de visualización
        plt.style.use('default')
        sns.set_palette("husl")
        
    def haversine(self, lon1, lat1, lon2, lat2):
        """Calcula la distancia haversine entre dos puntos en la Tierra"""
        # Convertir grados decimales a radianes
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        
        # Fórmula haversine
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        r = 6371  # Radio de la Tierra en kilómetros
        
        return c * r
    
    def cargar_poblacion(self):
        """Carga y prepara los datos de población"""
        print("\n📊 CARGANDO DATOS DE POBLACIÓN...")
        
        try:
            self.df_poblacion = pd.read_csv(self.archivo_poblacion)
            print(f"✅ Población cargada: {len(self.df_poblacion):,} registros")
            
            # Verificar columnas necesarias
            columnas_requeridas = ['latitud', 'longitud', 'localidad']
            faltantes = [col for col in columnas_requeridas if col not in self.df_poblacion.columns]
            
            if faltantes:
                print(f"❌ Faltan columnas: {faltantes}")
                return False
            
            # Filtrar registros con coordenadas válidas
            inicial = len(self.df_poblacion)
            self.df_poblacion = self.df_poblacion.dropna(subset=['latitud', 'longitud'])
            
            if len(self.df_poblacion) < inicial:
                print(f"⚠️  Removidos {inicial - len(self.df_poblacion)} registros sin coordenadas")
            
            print(f"✅ Datos de población listos: {len(self.df_poblacion):,} registros")
            return True
            
        except Exception as e:
            print(f"❌ Error cargando población: {str(e)}")
            return False
    
    def procesar_centros_salud(self):
        """Procesa y geocodifica los centros de salud"""
        print("\n🏥 PROCESANDO CENTROS DE SALUD...")
        
        try:
            # Intentar diferentes separadores y encodings
            try:
                self.df_centros = pd.read_csv(self.archivo_centros, sep=';', encoding='utf-8')
            except:
                try:
                    self.df_centros = pd.read_csv(self.archivo_centros, sep=';', encoding='latin-1')
                except:
                    self.df_centros = pd.read_csv(self.archivo_centros)
            print(f"✅ Centros cargados: {len(self.df_centros)} registros")
            
            # Verificar si ya tienen coordenadas
            if 'latitud' in self.df_centros.columns and 'longitud' in self.df_centros.columns:
                inicial = len(self.df_centros)
                self.df_centros = self.df_centros.dropna(subset=['latitud', 'longitud'])
                
                if len(self.df_centros) < inicial:
                    print(f"⚠️  Removidos {inicial - len(self.df_centros)} centros sin coordenadas")
                
                print(f"✅ Centros con coordenadas: {len(self.df_centros)}")
                return True
            
            # Si no tienen coordenadas, usar coordenadas aproximadas por localidad
            print("📍 Generando coordenadas aproximadas por localidad...")
            
            # Coordenadas centrales aproximadas de localidades de Bogotá
            coordenadas_localidades = {
                'USAQUEN': (4.7174, -74.0303),
                'CHAPINERO': (4.6492, -74.0628),
                'SANTA FE': (4.6097, -74.0817),
                'SAN CRISTOBAL': (4.5697, -74.0792),
                'USME': (4.4797, -74.1264),
                'TUNJUELITO': (4.5797, -74.1264),
                'BOSA': (4.6297, -74.1897),
                'KENNEDY': (4.6297, -74.1564),
                'FONTIBON': (4.6797, -74.1431),
                'ENGATIVA': (4.7097, -74.1231),
                'SUBA': (4.7597, -74.0831),
                'BARRIOS UNIDOS': (4.6797, -74.0831),
                'TEUSAQUILLO': (4.6297, -74.0831),
                'LOS MARTIRES': (4.6097, -74.0931),
                'ANTONIO NARIÑO': (4.5897, -74.0931),
                'PUENTE ARANDA': (4.6197, -74.1131),
                'LA CANDELARIA': (4.5975, -74.0736),
                'RAFAEL URIBE URIBE': (4.5597, -74.1131),
                'CIUDAD BOLIVAR': (4.4797, -74.1564),
                'SUMAPAZ': (4.2097, -74.3564)
            }
            
            def asignar_coordenadas(row):
                # Intentar diferentes nombres de columna para la localidad
                localidad_col = None
                for col_name in ['localidad', 'Localidad', 'LOCALIDAD']:
                    if col_name in row and pd.notna(row[col_name]):
                        localidad_col = col_name
                        break
                
                if localidad_col:
                    localidad = str(row[localidad_col]).upper().strip()
                else:
                    localidad = ''
                
                for loc, coords in coordenadas_localidades.items():
                    if localidad in loc or loc in localidad:
                        lat_base, lon_base = coords
                        lat_var = np.random.uniform(-0.01, 0.01)
                        lon_var = np.random.uniform(-0.01, 0.01)
                        return lat_base + lat_var, lon_base + lon_var
                
                # Si no encuentra coincidencia, usar coordenadas de Bogotá centro
                lat_base, lon_base = (4.6097, -74.0817)
                lat_var = np.random.uniform(-0.02, 0.02)
                lon_var = np.random.uniform(-0.02, 0.02)
                return lat_base + lat_var, lon_base + lon_var
            
            coordenadas = self.df_centros.apply(asignar_coordenadas, axis=1)
            self.df_centros['latitud'] = [coord[0] for coord in coordenadas]
            self.df_centros['longitud'] = [coord[1] for coord in coordenadas]
            
            print(f"✅ Coordenadas asignadas a {len(self.df_centros)} centros")
            return True
            
        except Exception as e:
            print(f"❌ Error procesando centros: {str(e)}")
            return False
    
    def analizar_accesibilidad(self, muestra_poblacion=9000):
        """Analiza la accesibilidad calculando distancias a centros más cercanos"""
        print(f"\n📐 CALCULANDO ACCESIBILIDAD...")
        print(f"   • Analizando muestra de {muestra_poblacion:,} personas")
        print(f"   • Centros disponibles: {len(self.df_centros)}")
        
        try:
            if len(self.df_poblacion) > muestra_poblacion:
                muestra = self.df_poblacion.sample(n=muestra_poblacion, random_state=42)
            else:
                muestra = self.df_poblacion.copy()
            
            print(f"   • Procesando {len(muestra):,} registros...")
            
            resultados = []
            contador = 0
            
            for idx, persona in muestra.iterrows():
                contador += 1
                if contador % 500 == 0:
                    print(f"   • Procesado: {contador:,}/{len(muestra):,} ({(contador/len(muestra)*100):.1f}%)")
                
                lat_persona = persona['latitud']
                lon_persona = persona['longitud']
                
                distancias = []
                for _, centro in self.df_centros.iterrows():
                    distancia = self.haversine(
                        lon_persona, lat_persona,
                        centro['longitud'], centro['latitud']
                    )
                    distancias.append({
                        'centro_idx': centro.name,
                        'distancia': distancia,
                        'centro_nombre': centro.get('centro_salud', centro.get('nombre', f'Centro_{centro.name}')),
                        'centro_localidad': centro.get('localidad', centro.get('Localidad', centro.get('LOCALIDAD', 'No_especificada')))
                    })
                
                centro_cercano = min(distancias, key=lambda x: x['distancia'])
                
                resultado = {
                    'persona_idx': idx,
                    'persona_localidad': persona['localidad'],
                    'persona_latitud': lat_persona,
                    'persona_longitud': lon_persona,
                    'centro_cercano_idx': centro_cercano['centro_idx'],
                    'centro_cercano_nombre': centro_cercano['centro_nombre'],
                    'centro_cercano_localidad': centro_cercano['centro_localidad'],
                    'distancia_km': centro_cercano['distancia'],
                    'misma_localidad': persona['localidad'] == centro_cercano['centro_localidad']
                }
                
                # Agregar información adicional si está disponible
                columnas_adicionales = {
                    'persona_edad': 'edad',
                    'persona_genero': 'genero', 
                    'persona_nivel_educativo': 'nivel_educativo',
                    'persona_afiliacion_salud': 'afiliacion_salud'
                }
                
                for resultado_col, archivo_col in columnas_adicionales.items():
                    if archivo_col in persona:
                        resultado[resultado_col] = persona[archivo_col]
                
                resultados.append(resultado)
            
            self.df_accesibilidad = pd.DataFrame(resultados)
            print(f"✅ Análisis completado: {len(self.df_accesibilidad):,} registros procesados")
            return True
            
        except Exception as e:
            print(f"❌ Error en análisis de accesibilidad: {str(e)}")
            return False
    
    def generar_metricas(self):
        """Genera métricas de accesibilidad"""
        print("\n📊 GENERANDO MÉTRICAS...")
        
        try:
            distancia_promedio = self.df_accesibilidad['distancia_km'].mean()
            distancia_mediana = self.df_accesibilidad['distancia_km'].median()
            distancia_max = self.df_accesibilidad['distancia_km'].max()
            distancia_min = self.df_accesibilidad['distancia_km'].min()
            
            pct_misma_localidad = (self.df_accesibilidad['misma_localidad'].sum() / 
                                 len(self.df_accesibilidad)) * 100
            
            rangos = {
                '0-2 km': len(self.df_accesibilidad[self.df_accesibilidad['distancia_km'] <= 2]),
                '2-5 km': len(self.df_accesibilidad[
                    (self.df_accesibilidad['distancia_km'] > 2) & 
                    (self.df_accesibilidad['distancia_km'] <= 5)
                ]),
                '5-10 km': len(self.df_accesibilidad[
                    (self.df_accesibilidad['distancia_km'] > 5) & 
                    (self.df_accesibilidad['distancia_km'] <= 10)
                ]),
                '>10 km': len(self.df_accesibilidad[self.df_accesibilidad['distancia_km'] > 10])
            }
            
            metricas = {
                'distancia_promedio': distancia_promedio,
                'distancia_mediana': distancia_mediana,
                'distancia_max': distancia_max,
                'distancia_min': distancia_min,
                'pct_misma_localidad': pct_misma_localidad,
                'rangos_distancia': rangos
            }
            
            print(f"✅ Métricas calculadas:")
            print(f"   • Distancia promedio: {distancia_promedio:.2f} km")
            print(f"   • Distancia mediana: {distancia_mediana:.2f} km")
            print(f"   • Acceso en misma localidad: {pct_misma_localidad:.1f}%")
            
            return metricas
            
        except Exception as e:
            print(f"❌ Error generando métricas: {str(e)}")
            return {}
    
    def analizar_por_localidad(self):
        """Analiza accesibilidad por localidad"""
        print("\n🏘️ ANALIZANDO POR LOCALIDAD...")
        
        try:
            acceso_localidad = self.df_accesibilidad.groupby('persona_localidad').agg({
                'distancia_km': ['mean', 'median', 'count'],
                'misma_localidad': 'sum'
            }).round(2)
            
            acceso_localidad.columns = ['dist_promedio', 'dist_mediana', 'poblacion', 'acceso_local']
            
            acceso_localidad['pct_acceso_local'] = (
                acceso_localidad['acceso_local'] / acceso_localidad['poblacion'] * 100
            ).round(1)
            
            acceso_localidad = acceso_localidad.sort_values('dist_promedio', ascending=False)
            
            print(f"✅ Análisis por localidad completado: {len(acceso_localidad)} localidades")
            
            return acceso_localidad
            
        except Exception as e:
            print(f"❌ Error en análisis por localidad: {str(e)}")
            return pd.DataFrame()
    
    def crear_visualizaciones(self):
        """Crea visualizaciones del análisis"""
        print("\n🎨 CREANDO VISUALIZACIONES...")
        
        try:
            fig, axes = plt.subplots(2, 2, figsize=(16, 12))
            fig.suptitle('Análisis de Accesibilidad a Centros de Salud - Bogotá D.C.', 
                        fontsize=16, fontweight='bold')
            
            # 1. Distribución de distancias
            ax1 = axes[0, 0]
            self.df_accesibilidad['distancia_km'].hist(bins=30, ax=ax1, alpha=0.7, color='skyblue')
            ax1.set_title('Distribución de Distancias al Centro Más Cercano')
            ax1.set_xlabel('Distancia (km)')
            ax1.set_ylabel('Frecuencia')
            ax1.axvline(self.df_accesibilidad['distancia_km'].mean(), color='red', 
                       linestyle='--', label='Promedio')
            ax1.legend()
            
            # 2. Accesibilidad por localidad
            ax2 = axes[0, 1]
            acceso_localidad = self.analizar_por_localidad()
            if not acceso_localidad.empty:
                top_10 = acceso_localidad.head(10)
                bars = ax2.barh(range(len(top_10)), top_10['dist_promedio'])
                ax2.set_yticks(range(len(top_10)))
                ax2.set_yticklabels(top_10.index, fontsize=8)
                ax2.set_title('Top 10 Localidades - Mayor Distancia Promedio')
                ax2.set_xlabel('Distancia Promedio (km)')
                
                for i, bar in enumerate(bars):
                    if top_10.iloc[i]['dist_promedio'] > 5:
                        bar.set_color('red')
                    elif top_10.iloc[i]['dist_promedio'] > 3:
                        bar.set_color('orange')
                    else:
                        bar.set_color('green')
            
            # 3. Rangos de distancia
            ax3 = axes[1, 0]
            metricas = self.generar_metricas()
            if metricas:
                rangos = list(metricas['rangos_distancia'].keys())
                valores = list(metricas['rangos_distancia'].values())
                
                wedges, texts, autotexts = ax3.pie(valores, labels=rangos, autopct='%1.1f%%', 
                                                  startangle=90)
                ax3.set_title('Distribución por Rangos de Distancia')
            
            # 4. Centros más demandados
            ax4 = axes[1, 1]
            demanda_centro = self.df_accesibilidad['centro_cercano_nombre'].value_counts().head(10)
            if not demanda_centro.empty:
                bars = ax4.bar(range(len(demanda_centro)), demanda_centro.values)
                ax4.set_xticks(range(len(demanda_centro)))
                ax4.set_xticklabels([name[:20] + '...' if len(name) > 20 else name 
                                    for name in demanda_centro.index], 
                                   rotation=45, ha='right', fontsize=8)
                ax4.set_title('Top 10 Centros Más Demandados')
                ax4.set_ylabel('Personas Asignadas')
                
                max_demanda = demanda_centro.max()
                for i, bar in enumerate(bars):
                    if demanda_centro.iloc[i] > max_demanda * 0.7:
                        bar.set_color('red')
                    elif demanda_centro.iloc[i] > max_demanda * 0.4:
                        bar.set_color('orange')
                    else:
                        bar.set_color('green')
            
            plt.tight_layout()
            
            nombre_archivo = 'analisis_accesibilidad_centros_salud.png'
            plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
            print(f"✅ Visualizaciones guardadas: {nombre_archivo}")
            
            plt.show()
            
        except Exception as e:
            print(f"❌ Error creando visualizaciones: {str(e)}")
    
    def generar_reporte_accesibilidad(self, metricas, acceso_localidad):
        """Genera un reporte completo de accesibilidad"""
        
        reporte = []
        reporte.append("REPORTE DE ACCESIBILIDAD A CENTROS DE SALUD")
        reporte.append("BOGOTÁ D.C. - ANÁLISIS BASADO EN DATOS SINTÉTICOS")
        reporte.append("="*80)
        reporte.append(f"Fecha del análisis: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        reporte.append(f"Población analizada: {len(self.df_accesibilidad):,} personas")
        reporte.append(f"Centros de salud incluidos: {len(self.df_centros)} centros")
        reporte.append("")
        
        # Resumen ejecutivo
        reporte.append("📋 RESUMEN EJECUTIVO:")
        reporte.append("-" * 30)
        reporte.append(f"• Distancia promedio al centro más cercano: {metricas['distancia_promedio']:.2f} km")
        reporte.append(f"• Distancia mediana: {metricas['distancia_mediana']:.2f} km")
        reporte.append(f"• Porcentaje con centro en su localidad: {metricas['pct_misma_localidad']:.1f}%")
        reporte.append("")
        
        # Distribución por distancias
        reporte.append("📍 DISTRIBUCIÓN POR RANGOS DE DISTANCIA:")
        reporte.append("-" * 40)
        total = len(self.df_accesibilidad)
        for rango, cantidad in metricas['rangos_distancia'].items():
            porcentaje = (cantidad / total) * 100
            reporte.append(f"• {rango}: {cantidad:,} personas ({porcentaje:.1f}%)")
        reporte.append("")
        
        # Accesibilidad por localidad
        reporte.append("🏘️ ACCESIBILIDAD POR LOCALIDAD:")
        reporte.append("-" * 40)
        reporte.append("Las 5 localidades con PEOR accesibilidad:")
        for i, (localidad, datos) in enumerate(acceso_localidad.head(5).iterrows(), 1):
            reporte.append(f"{i}. {localidad}: {datos['dist_promedio']:.1f} km promedio")
        
        reporte.append("\nLas 5 localidades con MEJOR accesibilidad:")
        for i, (localidad, datos) in enumerate(acceso_localidad.tail(5).iterrows(), 1):
            reporte.append(f"{i}. {localidad}: {datos['dist_promedio']:.1f} km promedio")
        reporte.append("")
        
        # Recomendaciones
        reporte.append("💡 RECOMENDACIONES:")
        reporte.append("-" * 25)
        
        localidades_problematicas = acceso_localidad[acceso_localidad['dist_promedio'] > 
                                                   metricas['distancia_promedio']].index.tolist()
        
        if localidades_problematicas:
            reporte.append("📍 Priorizar nuevos centros de salud en:")
            for localidad in localidades_problematicas[:5]:
                reporte.append(f"   • {localidad}")
        
        reporte.append("")
        reporte.append("="*80)
        
        # Guardar reporte
        reporte_texto = "\n".join(reporte)
        with open('reporte_accesibilidad_salud.txt', 'w', encoding='utf-8') as f:
            f.write(reporte_texto)
        
        print("✅ Reporte guardado: reporte_accesibilidad_salud.txt")
        
        return reporte_texto
    
    def ejecutar_analisis_completo(self, muestra_poblacion=9000):
        """Ejecuta el análisis completo de accesibilidad"""
        
        print("="*80)
        print("🏥 SISTEMA DE ANÁLISIS DE ACCESIBILIDAD A CENTROS DE SALUD")
        print("="*80)
        print(f"⏰ Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        if not self.cargar_poblacion():
            return None
        
        if not self.procesar_centros_salud():
            return None
        
        if not self.analizar_accesibilidad(muestra_poblacion):
            return None
        
        metricas = self.generar_metricas()
        acceso_localidad = self.analizar_por_localidad()
        
        print("\n📊 GENERANDO VISUALIZACIONES...")
        self.crear_visualizaciones()
        
        archivo_acceso = 'analisis_accesibilidad_poblacion.csv'
        self.df_accesibilidad.to_csv(archivo_acceso, index=False, encoding='utf-8')
        print(f"✅ Datos de accesibilidad guardados: {archivo_acceso}")
        
        archivo_centros_procesados = 'centros_salud_procesados.csv'
        self.df_centros.to_csv(archivo_centros_procesados, index=False, encoding='utf-8')
        print(f"✅ Centros procesados guardados: {archivo_centros_procesados}")
        
        self.generar_reporte_accesibilidad(metricas, acceso_localidad)
        
        print(f"\n🎉 ANÁLISIS COMPLETO DE ACCESIBILIDAD FINALIZADO")
        print("="*80)
        
        return {
            'metricas': metricas,
            'acceso_localidad': acceso_localidad,
            'df_accesibilidad': self.df_accesibilidad,
            'df_centros': self.df_centros
        }


def main():
    """Función principal para ejecutar el análisis completo"""
    
    print("🏥 SISTEMA DE ANÁLISIS DE ACCESIBILIDAD A CENTROS DE SALUD")
    print("="*70)
    
    archivos_poblacion_posibles = [
        'poblacion_sintetica_bogota.csv',
        'resultados_analisis_bogota/poblacion_sintetica_bogota.csv'
    ]
    
    archivo_poblacion = None
    for archivo in archivos_poblacion_posibles:
        if os.path.exists(archivo):
            archivo_poblacion = archivo
            break
    
    if not archivo_poblacion:
        print("❌ No se encontró archivo de población sintética")
        print("💡 Ejecuta primero el generador de datos sintéticos")
        return False
    
    if not os.path.exists('centros_salud.csv'):
        print("❌ No se encontró archivo centros_salud.csv")
        return False
    
    print(f"✅ Archivo de población encontrado: {archivo_poblacion}")
    print(f"✅ Archivo de centros encontrado: centros_salud.csv")
    
    muestra = 9000
    
    print(f"\n📊 Configuración automática:")
    print(f"   • Tamaño de muestra: {muestra:,} personas")
    print(f"   • Tiempo estimado: 2-3 minutos")
    
    sistema = SistemaAccesibilidadSalud(archivo_poblacion, 'centros_salud.csv')
    
    resultados = sistema.ejecutar_analisis_completo(muestra_poblacion=muestra)
    
    if resultados:
        print(f"\n🎉 ANÁLISIS COMPLETADO EXITOSAMENTE!")
        print(f"📁 Revisa los archivos generados en el directorio actual")
        print(f"📊 Visualizaciones: analisis_accesibilidad_centros_salud.png")
        print(f"📋 Reporte completo: reporte_accesibilidad_salud.txt")
        return True
    else:
        print(f"\n❌ El análisis no se completó correctamente")
        return False


if __name__ == "__main__":
    main()
