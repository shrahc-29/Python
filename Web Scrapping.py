import requests
from bs4 import BeautifulSoup

url = "https://www.wikipedia.org/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.title.string)
else:
    print("Failed to retrieve the webpage.")

#Accessing different parets of the web page
print(soup.title)
print(soup.title.name)
print(soup.title.string)

#Inspecting small parts of the code:
soup1 = soup.find_all("a")
print(soup1)

from bs4 import BeautifulSoup
from bs4 import Comment

data = '''
<html>
  <body>
    <div>
    <!-- desired text -->
    </div>
  </body>
</html>

 '''
soup = BeautifulSoup(data, 'html.parser')
comment = soup.find(text=lambda text:isinstance(text, Comment))
print(comment)
