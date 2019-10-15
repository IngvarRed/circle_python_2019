# initials

s_name = input("Please type your Name Second name and .. >> ").split(" ")

for i in range(len(s_name)):
    if s_name[i] != "":
        print(s_name[i][0:1].upper(), end=".")
