import requests
import json

img_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

response = requests.get(img_url)
content = response.content.decode('UTF-8')
jsonContent = json.loads(content)
img_add = jsonContent['url']

print(img_add)


# save image
res = requests.get(img_add)
with open('nasa.jpg', 'wb') as image:
    image.write(res.content)