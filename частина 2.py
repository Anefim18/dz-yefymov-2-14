class Converter:
    def __init__(self, usd, eur, pln):
        self.usd = usd
        self.eur = eur
        self.pln = pln

    def convert_to_usd(self, amount):
        return int(amount / self.usd)

    def convert_to_eur(self, amount):
        return int(amount / self.eur)

    def convert_to_pln(self, amount):
        return int(amount / self.pln)

    def convert_from_usd(self, amount):
        return int(amount * self.usd)

    def convert_from_eur(self, amount):
        return int(amount * self.eur)

    def convert_from_pln(self, amount):
        return int(amount * self.pln)


def main():
    converter = Converter(27.0, 33.0, 3.0)

    # Конвертація з гривні в інші валюти
    print("100 гривень в доларах США:", converter.convert_to_usd(100))
    print("100 гривень в євро:", converter.convert_to_eur(100))
    print("100 гривень в польських злотих:", converter.convert_to_pln(100))

    # Конвертація з інших валют у гривні
    print("100 доларів США в гривнях:", converter.convert_from_usd(100))
    print("100 євро в гривнях:", converter.convert_from_eur(100))
    print("100 польських злотих в гривнях:", converter.convert_from_pln(100))


if __name__ == "__main__":
    main()
    