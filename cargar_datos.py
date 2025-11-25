import csv
import psycopg2
from psycopg2.extras import execute_values

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "foodtrucks_db",
    "user": "postgres",
    "password": "****",
}

CSV_PATH = "C:\\Users\\Maxde\\Documents\\DS Course\\M2\\FoodTrucks-DB\\data\\orders.csv"


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def ensure_failed_table(cur):
    """
    Crea la tabla failed_orders si no existe.
    Guarda el id, la fila cruda y el mensaje de error.
    """
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS failed_orders (
            id SERIAL PRIMARY KEY,
            source_table VARCHAR(50) NOT NULL,
            raw_data TEXT NOT NULL,
            error_msg TEXT NOT NULL
        );
        """
    )


def load_orders():
    conn = get_connection()
    cur = conn.cursor()

    ensure_failed_table(cur)
    conn.commit()

    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        ok_rows = []
        failed_rows = []

        for row in reader:
            try:
                ok_rows.append(
                    (
                        int(row["order_id"]),
                        int(row["foodtruck_id"]),
                        row["order_date"],
                        row["status"],
                        float(row["total"]),
                    )
                )
            except Exception as e:
                failed_rows.append(
                    (
                        "orders",
                        str(row),
                        str(e),
                    )
                )

    # Inserción de filas válidas
    if ok_rows:
        execute_values(
            cur,
            """
            INSERT INTO Orders (order_id, foodtruck_id, order_date, status, total)
            VALUES %s
            ON CONFLICT (order_id) DO NOTHING;
            """,
            ok_rows,
        )

    # Registro de errores
    if failed_rows:
        execute_values(
            cur,
            """
            INSERT INTO failed_orders (source_table, raw_data, error_msg)
            VALUES %s;
            """,
            failed_rows,
        )

    conn.commit()
    cur.close()
    conn.close()

    print(f"Filas correctas insertadas: {len(ok_rows)}")
    print(f"Filas con error registradas: {len(failed_rows)}")


if __name__ == "__main__":
    load_orders()