FROM python:3.10-slim-buster

WORKDIR /webapp

COPY main.py .
COPY requirements.txt .
ADD ./app app

RUN apt-get update && apt-get install -y build-essential python3-pip
RUN pip install -r requirements.txt
RUN pip install google-cloud-profiler
RUN pip install google-python-cloud-debugger
RUN pip install google-cloud-error-reporting --upgrade

EXPOSE 8080/tcp

CMD ["python", "main.py"]