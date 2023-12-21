import requests
import json
import base64

def create_release(api_url, username, password, release_data):
    # Endpoint for creating a Release in Cherwell
    endpoint = f"{api_url}/api/V1/release"  # Adjust this if needed

    # Set up headers with content type and authorization
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {base64.b64encode(f'{username}:{password}'.encode('utf-8')).decode('utf-8')}"
    }

    # Convert Release data to JSON
    release_json = json.dumps(release_data)

    # Make the request to create a Release
    response = requests.post(endpoint, headers=headers, data=release_json)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        result = response.json()
        release_id = result.get("ReleaseID")
        print(f"Release created successfully! Release ID: {release_id}")
        return result
    else:
        print(f"Failed to create Release. Status code: {response.status_code}")
        return None

def create_change_request(api_url, username, password, release_id):
    # Endpoint for creating a Change Request in Cherwell
    endpoint = f"{api_url}/api/V1/changeRequest"  # Adjust this if needed

    # Set up headers with content type and authorization
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {base64.b64encode(f'{username}:{password}'.encode('utf-8')).decode('utf-8')}"
    }

    # Construct Change Request data linked to the provided release_id
    change_request_data = {
        "ReleaseID": release_id,
        # Add other Change Request data as needed
    }

    # Convert Change Request data to JSON
    change_request_json = json.dumps(change_request_data)

    # Make the request to create a Change Request
    response = requests.post(endpoint, headers=headers, data=change_request_json)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        result = response.json()
        change_request_id = result.get("ChangeRequestID")
        print(f"Change Request created successfully! Change Request ID: {change_request_id}")
        return result
    else:
        print(f"Failed to create Change Request. Status code: {response.status_code}")
        return None

# Example usage
api_url = "https://your-cherwell-instance"  # Adjust the URL
username = "your_username"
password = "your_password"

# Create a release
release_data = {
    "ReleaseName": "New Release",
    "Description": "This is a new release.",
    # Add other release data as needed
}

# Corrected function name in the next line
release_result = create_release(api_url, username, password, release_data)

# Check if the release was created successfully
if release_result:
    release_id = release_result.get("ReleaseID")

    # Create a Change Request linked to the release
    create_change_request(api_url, username, password, release_id)
