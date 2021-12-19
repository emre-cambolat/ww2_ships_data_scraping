from os import error
from types import NoneType
from bs4 import BeautifulSoup
import requests
import lxml


file = open("links/_all_ship_links.txt", "r", encoding="utf-8")
export_file = open("data/all_ships_properties.txt", "w")
error_links = open("__error_links.txt", "w")

for satir in file:
    requestsLink = requests.get(satir)
    soup = BeautifulSoup(requestsLink.content, "lxml")

    if soup.find("h2", attrs={"class": "articleHeader"}) != None: name = soup.find("h2", attrs={"class": "articleHeader"}).string
    else: 
        error_links.write(satir)
        continue
    if soup.find("td", text="Ship Class") != None: type = soup.find("td", text="Ship Class").findNext("td").string.split()[::-1][0]
    else:
        continue
    
    if soup.find("td", text="Displacement") != None: displacement = soup.find("td", text="Displacement").findNext("td").string.split()[0].replace(",","")
    else: displacement = "?"

    if soup.find("td",text="Length") != None: lenght = soup.find("td",text="Length").findNext("td").string.split()[0].replace(",","") 
    else: lenght = "?"
    
    if soup.find("td",text="Beam") != None: beam = soup.find("td",text="Beam").findNext("td").string.split()[0].replace(",","")
    else: beam = "?"
    
    if soup.find("td",text="Draft") != None: draft = soup.find("td",text="Draft").findNext("td").string.split()[0].replace(",","") 
    else: draft = "?"
    
    if soup.find("td",text="Speed") != None: speed = soup.find("td",text="Speed").findNext("td").string.split()[0].replace(",","") 
    else: speed = "?",
    
    if soup.find("td",text="Range") != None: range = soup.find("td",text="Range").findNext("td").string.split()[0].replace(",","") 
    else: range = "?"
    
    if soup.find("td",text="Crew") != None: crew = soup.find("td",text="Crew").findNext("td").string.split()[0].replace(",","") 
    else: crew = "?"
    
    if crew != "?" and range != "?" and speed != "?" and draft != "?" and beam != "?" and lenght != "?" and displacement != "?":
        export_file.write("'"+str(name)+"',"+str(displacement)+","+str(lenght)+","+str(beam)+","+str(draft)+","+str(speed)+","+str(range)+","+str(crew)+",'"+str(type)+"'"+"\n")

    print("--"+str(name)+"--")

export_file.close()  
error_links.close() 
