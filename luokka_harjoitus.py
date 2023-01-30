class Kasvi:
    def __init__ (self, suomalainen_nimi, latinalainen_nimi, kasvityyppi, kasvupaikka):
        self.suomalainen_nimi = suomalainen_nimi
        self.latinalainen_nimi = latinalainen_nimi
        self.kasvityyppi = kasvityyppi
        self.kasvupaikka = kasvupaikka

    def __str__(self):
        return f'{self.suomalainen_nimi}, latinaksi {self.latinalainen_nimi} on {self.kasvityyppi} ja sen kasvupaikka on {self.kasvupaikka}.'

voikukka = Kasvi('Voikukka', 'Taxum officinale', 'monivuotinen Kukka', 'niitty')
punaherukka = Kasvi('Punaherukka', 'Ribes rubrum', 'marjapensas', 'piha')

print(voikukka)
print(punaherukka)        