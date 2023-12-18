from CherwellAPI import CherwellClient

# Create a new CherwellClient Connection
cherwell_client = CherwellClient.Connection(<base_uri>,<api_key>,<username>,<password>)

# Create a new instance of a Release business object
release = cherwell_client.get_new_business_object("Release")

# Set the properties of the new Release
release.Description = "This is a test Release"
release.Status = "Scheduled"
release.ReleaseType = "Standard"
release.ReleaseName = "Test Release"

# Save the new Release
release.Save()

# Show the new business object record id
print("RecId for new Release: {}".format(release.busObRecId))
print("PublicId for new Release: {}".format(release.busObPublicId))
