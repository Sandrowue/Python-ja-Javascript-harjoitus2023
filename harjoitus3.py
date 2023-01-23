import time
from harjoitus2_funktio import kysy_nimi

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
