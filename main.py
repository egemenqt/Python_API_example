import requests
import termcolor
import datetime
import json

now = datetime.datetime.today()

#haberler --------------------------------
class News():
    def __init__(self):
        choice = int(input("1-Global News\n2-Turkey News\n:"))
        #türkiye haberleri

        if choice == 2:
            response = requests.get("https://newsapi.org/v2/top-headlines",params={
                "country": "tr",
                "apiKey":"a30720d85c9f4b039e76e0a6fb7f91f9",
                "from":str(now),
                "sortBy":"popularity",
            })
            result = response.json()
            
            for news in result['articles']:
                print(termcolor.colored(news["title"],attrs=["bold"]) + "\n" +"\n"+ "Haber Kaynağı    =>   " + news["url"] + termcolor.colored("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------",color="green"))
        
        #global haberler
        elif choice == 1:
            response = requests.get("https://newsapi.org/v2/top-headlines",params={
                "country": "us",
                "apiKey":"a30720d85c9f4b039e76e0a6fb7f91f9",
                "from":str(now),
                "sortBy":"popularity",
            })
            result = response.json()
            
            for news in result['articles']:
                print(termcolor.colored(news["title"],attrs=["bold"]) + "\n" +"\n"+ "Haber Kaynağı    =>   " + news["url"] + termcolor.colored("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------",color="green"))
         
            
#döviz-------------------------------   
class Doviz():
    
    def __init__(self):
        self.request()
        self.save()
        self.read()

    def request(self):
        url = 'https://v6.exchangerate-api.com/v6/73af99b11c97c618f2f978da/latest/USD'
        response = requests.get(url,params={
            "result": "success"
        })
        result = response.json()
        return result["conversion_rates"]

    def save(self):
        with open("exchanger.json", "w+",encoding="utf-8") as file:
            datas = json.dump(self.request(),file,ensure_ascii=False,indent=1)

    def read(self):
        with open("exchanger.json","r+",encoding="utf-8") as file:
            datas = json.load(file)
            try:
                print(datas)
                bozdur = input("bozdurulacak para birimi:")
                bozulacak = input("bozulacak para birimi:")
                user_miktar = int(input("bozdurulacak miktar:"))
            #math 
                data_bozdur = datas.get(bozdur) 
                data_bozul = datas.get(bozulacak)
                result = (data_bozul/data_bozdur)*user_miktar
                print(termcolor.colored(f"Başarılı\ntoplam {result} {bozulacak} eder!",color="green",attrs=["bold"]))
            except:
                print(termcolor.colored("bilinmeyen hata!\nlütfen listede belirtilen para birimlerini bozdurunuz!\nsayı girilmesi gereken yere karakter girmeyiniz!",color="red",attrs=["bold"]))

#filmler-------------------------------
class Movie():
    def __init__(self):
        userchoice = int(input("hoşgeldiniz\n1-haftanın filmleri\n2-haftanın tv şovları\n:"))
        if userchoice == 1:
            self.movie_api()
            self.movie_save()
            self.movie_read()
        
        elif userchoice == 2:
            self.tv_api()
            self.tv_save()
            self.tv_read()
        else:
            print(termcolor.colored("seçim yapılamadı",color="red"))
    #movie-------------------------------------
    def movie_api(self):
        api_key = "9d1f06d23d9c4e36caef462fe3ce6ceb"
        url="https://api.themoviedb.org/3/trending/movie/week?query=&api_key=9d1f06d23d9c4e36caef462fe3ce6ceb"
        response = requests.get(url)
        result = response.json()
        return result
    
    def movie_save(self):
        with open("movie.json","w+",encoding="utf-8") as file:
            dump = json.dump(self.movie_api(),file,ensure_ascii=False,indent=1)

    def movie_read(self):
        with open("movie.json","r+") as file:
            load = json.load(file)
            data = load["results"]
            for datas in data:
                print(termcolor.colored("isim =>"+datas["title"],attrs=["bold"]))
                print(termcolor.colored("KONUSU:",attrs=["bold"]))
                print(termcolor.colored(datas["overview"],color="blue"))
                print(termcolor.colored("------------------------------------------------------------------------------------------------------------------------------",color="green"))
#tv---------------------------------------------------------
    def tv_api(self):
        api_key = "9d1f06d23d9c4e36caef462fe3ce6ceb"
        url="https://api.themoviedb.org/3/trending/tv/week?query=&api_key=9d1f06d23d9c4e36caef462fe3ce6ceb"
        response = requests.get(url)
        result = response.json()
        return result
    
    def tv_save(self):
        with open("tv.json","w+",encoding="utf-8") as file:
            dump = json.dump(self.tv_api(),file,ensure_ascii=False,indent=1)
    
    def tv_read(self):
        with open("tv.json","r+") as file:
            load = json.load(file)
            data = load["results"]
            for datas in data:
                print(termcolor.colored("isim =>"+datas["name"],attrs=["bold"]))
                print(termcolor.colored("KONUSU:",attrs=["bold"]))
                print(termcolor.colored(datas["overview"],color="blue"))
                print(termcolor.colored("------------------------------------------------------------------------------------------------------------------------------",color="green"))
#hava durumu -------------------------------
class Weather():
    def __init__(self):
        self.weather_requests()

    def weather_requests(self):
        url = "http://api.weatherapi.com/v1/current.json"
        api_key = "7a0ceefd06cb41feb4643629231209"
        
        country = input("şehir giriniz:")
        
        response = requests.get(url,params={
                "key": api_key,
                "q":country,
                "lang":"tr"
        })
        try:
            result = response.json()
            sehir = result["location"]["region"]
            tempc = result["current"]["temp_c"]
            text = result["current"]["condition"]["text"]
            print(termcolor.colored(f"{sehir} anlık olarak {tempc} derece {text}",attrs=["bold"]))
        except KeyError:
            print(termcolor.colored("lütfen şehir adını doğru bir şekilde giriniz!",color="red",attrs=["bold"]))

#döngü ve kullanıcı seçimleri--------------------------------------
while True:
    try:
        userchoice = int(input(f"tarih:{now}\n***************\nHoşgeldiniz\n1-Haberler\n2-Döviz Hesapla\n3-Film Verileri\n4-Hava Durumu\n5-çıkış\n:"))
        if userchoice == 1:
            news = News()
        elif userchoice == 2:
            doviz = Doviz()
        elif userchoice == 3:
            movie = Movie()
        elif userchoice == 4:
            weather = Weather()
        elif userchoice == 5:
            exit()
    except ValueError as e:
        print("lütfen ekranda belirtilen sayılarla seçim yapın!\nERROR: " + str(e))