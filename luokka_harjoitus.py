class Kasvi:
    def __init__ (self, suomalainen_nimi, latinalainen_nimi, kasvityyppi, kasvupaikka,):
        self.suomalainen_nimi = suomalainen_nimi
        self.latinalainen_nimi = latinalainen_nimi
        self.kasvityyppi = kasvityyppi
        self.kasvupaikka = kasvupaikka
        self.istutusvuousi = None

        istutusvuosi = f'sen istutusvuosi on: -{self.istutusvuousi % 100:02d}' if self.istutusvuousi else ""

    def __str__(self):
        return f'{self.suomalainen_nimi}, latinaksi {self.latinalainen_nimi} on {self.kasvityyppi} ja sen kasvupaikka on {self.kasvupaikka}{self.istutusvuousi}.'

voikukka = Kasvi('Voikukka', 'Taxum officinale', 'monivuotinen Kukka', 'niitty')
punaherukka = Kasvi('Punaherukka', 'Ribes rubrum', 'marjapensas', 'piha')

punaherukka.istutusvuousi = '2013'

print(voikukka)
print(punaherukka)        