import requests, json
import pprint
data = {
    "image_url":input(),
    "resized_images":True # Or true
}
headers = {'Content-type': 'application/json'}
data = requests.post("http://ec2-18-221-131-219.us-east-2.compute.amazonaws.com:5000/search", headers=headers, data=json.dumps(data)).json()
pprint.PrettyPrinter(indent=1).pprint(data)
