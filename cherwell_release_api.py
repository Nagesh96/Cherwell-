import requests
import json

# Set the Cherwell API endpoint URL
url = "https://your_cherwell_instance.com/CherwellAPI/api/V1/savebusinessobject"

# Set the Cherwell API authentication credentials
username = "your_username"
password = "your_password"
client_id = "your_client_id"
client_secret = "your_client_secret"

# Set the Cherwell business object properties for the new release
new_release = {
    "busObId": "your_busObId",
    "fields": [
        {
            "dirty": True,
            "fieldId": "your_fieldId",
            "value": "your_value"
        },
        {
            "dirty": True,
            "fieldId": "your_fieldId",
            "value": "your_value"
        },
        {
            "dirty": True,
            "fieldId": "your_fieldId",
            "value": "your_value"
        }
    ]
}

# Set the Cherwell API request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + access_token
}

# Get the Cherwell API access token
auth_url = "https://your_cherwell_instance.com/CherwellAPI/token"
auth_data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret
}
auth_response = requests.post(auth_url, data=auth_data)
access_token = auth_response.json()["access_token"]

# Send the Cherwell API request to create the new release
response = requests.post(url, headers=headers, data=json.dumps(new_release))

# Check the Cherwell API response status code
if response.status_code == 200:
    response_json = response.json()
    record_id = response_json["busObRecId"]
    public_id = response_json["busObPublicId"]
    print(f"New release created successfully! Record ID: {record_id}, Public ID: {public_id}")
else:
    print("Failed to create new release.")
