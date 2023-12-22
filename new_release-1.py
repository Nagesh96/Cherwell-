import requests
import base64
import json

def create_cherwell_release(username, password, release):
    # Endpoint for creating a new release
    url = "https://charter.cherwellondemand.com/CherwellClient/CherwellAPI/api/V1/savebusinessobject"

    # Set up headers with content type and authorization
    headers = {
        "Content-Type": "application/json",
        "Authorization": get_authorization_header(username, password)
    }

    # Make a POST request to create a new release
    response = requests.post(url, headers=headers, data=json.dumps(release))
    response.raise_for_status()

    # Check if the release creation was successful (status code 201)
    if response.status_code == 201:
        print("New release created successfully!")
        # Extract busObRecId and busObPublicId from the response
        response_data = response.json()
        busObRecId = response_data.get('busObRecId')
        busObPublicId = response_data.get('busObPublicId')
        print(f"busObRecId: {busObRecId}, busObPublicId: {busObPublicId}")
        return busObRecId, busObPublicId
    else:
        print(f"Failed to create a new release. Status code: {response.status_code}")
        print(f"Response content: {response.text}")
        return None, None

def get_authorization_header(username, password):
    # Helper function to generate the Authorization header
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return f"Basic {encoded_credentials}"

# Example usage
username = "P3214461"
password = ""
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

busObRecId, busObPublicId = create_cherwell_release(username, password, release)
