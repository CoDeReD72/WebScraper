#pip install requests
#pip install bs4

import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Git User: ')
url = 'https://github.com/' + github_user # URL to be requested

r = requests.get(url)
soup = bs(r.content,  'html.parser') # r would return status code, .content returns source

profile_image = soup.find('img',{'alt' : 'Avatar'})['src']
print(profile_image)
