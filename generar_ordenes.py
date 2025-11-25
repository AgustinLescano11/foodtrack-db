import random
from datetime import date, timedelta

import psycopg2
from psycopg2.extras import execute_values

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "foodtrucks_db",   
    "user": "postgres",         
    "password": "****",  
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def insertar_ordenes_random(n=5):
    conn = get_connection()
    cur = conn.cursor()

    # 1) Traer el máximo order_id actual para no pisar nada
    cur.execute("SELECT COALESCE(MAX(order_id), 0) FROM orders;")
    base_id = cur.fetchone()[0]

    # 2) Traer los foodtruck_id existentes para asignarlos al azar
    cur.execute("SELECT foodtruck_id FROM foodtrucks;")
    trucks = [row[0] for row in cur.fetchall()]

    if not trucks:
        raise ValueError("No hay foodtrucks en la tabla; no se pueden crear órdenes.")

    estados = ["entregado", "pendiente", "cancelado"]
    hoy = date.today()

    nuevas_ordenes = []

    for i in range(1, n + 1):
        order_id = base_id + i
        foodtruck_id = random.choice(trucks)
        order_date = hoy - timedelta(days=random.randint(0, 30))
        status = random.choice(estados)
        total = random.randint(50, 200)  

        nuevas_ordenes.append(
            (order_id, foodtruck_id, order_date, status, total)
        )

    # 3) Insertar todo de una
    execute_values(
        cur,
        """
        INSERT INTO orders (order_id, foodtruck_id, order_date, status, total)
        VALUES %s;
        """,
        nuevas_ordenes,
    )

    conn.commit()
    cur.close()
    conn.close()

    print(f"Se insertaron {len(nuevas_ordenes)} nuevas órdenes.")
    for o in nuevas_ordenes:
        print(o)


if __name__ == "__main__":
    insertar_ordenes_random(n=5)
