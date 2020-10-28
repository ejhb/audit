# from bs4 import BeautifulSoup
# import requests

# # néttoie les doublon d'une liste


# url = 'http://eric.univ-lyon2.fr/~ricco/cours/cours_programmation_python.html'


# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# table = soup.find('table',{'class':'sortable rl-responsive-table-sortable'}).tbody
# rows = table.find_all('tr')

# import os
# import requests
# from urllib.parse import urljoin
# from bs4 import BeautifulSoup

# url = 'http://eric.univ-lyon2.fr/~ricco/cours/cours_programmation_python.html'

# response = requests.get(url)
# soup= BeautifulSoup(response.text, "html.parser")
# for link in soup.select("a[href$='.pdf']"):
# #Name the pdf files using the last portion of each link which are unique in this case
#     filename = os.path.join("2020-10-27-debian-gnome/",link['href'].split('/')[-1])
# with open(filename, 'wb') as f:
#     f.write(requests.get(urljoin(url,link['href'])).content)

wget -r -l1 -A.pdf http://eric.univ-lyon2.fr/~ricco/cours/cours_programmation_python.html

wget --no-directories --content-disposition -e robots=off -A.pdf -r \
    http://www.fayette-pva.com/