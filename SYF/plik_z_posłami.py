from bs4 import BeautifulSoup
import requests
import json

url = "https://www.sejm.gov.pl/sejm8.nsf/poslowie.xsp?type=P"

result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

name_text = doc.find_all(class_ = "deputyName")
role_text = doc.find_all(class_ = "deputy-box-details")

persons = {}

for i in range(0,505): #średnio optymalne ale łatwe do zmiany
    name = name_text[i].string
    role = role_text[i]
    strong = role.find("strong").string
    persons[name] = strong
    
list_persons = list(persons.keys())
print(list_persons[504])

textfile = open("name_file.txt", "w")

for key, value in persons.items():
    textfile.write(f"{key}:{value}\n")
textfile.close()
