
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


[Dependencies](https://github.com/DannyVol/Rdp_traffic_light/wiki/Dependencies)
