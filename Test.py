import requests
import json

# Set the Cherwell API endpoint URL
url = "https://charter.cherwellondemand.com/CherwellClient/CherwellAPI/api/V1/savebusinessobject"

# Set the Cherwell API key
api_key = "<api_key>"

# Set the Cherwell username and password
username = "<username>"
password = "<password>"

# Set the Release properties
release = {
    "busObId": "Release",
    "fields": [
        {
            "dirty": True,
            "Short Description": "Providing Dummy Data for Testing purpose",
            "Requestor": "annem, nageswara (P3214461)",
            "Request Group": "Spectrum Mobile App Support",
            "Program": "Spectrum Mobile 2.0",
            "Environment": "QA",
            "Primary Application (CI)": "SPECTRUM MOBILE 2.0 BACKOFFICE (SMBO M2) QA2",
            "Release Type": "Code",
            "Type Of Testing- Required": "Smoke Test only",
            "Deployment Description Summary": "Defect Fixes",
            "Build": "1.0.1",
            "Urgency": "Low",
            "Urgency Reason": "Defect Fixes",
            "Service Impact": "Yes - Continuous",
            "Impacts to Orders in Procress": "Yes"
        }
    ],
    "persist": True
}

# Set the headers for the Cherwell API request
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer " + api_key
}

# Authenticate with the Cherwell API
auth_data = {
    "grant_type": "password",
    "client_id": "api_client",
    "username": username,
    "password": password
}
auth_url = "https://<base_uri>/CherwellAPI/token"
auth_response = requests.post(auth_url, data=auth_data)
auth_response.raise_for_status()
auth_json = auth_response.json()
api_key = auth_json["access_token"]

# Set the headers for the Cherwell API request with the new API key
headers["Authorization"] = "Bearer " + api_key

# Create the new Release in Cherwell
response = requests.post(url, headers=headers, data=json.dumps(release))
response.raise_for_status()

# Show the new business object record id
print("RecId for new Release: {}".format(response.json()["busObRecId"]))
print("PublicId for new Release: {}".format(response.json()["busObPublicId"]))
