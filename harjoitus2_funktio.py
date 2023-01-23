#Tähän mennessä käytetyjä funktioita
# print(x)  tulostaa x
# X = input() luetaan merkkijono muuttujaan x
# str(X) muutetaan X merkkijonoksi

def kysy_nimi():
    nimi = input('Anna nimi: ')
    return nimi

# joku = kysy_nimi()
# print(joku)

def kysy_nimet(lkm):
    nimet = []
    while len(nimet) < lkm:
       nimi = kysy_nimi()
       nimet.append(nimi)
    return nimet


if __name__ == "__main__":
    nimilista = kysy_nimet(3)
    print(nimilista)


'''def kysy_nimet_rekursiolla(jäljellä, nimet=None):
    if jäljellä == 0:
        return nimet
    if nimet is None:
        nimet = []
    nimi = input("Anna nimi: ")
    return kysy_nimet_rekursiolla(jäljellä - 1, nimet + [nimi])
    
nimet = kysy_nimet_rekursiolla(3)
print(nimet)'''



