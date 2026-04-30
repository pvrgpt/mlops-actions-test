FROM python:3.9-slim
WORKDIR /app
COPY model.py .
CMD ["python","model.py"]
