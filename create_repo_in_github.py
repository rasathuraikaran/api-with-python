import requests
import json
url = "https://api.github.com/user/repos"
token = "your token"
headers = {
    "Authorization" : "token {}".format(token)
}

RepositoryName = input("Enter the name by which you want to create a Repository : ")
data = {
    "name" : "{}".format(RepositoryName)
}
requests.post(url,data = json.dumps(data),headers=headers)