# PostgreSQL Automation

Small automation scripts for PostgreSQL administration and health checks.

## Scripts

- replication lag check
- long-running transaction check
- blocking session check

## Planned

- WAL usage check
- connection usage check
- database size check
- backup status check
- Patroni cluster health check
- basic PostgreSQL health check

## Languages

- Python
- Bash

## Usage

Install dependencies:

'pip install -r requirements.txt'

Set PostgreSQL connection variables:

'PGHOST'
'PGPORT'
'PGDATABASE'
'PGUSER'
'PGPASSWORD'

Run a script:

'python check_replication_lag.py'

## Goal

Automate repetitive PostgreSQL checks and turn manual DBA tasks into simple reusable scripts.
