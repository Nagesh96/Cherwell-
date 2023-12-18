from CherwellAPI import Cherwell

# Replace these with your Cherwell API details
cherwell_url = "https://your-cherwell-instance"
username = "your_username"
password = "your_password"
client_id = "your_client_id"

# Connect to Cherwell
cherwell = Cherwell(cherwell_url, username, password, client_id)

# Specify the fields and values for the new change request
change_request_data = {
    "Requestor": "John Doe",  # Replace with the actual requestor
    "Short Description": "Change Request Example",
    "Change Type": "Standard",  # Adjust based on your Cherwell configuration
    "Description": "Details of the change request",
    "Primary configuration item": "Server001",
    "Environment": "Production",
    "Primary CI criticality": "High",
    "Assign Team": "IT Support",
    "Assign To": "Support Analyst",
    "Impact": "High",
    "Priority": "High",
    "Major Change - checkbox": False,  # Adjust based on your Cherwell configuration
    "Service Impact": "Yes",
    "Project": "ProjectX",
    "Stakeholder call required": False,
    "IT SOC Bridge required": False,
    "IT Impact Description": "Impact details of the change",
    "Release Manager": "Jane Smith"  # Replace with the actual release manager
}

# Create a new change request
try:
    response = cherwell.create_business_object("Change Request", change_request_data)
    if response.get("businessObjectId"):
        print("New change request created successfully!")
    else:
        print("Failed to create change request.")
        print(response)
except Exception as e:
    print(f"An error occurred: {e}")
