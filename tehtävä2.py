import requests

url = "https://api.github.com/search/repositories?q=language:python"
r = requests.get(url)
vastaus = r.json()
lista = []
count = 0
lista2 = []

class Kohta:
 
    def __init__(self, forks, name, desc):
        self.forks = forks
        self.name = name
        self.desc = desc
 
    def __repr__(self):
        return '{' + str(self.forks) + ', ' + self.name + ', ' + self.desc + '}'


for i in vastaus['items']:
    lista2.append(Kohta(i['forks'], i['name'],i['description']))
    
    kohta = {'forks': i['forks'], 'name': i['name'], 'description': i['description']}
    lista.append(kohta)

lista2.sort(key=lambda x: x.forks, reverse=True)
for i in lista2:
    print(i)