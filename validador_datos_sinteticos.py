# Validador de datos sintéticos simplificado
# Este archivo resuelve los problemas de dependencias complejas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class ValidadorDatosSinteticos:
    def __init__(self, archivo_csv):
        """Inicializa el validador con los datos sintéticos"""
        try:
            self.df = pd.read_csv(archivo_csv)
            print(f"✅ Datos cargados: {len(self.df)} registros")
        except FileNotFoundError:
            print(f"❌ Error: No se encontró el archivo {archivo_csv}")
            print("💡 Ejecuta primero el generador para crear los datos")
            return None
        
    def generar_resumen_estadistico(self):
        """Genera un resumen completo de las estadísticas del dataset"""
        print("="*60)
        print("RESUMEN ESTADÍSTICO DEL DATASET SINTÉTICO")
        print("="*60)
        
        print(f"\n📊 INFORMACIÓN GENERAL:")
        print(f"   • Total de registros: {len(self.df):,}")
        print(f"   • Localidades representadas: {self.df['localidad'].nunique()}")
        print(f"   • Rango de edades: {self.df['edad'].min()} - {self.df['edad'].max()} años")
        print(f"   • Edad promedio: {self.df['edad'].mean():.1f} años")
        
        print(f"\n🏘️ DISTRIBUCIÓN POR LOCALIDAD:")
        dist_localidad = self.df['localidad'].value_counts().sort_values(ascending=False)
        for localidad, count in dist_localidad.head(10).items():
            porcentaje = (count / len(self.df)) * 100
            print(f"   • {localidad}: {count:,} ({porcentaje:.1f}%)")
        
        print(f"\n👥 DISTRIBUCIÓN POR GÉNERO:")
        dist_genero = self.df['genero'].value_counts(normalize=True) * 100
        for genero, porcentaje in dist_genero.items():
            genero_nombre = "Femenino" if genero == 'F' else "Masculino"
            print(f"   • {genero_nombre}: {porcentaje:.1f}%")
        
        print(f"\n🏠 DISTRIBUCIÓN POR ESTRATO:")
        dist_estrato = self.df['estrato'].value_counts().sort_index()
        for estrato, count in dist_estrato.items():
            porcentaje = (count / len(self.df)) * 100
            print(f"   • Estrato {estrato}: {count:,} ({porcentaje:.1f}%)")
        
        print(f"\n🎓 DISTRIBUCIÓN POR EDUCACIÓN:")
        dist_educacion = self.df['nivel_educativo'].value_counts()
        for educacion, count in dist_educacion.items():
            porcentaje = (count / len(self.df)) * 100
            print(f"   • {educacion}: {count:,} ({porcentaje:.1f}%)")
        
        print(f"\n🏥 DISTRIBUCIÓN POR AFILIACIÓN A SALUD:")
        dist_salud = self.df['afiliacion_salud'].value_counts()
        for salud, count in dist_salud.items():
            porcentaje = (count / len(self.df)) * 100
            print(f"   • {salud}: {count:,} ({porcentaje:.1f}%)")
    
    def crear_visualizaciones_basicas(self):
        """Crea visualizaciones básicas usando matplotlib y seaborn"""
        
        # Configurar estilo
        plt.style.use('default')
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        fig.suptitle('Análisis Demográfico - Población Sintética Bogotá', fontsize=16, fontweight='bold')
        
        # 1. Distribución por edad
        axes[0, 0].hist(self.df['edad'], bins=20, alpha=0.7, color='skyblue', edgecolor='black')
        axes[0, 0].set_title('Distribución por Edad')
        axes[0, 0].set_xlabel('Edad (años)')
        axes[0, 0].set_ylabel('Frecuencia')
        
        # 2. Distribución por género
        genero_counts = self.df['genero'].value_counts()
        axes[0, 1].pie(genero_counts.values, labels=['Femenino', 'Masculino'], autopct='%1.1f%%', 
                       colors=['lightpink', 'lightblue'])
        axes[0, 1].set_title('Distribución por Género')
        
        # 3. Distribución por estrato
        estrato_counts = self.df['estrato'].value_counts().sort_index()
        axes[0, 2].bar(estrato_counts.index, estrato_counts.values, color='lightgreen', alpha=0.7)
        axes[0, 2].set_title('Distribución por Estrato')
        axes[0, 2].set_xlabel('Estrato')
        axes[0, 2].set_ylabel('Cantidad')
        
        # 4. Top 10 localidades
        top_localidades = self.df['localidad'].value_counts().head(10)
        axes[1, 0].barh(range(len(top_localidades)), top_localidades.values)
        axes[1, 0].set_yticks(range(len(top_localidades)))
        axes[1, 0].set_yticklabels(top_localidades.index)
        axes[1, 0].set_title('Top 10 Localidades')
        axes[1, 0].set_xlabel('Población')
        
        # 5. Nivel educativo
        educacion_counts = self.df['nivel_educativo'].value_counts()
        axes[1, 1].pie(educacion_counts.values, labels=educacion_counts.index, autopct='%1.1f%%')
        axes[1, 1].set_title('Nivel Educativo')
        
        # 6. Afiliación a salud
        salud_counts = self.df['afiliacion_salud'].value_counts()
        axes[1, 2].bar(salud_counts.index, salud_counts.values, color='orange', alpha=0.7)
        axes[1, 2].set_title('Afiliación a Salud')
        axes[1, 2].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('analisis_demografico_bogota.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("📊 Gráficos guardados como 'analisis_demografico_bogota.png'")
    
    def analizar_correlaciones(self):
        """Analiza correlaciones entre variables demográficas"""
        
        # Crear variables numéricas para análisis
        df_numerico = self.df.copy()
        df_numerico['genero_num'] = df_numerico['genero'].map({'F': 1, 'M': 0})
        df_numerico['educacion_num'] = df_numerico['nivel_educativo'].map({
            'Primaria': 1, 'Secundaria': 2, 'Técnica': 3, 'Universitaria': 4
        })
        df_numerico['salud_num'] = df_numerico['afiliacion_salud'].map({
            'No_afiliado': 0, 'Subsidiado': 1, 'Contributivo': 2
        })
        
        # Matriz de correlación
        variables_correlacion = ['edad', 'estrato', 'genero_num', 'educacion_num', 'salud_num']
        matriz_corr = df_numerico[variables_correlacion].corr()
        
        # Visualizar matriz de correlación
        plt.figure(figsize=(10, 8))
        sns.heatmap(
            matriz_corr, 
            annot=True, 
            cmap='coolwarm', 
            center=0,
            square=True,
            fmt='.3f',
            cbar_kws={'label': 'Correlación'}
        )
        plt.title('Matriz de Correlación - Variables Demográficas')
        plt.tight_layout()
        plt.savefig('matriz_correlacion.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("📊 Matriz de correlación guardada como 'matriz_correlacion.png'")
        return matriz_corr
    
    def validar_distribuciones_esperadas(self):
        """Valida que las distribuciones generadas coincidan con las esperadas"""
        
        print("\n🔍 VALIDACIÓN DE DISTRIBUCIONES:")
        print("="*50)
        
        # Validar distribución de género general
        dist_genero_real = self.df['genero'].value_counts(normalize=True) * 100
        print(f"\n👥 Distribución de Género:")
        print(f"   • Esperado: ~52% F, ~48% M")
        print(f"   • Obtenido: {dist_genero_real['F']:.1f}% F, {dist_genero_real['M']:.1f}% M")
        
        # Validar distribución por estratos
        dist_estratos = self.df['estrato'].value_counts(normalize=True).sort_index() * 100
        print(f"\n🏠 Distribución por Estratos:")
        for estrato, porcentaje in dist_estratos.items():
            print(f"   • Estrato {estrato}: {porcentaje:.1f}%")
        
        # Estratos 1-3 deberían ser ~86% según los datos reales
        estratos_bajos = dist_estratos[dist_estratos.index.isin([1, 2, 3])].sum()
        print(f"   • Estratos 1-3 combinados: {estratos_bajos:.1f}% (Esperado: ~86%)")
        
        # Validar por localidades específicas
        print(f"\n🏘️ Validación por Localidades Clave:")
        
        localidades_clave = ['Kennedy', 'Suba', 'Engativá', 'Ciudad Bolívar', 'Teusaquillo']
        for localidad in localidades_clave:
            if localidad in self.df['localidad'].values:
                df_loc = self.df[self.df['localidad'] == localidad]
                n_registros = len(df_loc)
                porcentaje_total = (n_registros / len(self.df)) * 100
                
                print(f"\n   {localidad}:")
                print(f"   • Registros: {n_registros:,} ({porcentaje_total:.1f}% del total)")
                
                # Distribución de estratos en esta localidad
                estratos_loc = df_loc['estrato'].value_counts().sort_index()
                estratos_principales = estratos_loc.head(2)
                print(f"   • Estratos principales: {dict(estratos_principales)}")
    
    def crear_mapa_interactivo(self):
        """Crea un mapa interactivo con la distribución poblacional"""
        
        try:
            import folium
            from folium.plugins import HeatMap
            print("📍 Creando mapa interactivo con Folium...")
        except ImportError:
            print("❌ Folium no está instalado")
            print("💡 Para mapas interactivos, instala: pip install folium")
            print("📊 Continuando sin mapa interactivo...")
            return None
        
        # Crear mapa base centrado en Bogotá
        mapa_bogota = folium.Map(
            location=[4.6097, -74.0817],
            zoom_start=10,
            tiles='OpenStreetMap'
        )
        
        # Preparar datos para el mapa de calor
        coordenadas_calor = [[row['latitud'], row['longitud']] for _, row in self.df.iterrows()]
        
        # Agregar mapa de calor
        HeatMap(coordenadas_calor, radius=8, blur=10).add_to(mapa_bogota)
        
        # Agregar marcadores por localidad (centros)
        centros_localidades = self.df.groupby('localidad').agg({
            'latitud': 'mean',
            'longitud': 'mean',
            'id': 'count'
        }).rename(columns={'id': 'poblacion'})
        
        for localidad, datos in centros_localidades.iterrows():
            folium.CircleMarker(
                location=[datos['latitud'], datos['longitud']],
                radius=max(5, min(20, datos['poblacion'] / 100)),
                popup=f"{localidad}<br>Población: {datos['poblacion']:,}",
                color='red',
                fill=True,
                fillColor='red',
                fillOpacity=0.6
            ).add_to(mapa_bogota)
        
        # Guardar mapa
        mapa_bogota.save('mapa_poblacion_bogota.html')
        print("🗺️ Mapa interactivo guardado como 'mapa_poblacion_bogota.html'")
        
        return mapa_bogota
    
    def generar_reporte_completo(self, guardar_archivo=True):
        """Genera un reporte completo del análisis"""
        
        reporte = []
        reporte.append("="*80)
        reporte.append("REPORTE DE ANÁLISIS - DATOS SINTÉTICOS POBLACIÓN BOGOTÁ")
        reporte.append("="*80)
        reporte.append(f"Fecha de generación: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")
        reporte.append(f"Total de registros analizados: {len(self.df):,}")
        reporte.append("")
        
        # Estadísticas generales
        reporte.append("📊 ESTADÍSTICAS GENERALES:")
        reporte.append("-" * 30)
        reporte.append(f"• Edad promedio: {self.df['edad'].mean():.1f} años")
        reporte.append(f"• Edad mediana: {self.df['edad'].median():.1f} años")
        reporte.append(f"• Desviación estándar edad: {self.df['edad'].std():.1f}")
        reporte.append("")
        
        # Top localidades
        reporte.append("🏘️ TOP 10 LOCALIDADES MÁS POBLADAS:")
        reporte.append("-" * 40)
        top_localidades = self.df['localidad'].value_counts().head(10)
        for i, (localidad, count) in enumerate(top_localidades.items(), 1):
            porcentaje = (count / len(self.df)) * 100
            reporte.append(f"{i:2d}. {localidad}: {count:,} ({porcentaje:.1f}%)")
        reporte.append("")
        
        # Distribución educativa
        reporte.append("🎓 DISTRIBUCIÓN EDUCATIVA:")
        reporte.append("-" * 30)
        dist_educacion = self.df['nivel_educativo'].value_counts()
        for educacion, count in dist_educacion.items():
            porcentaje = (count / len(self.df)) * 100
            reporte.append(f"• {educacion}: {count:,} ({porcentaje:.1f}%)")
        reporte.append("")
        
        # Análisis por estratos
        reporte.append("💰 ANÁLISIS POR ESTRATOS:")
        reporte.append("-" * 30)
        for estrato in sorted(self.df['estrato'].unique()):
            df_estrato = self.df[self.df['estrato'] == estrato]
            count = len(df_estrato)
            porcentaje = (count / len(self.df)) * 100
            edad_promedio = df_estrato['edad'].mean()
            
            reporte.append(f"Estrato {estrato}:")
            reporte.append(f"  • Población: {count:,} ({porcentaje:.1f}%)")
            reporte.append(f"  • Edad promedio: {edad_promedio:.1f} años")
            
            # Educación predominante en este estrato
            educacion_predominante = df_estrato['nivel_educativo'].mode().iloc[0]
            reporte.append(f"  • Educación predominante: {educacion_predominante}")
            reporte.append("")
        
        reporte_texto = "\n".join(reporte)
        
        if guardar_archivo:
            with open('reporte_datos_sinteticos.txt', 'w', encoding='utf-8') as f:
                f.write(reporte_texto)
            print("📄 Reporte guardado como 'reporte_datos_sinteticos.txt'")
        
        return reporte_texto

# Función principal para ejecutar todos los análisis
def analizar_datos_sinteticos(archivo_csv='poblacion_sintetica_bogota.csv'):
    """Función principal que ejecuta todo el análisis"""
    
    print("🚀 Iniciando análisis de datos sintéticos...")
    
    # Crear instancia del validador
    validador = ValidadorDatosSinteticos(archivo_csv)
    
    if validador.df is None:
        return None
    
    # Ejecutar análisis
    print("\n1️⃣ Generando resumen estadístico...")
    validador.generar_resumen_estadistico()
    
    print("\n2️⃣ Creando visualizaciones básicas...")
    validador.crear_visualizaciones_basicas()
    
    print("\n3️⃣ Analizando correlaciones...")
    correlaciones = validador.analizar_correlaciones()
    
    print("\n4️⃣ Validando distribuciones...")
    validador.validar_distribuciones_esperadas()
    
    print("\n5️⃣ Generando reporte completo...")
    reporte = validador.generar_reporte_completo()
    
    print("\n✅ Análisis completado exitosamente!")
    print("\n📁 Archivos generados:")
    print("   • analisis_demografico_bogota.png")
    print("   • matriz_correlacion.png")
    print("   • reporte_datos_sinteticos.txt")
    
    return validador

# Ejemplo de uso
if __name__ == "__main__":
    # Ejecutar análisis completo
    validador = analizar_datos_sinteticos('./resultados_analisis_bogota/poblacion_sintetica_bogota.csv')
