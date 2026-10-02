import os
import psycopg2

conn = psycopg2.connect(
    host=os.getenv("PGHOST", "localhost"),
    port=os.getenv("PGPORT", "5432"),
    dbname=os.getenv("PGDATABASE", "postgres"),
    user=os.getenv("PGUSER", "postgres"),
    password=os.getenv("PGPASSWORD"),
)

query = """
SELECT
    pid,
    usename,
    datname,
    now() - xact_start AS transaction_age,
    state,
    query
FROM pg_stat_activity
WHERE xact_start IS NOT NULL
  AND now() - xact_start > interval '5 minutes'
ORDER BY transaction_age DESC;
"""

with conn:
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()

if not rows:
    print("No long-running transactions found.")
else:
    for row in rows:
        pid, user, database, age, state, query = row

        print(f"PID: {pid}")
        print(f"User: {user}")
        print(f"Database: {database}")
        print(f"Transaction age: {age}")
        print(f"State: {state}")
        print(f"Query: {query}")
        print("-" * 60)

conn.close()
