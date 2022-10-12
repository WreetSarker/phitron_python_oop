import requests
import json

url = "https://www.espncricinfo.com/player/sabbir-rahman-373538"

response = requests.get(url)
content = response.content.decode('UTF-8')
# jsonContent = json.loads(content)
print(content[:100])