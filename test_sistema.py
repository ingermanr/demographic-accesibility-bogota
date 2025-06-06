#!/usr/bin/env python3
"""
SCRIPT DE PRUEBA Y DEMOSTRACIÓN
SISTEMA BOG_SINTE MEJORADO

Este script demuestra las nuevas funcionalidades del sistema,
incluyendo el análisis de centros de salud y accesibilidad.

Autor: Sistema de Análisis Demográfico
Fecha: Mayo 2025
"""

import os
import sys
import time
from datetime import datetime

def verificar_archivos_necesarios():
    """Verifica que todos los archivos necesarios estén presentes"""
    
    print("🔍 VERIFICANDO ARCHIVOS DEL PROYECTO...")
    print("="*50)
    
    archivos_necesarios = [
        'main_corregido.py',
        'generador_datos_sinteticos_bogota.py', 
        'validador_datos_sinteticos.py',
        'analizador_centros_salud.py',
        'centros_salud.csv',
        'README.md'
    ]
    
    archivos_faltantes = []
    archivos_presentes = []
    
    for archivo in archivos_necesarios:
        if os.path.exists(archivo):
            tamaño = os.path.getsize(archivo) / 1024  # KB
            archivos_presentes.append(f"✅ {archivo} ({tamaño:.1f} KB)")
        else:
            archivos_faltantes.append(f"❌ {archivo}")
    
    print("📄 ARCHIVOS PRESENTES:")
    for archivo in archivos_presentes:
        print(f"   {archivo}")
    
    if archivos_faltantes:
        print(f"\n⚠️ ARCHIVOS FALTANTES:")
        for archivo in archivos_faltantes:
            print(f"   {archivo}")
        return False
    
    print(f"\n✅ Todos los archivos necesarios están presentes")
    return True

def ejecutar_prueba_rapida():
    """Ejecuta una prueba rápida del sistema"""
    
    print(f"\n🚀 INICIANDO PRUEBA RÁPIDA DEL SISTEMA")
    print("="*50)
    
    try:
        # Importar sistema principal
        print("📦 Importando módulos...")
        from main_corregido import SistemaDatosSinteticosBogota
        
        # Crear instancia
        print("🔧 Creando instancia del sistema...")
        sistema = SistemaDatosSinteticosBogota()
        
        # Ejecutar con muestra pequeña para prueba
        print("⚡ Ejecutando análisis con muestra pequeña (1000 registros)...")
        inicio = time.time()
        
        exito = sistema.ejecutar_pipeline_completo(tamaño_muestra=1000)
        
        tiempo_total = time.time() - inicio
        
        if exito:
            print(f"\n🎉 PRUEBA COMPLETADA EXITOSAMENTE")
            print(f"⏱️ Tiempo total: {tiempo_total:.1f} segundos")
            
            # Verificar archivos generados
            directorio = "resultados_analisis_bogota"
            if os.path.exists(directorio):
                archivos_generados = os.listdir(directorio)
                print(f"\n📁 Archivos generados en {directorio}:")
                for archivo in sorted(archivos_generados):
                    ruta = os.path.join(directorio, archivo)
                    tamaño = os.path.getsize(ruta) / 1024  # KB
                    print(f"   • {archivo} ({tamaño:.1f} KB)")
            
            return True
        else:
            print(f"\n❌ La prueba falló")
            return False
            
    except Exception as e:
        print(f"\n❌ Error durante la prueba: {str(e)}")
        return False

def ejecutar_prueba_centros_salud():
    """Ejecuta una prueba específica del análisis de centros de salud"""
    
    print(f"\n🏥 PRUEBA ESPECÍFICA: ANÁLISIS DE CENTROS DE SALUD")
    print("="*60)
    
    try:
        # Verificar datos de población
        archivos_poblacion = [
            'resultados_analisis_bogota/poblacion_sintetica_bogota.csv',
            'poblacion_sintetica_bogota.csv'
        ]
        
        archivo_poblacion = None
        for archivo in archivos_poblacion:
            if os.path.exists(archivo):
                archivo_poblacion = archivo
                break
        
        if not archivo_poblacion:
            print("⚠️ No se encontraron datos de población")
            print("💡 Ejecuta primero una prueba completa")
            return False
        
        print(f"✅ Usando archivo de población: {archivo_poblacion}")
        
        # Importar módulo de centros de salud
        from analizador_centros_salud import SistemaAccesibilidadSalud
        
        # Crear sistema
        sistema_acceso = SistemaAccesibilidadSalud(archivo_poblacion, 'centros_salud.csv')
        
        # Ejecutar análisis
        print("🔍 Ejecutando análisis de accesibilidad...")
        inicio = time.time()
        
        resultados = sistema_acceso.ejecutar_analisis_completo(muestra_poblacion=500)
        
        tiempo = time.time() - inicio
        
        if resultados:
            print(f"\n✅ ANÁLISIS DE CENTROS DE SALUD COMPLETADO")
            print(f"⏱️ Tiempo: {tiempo:.1f} segundos")
            
            # Mostrar métricas clave
            if 'metricas' in resultados:
                metricas = resultados['metricas']
                print(f"\n📊 MÉTRICAS CLAVE:")
                print(f"   • Distancia promedio: {metricas['distancia_promedio']:.2f} km")
                print(f"   • Distancia mediana: {metricas['distancia_mediana']:.2f} km")
                print(f"   • % con centro en su localidad: {metricas['pct_misma_localidad']:.1f}%")
            
            return True
        else:
            print(f"\n❌ El análisis de centros de salud falló")
            return False
            
    except Exception as e:
        print(f"\n❌ Error en análisis de centros: {str(e)}")
        return False

def mostrar_resumen_mejoras():
    """Muestra un resumen de las mejoras implementadas"""
    
    print(f"\n🌟 RESUMEN DE MEJORAS IMPLEMENTADAS")
    print("="*50)
    
    mejoras = [
        "🏥 Análisis completo de centros de salud",
        "📍 Cálculo de distancias y accesibilidad",
        "📊 Métricas de cobertura sanitaria",
        "👥 Análisis de grupos vulnerables",
        "🗺️ Visualizaciones de accesibilidad",
        "📋 Reportes especializados",
        "🔧 Código modular y organizado",
        "🧹 Eliminación de archivos duplicados",
        "📖 Documentación completa",
        "⚡ Pipeline automatizado"
    ]
    
    for mejora in mejoras:
        print(f"   ✅ {mejora}")
    
    print(f"\n🎯 CASOS DE USO PRINCIPALES:")
    casos_uso = [
        "Planificación urbana y servicios públicos",
        "Análisis de accesibilidad sanitaria", 
        "Optimización de ubicación de centros",
        "Identificación de zonas vulnerables",
        "Evaluación de políticas públicas",
        "Investigación académica",
        "Desarrollo de aplicaciones"
    ]
    
    for caso in casos_uso:
        print(f"   • {caso}")

def main():
    """Función principal del script de prueba"""
    
    print("🧪 SCRIPT DE PRUEBA - SISTEMA BOG_SINTE MEJORADO")
    print("="*70)
    print(f"⏰ Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    
    # Paso 1: Verificar archivos
    if not verificar_archivos_necesarios():
        print("\n❌ Faltan archivos necesarios. Verifica la instalación.")
        return False
    
    # Paso 2: Mostrar resumen de mejoras
    mostrar_resumen_mejoras()
    
    # Paso 3: Configuración automática de pruebas
    print(f"\n🚀 CONFIGURACIÓN AUTOMÁTICA DE PRUEBAS")
    print("   Ejecutando: Prueba rápida completa (1000 registros)")
    print("   Tiempo estimado: ~1 minuto")
    print("   Para cambiar configuración, edita el código fuente")
    
    # Configuración automática
    opcion = 1  # Prueba rápida completa por defecto
    
    exito_total = True
    
    if opcion in [1, 3]:
        # Prueba completa
        exito_completa = ejecutar_prueba_rapida()
        exito_total = exito_total and exito_completa
    
    if opcion in [2, 3]:
        # Prueba de centros de salud
        exito_centros = ejecutar_prueba_centros_salud()
        if opcion == 2:  # Solo centros
            exito_total = exito_centros
        else:  # Ambas
            exito_total = exito_total and exito_centros
    
    if opcion == 4:
        print("\n📋 Información mostrada. No se ejecutaron pruebas.")
        exito_total = True
    
    # Resumen final
    print(f"\n" + "="*70)
    if exito_total and opcion != 4:
        print("🎉 TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
        print("\n✨ El sistema BOG_SINTE mejorado está funcionando correctamente")
        print("📁 Revisa los archivos generados en: resultados_analisis_bogota/")
        print("\n💡 Para uso completo ejecuta: python main_corregido.py")
    elif opcion == 4:
        print("📖 INFORMACIÓN DEL SISTEMA MOSTRADA")
        print("\n💡 Para ejecutar el sistema completo: python main_corregido.py")
    else:
        print("⚠️ ALGUNAS PRUEBAS FALLARON")
        print("\n🔧 Verifica las dependencias: pip install pandas numpy matplotlib seaborn")
        print("📖 Consulta el README.md para más información")
    
    print("="*70)
    return exito_total

if __name__ == "__main__":
    main()
