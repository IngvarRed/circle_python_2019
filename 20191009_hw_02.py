# A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward

pln = input("Please, type your palindrome : ")

if pln == pln[::-1]:
    print("Your phrase is palindrome !")
else:
    print("Your phrase is not palindrome !")