from aws_jserver import generate_presigned_url_post
import requests
import logging

bucket1 = "robin-csv-upload"
bucket2 = "robin-finished-xlsx"
object_name = "tests/2024-02-20_15-11-52.png"

result = generate_presigned_url_post(bucket1, object_name)
url2 = generate_presigned_url_post(bucket2, object_name)
#print(url1)
print(url2)

#f = open("/home/jsat/.site-packages/aws_jserver/tests/2024-02-20_15-11-52.png", "r")
# Demonstrate how another Python program can use the presigned URL to upload a file
with open(object_name, 'rb') as f:
    files = {'file': (object_name, f)}
    http_response = requests.post(result['url'], data=result['fields'], files=files)
# If successful, returns HTTP status code 204
logging.info(f'File upload HTTP status code: {http_response.status_code}')