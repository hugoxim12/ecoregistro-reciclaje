"""
=======================================================
  ECOREGISTRO — SISTEMA DE REGISTRO DE RECICLAJE COMUNITARIO
=======================================================
  Descripción:
    Sistema desarrollado en Python que permite registrar,
    consultar y analizar el reciclaje realizado por ciudadanos
    de una comunidad, calculando el impacto ambiental en CO₂.

  Autor   : [Tu Nombre Completo]
  Materia : Fundamentos de Programación
  Fecha   : Junio 2025
  Versión : 2.0

  Unidades integradas:
    - Unidad 1: Diagramas de funcionalidad y arquitectura
    - Unidad 2: Entorno de desarrollo y GitHub
    - Unidad 3: Estructuras lógicas (condicionales y bucles)
    - Unidad 4: Organización funcional del código
=======================================================
"""

# ─────────────────────────────────────────────────────
#  IMPORTACIÓN DE MÓDULOS
#  - os    : para limpiar la pantalla según el sistema operativo
#  - json  : para guardar y cargar datos en formato JSON
#  - datetime : para registrar la fecha y hora de cada reciclaje
# ─────────────────────────────────────────────────────
import os
import json
from datetime import datetime


# ─────────────────────────────────────────────────────
#  CONSTANTES Y CONFIGURACIÓN GLOBAL
#
#  registros      : lista principal donde se almacenan todos
#                   los registros durante la ejecución
#  ARCHIVO_DATOS  : nombre del archivo JSON donde se persisten
#                   los datos entre sesiones
#  MATERIALES_VALIDOS : diccionario que mapea opciones del menú
#                       con el nombre real del material
#  IMPACTO_CO2    : factor de conversión kg CO₂ ahorrado
#                   por cada kg de material reciclado
# ─────────────────────────────────────────────────────
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

# Fuente: estimaciones estándar de ciclo de vida de materiales reciclados
IMPACTO_CO2 = {
    "Plástico":             1.5,
    "Vidrio":               0.3,
    "Papel / Cartón":       1.0,
    "Metal / Lata":         4.0,
    "Orgánico":             0.5,
    "Electrónico (E-waste)": 2.0
}


# ─────────────────────────────────────────────────────
#  FUNCIONES DE UTILIDAD
#  Estas funciones no tienen lógica de negocio.
#  Solo ayudan a mostrar la interfaz de manera limpia.
# ─────────────────────────────────────────────────────

def limpiar_pantalla():
    """Limpia la consola. Usa 'cls' en Windows y 'clear' en Linux/Mac."""
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    """Pausa la ejecución hasta que el usuario presione Enter."""
    input("\n  Presiona ENTER para continuar...")


def linea(caracter="─", largo=54):
    """Imprime una línea decorativa de separación."""
    print(f"  {caracter * largo}")


def encabezado(titulo):
    """Limpia la pantalla y muestra un encabezado con el título dado."""
    limpiar_pantalla()
    linea("═")
    print(f"  ♻️  {titulo}")
    linea("═")
    print()


# ─────────────────────────────────────────────────────
#  FUNCIONES DE PERSISTENCIA DE DATOS
#  Manejan la lectura y escritura del archivo JSON.
#  Esto es la "capa de datos" de la arquitectura.
# ─────────────────────────────────────────────────────

def cargar_datos():
    """
    Carga los registros guardados desde el archivo JSON.
    Si el archivo no existe o está dañado, inicia con lista vacía.
    Se llama una sola vez al arrancar el programa.
    """
    global registros
    if os.path.exists(ARCHIVO_DATOS):
        try:
            with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
                registros = json.load(archivo)
            print(f"  ✅ {len(registros)} registro(s) cargado(s) desde {ARCHIVO_DATOS}")
        except (json.JSONDecodeError, IOError):
            # Si el archivo está corrupto, se inicia desde cero
            registros = []
            print("  ⚠ No se pudo leer el archivo de datos. Iniciando desde cero.")


def guardar_datos():
    """
    Guarda la lista de registros en el archivo JSON.
    Se llama cada vez que se agrega o elimina un registro,
    garantizando que los datos no se pierdan al cerrar el programa.
    """
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        # indent=2 hace que el JSON sea legible para humanos
        json.dump(registros, archivo, ensure_ascii=False, indent=2)


# ─────────────────────────────────────────────────────
#  MÓDULO 1 — REGISTRAR NUEVO RECICLAJE
#
#  Estructura lógica utilizada:
#    - Bucles while: para repetir la solicitud hasta obtener
#      un valor válido (validación de entradas)
#    - Condicionales if: para verificar que los datos sean correctos
#    - Diccionarios: para almacenar cada registro como objeto
# ─────────────────────────────────────────────────────

def registrar_reciclaje():
    """
    Solicita al usuario los datos de un nuevo registro de reciclaje:
    nombre del ciudadano, barrio, tipo de material y cantidad en kg.
    Calcula el CO₂ ahorrado y guarda el registro en el archivo JSON.
    """
    encabezado("REGISTRAR NUEVO RECICLAJE")

    # ── Validación del nombre ──────────────────────────
    # Usamos un bucle while para repetir la solicitud
    # hasta que el usuario ingrese un nombre no vacío
    while True:
        nombre = input("  Nombre del ciudadano: ").strip()
        if nombre:
            break  # Sale del bucle si el nombre es válido
        print("  ⚠ El nombre no puede estar vacío. Intenta de nuevo.")

    # ── Validación del barrio ──────────────────────────
    while True:
        barrio = input("  Barrio o sector: ").strip()
        if barrio:
            break
        print("  ⚠ El barrio no puede estar vacío. Intenta de nuevo.")

    # ── Selección del tipo de material ────────────────
    # Mostramos las opciones disponibles con un bucle for
    print()
    print("  Tipos de material disponibles:")
    for clave, nombre_material in MATERIALES_VALIDOS.items():
        # Muestra el factor de CO₂ junto a cada material
        co2 = IMPACTO_CO2[nombre_material]
        print(f"    [{clave}] {nombre_material:<22} (ahorra {co2} kg CO₂ por kg reciclado)")
    print()

    # Validamos que la opción esté entre las válidas
    while True:
        opcion = input("  Selecciona el tipo de material [1-6]: ").strip()
        if opcion in MATERIALES_VALIDOS:
            material = MATERIALES_VALIDOS[opcion]
            break
        print("  ⚠ Opción inválida. Elige un número del 1 al 6.")

    # ── Validación de la cantidad ──────────────────────
    # Usamos try/except dentro del bucle para capturar
    # errores cuando el usuario escribe texto en vez de número
    while True:
        try:
            cantidad = float(input("  Cantidad reciclada (kg): ").strip())
            if cantidad > 0:
                break  # Valor válido: sale del bucle
            else:
                print("  ⚠ La cantidad debe ser mayor a 0.")
        except ValueError:
            # Se ejecuta si el usuario escribe letras en vez de números
            print("  ⚠ Ingresa un número válido (ejemplo: 3.5)")

    # ── Crear el registro como diccionario ────────────
    # Calculamos el CO₂ multiplicando cantidad × factor del material
    co2_ahorrado = round(cantidad * IMPACTO_CO2[material], 3)

    nuevo_registro = {
        "id":             len(registros) + 1,
        "fecha":          datetime.now().strftime("%Y-%m-%d %H:%M"),
        "nombre":         nombre,
        "barrio":         barrio,
        "material":       material,
        "cantidad_kg":    cantidad,
        "co2_ahorrado_kg": co2_ahorrado
    }

    # Agregamos el registro a la lista y guardamos en JSON
    registros.append(nuevo_registro)
    guardar_datos()

    # ── Confirmación al usuario ────────────────────────
    print()
    linea()
    print(f"  ✅ Registro #{nuevo_registro['id']} guardado exitosamente.")
    print(f"     Ciudadano : {nombre} ({barrio})")
    print(f"     Material  : {material}")
    print(f"     Cantidad  : {cantidad} kg")
    print(f"     CO₂ ahorrado: {co2_ahorrado} kg")
    linea()
    pausar()


# ─────────────────────────────────────────────────────
#  MÓDULO 2 — VER TODOS LOS REGISTROS
#
#  Estructura lógica utilizada:
#    - Condicional if: verifica si hay registros antes de mostrar
#    - Bucle for: recorre la lista para imprimir cada registro
# ─────────────────────────────────────────────────────

def ver_registros():
    """
    Muestra todos los registros guardados en formato de tabla.
    Si no hay registros, informa al usuario.
    """
    encabezado("HISTORIAL COMPLETO DE REGISTROS")

    # Condicional: si la lista está vacía no hay nada que mostrar
    if not registros:
        print("  No hay registros guardados aún.")
        print("  Usa la opción [1] para registrar el primer reciclaje.")
        pausar()
        return

    # Encabezado de la tabla
    print(f"  {'#':<4} {'Fecha':<17} {'Ciudadano':<18} {'Barrio':<14} {'Material':<22} {'kg':>5} {'CO₂(kg)':>9}")
    linea()

    # Bucle for: recorre cada registro e imprime sus datos
    for r in registros:
        print(f"  {r['id']:<4} {r['fecha']:<17} {r['nombre']:<18} {r['barrio']:<14} {r['material']:<22} {r['cantidad_kg']:>5.1f} {r['co2_ahorrado_kg']:>9.3f}")

    linea()
    print(f"  Total de registros: {len(registros)}")
    pausar()


# ─────────────────────────────────────────────────────
#  MÓDULO 3 — ESTADÍSTICAS POR MATERIAL
#
#  Estructura lógica utilizada:
#    - Bucle for: recorre registros para acumular totales
#    - Diccionario: agrupa datos por tipo de material
#    - Condicional if: evita división por cero al calcular %
#    - Función sorted(): ordena de mayor a menor cantidad
# ─────────────────────────────────────────────────────

def ver_estadisticas():
    """
    Calcula y muestra estadísticas agrupadas por tipo de material:
    cantidad total, CO₂ ahorrado, porcentaje del total y barra visual.
    También muestra el equivalente en árboles plantados.
    """
    encabezado("ESTADÍSTICAS POR MATERIAL")

    if not registros:
        print("  No hay datos suficientes para calcular estadísticas.")
        pausar()
        return

    # ── Acumular totales por material ─────────────────
    # Usamos un diccionario vacío que vamos llenando con un bucle for
    totales = {}

    for r in registros:
        material = r["material"]
        # Si el material no está en el diccionario, lo inicializamos
        if material not in totales:
            totales[material] = {"cantidad": 0.0, "co2": 0.0, "veces": 0}
        # Sumamos los valores al material correspondiente
        totales[material]["cantidad"] += r["cantidad_kg"]
        totales[material]["co2"]      += r["co2_ahorrado_kg"]
        totales[material]["veces"]    += 1

    # Calculamos los totales generales
    total_kg  = sum(v["cantidad"] for v in totales.values())
    total_co2 = sum(v["co2"]      for v in totales.values())

    # ── Mostrar tabla de estadísticas ─────────────────
    print(f"  {'Material':<22} {'Veces':>6} {'Total kg':>10} {'CO₂ ahorr.':>12} {'% total':>8}  Barra")
    linea()

    # sorted() ordena el diccionario de mayor a menor cantidad
    for mat, datos in sorted(totales.items(), key=lambda x: x[1]["cantidad"], reverse=True):
        # Condicional: evita división por cero si total_kg fuera 0
        porcentaje = (datos["cantidad"] / total_kg * 100) if total_kg > 0 else 0
        # Barra visual: cada █ representa 5% del total
        barra = "█" * int(porcentaje / 5)
        print(f"  {mat:<22} {datos['veces']:>6} {datos['cantidad']:>10.2f} {datos['co2']:>12.2f} {porcentaje:>7.1f}%  {barra}")

    # ── Resumen final ──────────────────────────────────
    linea()
    print(f"  {'TOTAL GENERAL':<22} {len(registros):>6} {total_kg:>10.2f} {total_co2:>12.2f}")
    print()
    print(f"  🌱 CO₂ total evitado  : {total_co2:.2f} kg")
    # Un árbol adulto absorbe aproximadamente 21 kg de CO₂ al año
    print(f"  🌳 Equivale a plantar : {int(total_co2 / 21)} árbol(es) durante un año")
    pausar()


# ─────────────────────────────────────────────────────
#  MÓDULO 4 — BUSCAR REGISTROS
#
#  Estructura lógica utilizada:
#    - Condicional if/elif: selecciona el criterio de búsqueda
#    - List comprehension con if: filtra registros que coincidan
#    - Método .lower(): hace la búsqueda insensible a mayúsculas
# ─────────────────────────────────────────────────────

def buscar_registros():
    """
    Permite buscar registros filtrando por nombre del ciudadano
    o por barrio. La búsqueda no distingue mayúsculas de minúsculas.
    Muestra un resumen del total reciclado por el criterio buscado.
    """
    encabezado("BUSCAR REGISTROS")

    print("  Buscar por:")
    print("    [1] Nombre del ciudadano")
    print("    [2] Barrio o sector")
    print()

    opcion = input("  Elige una opción: ").strip()

    # Condicional if/elif para determinar el criterio de búsqueda
    if opcion == "1":
        termino = input("  Nombre a buscar: ").strip().lower()
        # List comprehension: filtra registros cuyo nombre contenga el término
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

    # Mostrar resultados
    print()
    if not resultados:
        print(f"  No se encontraron registros para '{termino}'.")
    else:
        print(f"  Se encontraron {len(resultados)} resultado(s) para '{termino}':\n")
        print(f"  {'#':<4} {'Fecha':<17} {'Ciudadano':<18} {'Barrio':<14} {'Material':<22} {'kg':>5}")
        linea()
        total_kg = 0
        for r in resultados:
            print(f"  {r['id']:<4} {r['fecha']:<17} {r['nombre']:<18} {r['barrio']:<14} {r['material']:<22} {r['cantidad_kg']:>5.1f}")
            total_kg += r["cantidad_kg"]
        linea()
        print(f"  Total reciclado por este {criterio}: {total_kg:.2f} kg")

    pausar()


# ─────────────────────────────────────────────────────
#  MÓDULO 5 — ELIMINAR REGISTRO
#
#  Estructura lógica utilizada:
#    - try/except: maneja el error si el ID no es un número
#    - Bucle for: busca el registro por su ID
#    - Condicional if: pide confirmación antes de eliminar
# ─────────────────────────────────────────────────────

def eliminar_registro():
    """
    Permite eliminar un registro específico ingresando su ID.
    Muestra los datos del registro encontrado y pide confirmación
    antes de eliminarlo definitivamente.
    """
    encabezado("ELIMINAR REGISTRO")

    if not registros:
        print("  No hay registros para eliminar.")
        pausar()
        return

    # Mostramos primero la lista para que el usuario sepa el ID
    print(f"  {'#':<4} {'Ciudadano':<18} {'Material':<22} {'kg':>5}")
    linea()
    for r in registros:
        print(f"  {r['id']:<4} {r['nombre']:<18} {r['material']:<22} {r['cantidad_kg']:>5.1f}")
    linea()
    print()

    # try/except: captura el error si el usuario escribe letras
    try:
        id_eliminar = int(input("  Ingresa el # ID del registro a eliminar: ").strip())
    except ValueError:
        print("  ⚠ Debes ingresar un número entero.")
        pausar()
        return

    # Bucle for: busca en la lista el registro con ese ID
    encontrado = None
    for r in registros:
        if r["id"] == id_eliminar:
            encontrado = r
            break  # Sale del bucle al encontrar el registro

    # Condicional: verifica si se encontró el registro
    if not encontrado:
        print(f"  ⚠ No existe un registro con ID #{id_eliminar}.")
        pausar()
        return

    # Muestra los datos y pide confirmación antes de eliminar
    print(f"\n  Registro a eliminar:")
    print(f"    Ciudadano : {encontrado['nombre']} ({encontrado['barrio']})")
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
        print("  Operación cancelada. El registro se conserva.")

    pausar()


# ─────────────────────────────────────────────────────
#  MENÚ PRINCIPAL
#
#  Estructura lógica utilizada:
#    - Bucle while True: mantiene el programa corriendo
#      hasta que el usuario elija salir (opción 0)
#    - Condicionales if/elif/else: dirigen al módulo correcto
#      según la opción elegida por el usuario
# ─────────────────────────────────────────────────────

def menu_principal():
    """
    Punto de control principal del programa.
    Muestra el menú, lee la opción del usuario y llama
    a la función correspondiente. El bucle while True
    mantiene el programa activo hasta que se elige salir.
    """
    # Cargamos los datos guardados al iniciar el programa
    cargar_datos()
    pausar()

    # Bucle principal: se repite indefinidamente hasta opción 0
    while True:
        encabezado("SISTEMA DE RECICLAJE COMUNITARIO — EcoRegistro")
        print("  Menú Principal\n")
        print("    [1]  Registrar nuevo reciclaje")
        print("    [2]  Ver todos los registros")
        print("    [3]  Estadísticas por material")
        print("    [4]  Buscar por ciudadano o barrio")
        print("    [5]  Eliminar registro")
        print("    [0]  Salir del sistema")
        print()
        linea()

        opcion = input("  Selecciona una opción: ").strip()

        # Estructura if/elif/else: dirige al módulo correcto
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
            # Salida limpia del programa
            limpiar_pantalla()
            print("\n  ♻️  ¡Gracias por contribuir al planeta! Hasta pronto.\n")
            break  # Rompe el bucle while y termina el programa
        else:
            print("  ⚠ Opción no válida. Elige un número del 0 al 5.")
            pausar()


# ─────────────────────────────────────────────────────
#  PUNTO DE ENTRADA DEL PROGRAMA
#
#  Esta condición verifica que el archivo se esté ejecutando
#  directamente (no importado como módulo desde otro archivo).
#  Es la práctica estándar en Python para iniciar programas.
# ─────────────────────────────────────────────────────
if __name__ == "__main__":
    menu_principal()
