# list

week_days = []
print(week_days)
week_days = ['Monday', 'Tuesday', 'Wednesdayy']
print(week_days)
# first item in the list
print(week_days[0])
# slice
print(week_days[0:2])

another_list = list()
print(another_list)

# iterarate by string
ll1 = list('cat')
print(ll1)

ll2 = ['cat']
print(ll2)

ll3 = ['cat', 'dog']

# error
# ll4 = list('cat', 'dog')
# print(ll4)

# magic :)
ll4 = list(('cat', 'dog'))
print(ll4)