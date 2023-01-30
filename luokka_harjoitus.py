class Kasvi:
    def __init__ (self, suomalainen_nimi, latinalainen_nimi, kasvityyppi, kasvupaikka,):
        self.suomalainen_nimi = suomalainen_nimi
        self.latinalainen_nimi = latinalainen_nimi
        self.kasvityyppi = kasvityyppi
        self.kasvupaikka = kasvupaikka
        self.istutusvuosi = None

    def __str__(self):
        istutusvuosi = f'sen istutusvuosi on: -{self.istutusvuosi % 100:02d}' if self.istutusvuosi else ""
        return f'{self.suomalainen_nimi}, latinaksi {self.latinalainen_nimi} on {self.kasvityyppi} ja sen kasvupaikka on {self.kasvupaikka}{istutusvuosi}.'

voikukka = Kasvi('Voikukka', 'Taxum officinale', 'monivuotinen Kukka', 'niitty')
punaherukka = Kasvi('Punaherukka', 'Ribes rubrum', 'marjapensas', 'piha')

punaherukka.istutusvuosi = 2013

print(voikukka)
print(punaherukka)        