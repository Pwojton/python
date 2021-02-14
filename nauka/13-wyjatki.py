countries_and_capitals = {'Poland':'Warsaw'}


try:
    print(2 / 0)
    print(countries_and_capitals['USA'])
except KeyError:
    print("Klucz nie został znaleziony")
except ZeroDivisionError:
    print("Nie można dzielić przez zero")