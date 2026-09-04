FROM python:3.12-slim

WORKDIR /app
COPY service.py /app/service.py

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HOST=0.0.0.0 \
    PORT=8090

EXPOSE 8090

CMD ["python", "service.py"]
