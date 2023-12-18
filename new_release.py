from CherwellAPI import CherwellClient

# Replace these with your Cherwell API details
cherwell_url = "https://your-cherwell-instance"
api_key = "your_api_key"  # If your Cherwell instance requires an API key
username = "your_username"
password = "your_password"

# Create a new CherwellClient Connection
cherwell_client = CherwellClient.Connection(cherwell_url, api_key, username, password)

# Create a new instance of a Release business object
release = cherwell_client.get_new_business_object("Release")

# Define the properties for the new Release
release_properties = {
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

# Set the properties of the new Release
for key, value in release_properties.items():
    setattr(release, key, value)

# Save the new Release
try:
    release.Save()
    print("New release created successfully!")
except Exception as e:
    print(f"Failed to create release. An error occurred: {e}")
