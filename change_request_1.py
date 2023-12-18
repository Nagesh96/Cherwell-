from CherwellAPI import CherwellClient

# Create a new CherwellClient Connection
cherwell_client = CherwellClient.Connection(<base_uri>,<api_key>,<username>,<password>)

# Create a new instance of a Change business object
change = cherwell_client.get_new_business_object("Change")

# Set the properties of the new Change
change.Description = "This is a test Change"
change.Status = "Scheduled"
change.ChangeType = "Standard"
change.ChangeName = "Test Change"

# Save the new Change
change.Save()

# Show the new business object record id
print("RecId for new Change: {}".format(change.busObRecId))
print("PublicId for new Change: {}".format(change.busObPublicId))
