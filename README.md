
# Rdp Traffic Light
This project is trace RDP connactions chain and show the first client in every chain.

# Project components:
- **influxdb:2.0**:

[Source](https://github.com/influxdata/influxdb/tree/2.0)

[Dockerfile](https://github.com/influxdata/influxdata-docker/tree/influxdb-2.0/influxdb/2.0)

- **influxdb:2.0 on docker**
```console
docker run -p 8086:8086 \
      influxdb:2.0
```

- **RDTL.py**:
Program source file.
- **Sys.py**:
System and network modules.
- **db.py**:
Database querys, configuration and GUI modules.

[Dependencies](https://github.com/DannyVol/Rdp_traffic_light/wiki/Dependencies)
