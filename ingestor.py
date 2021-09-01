import json
import datetime
import random
import boto3
from botocore.config import Config
import time

f = open('cardio_train_ingest.json')
data = json.load(f)
config = Config(
    region_name='us-east-1'
)
kinesis_client = boto3.client('kinesis', config=config)
i = 0
kinesis_records = []

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

for d in data['data']:
    i = i + 1
    print(i)
    d['email'] = 'test@test.com'
    d['ingest_timestamp'] = datetime.datetime.now()
    now_time = datetime.datetime.now()
    source_time = datetime.datetime.now() - datetime.timedelta(random.randint(0, 9))
    d['source_timestamp'] = source_time
    d['source_date'] = source_time.strftime("%Y-%m-%d")
    d['client_id'] = random.randint(1200, 2200)
    d['customer_id'] = random.randint(1000, 1000000)
    record = {'Data': json.dumps(d, default=myconverter), 'PartitionKey': str(hash(d["client_id"]))}
    kinesis_records.append(record)
    if i % 5 == 0:
        print(kinesis_records)
        kinesis_client.put_records(Records=kinesis_records, StreamName="health_ingest_stream")
        kinesis_records = []
        time.sleep(2)

