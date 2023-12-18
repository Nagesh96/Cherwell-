from CherwellAPI import CherwellClient

# Replace these with your Cherwell API details
cherwell_url = "https://your-cherwell-instance"
api_key = "your_api_key"
username = "your_username"
password = "your_password"

# Create a new CherwellClient Connection
cherwell_client = CherwellClient.Connection(cherwell_url, api_key, username, password)

# Create a new instance of a Change Request business object
change_request = cherwell_client.get_new_business_object("Change Request")

# Define the properties for the new Change Request
change_request_properties = {
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

# Set the properties of the new Change Request
for key, value in change_request_properties.items():
    setattr(change_request, key, value)

# Save the new Change Request
try:
    change_request.Save()
    print("New change request created successfully!")
except Exception as e:
    print(f"Failed to create change request. An error occurred: {e}")
