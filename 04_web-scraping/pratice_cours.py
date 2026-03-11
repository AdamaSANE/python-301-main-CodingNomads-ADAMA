# import requests
# from bs4 import BeautifulSoup

# BASE_URL = "https://codingnomads.github.io/recipes/"
# page = requests.get(BASE_URL)
# print(page.text)

# soup = BeautifulSoup(page.text)
# links = soup.find_all("a")

# urls = [link["href"] for link in links]
# print(urls)


import requests
from bs4 import BeautifulSoup

BASE_URL = "https://codingnomads.github.io/recipes/"

# Étape 1 : récupérer toutes les URLs depuis la page d'index
index_page = requests.get(BASE_URL)
index_soup = BeautifulSoup(index_page.text, "html.parser")
links = index_soup.find_all("a")
urls = [link["href"] for link in links]

# Étape 2 : parcourir chaque URL et extraire titre + corps de la recette
for url in urls:
    full_url = BASE_URL + url
    page = requests.get(full_url)
    soup = BeautifulSoup(page.text, "html.parser")

    title = soup.find("h1").get_text(strip=True)
    recipe = soup.find("div", class_="recipe-body").get_text(strip=True)

    print(f"Titre   : {title}")
    print(f"Recette : {recipe[:200]}...")
    print("-" * 60)

