# Chequear sintaxis y uso de HTTP services
# httpbin.org

import requests
import os
import json


# Initial GET request to retrieve the resource
url = "https://jsonplaceholder.typicode.com/posts/1"
print("Before PUT request:")
response = requests.get(url)
print(response.json())

# PUT request to update the resource
update_data = {
    "id": 777,
    "title": "Updated Title",
    "body": "This is the updated body of the post.",
    "userId": 1
}
put_response = requests.put(url, json=update_data)

# Check if the PUT request was successful
if put_response.status_code == 200:
    print("\nPUT request successful. Resource updated.")

# GET request again to retrieve the updated resource
print("\nAfter PUT request:")
response = requests.get(url)
print(response.json())
