import requests, re
from bs4 import BeautifulSoup

url = "https://cnn.com"
out = requests.get(url)
# ---------- rozwiązanie z wyrażeniem regularnym
wyniki = re.findall("<img.*?>",out.text)
print(wyniki)

# ---------- rozwiązanie z wyrażeniem regularnym
soup = BeautifulSoup(out.text, "html.parser")
print(soup.find_all("img"))