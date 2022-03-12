import requests

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
out = requests.get(url)
print(out.text)
