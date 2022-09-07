## Systemd

```
$ sudo cp random-wiki.py /opt
$ sudo cp random-wiki.service /etc/systemd/system
$ systemctl start random-wiki
$ journalctl -f -u random-wiki
```

## Docker

```
$ docker build -t random-wiki-image .
...
$ docker run -d --name random-wiki-container random-wiki-image
...
$ docker logs -f inspiring_mayer
```
