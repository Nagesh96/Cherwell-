import requests
import json
import base64

def create_cherwell_release(api_url, username, password, release_data):
    # Endpoint for creating a release in Cherwell
    endpoint = f"{api_url}/api/V1/release"  # Adjust this if needed

    # Set up headers with content type and authorization
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {base64.b64encode(f'{username}:{password}'.encode('utf-8')).decode('utf-8')}"
    }

    # Convert release data to JSON
    release_json = json.dumps(release_data)

    # Make the request to create a release
    response = requests.post(endpoint, headers=headers, data=release_json)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print("Release created successfully!")
        return response.json()
    else:
        print(f"Failed to create release. Status code: {response.status_code}")
        return None

# Example usage
api_url = "https://your-cherwell-instance"  # Adjust the URL
username = "your_username"
password = "your_password"

release_data = {
    "ReleaseName": "New Release",
    "Description": "This is a new release.",
    # Add other release data as needed
}

create_cherwell_release(api_url, username, password, release_data)￼Enter
