from influxdb import InfluxDBClient


client = InfluxDBClient(host='localhost',port=8086,database='telegraf')
result = client.query('select usage_system from cpu limit 50;')
for i in result:
    for s in i:
        print s