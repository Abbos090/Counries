from abc import ABC,abstractmethod

class Mamlakat(ABC):

    @abstractmethod

    def valyuta(self):
        pass

    def info(self):
        pass
        
    def get_space(self):
            pass

    def get_population(self):
        pass
    

class Uzbekistan(Mamlakat):
    def valyuta(self):
        return f"So'm"

    def info(self):
        return "O‘zbekiston – Markaziy Osiyodagi davlat. Poytaxti – Toshkent. Rasmiy tili – o‘zbek tili. Aholisi – taxminan 36 million kishi. Pul birligi – so‘m. Davlat boshqaruvi – prezidentlik respublikasi. Asosiy tarmoqlari – qishloq xo‘jaligi, sanoat, energetika. Mashhur shaharlari – Samarqand, Buxoro, Xiva."  

    def get_space(self):
        return "448,978 km²"

    def get_population(self):
        return 37000000
    
class USA(Mamlakat):
    def valyuta(self):
        return "Dollar"

    def info(self):
        return "Amerika Qo‘shma Shtatlari (AQSh) – Shimoliy Amerikadagi davlat. Poytaxti – Vashington. Eng yirik shahri – Nyu-York. Rasmiy tili – ingliz tili. Aholisi – taxminan 330 million. Pul birligi – AQSh dollari. Davlat boshqaruvi – prezidentlik respublikasi. Iqtisodiyotining asosiy tarmoqlari – texnologiya, sanoat, moliya, harbiy sanoat. 50 shtatdan iborat." 

    def get_space(self):
        return "9,525,067 km²"

    def get_population(self):
        return 334000000
    
class Russia(Mamlakat):
    def valyuta(self):
        return "Rubl"

    def info(self):
        return "Rossiya – dunyodagi eng katta davlat. Poytaxti – Moskva. Rasmiy tili – rus tili. Aholisi – taxminan 144 million. Pul birligi – rubl. Davlat boshqaruvi – prezidentlik respublikasi. Asosiy tarmoqlari – energetika, sanoat, mudofaa. Eng yirik shaharlari – Moskva, Sankt-Peterburg, Novosibirsk."    

    def get_space(self):
        return "17,098,246 km²"

    def get_population(self):
        return 146000000

class China(Mamlakat):
    def valyuta(self):
        return "Yuan"

    def info(self):
        return "Xitoy – Osiyodagi eng katta va eng ko‘p aholi yashaydigan davlat. Poytaxti – Pekin. Eng yirik shahri – Shanxay. Rasmiy tili – xitoy (mandarin). Aholisi – taxminan 1,4 milliard. Pul birligi – yuan (RMB). Davlat boshqaruvi – kommunistik tizim. Asosiy tarmoqlari – sanoat, texnologiya, savdo, qishloq xo‘jaligi. Dunyodagi eng yirik iqtisodiyotlardan biri." 

    def get_space(self):
        return "9,596,961 km²"

    def get_population(self):
        return 1500000000

class BB(Mamlakat):
    def valyuta(self):
        return "Funt Sterling"

    def info(self):
        return "Buyuk Britaniya – G‘arbiy Yevropada joylashgan orol davlati. Poytaxti – London. Rasmiy tili – ingliz tili. Aholisi – taxminan 67 million. Pul birligi – funt sterling (GBP). Davlat boshqaruvi – konstitutsion monarxiya. Asosiy tarmoqlari – moliya, sanoat, xizmatlar. Madaniyati, adabiyoti, san'ati va sporti bilan mashhur."  

    def get_space(self):
        return "243,610 km²"

    def get_population(self):
        return 68000000

class Japan(Mamlakat):
    def valyuta(self):
        return "Yen"

    def info(self):
        return "Yaponiya – Sharqiy Osiyodagi orol davlati. Poytaxti – Tokio. Rasmiy tili – yapon tili. Aholisi – taxminan 125 million. Pul birligi – yen (JPY). Davlat boshqaruvi – konstitutsion monarxiya. Asosiy tarmoqlari – texnologiya, avtomobil sanoati, robototexnika. Madaniyati, animelari va innovatsiyalari bilan mashhur."  

    def get_space(self):
        return "377,975 km²"

    def get_population(self):
        return 124000000


uzbekistan = Uzbekistan()
print(uzbekistan.get_population())