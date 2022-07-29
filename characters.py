from bs4 import BeautifulSoup
import requests

url= "https://onepiece.fandom.com"
website = "https://onepiece.fandom.com/wiki/List_of_Canon_Characters"
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'html.parser')

tds = soup.find_all('td')
count = 0
personajes = list()
aux = list()
flagIsLastValue = False

# TODO Si un td está vacio rompe el contador al no encontrar datos, falta validar
for td in tds:
    try:
        if count == 1:
            nombre = td.find('a').text
            link_wiki = td.find('a', href=True)['href']

            # TODO en fandom para characters hay más de una tabla, por lo que hay que determinar el fin de la primera tabla con el ultimo valor
            # TODO imlementar flag
            if nombre == "Zunesha":
                flagIsLastValue = True

            aux.append(nombre)
            aux.append(url+link_wiki)
        
        if count == 2:
            appearance_chapter = td.find('a', title=True)['title']
            aux.append(appearance_chapter)
        
        if count == 4:
            year = td.text
            aux.append(year)

        if count == 5:
            personajes.append(aux)
            aux = list()
            count = 0
            if flagIsLastValue == True:
                break
            continue
        count = count+1
    except:
        continue

# print(personajes)
f = open("personajes.txt", "a")
for personaje in personajes:
    f.write(' ; '.join(personaje))
