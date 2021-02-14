# names_list = []
# names_list.append('Kamil')
# names_list.append('Mariusz')
#
# names_list = ["Kamil", "Mariusz", "Adam"]
#
# # names_list.reverse()
#
# names_list3 = names_list + names_list2
#
# print(names_list3)
#
# # names_list.sort(reverse = True)
#
# for name in names_list:
#     print(name)
#
# print(names_list.pop(0))
#
# names_list = ("Kamil", "Mariusz", "Adam", "Kamil")
#
# print(names_list)

# pusty_set = set()
names_set = {"Kamil", "Mariusz"}
#
# names_list = []
# names_tuple = ()
#
# names_set.add("Kamil")
# names_set.add("Domino")
#
# # names_set.remove("Kamil")
#
# names_set.discard("Kamil")
#
# print(names_set)

names_set2 = {"Mariusz", "Tyrus"}
names_list = ["Artur", "Rafał"]

names_set3 = names_set.union(names_set2)
names_set4 = names_set.difference(names_set2)

names_list.extend(names_set2)

for name in names_list:
    print(name)
