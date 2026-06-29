# DOCUMENTO DEL PROYECTO INTEGRADOR

**Asignatura:** Logica de Programación Programación  
**Proyecto:** EcoRegistro — Sistema de Registro de Reciclaje Comunitario  
**Estudiante:** Hugo Imbaquingo
**Fecha:** 26 Junio 2026

---

## 1. Introducción

Las tecnologías de la información han transformado la manera en que las sociedades gestionan sus recursos y problemáticas ambientales. En la actualidad, existe una brecha significativa entre la voluntad ciudadana de reciclar y la capacidad institucional para medir, registrar y analizar ese esfuerzo colectivo.

El presente proyecto propone el desarrollo de **EcoRegistro**, un sistema de software en Python que digitaliza el registro de reciclaje comunitario, permitiendo cuantificar el impacto ambiental real generado por los ciudadanos de un barrio o municipio.

---

## 2. Descripción del Problema

En muchas comunidades de Ecuador y Latinoamérica, el reciclaje se realiza de manera informal y sin ningún tipo de registro. Esto genera los siguientes problemas:

- **Invisibilidad del impacto:** No se puede medir cuánto material se recicla ni el CO₂ que se evita emitir.
- **Falta de motivación:** Sin datos concretos, los ciudadanos no perciben el resultado de sus acciones.
- **Gestión deficiente:** Los gestores municipales no cuentan con información para tomar decisiones.
- **Desigualdad de participación:** No se identifican qué barrios o sectores participan más.

**EcoRegistro** resuelve este problema ofreciendo una herramienta simple, accesible y funcional para registrar y analizar el reciclaje comunitario.

---

## 3. Relación con los Contenidos de la Asignatura

| Unidad | Tema | Aplicación en el Proyecto |
|--------|------|---------------------------|
| **Unidad 1** | Fundamentos de programación y diagramas | Diagramas de casos de uso, flujo y arquitectura del sistema |
| **Unidad 2** | Introducción al desarrollo de software | Configuración de GitHub, estructura modular del código, entorno de desarrollo |
| **Unidad 3** | Estructuras lógicas | Uso de condicionales (`if/elif/else`) para validar entradas y controlar el menú; bucles `while` y `for` para iteración de registros |
| **Unidad 4** | Técnicas de programación funcional | Código organizado en funciones con responsabilidad única: `registrar_reciclaje()`, `ver_estadisticas()`, `buscar_registros()`, etc. |

---

## 4. Explicación del Sistema Desarrollado

### 4.1 Arquitectura General

El sistema sigue una arquitectura de **tres capas lógicas**:

1. **Capa de Presentación:** Menú de consola con interfaz de texto clara y estructurada.
2. **Capa de Lógica de Negocio:** Funciones que procesan las operaciones (registrar, buscar, calcular estadísticas).
3. **Capa de Datos:** Persistencia mediante archivo JSON local (`datos_reciclaje.json`).

### 4.2 Funcionalidades Principales

**Registro de reciclaje**  
El usuario ingresa: nombre del ciudadano, barrio, tipo de material (entre 6 opciones) y cantidad en kilogramos. El sistema valida cada entrada con bucles `while` y calcula automáticamente el CO₂ ahorrado usando factores de conversión estándar.

**Estadísticas por material**  
El sistema agrupa los registros por tipo de material, calcula totales, porcentajes y genera una barra de progreso visual en consola. Traduce el CO₂ ahorrado a equivalentes comprensibles (árboles plantados).

**Búsqueda**  
Permite filtrar registros por nombre de ciudadano o barrio usando comparación de cadenas con `.lower()` para búsqueda insensible a mayúsculas.

**Persistencia**  
Los datos se guardan y cargan automáticamente en formato JSON, garantizando que la información no se pierde al cerrar el programa.

### 4.3 Estructuras Lógicas Utilizadas

```python
# Condicional para validar opción del menú
if opcion == "1":
    registrar_reciclaje()
elif opcion == "2":
    ver_registros()
...

# Bucle para validar entrada del usuario
while True:
    cantidad = float(input("Cantidad (kg): "))
    if cantidad > 0:
        break

# Bucle para recorrer registros y calcular estadísticas
for r in registros:
    totales[r["material"]]["cantidad"] += r["cantidad_kg"]
```

---

## 5. Reflexión sobre el Impacto de la Tecnología

El desarrollo de este proyecto permite reflexionar sobre varios aspectos del impacto tecnológico en la sociedad:

**Democratización de la tecnología:** Una solución en Python de consola puede ejecutarse en cualquier computador sin necesidad de conexión a internet ni hardware especializado, lo que la hace accesible para comunidades con recursos limitados.

**Datos como herramienta de cambio social:** Al cuantificar el reciclaje, la tecnología convierte una acción individual en un dato colectivo. Este dato tiene el poder de informar políticas públicas, motivar a más ciudadanos y medir el progreso hacia metas ambientales.

**Limitaciones actuales:** El sistema opera localmente en un solo equipo. Para escalar a nivel comunitario real, se requeriría una base de datos compartida, acceso web o móvil, y mecanismos de autenticación. Estas son las proyecciones naturales del proyecto.

**El rol del programador:** Este proyecto evidencia que un desarrollador no solo escribe código — identifica problemas sociales reales y propone soluciones técnicas concretas. La programación es una herramienta de transformación social.

---

## 6. Conclusiones

- Se desarrolló un sistema funcional en Python que resuelve una necesidad real de gestión ambiental comunitaria.
- El proyecto integró los contenidos de las cuatro unidades: diseño con diagramas, configuración de entorno con GitHub, estructuras lógicas (condicionales y bucles) y organización funcional del código.
- La solución demuestra que tecnologías simples, bien aplicadas, pueden generar un impacto significativo en comunidades reales.
- El sistema tiene potencial de escalabilidad hacia una aplicación web o móvil con base de datos en la nube.

---

## 7. Bibliografía

- Van Rossum, G. (2023). *Python Documentation*. Python Software Foundation. https://docs.python.org
- Pressman, R. (2014). *Ingeniería del Software: Un enfoque práctico* (7.ª ed.). McGraw-Hill.
- IPCC (2021). *Climate Change 2021: The Physical Science Basis*. Intergovernmental Panel on Climate Change.
- Ministerio del Ambiente Ecuador (2022). *Guía de gestión de residuos sólidos urbanos*.
