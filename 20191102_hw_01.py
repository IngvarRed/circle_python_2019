# animals
animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
animals.update({'d': 'hiena'})

print("   | key | value","\n","-"*20)
for nmr, item in enumerate((animals)):
    print(f"{(nmr+1): 02} | {item}   | {animals[item]}")

# print(animals)

print(f"Lenght of dict <animals> is {len(animals)}")

while True:
    print("For exit please type '0' ")
    key_a = input("Type your key, I chek it if present in our dictionary : ")
    if key_a == "0":
        break
    elif animals.get(key_a):
        print(f"Yes! Your key {key_a} presented in dictionary <animals> = {animals[key_a]}")
    else:
        print(f"Your key {key_a} not present !")
