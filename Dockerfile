FROM python:3.8

COPY requirements.txt /app/ 
WORKDIR /app
RUN pip install -r requirements.txt

COPY . .

ENV PORT 8083

CMD uvicorn app:app --host 0.0.0.0 --port ${PORT} --workers 1