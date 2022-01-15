FROM python:3.9-slim 
WORKDIR /app
RUN python example.py > index.html
COPY index.html /app
