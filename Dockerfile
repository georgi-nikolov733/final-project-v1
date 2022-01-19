FROM python:latest
WORKDIR /app

COPY example.py /app

CMD [ "python", "example.py" ]
