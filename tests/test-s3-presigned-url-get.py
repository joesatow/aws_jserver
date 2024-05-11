from aws_jserver import generate_presigned_url_get

bucket_name = "chart-stamp"
object_name = "UPS_20240426_025424.png"

url = generate_presigned_url_get(bucket_name, object_name)
print(url)