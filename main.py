from os import error
from types import NoneType
from bs4 import BeautifulSoup
import requests
import lxml


# Gemi verilerinin bulunduğu linkleri içeren txt dosyasını okunabilir şekilde açıyor.
file = open("links/_all_ship_links.txt", "r", encoding="utf-8")

# Elde edilen verileri kaydedeceği txt dosyasını yazılabilir şekilde oluşturup açıyor.
export_file = open("data/all_ships_properties.txt", "w")

# Eğer açılmayan sayfa varsa daha sonra kontrol edebilmek için açılmayan sayfa/sayfaların linklerini yazdılabilir txt dosyası oluşturup kaydediyor.
error_links = open("__error_links.txt", "w")

# Gemi linklerinin bulunduğu dosyayı satır satır gezen for döngüsü
for satir in file:

    # Dosyadan alınan gemi linkini lxml formatında açıyor.
    requestsLink = requests.get(satir)
    soup = BeautifulSoup(requestsLink.content, "lxml")

    # Eğer açılamayan sayfa varsa bu sayfayı ilgili txt dosyasına kaydedip döngüde sonraki satıra geçmesini sağlayan kontrol yapısı.
    if soup.find("h2", attrs={"class": "articleHeader"}) != None: 
        name = soup.find("h2", attrs={"class": "articleHeader"}).string
    else: 
        error_links.write(satir)
        continue

    # Eğer açılan sayfada geminin sınıfına erişilemiyor ise döngüde sonraki satıra geçmesini sağlayan kontrol yapısı. 
    if soup.find("td", text="Ship Class") != None: 
        type = soup.find("td", text="Ship Class").findNext("td").string.split()[::-1][0]
    else:
        continue
    
    # Eğer gelen veri boş ise veya açılan sayfada böyle bir kısım yok ise ilgili değişkene '?' değeri atayan boş değer kontrolü yapan kontrol yapıları. 
    if soup.find("td", text="Displacement") != None: 
        # split() ve replace() metotlarıyla string ifadenin daha sonra integer değer olarak kullanılabilmesi için içindeki virgül karakterinin kaldırılması.
        displacement = soup.find("td", text="Displacement").findNext("td").string.split()[0].replace(",","")
    else: displacement = "?"

    if soup.find("td",text="Length") != None: 
        lenght = soup.find("td",text="Length").findNext("td").string.split()[0].replace(",","") 
    else: lenght = "?"
    
    if soup.find("td",text="Beam") != None: 
        beam = soup.find("td",text="Beam").findNext("td").string.split()[0].replace(",","")
    else: beam = "?"
    
    if soup.find("td",text="Draft") != None: 
        draft = soup.find("td",text="Draft").findNext("td").string.split()[0].replace(",","") 
    else: draft = "?"
    
    if soup.find("td",text="Speed") != None: 
        speed = soup.find("td",text="Speed").findNext("td").string.split()[0].replace(",","") 
    else: speed = "?",
    
    if soup.find("td",text="Range") != None: 
        range = soup.find("td",text="Range").findNext("td").string.split()[0].replace(",","") 
    else: range = "?"
    
    if soup.find("td",text="Crew") != None: 
        crew = soup.find("td",text="Crew").findNext("td").string.split()[0].replace(",","") 
    else: crew = "?"
    
    # Eğer veriye ait ilgili özellikler boş değil ise verileri aralarına virgül koyarak string ifadeye çevirerek txt dosyasına yaz ve alt satıra geç.
    if crew != "?" and range != "?" and speed != "?" and draft != "?" and beam != "?" and lenght != "?" and displacement != "?":
        export_file.write("'"+str(name)+"',"+str(displacement)+","+str(lenght)+","+str(beam)+","+str(draft)+","+str(speed)+","+str(range)+","+str(crew)+",'"+str(type)+"'"+"\n")

    # Açılan sayfadaki gemi adını terminale yaz. (Verileri çekerken bir aksaklık olup olmadığını terminalden kontrol etmek için.)
    print("--"+str(name)+"--")

# Döngü sonlandığında açılan dosyaları kapat ve kaydet.
export_file.close()  
error_links.close() 
