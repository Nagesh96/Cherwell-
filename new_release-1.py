import requests

# Replace these with your Cherwell API details
cherwell_url = "https://your-cherwell-instance"
username = "your_username"
password = "your_password"
api_key = "your_api_key"  # If your Cherwell instance requires an API key

# API endpoint for creating a new Release
api_endpoint = f"{cherwell_url}/api/V1/your_release_endpoint"

# Specify the headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {api_key}" if api_key else None
}

# Specify the data for the new Release
release_data = {
    "ShortDescription": "Mobile deployment prod",
    "Requestor": "Nagisetti, Sheela (P4567)",
    "RequestGroup": "Spectrum Mobile App Support",
    "Program": "Mobile 2.0",
    "Environment": "prod",
    "PrimaryApplicationCI": "MOBILE 2.0 Back office",
    "ReleaseType": "Code",
    "TypeOfTesting": "Sanity and Smoke Test",
    "CurrentPlannedStartDate": "2023-12-20",
    "DeploymentDescriptionSummary": "Defect Fixes",
    "Build": "1.1.350",
    "Urgency": "High",
    "UrgencyReason": "Prod Deployment",
    "ServiceImpact": "Yes - Continuous",
    "ImpactToOrderInProgress": "Yes"
}

# Send HTTP POST request to create a new Release
try:
    response = requests.post(api_endpoint, json=release_data, headers=headers, auth=(username, password))
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Print the response details
    print("New Release created successfully!")
    print("Response Status Code:", response.status_code)
    print("Response Content:", response.text)
except requests.exceptions.RequestException as e:
    print(f"Failed to create Release. An error occurred: {e}")
