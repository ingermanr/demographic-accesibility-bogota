#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Prueba completa del sistema de análisis corregido
"""

import sys
import os

def probar_sistema():
    print("🏥 PRUEBA COMPLETA DEL SISTEMA CORREGIDO")
    print("=" * 60)
    
    try:
        # Importar el sistema
        from analizador_centros_salud import SistemaAccesibilidadSalud
        
        # Verificar archivos
        archivos_poblacion = [
            'poblacion_sintetica_bogota.csv',
            'resultados_analisis_bogota/poblacion_sintetica_bogota.csv'
        ]
        
        archivo_poblacion = None
        for archivo in archivos_poblacion:
            if os.path.exists(archivo):
                archivo_poblacion = archivo
                break
        
        if not archivo_poblacion:
            print("❌ No se encontró archivo de población")
            return False
        
        if not os.path.exists('centros_salud.csv'):
            print("❌ No se encontró archivo de centros de salud")
            return False
        
        print(f"✅ Archivo población: {archivo_poblacion}")
        print(f"✅ Archivo centros: centros_salud.csv")
        
        # Crear sistema
        sistema = SistemaAccesibilidadSalud(archivo_poblacion, 'centros_salud.csv')
        
        # Probar carga de población
        print(f"\n📊 CARGANDO POBLACIÓN...")
        if not sistema.cargar_poblacion():
            print(f"❌ Error cargando población")  
            return False
        
        print(f"✅ Población cargada: {len(sistema.df_poblacion):,} registros")
        
        # Probar carga de centros
        print(f"\n🏥 PROCESANDO CENTROS...")
        if not sistema.procesar_centros_salud():
            print(f"❌ Error procesando centros")
            return False
        
        print(f"✅ Centros procesados: {len(sistema.df_centros)} centros")
        
        # Mostrar muestra de centros
        print(f"\n📋 MUESTRA DE CENTROS:")
        for i, (idx, centro) in enumerate(sistema.df_centros.head(3).iterrows()):
            nombre = centro.get('centro_salud', f'Centro_{idx}')
            localidad = centro.get('localidad', 'N/A')
            lat = centro.get('latitud', 'N/A')
            lon = centro.get('longitud', 'N/A')
            print(f"   {i+1}. {nombre[:40]}... - {localidad} ({lat:.4f}, {lon:.4f})")
        
        # Probar análisis rápido con muestra pequeña
        print(f"\n🔍 PROBANDO ANÁLISIS (muestra pequeña)...")
        if sistema.analizar_accesibilidad(muestra_poblacion=100):
            print(f"✅ Análisis completado: {len(sistema.df_accesibilidad)} registros")
            
            # Mostrar estadísticas básicas
            distancia_promedio = sistema.df_accesibilidad['distancia_km'].mean()
            distancia_max = sistema.df_accesibilidad['distancia_km'].max()
            distancia_min = sistema.df_accesibilidad['distancia_km'].min()
            
            print(f"\n📈 ESTADÍSTICAS BÁSICAS:")
            print(f"   • Distancia promedio: {distancia_promedio:.2f} km")
            print(f"   • Distancia máxima: {distancia_max:.2f} km")
            print(f"   • Distancia mínima: {distancia_min:.2f} km")
            
            return True
        else:
            print(f"❌ Error en análisis")
            return False
        
    except ImportError as e:
        print(f"❌ Error importando: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    exito = probar_sistema()
    if exito:
        print(f"\n🎉 SISTEMA FUNCIONANDO CORRECTAMENTE")
        print(f"   • Listo para ejecutar análisis completo")
        print(f"   • Ejecuta: python analizador_centros_salud.py")
    else:
        print(f"\n❌ SISTEMA TIENE PROBLEMAS")
        print(f"   • Revisa los errores anteriores")
