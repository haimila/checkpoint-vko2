import requests
import boto3

# json.tiedoston hakeminen
url = "https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json"

response = requests.get(url)
json_data = response.json()

tekstitiedosto = open("checkpoint.txt","w+")
parameter_list = []

# parametrien liittäminen listaan
for items in json_data["items"]:
    parameter_list.append(items["parameter"])

# listan kikkailu omille riveilleen ja tekstitiedostoon
ordered_list = "\n".join(parameter_list)
tekstitiedosto.write(ordered_list)
tekstitiedosto.close()

# Tämä osa skriptistä tekee bucketin ja lähettää sinne tiedoston
s3 = boto3.client("s3")
s3.create_bucket(Bucket="mitja-checkpoint-vko2")
s3.upload_file("checkpoint.txt","mitja-checkpoint-vko2","checkpoint1.txt")

print("Success!")


