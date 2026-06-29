"""
=======================================================
  SISTEMA DE REGISTRO DE RECICLAJE COMUNITARIO
  Proyecto Integrador - Fundamentos de Programación
  Autor: Hugo Snyder Imbaquingo Chulde 
  Fecha: 26 de  Junio de 2026
=======================================================
"""

import os
import json
from datetime import datetime

# ─────────────────────────────────────────────
#  DATOS EN MEMORIA (lista de registros)
# ─────────────────────────────────────────────
registros = []

ARCHIVO_DATOS = "datos_reciclaje.json"

MATERIALES_VALIDOS = {
    "1": "Plástico",
    "2": "Vidrio",
    "3": "Papel / Cartón",
    "4": "Metal / Lata",
    "5": "Orgánico",
    "6": "Electrónico (E-waste)"
}

# Factor de CO2 ahorrado por kg de material reciclado (kg CO2 / kg material)
IMPACTO_CO2 = {
    "Plástico":            1.5,
    "Vidrio":              0.3,
    "Papel / Cartón":      1.0,
    "Metal / Lata":        4.0,
    "Orgánico":            0.5,
    "Electrónico (E-waste)": 2.0
}


# ─────────────────────────────────────────────
#  UTILIDADES
# ─────────────────────────────────────────────
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\n  Presiona ENTER para continuar...")


def linea(car="─", largo=52):
    print(f"  {car * largo}")


def encabezado(titulo):
    limpiar_pantalla()
    linea("═")
    print(f"  ♻️  {titulo}")
    linea("═")
    print()


def cargar_datos():
    """Carga registros desde archivo JSON si existe."""
    global registros
    if os.path.exists(ARCHIVO_DATOS):
        try:
            with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
                registros = json.load(f)
        except (json.JSONDecodeError, IOError):
            registros = []


def guardar_datos():
    """Persiste los registros en un archivo JSON."""
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
        json.dump(registros, f, ensure_ascii=False, indent=2)


# ─────────────────────────────────────────────
#  MÓDULO 1 — REGISTRAR RECICLAJE
# ─────────────────────────────────────────────
def registrar_reciclaje():
    encabezado("REGISTRAR NUEVO RECICLAJE")

    # Nombre del ciudadano
    while True:
        nombre = input("  Nombre del ciudadano: ").strip()
        if nombre:
            break
        print("  ⚠ El nombre no puede estar vacío.")

    # Barrio / sector
    while True:
        barrio = input("  Barrio o sector: ").strip()
        if barrio:
            break
        print("  ⚠ El barrio no puede estar vacío.")

    # Tipo de material
    print()
    print("  Tipos de material:")
    for clave, nombre in MATERIALES_VALIDOS.items():
        print(f"    [{clave}] {nombre}")
    print()

    while True:
        opcion = input("  Selecciona el tipo de material [1-6]: ").strip()
        if opcion in MATERIALES_VALIDOS:
            material = MATERIALES_VALIDOS[opcion]
            break
        print("  ⚠ Opción inválida, elige entre 1 y 6.")

    # Cantidad en kilogramos
    while True:
        try:
            cantidad = float(input("  Cantidad reciclada (kg): ").strip())
            if cantidad > 0:
                break
            print("  ⚠ La cantidad debe ser mayor a 0.")
        except ValueError:
            print("  ⚠ Ingresa un número válido.")

    # Crear registro
    nuevo = {
        "id": len(registros) + 1,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "nombre": nombre,
        "barrio": barrio,
        "material": material,
        "cantidad_kg": cantidad,
        "co2_ahorrado_kg": round(cantidad * IMPACTO_CO2[material], 3)
    }

    registros.append(nuevo)
    guardar_datos()

    print()
    linea()
    print(f"  ✅ Registro #{nuevo['id']} guardado correctamente.")
    print(f"     Material : {material}")
    print(f"     Cantidad : {cantidad} kg")
    print(f"     CO₂ ahorrado: {nuevo['co2_ahorrado_kg']} kg")
    linea()
    pausar()


# ─────────────────────────────────────────────
#  MÓDULO 2 — VER TODOS LOS REGISTROS
# ─────────────────────────────────────────────
def ver_registros():
    encabezado("HISTORIAL DE REGISTROS")

    if not registros:
        print("  No hay registros aún.")
        pausar()
        return

    print(f"  {'#':<4} {'Fecha':<17} {'Ciudadano':<18} {'Barrio':<14} {'Material':<22} {'kg':>5} {'CO₂(kg)':>8}")
    linea()

    for r in registros:
        print(f"  {r['id']:<4} {r['fecha']:<17} {r['nombre']:<18} {r['barrio']:<14} {r['material']:<22} {r['cantidad_kg']:>5.1f} {r['co2_ahorrado_kg']:>8.2f}")

    linea()
    print(f"  Total de registros: {len(registros)}")
    pausar()


# ─────────────────────────────────────────────
#  MÓDULO 3 — ESTADÍSTICAS POR MATERIAL
# ─────────────────────────────────────────────
def ver_estadisticas():
    encabezado("ESTADÍSTICAS POR MATERIAL")

    if not registros:
        print("  No hay datos suficientes para mostrar estadísticas.")
        pausar()
        return

    # Acumular totales por material
    totales = {}
    for r in registros:
        m = r["material"]
        if m not in totales:
            totales[m] = {"cantidad": 0.0, "co2": 0.0, "veces": 0}
        totales[m]["cantidad"] += r["cantidad_kg"]
        totales[m]["co2"] += r["co2_ahorrado_kg"]
        totales[m]["veces"] += 1

    total_kg = sum(v["cantidad"] for v in totales.values())
    total_co2 = sum(v["co2"] for v in totales.values())

    print(f"  {'Material':<22} {'Veces':>6} {'Total kg':>10} {'CO₂ ahorr.':>12} {'% del total':>12}")
    linea()

    # Ordenar de mayor a menor cantidad
    for mat, datos in sorted(totales.items(), key=lambda x: x[1]["cantidad"], reverse=True):
        porcentaje = (datos["cantidad"] / total_kg * 100) if total_kg > 0 else 0
        barra = "█" * int(porcentaje / 5)
        print(f"  {mat:<22} {datos['veces']:>6} {datos['cantidad']:>10.2f} {datos['co2']:>12.2f} {porcentaje:>11.1f}%  {barra}")

    linea()
    print(f"  {'TOTAL':<22} {len(registros):>6} {total_kg:>10.2f} {total_co2:>12.2f}")
    print()
    print(f"  🌱 CO₂ total evitado: {total_co2:.2f} kg")
    print(f"  🌳 Equivale a plantar aprox. {int(total_co2 / 21)} árbol(es) en un año")
    pausar()


# ─────────────────────────────────────────────
#  MÓDULO 4 — BUSCAR POR CIUDADANO O BARRIO
# ─────────────────────────────────────────────
def buscar_registros():
    encabezado("BUSCAR REGISTROS")

    print("  Buscar por:")
    print("    [1] Nombre del ciudadano")
    print("    [2] Barrio o sector")
    print()

    opcion = input("  Elige una opción: ").strip()

    if opcion == "1":
        termino = input("  Nombre a buscar: ").strip().lower()
        resultados = [r for r in registros if termino in r["nombre"].lower()]
        criterio = "ciudadano"
    elif opcion == "2":
        termino = input("  Barrio a buscar: ").strip().lower()
        resultados = [r for r in registros if termino in r["barrio"].lower()]
        criterio = "barrio"
    else:
        print("  ⚠ Opción inválida.")
        pausar()
        return

    print()
    if not resultados:
        print(f"  No se encontraron registros para '{termino}'.")
    else:
        print(f"  {len(resultados)} resultado(s) encontrado(s) para '{termino}':\n")
        print(f"  {'#':<4} {'Fecha':<17} {'Ciudadano':<18} {'Barrio':<14} {'Material':<22} {'kg':>5}")
        linea()
        total_kg = 0
        for r in resultados:
            print(f"  {r['id']:<4} {r['fecha']:<17} {r['nombre']:<18} {r['barrio']:<14} {r['material']:<22} {r['cantidad_kg']:>5.1f}")
            total_kg += r["cantidad_kg"]
        linea()
        print(f"  Total reciclado: {total_kg:.2f} kg")

    pausar()


# ─────────────────────────────────────────────
#  MÓDULO 5 — ELIMINAR REGISTRO
# ─────────────────────────────────────────────
def eliminar_registro():
    encabezado("ELIMINAR REGISTRO")

    if not registros:
        print("  No hay registros para eliminar.")
        pausar()
        return

    try:
        id_eliminar = int(input("  Ingresa el # ID del registro a eliminar: ").strip())
    except ValueError:
        print("  ⚠ ID inválido.")
        pausar()
        return

    encontrado = None
    for r in registros:
        if r["id"] == id_eliminar:
            encontrado = r
            break

    if not encontrado:
        print(f"  ⚠ No se encontró un registro con ID #{id_eliminar}.")
        pausar()
        return

    print()
    print(f"  Registro encontrado:")
    print(f"    Ciudadano : {encontrado['nombre']}")
    print(f"    Material  : {encontrado['material']}")
    print(f"    Cantidad  : {encontrado['cantidad_kg']} kg")
    print(f"    Fecha     : {encontrado['fecha']}")
    print()

    confirmacion = input("  ¿Confirmas la eliminación? (s/n): ").strip().lower()
    if confirmacion == "s":
        registros.remove(encontrado)
        guardar_datos()
        print("  ✅ Registro eliminado correctamente.")
    else:
        print("  Operación cancelada.")

    pausar()


# ─────────────────────────────────────────────
#  MENÚ PRINCIPAL
# ─────────────────────────────────────────────
def menu_principal():
    cargar_datos()

    while True:
        encabezado("SISTEMA DE RECICLAJE COMUNITARIO")
        print("  Menú Principal")
        print()
        print("    [1]  Registrar nuevo reciclaje")
        print("    [2]  Ver todos los registros")
        print("    [3]  Estadísticas por material")
        print("    [4]  Buscar por ciudadano o barrio")
        print("    [5]  Eliminar registro")
        print("    [0]  Salir")
        print()
        linea()

        opcion = input("  Selecciona una opción: ").strip()

        if opcion == "1":
            registrar_reciclaje()
        elif opcion == "2":
            ver_registros()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            buscar_registros()
        elif opcion == "5":
            eliminar_registro()
        elif opcion == "0":
            limpiar_pantalla()
            print("\n  ♻️  ¡Gracias por cuidar el planeta! Hasta pronto.\n")
            break
        else:
            print("  ⚠ Opción no válida. Intenta de nuevo.")
            pausar()


# ─────────────────────────────────────────────
#  PUNTO DE ENTRADA
# ─────────────────────────────────────────────
if __name__ == "__main__":
    menu_principal()
