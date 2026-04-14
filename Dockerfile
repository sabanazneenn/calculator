FROM python:3.10-slim

WORKDIR /app

COPY calculator.py .

RUN pip install flask

EXPOSE 6060

CMD ["python", "calculator.py"]

