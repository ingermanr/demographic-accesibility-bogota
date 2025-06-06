#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DEMO: Integración de Centros de Salud con Mapa de Población de Bogotá
Este script demuestra cómo usar el IntegradorCentrosSaludBogota

Autor: Sistema de Análisis de Bogotá
Fecha: 2024
"""

import pandas as pd
import os
from datetime import datetime

def demo_integracion():
    """Demostración completa del integrador de centros de salud"""
    
    print("🎯 DEMO: INTEGRACIÓN DE CENTROS DE SALUD - BOGOTÁ")
    print("=" * 60)
    print(f"📅 Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Verificar dependencias
    print("🔍 VERIFICANDO DEPENDENCIAS...")
    dependencias = ['pandas', 'folium', 'geopy', 'numpy']
    dependencias_ok = True
    
    for dep in dependencias:
        try:
            __import__(dep)
            print(f"   ✅ {dep}")
        except ImportError:
            print(f"   ❌ {dep} - NO INSTALADO")
            dependencias_ok = False
    
    if not dependencias_ok:
        print("\n⚠️  INSTALA LAS DEPENDENCIAS FALTANTES:")
        print("   pip install pandas folium geopy numpy")
        return False
    
    # Importar el integrador
    try:
        from integrador_centros_salud import IntegradorCentrosSaludBogota
        print("   ✅ IntegradorCentrosSaludBogota")
    except ImportError:
        print("   ❌ No se pudo importar IntegradorCentrosSaludBogota")
        print("   Asegúrate de que integrador_centros_salud.py esté en el directorio")
        return False
    
    print("\n📁 VERIFICANDO ARCHIVOS...")
    
    # Verificar archivos
    archivos = {
        'centros_salud.csv': 'REQUERIDO',
        'resultados_analisis_bogota/poblacion_sintetica_bogota.csv': 'OPCIONAL',
        'mapa_poblacion_bogota.html': 'OPCIONAL'
    }
    
    archivos_disponibles = {}
    for archivo, tipo in archivos.items():
        if os.path.exists(archivo):
            print(f"   ✅ {archivo} ({tipo})")
            archivos_disponibles[archivo] = True
        else:
            print(f"   ❌ {archivo} ({tipo})")
            archivos_disponibles[archivo] = False
    
    # Si no está el archivo principal, mostrar estructura esperada
    if not archivos_disponibles['centros_salud.csv']:
        print("\n📋 ESTRUCTURA ESPERADA DEL CSV:")
        print("   centro_salud;barrio;localidad;capacidad_ambulancias;capacidad_camas;...")
        print("   HOSPITAL EJEMPLO;BARRIO;Kennedy;5;100;20;15;8")
        print("   CENTRO DE SALUD;OTRO BARRIO;Suba;0;0;5;10;2")
        return False
    
    # Crear instancia del integrador
    print(f"\n🚀 INICIANDO INTEGRACIÓN...")
    integrador = IntegradorCentrosSaludBogota()
    
    # Mostrar configuración
    print(f"   📍 Coordenadas base: {integrador.bogota_coords}")
    print(f"   🗺️  Localidades configuradas: {len(integrador.coordenadas_localidades)}")
    print(f"   🔄 Mapeo de nombres: {len(integrador.mapeo_localidades)} correcciones")
    
    # Ejecutar integración
    try:
        print(f"\n⚡ EJECUTANDO PROCESO...")
        
        archivo_salida = f"demo_mapa_centros_salud_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        
        mapa, datos = integrador.ejecutar_integracion(
            archivo_centros_csv='centros_salud.csv',
            archivo_poblacion_csv='resultados_analisis_bogota/poblacion_sintetica_bogota.csv' if archivos_disponibles['resultados_analisis_bogota/poblacion_sintetica_bogota.csv'] else None,
            archivo_poblacion_html='mapa_poblacion_bogota.html' if archivos_disponibles['mapa_poblacion_bogota.html'] else None,
            archivo_salida=archivo_salida
        )
        
        print(f"\n🎉 ¡DEMO COMPLETADO EXITOSAMENTE!")
        print("=" * 60)
        
        # Mostrar estadísticas finales
        print(f"📊 ESTADÍSTICAS FINALES:")
        print(f"   • Total centros procesados: {len(datos)}")
        
        if 'localidad' in datos.columns:
            print(f"   • Localidades cubiertas: {datos['localidad'].nunique()}")
            print(f"   • Top 3 localidades:")
            top_localidades = datos['localidad'].value_counts().head(3)
            for loc, count in top_localidades.items():
                print(f"     - {loc}: {count} centros")
        
        # Contar por tipo
        hospitales = len(datos[datos['centro_salud'].str.contains('HOSPITAL', na=False, case=False)])
        unidades = len(datos[datos['centro_salud'].str.contains('UNIDAD', na=False, case=False)])
        centros = len(datos) - hospitales - unidades
        
        print(f"   • Hospitales: {hospitales}")
        print(f"   • Centros de Salud: {centros}")
        print(f"   • Unidades de Servicios: {unidades}")
        
        # Calcular capacidades totales si están disponibles
        capacidades_cols = ['capacidad_ambulancias', 'capacidad_camas', 'capacidad_camillas', 
                          'capacidad_consultorios', 'capacidad_salas']
        
        capacidades_disponibles = [col for col in capacidades_cols if col in datos.columns]
        if capacidades_disponibles:
            print(f"   • Capacidades totales:")
            for col in capacidades_disponibles:
                total = datos[col].sum()
                if total > 0:
                    nombre = col.replace('capacidad_', '').replace('_', ' ').title()
                    print(f"     - {nombre}: {int(total)}")
        
        print(f"\n📄 ARCHIVOS GENERADOS:")
        print(f"   🗺️  {archivo_salida}")
        print(f"   📊 {archivo_salida.replace('.html', '_datos.csv')}")
        
        print(f"\n💡 SIGUIENTE PASO:")
        print(f"   Abre '{archivo_salida}' en tu navegador para ver el mapa interactivo")
        
        # Verificar tamaño de archivos generados
        if os.path.exists(archivo_salida):
            size_mb = os.path.getsize(archivo_salida) / (1024 * 1024)
            print(f"   📏 Tamaño del mapa: {size_mb:.2f} MB")
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR DURANTE LA DEMO:")
        print(f"   {str(e)}")
        print(f"\n🔧 SUGERENCIAS:")
        print(f"   • Verifica el formato del archivo CSV")
        print(f"   • Asegúrate de tener permisos de escritura")
        print(f"   • Revisa que todas las dependencias estén instaladas")
        return False

def mostrar_ayuda():
    """Muestra información de ayuda"""
    print("🆘 AYUDA - INTEGRADOR DE CENTROS DE SALUD")
    print("=" * 50)
    print("COMANDOS DISPONIBLES:")
    print("  python demo_integracion.py        - Ejecutar demo completa")
    print("  python demo_integracion.py help   - Mostrar esta ayuda")
    print()
    print("REQUISITOS:")
    print("  • Python 3.6+")
    print("  • pandas, folium, geopy, numpy")
    print("  • Archivo centros_salud.csv")
    print()
    print("ARCHIVOS OPCIONALES:")
    print("  • resultados_analisis_bogota/poblacion_sintetica_bogota.csv")
    print("  • mapa_poblacion_bogota.html")
    print()
    print("FORMATO DEL CSV:")
    print("  centro_salud;barrio;localidad;capacidad_ambulancias;...")
    print()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1].lower() in ['help', '-h', '--help']:
        mostrar_ayuda()
    else:
        exito = demo_integracion()
        
        if exito:
            print(f"\n✨ ¡DEMO COMPLETADA CON ÉXITO!")
            print(f"El mapa interactivo está listo para usar.")
        else:
            print(f"\n⚠️  La demo no se pudo completar.")
            print(f"Revisa los mensajes de error arriba.")
            print(f"Ejecuta: python demo_integracion.py help para más información.")
