countries_and_capitals = {"Poland":"Warsaw", "Germany":"Berlin"}
countries_and_capitals['Czechia'] = "Prague"

# print(countries_and_capitals)
#
# for country, capital in countries_and_capitals.items():
#     print(country+ "-" + capital)

# print(countries_and_capitals["Poland"])
# print(countries_and_capitals.get("Poland"))

print(countries_and_capitals.setdefault("USA", "Washington DC"))

if "Poland" in countries_and_capitals.keys():
    print("Znaleziono ")