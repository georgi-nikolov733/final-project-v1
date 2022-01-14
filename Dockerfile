FROM nginx:1.20-alpine 
WORKDIR /app
COPY index.html /app
COPY result.html /app