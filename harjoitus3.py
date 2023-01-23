import time
from harjoitus2_funktio import kysy_nimi
from pprint import pprint

aikaleima = time.time()
print(aikaleima)

aikateksti = time.ctime(aikaleima)
print(aikateksti)

aika_1 = time.time()

time.sleep(3)

aika_2 = time.time()

print(aika_1)
print(aika_2)
print(aika_2 - aika_1)

nimimerkintä = kysy_nimi()
print(nimimerkintä)

esimerkki_kuvio = {
    "nimi": "Esimerkki",
    "tyyppi": "monikulmio",
    "luotu": time.ctime(aikaleima),
    "pisteet": [
        {"x": 10, "y": 20, "z": 30},
        {"x": 20, "y": 5, "z": 10},
        {"x": 30, "y": 15, "z": 20},
    ]
}

pprint(esimerkki_kuvio, sort_dicts=False)
