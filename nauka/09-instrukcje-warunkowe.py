light = input("Jakie jest swiatlo?(red, green)")

if light == 'red':
    print("Czekaj")
elif light == 'yellow':
    print('czekaj')
else:
    print("Jedz")

print('jedz') if light == 'green' else print("Czekaj")