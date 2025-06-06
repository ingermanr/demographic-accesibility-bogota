#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para ejecutar la integración de centros de salud con el mapa de Bogotá
VERSIÓN CORREGIDA - Maneja automáticamente problemas de codificación UTF-8/Latin-1
"""

import os
import sys
from datetime import datetime

def instalar_dependencia_si_falta(paquete, nombre_import=None):
    """Instala una dependencia si no está disponible"""
    if nombre_import is None:
        nombre_import = paquete
    
    try:
        __import__(nombre_import)
        return True
    except ImportError:
        print(f"📦 Instalando {paquete}...")
        try:
            import subprocess
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', paquete])
            print(f"✅ {paquete} instalado correctamente")
            return True
        except Exception as e:
            print(f"❌ Error instalando {paquete}: {e}")
            return False

def main():
    print("🚀 INTEGRADOR DE CENTROS DE SALUD - VERSIÓN CORREGIDA")
    print("=" * 60)
    print("🔧 Con detección automática de codificación")
    print()
    
    # Verificar e instalar dependencias automáticamente
    print("📦 VERIFICANDO DEPENDENCIAS...")
    dependencias = [
        ('pandas', 'pandas'),
        ('folium', 'folium'),
        ('geopy', 'geopy'),
        ('numpy', 'numpy'),
        ('chardet', 'chardet')  # Para detección de codificación
    ]
    
    dependencias_ok = True
    for paquete, import_name in dependencias:
        if instalar_dependencia_si_falta(paquete, import_name):
            print(f"   ✅ {paquete}")
        else:
            print(f"   ❌ {paquete} - NO SE PUDO INSTALAR")
            dependencias_ok = False
    
    if not dependencias_ok:
        print("\n❌ No se pudieron instalar todas las dependencias.")
        print("💡 Intenta instalar manualmente:")
        print("   pip install pandas folium geopy numpy chardet")
        return False
    
    # Verificar archivos disponibles
    print(f"\n📁 VERIFICANDO ARCHIVOS...")
    
    archivos_encontrados = []
    archivos_faltantes = []
    
    # Archivo principal (requerido)
    archivo_centros = "centros_salud.csv"
    if os.path.exists(archivo_centros):
        size_kb = os.path.getsize(archivo_centros) / 1024
        archivos_encontrados.append(f"✅ {archivo_centros} ({size_kb:.1f} KB)")
    else:
        archivos_faltantes.append(f"❌ {archivo_centros} (REQUERIDO)")
    
    # Archivos opcionales
    archivo_poblacion_csv = "resultados_analisis_bogota/poblacion_sintetica_bogota.csv"
    if os.path.exists(archivo_poblacion_csv):
        size_mb = os.path.getsize(archivo_poblacion_csv) / (1024 * 1024)
        archivos_encontrados.append(f"✅ {archivo_poblacion_csv} ({size_mb:.1f} MB)")
    else:
        archivos_faltantes.append(f"⚠️  {archivo_poblacion_csv} (opcional)")
    
    archivo_poblacion_html = "mapa_poblacion_bogota.html"
    if os.path.exists(archivo_poblacion_html):
        size_mb = os.path.getsize(archivo_poblacion_html) / (1024 * 1024)
        archivos_encontrados.append(f"✅ {archivo_poblacion_html} ({size_mb:.1f} MB)")
    else:
        archivos_faltantes.append(f"⚠️  {archivo_poblacion_html} (opcional)")
    
    # Mostrar estado de archivos
    print("   ARCHIVOS ENCONTRADOS:")
    for archivo in archivos_encontrados:
        print(f"     {archivo}")
    print("   ARCHIVOS FALTANTES:")
    for archivo in archivos_faltantes:
        print(f"     {archivo}")
    
    # Si falta el archivo principal, no continuar
    if not os.path.exists(archivo_centros):
        print(f"\n❌ ERROR: No se encontró el archivo principal '{archivo_centros}'")
        print("💡 SOLUCIÓN:")
        print("   1. Asegúrate de que el archivo esté en el directorio actual")
        print("   2. Verifica que el nombre sea exactamente 'centros_salud.csv'")
        print("   3. Si el archivo tiene otro nombre, renómbralo o modifica el script")
        return False
    
    # Importar el integrador con la nueva versión
    try:
        from integrador_centros_salud_v2 import IntegradorCentrosSaludBogota
        print(f"\n✅ Integrador cargado correctamente (versión corregida)")
    except ImportError:
        print(f"\n❌ No se pudo importar el integrador")
        print("💡 Asegúrate de que 'integrador_centros_salud_v2.py' esté en el directorio")
        return False
    
    print(f"\n🔄 INICIANDO PROCESAMIENTO...")
    
    # Crear instancia del integrador
    integrador = IntegradorCentrosSaludBogota()
    
    # Ejecutar integración
    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        archivo_salida = f"mapa_centros_salud_bogota_{timestamp}.html"
        
        mapa, datos = integrador.ejecutar_integracion(
            archivo_centros_csv=archivo_centros,
            archivo_poblacion_csv=archivo_poblacion_csv if os.path.exists(archivo_poblacion_csv) else None,
            archivo_poblacion_html=archivo_poblacion_html if os.path.exists(archivo_poblacion_html) else None,
            archivo_salida=archivo_salida
        )
        
        print("\n" + "=" * 60)
        print("🎉 ¡INTEGRACIÓN COMPLETADA!")
        print("=" * 60)
        
        # Verificar archivos generados
        archivos_generados = []
        if os.path.exists(archivo_salida):
            size_mb = os.path.getsize(archivo_salida) / (1024 * 1024)
            archivos_generados.append(f"🗺️  {archivo_salida} ({size_mb:.2f} MB)")
        
        archivo_datos = archivo_salida.replace('.html', '_datos.csv')
        if os.path.exists(archivo_datos):
            size_kb = os.path.getsize(archivo_datos) / 1024
            archivos_generados.append(f"📊 {archivo_datos} ({size_kb:.1f} KB)")
        
        print(f"📄 ARCHIVOS GENERADOS:")
        for archivo in archivos_generados:
            print(f"   {archivo}")
        
        # Estadísticas finales
        print(f"\n📈 ESTADÍSTICAS FINALES:")
        print(f"   • Total centros mapeados: {len(datos)}")
        
        if 'localidad_normalizada' in datos.columns:
            print(f"   • Localidades cubiertas: {datos['localidad_normalizada'].nunique()}")
            print(f"   • Top 3 localidades:")
            top_localidades = datos['localidad_normalizada'].value_counts().head(3)
            for loc, count in top_localidades.items():
                print(f"     - {loc}: {count} centros")
        
        # Contar por tipo
        hospitales = len(datos[datos['centro_salud'].str.contains('HOSPITAL', na=False, case=False)])
        unidades = len(datos[datos['centro_salud'].str.contains('UNIDAD', na=False, case=False)])
        centros = len(datos) - hospitales - unidades
        
        print(f"   • Hospitales: {hospitales}")
        print(f"   • Centros de Salud: {centros}")
        print(f"   • Unidades de Servicios: {unidades}")
        
        print(f"\n💡 INSTRUCCIONES:")
        print(f"   1. Abre '{archivo_salida}' en tu navegador web")
        print(f"   2. Usa las casillas en la esquina superior derecha para activar/desactivar capas")
        print(f"   3. Haz clic en los marcadores para ver información detallada")
        print(f"   4. Los colores representan:")
        print(f"      🔴 Rojos = Hospitales")
        print(f"      🔵 Azules = Centros de Salud") 
        print(f"      🟢 Verdes = Unidades de Servicios")
        print(f"      🌡️ Mapa de calor = Densidad Poblacional")
        
        print(f"\n🎯 PROBLEMAS RESUELTOS EN ESTA VERSIÓN:")
        print(f"   ✅ Detección automática de codificación UTF-8/Latin-1")
        print(f"   ✅ Manejo de caracteres especiales (ñ, ó, í, etc.)")
        print(f"   ✅ Normalización automática de nombres de localidades")
        print(f"   ✅ Instalación automática de dependencias faltantes")
        print(f"   ✅ Verificación de archivos y tamaños")
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR durante la integración:")
        print(f"   {str(e)}")
        
        # Diagnóstico adicional
        print(f"\n🔧 DIAGNÓSTICO:")
        if "'utf-8' codec can't decode" in str(e):
            print(f"   • Problema de codificación - usando detección automática")
        elif "No such file" in str(e):
            print(f"   • Archivo no encontrado - verifica la ruta")
        elif "Permission denied" in str(e):
            print(f"   • Sin permisos de escritura - ejecuta como administrador")
        else:
            print(f"   • Error inesperado - revisa los detalles arriba")
        
        print(f"\n💡 SOLUCIONES:")
        print(f"   • Si es problema de codificación: El script debería manejarlo automáticamente")
        print(f"   • Si faltan archivos: Verifica que centros_salud.csv exista")
        print(f"   • Si faltan permisos: Ejecuta desde un directorio con permisos de escritura")
        print(f"   • Si persiste el error: Copia el mensaje completo para análisis")
        
        return False

if __name__ == "__main__":
    exito = main()
    
    if exito:
        print(f"\n✨ ¡PROCESO COMPLETADO CON ÉXITO!")
        print(f"Tu mapa interactivo está listo para usar.")
    else:
        print(f"\n⚠️  El proceso no se pudo completar.")
        print(f"Revisa los mensajes de error y soluciones sugeridas arriba.")
    
    input(f"\nPresiona ENTER para salir...")
