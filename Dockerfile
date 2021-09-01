FROM python:3

ADD ingestor.py /

ADD cardio_train_ingest.json /

RUN pip install boto3

CMD [ "python", "./ingestor.py" ]