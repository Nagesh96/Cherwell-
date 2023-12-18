from CherwellAPI import Cherwell

# Replace these with your Cherwell API details
cherwell_url = "https://your-cherwell-instance"
username = "your_username"
password = "your_password"
client_id = "your_client_id"

# Connect to Cherwell
cherwell = Cherwell(cherwell_url, username, password, client_id)

# Specify the fields and values for the new release
release_data = {
    "Short Description": "Mobile deployment prod",
    "Requestor": "Nagisetti, Sheela (P4567)",
    "Request Group": "Spectrum Mobile App Support",
    "Program": "Mobile 2.0",
    "Environment": "prod",
    "Primary Application (CI)": "MOBILE 2.0 Back office",
    "Release Type": "Code",  # Adjust based on your Cherwell configuration
    "Type of Testing": "Sanity and Smoke Test",
    "Current Planned Start Date": "2023-12-20",  # Replace with the actual date
    "Deployment Description Summary": "Defect Fixes",
    "Build": "1.1.350",
    "Urgency": "High",
    "Urgency Reason": "Prod Deployment",
    "Service Impact": "Yes - Continuous",
    "Impact to order in process": "Yes"
}

# Create a new release
try:
    response = cherwell.create_business_object("Release", release_data)
    if response.get("businessObjectId"):
        print("New release created successfully!")
    else:
        print("Failed to create release.")
        print(response)
except Exception as e:
    print(f"An error occurred: {e}")
