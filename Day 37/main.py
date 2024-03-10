# requests.get()
# requests.post()
# requests.put()
# requests.delete()

import requests

token = "IAmOlafThisIsMyKey"
username = "olaf"
pixela_endpoint = f"https://pixe.la/v1/users/"

# Create account
user_params = {
    "token": "IAmOlafThisIsMyKey",
    "username": "olaf",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create account
'''response = requests.post(pixela_endpoint, json=user_params)'''

#graphs
graph_endpoint = f"{pixela_endpoint}{username}/graphs"

graph_config = {
    "id": "graph1",
    "name": "sailing",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

config = {
    "pinnedGraphID": "graph1",
    "title": "Software Dev",
    "displayName": "Olaf",
    "aboutURL": "https://www.brandonolafsen.com"

}

pin_endpoint = f"{pixela_endpoint}{username}"
entry = requests.put(pin_endpoint, json=config, headers=headers)
print(entry.text)
