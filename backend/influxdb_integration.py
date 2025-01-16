
# InfluxDB Integration
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

# PostgreSQL Integration
import psycopg2

# CockroachDB Integration
from sqlalchemy import create_engine

# Initialize InfluxDB client
influx_client = influxdb_client.InfluxDBClient(
    url="http://localhost:8086",
    token="your-influxdb-token",
    org="your-org"
)
write_api = influx_client.write_api(write_options=SYNCHRONOUS)

# PostgreSQL connection
def connect_postgresql():
    connection = psycopg2.connect(
        dbname="your-dbname",
        user="your-username",
        password="your-password",
        host="your-host",
        port="your-port"
    )
    return connection

# CockroachDB connection
def connect_cockroachdb():
    engine = create_engine(
        "cockroachdb://username:password@host:port/defaultdb",
        echo=True
    )
    return engine

# Example usage for InfluxDB
def write_to_influxdb(bucket, measurement, fields, tags=None):
    point = {
        "measurement": measurement,
        "tags": tags or {},
        "fields": fields
    }
    write_api.write(bucket=bucket, record=point)

# Example usage for PostgreSQL
def write_to_postgresql(table, data):
    connection = connect_postgresql()
    cursor = connection.cursor()
    query = f"INSERT INTO {table} (columns) VALUES (%s, %s)"
    cursor.executemany(query, data)
    connection.commit()
    cursor.close()
    connection.close()

# Example usage for CockroachDB
def write_to_cockroachdb(table, data):
    engine = connect_cockroachdb()
    with engine.connect() as connection:
        query = f"INSERT INTO {table} (columns) VALUES (:value1, :value2)"
        connection.execute(query, data)
