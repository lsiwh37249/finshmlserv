# finshmlserv

### Deploy
![deploy_image](https://github.com/user-attachments/assets/aa0556f8-1873-4adc-af03-69b0a1a69eb4)

### Run
- dev
- http://127.0.0.1:8000/docs
```bash
# unicorn --help
$ uvicorn src.finshmlserv.main:app --reload

```
- prd
```bash
# delete reload parameter
$ unicorn src.finshmlserv.main:app --host 0.0.0.0 --port 8949
```

- docker
```bash
$ sudo docker build -t fishmlserv:0.4.0 .
$ sudo docker run -d --name fmlserv-040 -p 8877:8765 fishmlserv:0.4.0
```

- docker 안으로 접근
```bash
# docker 컨테이너 안으로...
$ sudo docker exec -it fml071 bash

# docker 컨테이너 안에서 ...
root@7244097edb66:/code# cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 12 (bookworm)"
NAME="Debian GNU/Linux"
VERSION_ID="12"
VERSION="12 (bookworm)"
VERSION_CODENAME=bookworm
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"

# 다시 호스트OS(WSL) 로 exit
root@7244097edb66:/code# exit
```

- fly
```bash
$ fly launch --no-deploy
$ flyctl launch --name mariofish
$ flyctl scale memory 256
$ flyctl deploy
```
