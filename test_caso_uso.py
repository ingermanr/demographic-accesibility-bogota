#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test del archivo caso_uso.py
Verifica que todas las funcionalidades estén funcionando correctamente
"""

import os
import sys
import pandas as pd

def verificar_dependencias():
    """Verifica que todas las dependencias necesarias estén instaladas"""
    dependencias_requeridas = [
        'pandas', 'numpy', 'sklearn', 'matplotlib', 'seaborn'
    ]
    
    dependencias_opcionales = [
        'plotly', 'geopy', 'geopandas'
    ]
    
    print("🔍 VERIFICANDO DEPENDENCIAS...")
    print("="*50)
    
    # Verificar dependencias requeridas
    for dep in dependencias_requeridas:
        try:
            __import__(dep)
            print(f"✅ {dep} - Instalado")
        except ImportError:
            print(f"❌ {dep} - NO instalado (REQUERIDO)")
            return False
    
    # Verificar dependencias opcionales
    for dep in dependencias_opcionales:
        try:
            __import__(dep)
            print(f"✅ {dep} - Instalado")
        except ImportError:
            print(f"⚠️  {dep} - NO instalado (opcional)")
    
    return True

def verificar_archivos():
    """Verifica que los archivos necesarios existan"""
    print("\n📁 VERIFICANDO ARCHIVOS...")
    print("="*50)
    
    archivos_requeridos = [
        'caso_uso.py',
        'generador_datos_sinteticos_bogota.py',
        'requirements.txt'
    ]
    
    archivos_datos = [
        'resultados_analisis_bogota/poblacion_sintetica_bogota.csv'
    ]
    
    # Verificar archivos del sistema
    for archivo in archivos_requeridos:
        if os.path.exists(archivo):
            print(f"✅ {archivo} - Encontrado")
        else:
            print(f"❌ {archivo} - NO encontrado")
            return False
    
    # Verificar archivos de datos
    datos_disponibles = False
    for archivo in archivos_datos:
        if os.path.exists(archivo):
            print(f"✅ {archivo} - Encontrado")
            datos_disponibles = True
        else:
            print(f"⚠️  {archivo} - NO encontrado (se puede generar)")
    
    return True, datos_disponibles

def test_importacion_caso_uso():
    """Prueba que se pueda importar el módulo caso_uso correctamente"""
    print("\n🧪 PROBANDO IMPORTACIÓN DE CASO_USO...")
    print("="*50)
    
    try:
        from caso_uso import CasosUsoEspecificos, ejecutar_casos_uso_completos
        print("✅ Importación exitosa")
        print(f"✅ Clase CasosUsoEspecificos disponible")
        print(f"✅ Función ejecutar_casos_uso_completos disponible")
        return True
    except ImportError as e:
        print(f"❌ Error de importación: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

def test_datos_sinteticos():
    """Verifica si existen datos sintéticos o genera una muestra pequeña"""
    print("\n📊 VERIFICANDO DATOS SINTÉTICOS...")
    print("="*50)
    
    archivo_datos = 'resultados_analisis_bogota/poblacion_sintetica_bogota.csv'
    
    if os.path.exists(archivo_datos):
        try:
            df = pd.read_csv(archivo_datos)
            print(f"✅ Datos encontrados: {len(df):,} registros")
            print(f"✅ Columnas: {list(df.columns)}")
            return True, archivo_datos
        except Exception as e:
            print(f"❌ Error leyendo datos: {e}")
            return False, None
    else:
        print("⚠️  No se encontraron datos sintéticos")
        print("💡 Ejecuta 'python main_corregido.py' para generar datos")
        return False, None

def test_caso_uso_basico():
    """Prueba básica del sistema de casos de uso"""
    print("\n🎯 PROBANDO CASOS DE USO BÁSICOS...")
    print("="*50)
    
    # Verificar datos
    datos_ok, archivo_datos = test_datos_sinteticos()
    if not datos_ok:
        print("⚠️  No se pueden probar casos de uso sin datos")
        return False
    
    try:
        from caso_uso import CasosUsoEspecificos
        
        # Crear instancia
        casos_uso = CasosUsoEspecificos(archivo_datos)
        print(f"✅ Instancia creada con {len(casos_uso.df):,} registros")
        
        # Probar método de dashboard ejecutivo (el más simple)
        print("🔄 Probando dashboard ejecutivo...")
        dashboard = casos_uso.generar_dashboard_ejecutivo()
        print("✅ Dashboard ejecutivo generado correctamente")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en prueba básica: {e}")
        return False

def main():
    """Función principal de testing"""
    print("🚀 INICIANDO PRUEBAS DEL SISTEMA CASO_USO")
    print("="*60)
    
    # Cambiar al directório del proyecto
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    resultados = []
    
    # 1. Verificar dependencias
    resultados.append(("Dependencias", verificar_dependencias()))
    
    # 2. Verificar archivos
    archivos_ok, datos_disponibles = verificar_archivos()
    resultados.append(("Archivos", archivos_ok))
    
    # 3. Probar importación
    resultados.append(("Importación", test_importacion_caso_uso()))
    
    # 4. Probar caso de uso básico (si hay datos)
    if datos_disponibles:
        resultados.append(("Caso de uso básico", test_caso_uso_basico()))
    
    # Resumen final
    print("\n📋 RESUMEN DE PRUEBAS")
    print("="*60)
    
    todas_ok = True
    for nombre, resultado in resultados:
        status = "✅ PASÓ" if resultado else "❌ FALLÓ"
        print(f"{nombre:<20}: {status}")
        if not resultado:
            todas_ok = False
    
    print("\n" + "="*60)
    if todas_ok:
        print("🎉 ¡TODAS LAS PRUEBAS PASARON!")
        print("✅ El archivo caso_uso.py está funcionando correctamente")
        if datos_disponibles:
            print("💡 Puedes ejecutar: python -c \"from caso_uso import ejecutar_casos_uso_completos; ejecutar_casos_uso_completos()\"")
        else:
            print("💡 Primero genera datos con: python main_corregido.py")
    else:
        print("⚠️  Algunas pruebas fallaron")
        print("💡 Revisa los errores anteriores y las dependencias")
    
    return todas_ok

if __name__ == "__main__":
    exito = main()
    sys.exit(0 if exito else 1)
