FROM python:3.9-slim-buster
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY requirements.txt /app
COPY example.py /app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
