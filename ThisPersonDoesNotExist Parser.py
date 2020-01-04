#parser image from site "https://thispersondoesnotexist.com"
import requests

url = 'https://thispersondoesnotexist.com/image'
headers = {
    "Host": "thispersondoesnotexist.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
    "Accept": "image/webp,*/*",
}
#get request
result = requests.get(url, headers=headers)

if result.status_code == 200:
    with open("img.jpg", 'wb') as img:
        img.write(result.content)
