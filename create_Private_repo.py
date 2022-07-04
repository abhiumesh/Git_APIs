import requests
import json

with open("token.json",'r') as data:
    config_file = data.read()
token = json.loads(config_file)

path = "user/repos"
url = f"https://api.github.com/{path}"


header = {
    "Authorization" : f"token {token['token']}"
}

data = {
    'name':'Git_API',
    'description':'Generated By Python',
    'private': True
}

data = json.dumps(data)

response = requests.post(url,headers=header,data=data)
print(response.status_code)