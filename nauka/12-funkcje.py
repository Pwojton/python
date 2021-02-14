countries_information = {}
countries_information["Polska"] = ("Warszawa", 37.97)
countries_information["Niemcy"] = ("Berlin", 83.02)
countries_information["Słowacja"] = ("Bratysława", 5.45)

for country in countries_information.keys():
    print(country)

def show_country_info(country):
    country_information = countries_information.get(country)
    print()
    print(country)
    print("Stolica: " + country_information[0])
    print("Liczba mieszakńców (mln): " + str(country_information[1]))

country = input("Informacje o jakim kraju chcesz wyświetlić")
show_country_info(country)



