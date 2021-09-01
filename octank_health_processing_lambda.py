import json
import boto3
import base64
import random

firehose = boto3.client('firehose')
def lambda_handler(event, context):
# records = event.get("Records")
# f = open('octank_sample_json')
# records = json.load(f)["Records"]
    records=event.get("Records")
    for record in records:
        try:
            # Process your record
            payload = json.loads(base64.b64decode(record['kinesis']['data']).decode("utf-8"))
            payload["health_prediction"] = random.randint(0, 1)
            response = firehose.put_record(
                DeliveryStreamName="PUT-S3-6UYHe",
                Record={'Data': json.dumps(payload) + "\n"}
            )
        except Exception as e:
            return {"batchItemFailures":[]}

    return {"batchItemFailures":[]}
