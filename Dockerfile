FROM python:3.7-slim

WORKDIR /webapp

COPY main.py .
COPY requirements.txt .
ADD ./app app

RUN apt-get update && apt-get install -y build-essential python3-pip
RUN pip install google-cloud-profiler
RUN pip install -r requirements.txt

EXPOSE 8080/tcp

CMD ["python", "main.py"]