'''
greedy seller
25cent 10cent 5cent 1cent
'''
explntn = '''
In which country do we make the calculations? 
1 - USA
2 - EUROPE
3 - UKRAINE'''
print(explntn)
chz = True

chz = True
while chz:
    cntr = int(input("please write your choice : "))
    if 1<= cntr <= 3:
        chz = False

# avialable monets
if cntr == 1:
    monets = [25, 10, 5, 1]
elif cntr == 2:
    monets = [50, 20, 10, 5, 2, 1]
elif cntr == 3:
    monets = [50, 20, 10, 5, 2, 1]

change = round(float(input("O hi! How much change is owed ? : ")) * 100, 0)
amount = 0
i = 0
while change > 0:
    while i < len(monets):
        if change >= monets[i]:
            change = change - monets[i]
            amount += 1
        else:
            i += 1

print("this is your rest, " + str(amount) + " coins")