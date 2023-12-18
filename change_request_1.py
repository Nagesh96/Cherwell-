import requests

# Replace these with your Cherwell API details
cherwell_url = "https://your-cherwell-instance"
username = "your_username"
password = "your_password"
api_key = "your_api_key"  # If your Cherwell instance requires an API key

# API endpoint for creating a Change Request
api_endpoint = f"{cherwell_url}/api/V1/your_change_request_endpoint"

# Specify the headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {api_key}" if api_key else None
}

# Specify the data for the new Change Request
change_request_data = {
    "Requestor": "John Doe",
    "ShortDescription": "Change Request Example",
    "ChangeType": "Standard",
    "Description": "Details of the change request",
    "PrimaryConfigurationItem": "Server001",
    "Environment": "Prod",
    "PrimaryCICriticality": "High",
    "AssignTeam": "IT Support",
    "AssignTo": "Support Analyst",
    "Impact": "High",
    "Priority": "High",
    "MajorChangeCheckbox": False,
    "ServiceImpact": "Yes",
    "Project": "ProjectX",
    "StakeholderCallRequired": False,
    "ITSOCBridgeRequired": False,
    "ITImpactDescription": "Impact details of the change",
    "ReleaseManager": "Jane Smith",
    "Schedule": "Scheduled",
    "ProposedStartDateAndTime": "2023-12-25T08:00:00",
    "ProposedEndDateAndTime": "2023-12-25T16:00:00",
    "Duration": "8 hours"
}

# Send HTTP POST request to create a new Change Request
try:
    response = requests.post(api_endpoint, json=change_request_data, headers=headers, auth=(username, password))
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Print the response details
    print("New Change Request created successfully!")
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.text)
except requests.exceptions.RequestException as e:
    print(f"Failed to create Change Request. An error occurred: {e}")
