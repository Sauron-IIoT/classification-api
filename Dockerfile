FROM kumatea/tensorflow:2.6.0-py38

COPY requirements.txt /app/ 
WORKDIR /app
RUN pip install -r requirements.txt

RUN apt update -y
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY . .

ENV PORT 8083

CMD uvicorn app:app --host 0.0.0.0 --port ${PORT} --workers 1