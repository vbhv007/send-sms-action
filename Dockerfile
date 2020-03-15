FROM python:3.7-slim
ADD . /app
WORKDIR /app
RUN pip install --target=/app requests
RUN chmod +x /app/main.py
CMD ["python", "/app/main.py"]
