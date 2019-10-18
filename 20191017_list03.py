# list

ll = [12, 125]
print(ll)

ll[0] = 125478
print(ll)

ll[1] = [2, 4, 5, 6, 7]
print(ll)

ll[1:] = [2, 4, 5, 6, 7]
print(ll)

bord = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,1,1],
    [1,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0]
]
print(bord)

# todo How to pritify? ==> by loop
'''
  a b c d ..
------------
1 | 0 0 0
2 | 0 0
'''
playing_field = '''
    a b c d e f g h i j
  ---------------------'''
print(playing_field)
for i, l_board in enumerate(bord):
    print(i, "| ", end="")
    for n in range(len(l_board)):
        print(l_board[n], "", end="")
    print()
