import json
import requests

img_url = "https://scontent.fdac138-1.fna.fbcdn.net/v/t1.6435-9/125191623_4657133991026616_4345305389435009406_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=aAf8gxn1L6UAX-wbXRb&_nc_ht=scontent.fdac138-1.fna&oh=00_AT9RD8WWcD-iAhSVohu64JP1wZiUMlONmc3AvaJ2VC9WTw&oe=636CD6B0"

response = requests.get(img_url)
content = response.content

with open('vetki.png', 'wb') as image:
    image.write(content)