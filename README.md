
# Rdp Traffic Light
This project is trace RDP connactions chain and show the first client in every chain.

# Project components:
- **Sqlite3**:

[Docker/SqliteBrowse](https://hub.docker.com/r/linuxserver/sqlitebrowser)

```console
docker run -d \
  --name=sqlitebrowser \
  -e PUID=1000 \
  -e PGID=1000 \
  -p 3000:3000 \
  -v /path/to/config:/config \
  lscr.io/linuxserver/sqlitebrowser:latest
```

- **RDTL.py**:
Program source file.
- **Sys.py**:
System and network modules.
- **db.py**:
Database querys, configuration and GUI modules.

[Dependencies](https://github.com/DannyVol/Rdp_traffic_light/wiki/Dependencies)
