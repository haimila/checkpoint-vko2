import requests
import boto3

url = "https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json"

response = requests.get(url)
json_data = response.json()

tekstitiedosto = open("checkpoint.txt","w+")
parameter_list = []

for items in json_data["items"]:
    parameter_list.append(items["parameter"])

ordered_list = "\n".join(parameter_list)
tekstitiedosto.write(ordered_list)
tekstitiedosto.close()


