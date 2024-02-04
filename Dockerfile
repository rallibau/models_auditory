FROM python:3.11.7-slim-bullseye
ENV PYTHONUNBUFFERED 1
RUN mkdir /models_auditory/
ADD rallibau ./models_auditory/rallibau/
WORKDIR /models_auditory/rallibau
RUN pip install -r dependences/requirements.txt
