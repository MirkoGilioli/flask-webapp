FROM python:3.10-slim-buster

WORKDIR /webapp

COPY main.py .
COPY requirements.txt .
COPY app .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]