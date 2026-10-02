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
    blocked.pid AS blocked_pid,
    blocked.usename AS blocked_user,
    blocking.pid AS blocking_pid,
    blocking.usename AS blocking_user,
    blocked.query AS blocked_query,
    blocking.query AS blocking_query
FROM pg_stat_activity blocked
JOIN pg_stat_activity blocking
    ON blocking.pid = ANY(pg_blocking_pids(blocked.pid))
ORDER BY blocked.pid;
"""

with conn:
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()

if not rows:
    print("No blocking sessions found.")
else:
    for row in rows:
        (
            blocked_pid,
            blocked_user,
            blocking_pid,
            blocking_user,
            blocked_query,
            blocking_query,
        ) = row

        print(f"Blocked PID: {blocked_pid}")
        print(f"Blocked user: {blocked_user}")
        print(f"Blocking PID: {blocking_pid}")
        print(f"Blocking user: {blocking_user}")
        print(f"Blocked query: {blocked_query}")
        print(f"Blocking query: {blocking_query}")
        print("-" * 60)

conn.close()
