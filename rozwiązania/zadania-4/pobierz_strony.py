# ---------- Sposób pierwszy: z biblioteką "urlib"
from urllib.request import urlopen

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
with urlopen(url) as response:
    body = response.read()
print(body)

# ---------- Sposób drugi: z biblioteką "requests"
import requests

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
out = requests.get(url)
print(out.text)
