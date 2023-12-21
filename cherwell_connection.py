import requests
import base64

def check_cherwell_connection(api_url, username, password):
    # Endpoint for a basic Cherwell API call (you might want to adjust this based on Cherwell's API)
    endpoint = f"{api_url}/api/V1/heartbeat"

    # Set up headers with content type and authorization
    headers = {
        "Content-Type": "application/json",
        "Authorization": get_authorization_header(username, password)
    }

    # Make a simple request to check the connection
    response = requests.get(endpoint, headers=headers)

    # Check if the connection was successful (status code 200)
    if response.status_code == 200:
        print("Connection to Cherwell successful!")
        return True
    else:
        print(f"Failed to connect to Cherwell. Status code: {response.status_code}")
        return False

def get_authorization_header(username, password):
    # Helper function to generate the Authorization header
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return f"Basic {encoded_credentials}"

# Example usage
api_url = "https://your-cherwell-instance"  # Adjust the URL
username = "your_username"
password = "your_password"

check_cherwell_connection(api_url, username, password)
