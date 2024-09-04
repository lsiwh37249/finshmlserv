FROM lsiwh37249/finshmlserv:0.8.5
#FROM datamario24/python311scikitlearn-fastapi:1.0.0
#FROM python:3.8
#FROM python:3.11.9-alpine3.20
 
WORKDIR /code

#COPY . /code/
COPY src/finshmlserv/main.py /code/
#COPY requirements.txt /code/

#COPY ./requirements.txt ./code/requirements.txt

#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#ADD git@github.com:moby/buildkit.git#v0.14.1:docs /buildkit-docs

#모델 서빙 역할(의존성의 위 BASE 이미지에서 모두 설치 했다)
#RUN pip install --no-cache-dir --upgrade  git+https://github.com/lsiwh37249/finshmlserv.git@0.8/hub
RUN pip install git+https://github.com/lsiwh37249/finshmlserv.git@1.1.1/k
 
#모델 서빙을 위해 API 구동을 위한 FASTAPI RUN
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
