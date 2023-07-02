def anagram(text):
    printable = ''
    for x in range(0, a, 3):
        str_a = text[x]
        str_b = text[x+1]
        str_c = text[x+2]
        printable = printable + str_b + str_c + str_a

    return printable


def de_anagram(text):
    printable = ''
    for x in range(0, a, 3):
        str_a = text[x]
        str_b = text[x+1]
        str_c = text[x+2]
        printable = printable + str_c + str_a + str_b

    return printable


inp = input("Enter :")
a = len(inp)

if a % 3 == 1:
    inp = inp + "  "
elif a % 3 == 2:
    inp = inp + " "

out1 = anagram(inp)
out2 = de_anagram(inp)
print(out1)
print(out2)
