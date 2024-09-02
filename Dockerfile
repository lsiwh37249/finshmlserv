# FROM python:3.8
FROM python:3.11.9-alpine3.20
 
WORKDIR /code

#COPY . /code/
COPY src/finshmlserv/main.py /code/
COPY requirements.txt /code/

COPY ./requirements.txt ./code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#RUN pip install git+http://<MY_PIP_GITHUB_URL>
 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
