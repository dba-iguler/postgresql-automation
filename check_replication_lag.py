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
    application_name,
    client_addr,
    state,
    write_lag,
    flush_lag,
    replay_lag
FROM pg_stat_replication;
"""

with conn:
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()

if not rows:
    print("No replicas found.")
else:
    for row in rows:
        application_name, client_addr, state, write_lag, flush_lag, replay_lag = row

        print(f"Replica: {application_name}")
        print(f"Client: {client_addr}")
        print(f"State: {state}")
        print(f"Write lag: {write_lag}")
        print(f"Flush lag: {flush_lag}")
        print(f"Replay lag: {replay_lag}")
        print("-" * 40)

conn.close()
