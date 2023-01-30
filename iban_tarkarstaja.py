from stdnum import iban


def main():
    tilinumero = input('Anna IBAN-tilinumero: ')
    on_oikea_iban = iban.is_valid(tilinumero)
    if on_oikea_iban:
        print(f"Antamasi tilinumero {tilinumero} on oikea IBAN")
        muotoilu = iban.format(tilinumero)
        print(f'Tilinumero muotoiltuna: {muotoilu}')
    else:
        print(f"Antamasi tilinumer {tilinumero} ei ole oikea IBAN")


if __name__ == '__main__':
    main()

