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

