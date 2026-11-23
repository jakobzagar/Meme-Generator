FROM python:3.12-slim AS dependencies

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt


FROM dependencies AS run

COPY . .

EXPOSE 5001

CMD ["python", "app.py"]
