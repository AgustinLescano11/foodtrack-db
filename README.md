# Homework L1 M2

# FoodTrack – Esquema Relacional y Automatización 

Este proyecto desarrolla el esquema relacional inicial de **FoodTrack**, una plataforma para gestionar operaciones de foodtrucks en distintos puntos de una ciudad.

El objetivo es simular un entorno de desarrollo profesional integrando:

- Diseño del modelo relacional.  
- Creación del esquema en PostgreSQL utilizando DBeaver como cliente.  
- Carga y validación de datos desde archivos CSV.  
- Control de versiones con Git y GitHub.  
- Automatización opcional de carga con Python.

---

## Estructura del repositorio

```
FoodTrucks-DB/
│
├── data/                      
│   ├── foodtrucks.csv
│   ├── products.csv
│   ├── orders.csv
│   ├── order_items.csv
│   └── locations.csv
│
├── scripts/
│   └── 01_create_tables.sql   
│
├── cargar_datos.py            
├── generar_ordenes.py         
│
└── README.md
```

---

## Modelo Relacional

### **FOODTRUCKS**
- `foodtruck_id` (PK)  
- `name`  
- `cuisine_type`  
- `city`  

### **PRODUCTS**
- `product_id` (PK)  
- `foodtruck_id` (FK → foodtrucks.foodtruck_id)  
- `name`  
- `price`  
- `stock`

### **ORDERS**
- `order_id` (PK)  
- `foodtruck_id` (FK → foodtrucks.foodtruck_id)  
- `order_date`  
- `status`  
- `total`

### **ORDER_ITEMS**
- `order_item_id` (PK)  
- `order_id` (FK → orders.order_id)  
- `product_id` (FK → products.product_id)  
- `quantity`

### **LOCATIONS**
- `location_id` (PK)  
- `foodtruck_id` (FK → foodtrucks.foodtruck_id)  
- `location_date`  
- `zone`

---

## Relaciones Principales

- Un **foodtruck** tiene muchos **productos**.  
- Un **foodtruck** tiene muchos **pedidos**.  
- Un **foodtruck** puede registrarse en muchas **ubicaciones**.  
- Un **pedido** contiene muchos **items**.  
- Un **producto** puede aparecer en muchos **items de pedido**.

---

## Creación del esquema SQL

El archivo `scripts/01_create_tables.sql` contiene el DDL con todas las tablas, claves primarias, foráneas y restricciones necesarias para el modelo.

Las tablas se crearon en PostgreSQL utilizando DBeaver como cliente.

---

## Carga de datos desde CSV

Los CSV provistos en la consigna se importaron a PostgreSQL mediante:

- El asistente de importación de DBeaver (IMPORT DATA).  
- Verificación posterior con consultas `SELECT COUNT(*)` para asegurar consistencia.  

---

## Automatización con Python (Extra)

Se incluyen dos scripts opcionales:

### `cargar_datos.py`
Carga programática del archivo `orders.csv` en la tabla `orders` utilizando `psycopg2`.

- Lee todos los registros del CSV.
- Inserta filas válidas.
- Evita duplicados mediante `ON CONFLICT DO NOTHING`.
- Registra errores en una tabla auxiliar (`failed_orders`) si fuera necesario.

### `generar_ordenes.py`
Genera órdenes nuevas de forma automática:

- Obtiene `MAX(order_id)` de la tabla.
- Crea 5 órdenes aleatorias (`foodtruck_id`, fecha, estatus y total).
- Inserta todas en la tabla `orders`.

Esto demuestra carga programática y manipulación dinámica del modelo.

---

## Instrucciones de ejecución

### Crear el esquema
Ejecutar en DBeaver:

```
scripts/01_create_tables.sql
```

### Importar CSV
Desde DBeaver:  
**Right click en tabla → Import Data → CSV**

### Ejecutar scripts Python

```
python cargar_datos.py
python generar_ordenes.py
```

---

