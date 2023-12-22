import requests
import base64
import json

def create_cherwell_release(api_url, username, password, release_data):
    # Endpoint for creating a new release (adjust based on Cherwell's API)
    endpoint = f"{api_url}/api/V1/releases"

    # Set up headers with content type and authorization
    headers = {
        "Content-Type": "application/json",
        "Authorization": get_authorization_header(username, password)
    }

    # Make a POST request to create a new release
    response = requests.post(endpoint, headers=headers, data=json.dumps(release_data))

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
        return None, None

def get_authorization_header(username, password):
    # Helper function to generate the Authorization header
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return f"Basic {encoded_credentials}"

# Example usage
api_url = ""  # Adjust the URL
username = ""
password = ""

release_data = {
    "name": "Release 1.0",
    "description": "This is the first release of the project.",
    # Add more relevant data based on Cherwell's API documentation
}

busObRecId, busObPublicId = create_cherwell_release(api_url, username, password, release_data)
