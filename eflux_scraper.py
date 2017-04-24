import requests
from bs4 import BeautifulSoup, SoupStrainer


url = "http://www.e-flux.com/announcements/2017"

result  = requests.get(url, allow_redirects=False)
page_content = result.content

#print result

soup = BeautifulSoup(page_content, "html.parser")

for link in soup.find_all("div", { "id" : "data-href" }):
#for link in soup.find_all("a"):
    print(link)
