class Address:
    def __init__(self, index, country, city, street, house, apartment):
        self._index = index
        self._country = country
        self._city = city
        self._street = street
        self._house = house
        self._apartment = apartment

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, new_index):
        self._index = new_index

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, new_country):
        self._country = new_country

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, new_city):
        self._city = new_city

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, new_street):
        self._street = new_street

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, new_house):
        self._house = new_house

    @property
    def apartment(self):
        return self._apartment

    @apartment.setter
    def apartment(self, new_apartment):
        self._apartment = new_apartment


def main():
    address = Address(12345, "Україна", "Київ", "Вулиця Леніна", 1, 2)
    print(address.index, address.country, address.city, address.street, address.house, address.apartment)


if __name__ == "__main__":
    main()