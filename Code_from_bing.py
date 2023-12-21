import requests

url = "https://<your_cherwell_instance>/CherwellAPI/release"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <your_access_token>"
}
data = {
    "Title": "New Release",
    "Description": "This is a new release",
    "Requestor": "John Doe",
    "CI": "Computer",
    "ChangeRequestID": "12345"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("New release created successfully!")
else:
    print("Failed to create new release.")
