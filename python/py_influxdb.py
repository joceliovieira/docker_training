from datetime import datetime
import influxdb_client
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = ' --- INSERIR TOKEN ---'
org = " --- ORG --- "
bucket = " --- BUCKER ---"


with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
    query_api = client.query_api()
    query = 'from(bucket: "bucket")\
        |> range(start: -1h)\
        |> filter(fn: (r) => r["host"] == "host1")'
    result = query_api.query(org=org, query=query)
    results = []
    for table in result:
        for record in table.records:
            results.append((record.get_field(), record.get_value()))
    print(results)
    client.close()
    print("fim")


with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
    write_api = client.write_api(write_options=SYNCHRONOUS)
    point = Point("mem") \
        .tag("host", "host1") \
        .field("used_percent", 1045.5) \
        .time(datetime.utcnow(), WritePrecision.NS)
    write_api.write(bucket, org, point)

with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
    query_api = client.query_api()
    query = 'from(bucket: "bucket")\
        |> range(start: -1h)\
        |> filter(fn: (r) => r["host"] == "host1")'
    result = query_api.query(org=org, query=query)
    results = []
    for table in result:
        for record in table.records:
            results.append((record.get_field(), record.get_value()))
    print(results)
    client.close()
    print("fim")