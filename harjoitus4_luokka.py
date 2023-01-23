class Ihminen:
    def __init__(self, etunimi, sukunimi, syntymävuosi):
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.syntymävuosi = syntymävuosi

    def __str__(self):
        return self.etunimi + ' ' + self.sukunimi + " (" + str(self.syntymävuosi) + ")"

henkilo1 = Ihminen('Sandro', 'Wuethrich', 1978)
henkilo2 = Ihminen('Petri', 'Huhtala', 1999)

print(henkilo1)
print(henkilo2)


