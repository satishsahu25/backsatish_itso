FROM python:3.11

# setup a working directory
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir  --upgrade  -r /code/requirements.txt


COPY ./app /code/app


CMD ["uvicorn","app.back:app","--host","--reload","0.0.0.0","--port","80" ]
