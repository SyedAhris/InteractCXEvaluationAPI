FROM python:3.10.10-slim-buster

EXPOSE 8000

RUN mkdir /code

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]