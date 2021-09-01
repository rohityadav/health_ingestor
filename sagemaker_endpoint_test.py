import boto3
import json

test='{"age": 19240, "gender": 2, "height": 168, "weight": 76.0, "ap_hi": 120, "ap_lo": 80, "cholesterol": 1, "gluc": 1, "smoke": 1, "alco": 0, "active": 1, "email": "test@test.com", "ingest_timestamp": "2021-08-31 22:47:46.432647", "source_timestamp": "2021-08-28 22:47:46.432648", "source_date": "2021-08-28", "client_id": 1208, "customer_id": 929706}'

f = json.loads(test)
ml_request = str(f['age']/365) + ',' + str(f['gender']) + ',' + str(f['height']) + ',' + str(f['weight']) + ',' + str(f['ap_hi']) + ',' + str(f['ap_lo']) + ',' + str(f['cholesterol']) + ',' + str(f['gluc']) + ',' + str(f['smoke']) + ',' + str(f['alco']) + ',' + str(f['active'])

print(ml_request)

runtime= boto3.client('runtime.sagemaker')

response = runtime.invoke_endpoint(EndpointName='octankmlcardioendpoint',
                                   ContentType='text/csv',
                                   Body=bytes(ml_request, 'utf-8'))

result = json.loads(response['Body'].read().decode())
print(result)

