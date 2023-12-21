# Create a release
release_data = {
    "ReleaseName": "New Release",
    "Description": "This is a new release.",
    "CurrentPlannedStartDate": "2023-12-21",  # Replace with the actual value
    # Add other release data as needed
}

release_result = create_cherwell_release(api_url, username, password, release_data)

# Check if the release was created successfully
if release_result:
    release_id = release_result.get("ReleaseID")

    # Create a Change Request linked to the release with the same "Current Planned Start Date"
    change_request_data = {
        "ReleaseID": release_id,
        "CurrentPlannedStartDate": release_data.get("CurrentPlannedStartDate"),
        # Add other Change Request data as needed
    }

    create_change_request(api_url, username, password, change_request_data)
