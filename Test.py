import requests
import base64
import json

def create_cherwell_release(api_url, username, password, release_data):
    # Endpoint for creating a new release
    endpoint = f"{api_url}/api/V1/object/release"

    # Set up headers with content type and authorization
    headers = {
        "Content-Type": "application/json",
        "Authorization": get_authorization_header(username, password)
    }

    # Make a POST request to create a new release
    response = requests.post(endpoint, headers=headers, json=release_data)

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
api_url = ""
username = ""
password = ""

release_data = {
    "Short Description": "Providing Dummy Data for Testing purpose",
    "Requestor": "Nageswara",
    "Request Group": "Spectrum Mobile App Support",
    "Program": "Mobile 2.0",
    "Environment": "QA",
    "Primary Application (CI)": "MOBILE 2.0 Back office",
    "Release Type": "Code",
    "TypeOfTesting": "Smoke Test only",
    "Current Planned Start Date": "12-23-2023 02:59 PM",
    "Deployment Description Summary": "Defect Fixes",
    "Build": "1.0.1",
    "Urgency": "Low",
    "Urgency Reason": "Defect Fixes",
    "Service Impact": "Yes - Continuous",
    "Impacts to Orders in Progress": "Yes"
}

busObRecId, busObPublicId = create_cherwell_release(api_url, username, password, release_data)
