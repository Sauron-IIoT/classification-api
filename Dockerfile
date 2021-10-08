FROM kumatea/tensorflow:2.4.1-py38

WORKDIR /app

RUN apt update -y

RUN pip install pipenv

COPY Pipfile* .

RUN pipenv lock

RUN pipenv install --system

RUN apt-get install python3-h5py -y

RUN apt-get install ffmpeg libsm6 libxext6 -y

COPY . .

ENV PORT 8083

CMD uvicorn app:app --host 0.0.0.0 --port ${PORT} --workers 1