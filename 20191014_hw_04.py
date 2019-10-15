# Caesar's encryption

text_input = input(" Please type your text : ")
key_cs = int(input("Specify your code (integer) : "))

text_output = list("".join(text_input))
for i in range(len(text_input)):
    # print(text_output[i], ord(text_output[i]))
    if ("A" <= text_output[i] <= "Z") or ("a" <= text_output[i] <= "z"):
        text_output[i] = chr((ord(text_output[i]) + key_cs))
    print(text_output[i], end="")
