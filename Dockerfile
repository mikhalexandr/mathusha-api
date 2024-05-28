FROM python:3.11
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
CMD ["python3", "app.py"]
