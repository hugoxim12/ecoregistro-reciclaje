# ♻️ Sistema de Registro de Reciclaje Comunitario

## Nombre del Proyecto
**EcoRegistro** — Sistema de Registro de Reciclaje Comunitario

## Nombre Estudiante
Hugo Imbaquingo

## Objetivo del Sistema
Desarrollar una solución informática en Python que permita registrar, consultar y analizar el reciclaje realizado por ciudadanos de una comunidad, contribuyendo a la conciencia ambiental mediante el seguimiento del impacto ecológico generado.

---

## Descripción de Funcionalidades

| # | Funcionalidad | Descripción |
|---|---------------|-------------|
| 1 | **Registrar reciclaje** | Ingresa un nuevo registro con nombre del ciudadano, barrio, tipo de material y cantidad en kg |
| 2 | **Ver historial** | Muestra todos los registros guardados en formato tabular |
| 3 | **Estadísticas** | Calcula totales por tipo de material, porcentajes y CO₂ ahorrado |
| 4 | **Buscar** | Filtra registros por nombre de ciudadano o barrio |
| 5 | **Eliminar** | Permite eliminar un registro específico por su ID |
| 6 | **Persistencia** | Los datos se guardan en un archivo JSON local entre sesiones |

---

## Materiales Soportados

- 🧴 Plástico
- 🫙 Vidrio
- 📦 Papel / Cartón
- 🥫 Metal / Lata
- 🌿 Orgánico
- 💻 Electrónico (E-waste)

---

## Cómo Ejecutar

### Requisitos
- Python 3.7 o superior
- No requiere librerías externas

### Ejecución
```bash
python3 reciclaje.py
```

---

## Estructura del Proyecto

```
reciclaje_comunitario/
├── reciclaje.py              # Código principal del sistema
├── datos_reciclaje.json      # Datos persistentes (se genera automáticamente)
├── README.md                 # Este archivo
├── docs/
│   └── documento_proyecto.md # Documento académico del proyecto
└── diagramas/
    ├── caso_de_uso.png       # Diagrama de casos de uso
    ├── flujo_registro.png    # Diagrama de flujo — registrar reciclaje
    └── arquitectura.png      # Diagrama de arquitectura del sistema
```

---

## Impacto Tecnológico y Social

Este sistema responde a la necesidad de digitalizar el seguimiento ambiental en comunidades con recursos limitados. Permite visibilizar el esfuerzo colectivo de reciclaje, motivar la participación ciudadana mediante datos concretos, y sentar la base para políticas públicas basadas en información real.

---

## Fecha
Junio 2026
