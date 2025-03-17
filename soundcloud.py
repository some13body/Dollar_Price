import requests
res = requests.get('https://lucida.to/?url=https://soundcloud.com/milad-goodarzi-167303920/gham-gerefte-hame-kooche-haye-ma_amir-tataloo_320?si=cb19f7e4c2bc40e6944bd49554960f7a&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing&country=auto')
print(res.content)