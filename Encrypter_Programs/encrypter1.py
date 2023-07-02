import random as rd
import time

inp = input("Enter text to be encrypted or decrypted : ")
print("Enter decision:")
print("0. Encryption")
dec = int(input("1. Decryption :"))
a_ = len(inp)

if a_ % 6 == 1:
    inp = inp + '     '
elif a_ % 6 == 2:
    inp = inp + '    '
elif a_ % 6 == 3:
    inp = inp + '   '
elif a_ % 6 == 4:
    inp = inp + '  '
elif a_ % 6 == 5:
    inp = inp + ' '
else:
    inp = inp


rnd = rd.randint(0, 7)
rnd1 = rd.randint(0, 7)
rnd2 = rd.randint(0, 7)
rnd3 = rd.randint(0, 7)
rnd4 = rd.randint(0, 7)
rnd5 = rd.randint(0, 7)
rnd6 = rd.randint(0, 7)
rnd8 = rd.randint(0, 7)
rnd7 = rd.randint(0, 7)
rnd0 = rd.randint(0, 7)
rnd10 = rd.randint(0, 7)
rnd20 = rd.randint(0, 7)
rnd30 = rd.randint(0, 7)
rnd40 = rd.randint(0, 7)
rnd50 = rd.randint(0, 7)
rnd60 = rd.randint(0, 7)
rnd70 = rd.randint(0, 7)
rnd80 = rd.randint(0, 7)


def split_string(string):
    even_chars = ""
    odd_chars = ""
    for ctrl in range(len(string)):
        if ctrl % 2 == 0:
            even_chars += string[ctrl]
        else:
            odd_chars += string[ctrl]
    return odd_chars, even_chars


def combine_strings(s1, s2):
    combined_string = ""
    for ctrl in range(min(len(s1), len(s2))):
        combined_string += s1[ctrl] + s2[ctrl]
    if len(s1) > len(s2):
        combined_string += s1[len(s2):]
    elif len(s2) > len(s1):
        combined_string += s2[len(s1):]
    return combined_string


def anagram(text, lt):
    printable = ''
    lt = int(lt)
    for x in range(0, lt, 3):
        str_a = text[x]
        str_b = text[x+1]
        str_c = text[x+2]
        printable = printable + str_b + str_c + str_a

    return printable


def de_anagram(text, lt):
    printable = ''
    lt = int(lt)
    for x in range(0, lt, 3):
        str_a = text[x]
        str_b = text[x+1]
        str_c = text[x+2]
        printable = printable + str_c + str_a + str_b

    return printable


cnv1 = {
    '1': 'x', '2': 'M', '3': 'H', '4': 'A', '5': 'y', '6': 'l',
    '7': 'o', '8': 'r', '9': 'd', '0': '-', 'a': '{', 'b': '"',
    'c': '^', 'd': "'", 'e': 'T', 'f': 'R', 'g': 'W', 'h': 'L',
    'i': '[', 'j': '1', 'k': ')', 'l': 'K', 'm': '4', 'n': '@',
    'o': 'B', 'p': '#', 'q': ':', 'r': 'U', 's': '*', 't': '|',
    'u': 'h', 'v': '<', 'w': 't', 'x': 'j', 'y': 'S', 'z': '(',
    'A': 'm', 'B': '7', 'C': 'O', 'D': 'v', 'E': 'e', 'F': '+',
    'G': ';', 'H': '?', 'I': '0', 'J': 'X', 'K': '6', 'L': 'u',
    'M': 'Q', 'N': 'C', 'O': 'N', 'P': 'g', 'Q': '2', 'R': '$',
    'S': '5', 'T': 'E', 'U': '8', 'V': '_', 'W': 'P', 'X': '!',
    'Y': ',', 'Z': 'G', '[': '=', ']': 'n', '\\': 'S', ';': 'Z',
    ' ': 'a', ',': '&', '.': 'V', '/': 'F', '{': ' ', '}': 'p',
    '|': 'w', ':': '`', '"': '>', '<': 'v', '>': 'b', '?': '3',
    '~': 'z', '`': 'q', '-': 'I', '=': 'i', '!': 'J', '@': ']',
    '#': '}', '$': 'f', '%': 'c', '^': '%', '&': 'Y', '*': '\\',
    '(': '~', ')': '₹', '_': '.', "+": '/', "'": '9', '₹': 'k'
}
cnv1d = {v: k for k, v in cnv1.items()}


def conv1(inp_conv1):
    string1 = ''
    for x in inp_conv1:
        temp = x
        string1 = string1 + cnv1[temp]

    return string1


def de_converter1(encrypted_str):
    decrypted_str = ''
    for char in encrypted_str:
        if char in cnv1d:
            decrypted_str += cnv1d[char]
        else:
            decrypted_str += char
    return decrypted_str


cnv2 = {
    '1': 'h', '2': 'e', '3': 'l', '4': 'p', '5': 'z', '6': 'j',
    '7': 'u', '8': 'b', '9': 'g', '0': 'd', 'a': '@', 'b': 'o',
    'c': '&', 'd': '#', 'e': '{', 'f': 'N', 'g': 'i', 'h': '0',
    'i': 'x', 'j': 'n', 'k': 'C', 'l': '4', 'm': '<', 'n': 'O',
    'o': 'r', 'p': 'B', 'q': 'v', 'r': '*', 's': '\\', 't': '5',
    'u': 'M', 'v': 'I', 'w': 'q', 'x': 'T', 'y': '(', 'z': 'm',
    'A': 'Z', 'B': ':', 'C': '7', 'D': '.', 'E': '=', 'F': '_',
    'G': 'L', 'H': 'X', 'I': 'y', 'J': 'F', 'K': 'P', 'L': 'V',
    'M': "'", 'N': 's', 'O': 'W', 'P': '+', 'Q': '|', 'R': 'Y',
    'S': '-', 'T': '?', 'U': 'H', 'V': ']', 'W': '$', 'X': 'E',
    'Y': 'f', 'Z': '[', '[': ')', ']': '`', '\\': 'R', ';': 'U',
    ' ': 'c', ',': ' ', '.': 'A', '/': '1', '{': '^', '}': '"',
    '|': '2', ':': '3', '"': ',', '<': '!', '>': 'G', '?': '9',
    '~': 'a', '`': '>', '-': '%', '=': ';', '!': 't', '@': 'J',
    '#': '/', '$': '6', '%': 'K', '^': 'Q', '&': '}', '*': '₹',
    '(': 'w', ')': 'D', '_': '~', "+": 'S', "'": 'k', '₹': '8'
}
cnv2d = {v: k for k, v in cnv2.items()}


def conv2(inp_conv2):
    string2 = ''
    for x in inp_conv2:
        temp = x
        string2 = string2 + cnv2[temp]

    return string2


def de_converter2(encrypted_str):
    decrypted_str = ''
    for char in encrypted_str:
        if char in cnv2d:
            decrypted_str += cnv2d[char]
        else:
            decrypted_str += char
    return decrypted_str


cnv3 = {
    '1': '7', '2': '8', '3': '9', '4': '0', '5': 'a', '6': 'b',
    '7': 'c', '8': 'd', '9': 'e', '0': 'f', 'a': 'g', 'b': 'h',
    'c': 'i', 'd': 'j', 'e': 'k', 'f': 'l', 'g': 'm', 'h': 'n',
    'i': 'o', 'j': 'p', 'k': 'q', 'l': 'r', 'm': 's', 'n': 't',
    'o': 'u', 'p': 'v', 'q': 'w', 'r': 'x', 's': 'y', 't': 'z',
    'u': 'A', 'v': 'B', 'w': 'C', 'x': 'D', 'y': 'E', 'z': 'F',
    'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K', 'F': 'L',
    'G': 'M', 'H': 'N', 'I': 'O', 'J': 'P', 'K': 'Q', 'L': 'R',
    'M': 'S', 'N': 'T', 'O': 'U', 'P': 'V', 'Q': 'W', 'R': 'X',
    'S': 'Y', 'T': 'Z', 'U': '[', 'V': ']', 'W': '\\', 'X': ';',
    'Y': ' ', 'Z': ',', '[': '.', ']': '/', '\\': '{', ';': '}',
    ' ': '|', ',': ':', '.': '"', '/': '<', '{': '>', '}': '?',
    '|': '~', ':': '`', '"': '-', '<': '=', '>': '!', '?': '@',
    '~': '#', '`': '$', '-': '%', '=': '^', '!': '&', '@': '*',
    '#': '(', '$': ')', '%': '_', '^': '+', '&': "'", '*': '₹',
    '(': '1', ')': '2', '_': '3', "+": '4', "'": '5', '₹': '6'
}
cnv3d = {v: k for k, v in cnv3.items()}


def conv3(inp_conv3):
    string3 = ''
    for x in inp_conv3:
        temp = x
        string3 = string3 + cnv3[temp]

    return string3


def de_converter3(encrypted_str):
    decrypted_str = ''
    for char in encrypted_str:
        if char in cnv3d:
            decrypted_str += cnv3d[char]
        else:
            decrypted_str += char
    return decrypted_str


cnv4 = {
    '1': '(', '2': ')', '3': '_', '4': '+', '5': "'", '6': '₹',
    '7': '1', '8': '2', '9': '3', '0': '4', 'a': '5', 'b': '6',
    'c': '7', 'd': '8', 'e': '9', 'f': '0', 'g': 'a', 'h': 'b',
    'i': 'c', 'j': 'd', 'k': 'e', 'l': 'f', 'm': 'g', 'n': 'h',
    'o': 'i', 'p': 'j', 'q': 'k', 'r': 'l', 's': 'm', 't': 'n',
    'u': 'o', 'v': 'p', 'w': 'q', 'x': 'r', 'y': 's', 'z': 't',
    'A': 'u', 'B': 'v', 'C': 'w', 'D': 'x', 'E': 'y', 'F': 'z',
    'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D', 'K': 'E', 'L': 'F',
    'M': 'G', 'N': 'H', 'O': 'I', 'P': 'J', 'Q': 'K', 'R': 'L',
    'S': 'M', 'T': 'N', 'U': 'O', 'V': 'P', 'W': 'Q', 'X': 'R',
    'Y': 'S', 'Z': 'T', '[': 'U', ']': 'V', '\\': 'W', ';': 'X',
    ' ': 'Y', ',': 'Z', '.': '[', '/': ']', '{': '\\', '}': ';',
    '|': ' ', ':': ',', '"': '.', '<': '/', '>': '{', '?': '}',
    '~': '|', '`': ':', '-': '"', '=': '<', '!': '>', '@': '?',
    '#': '~', '$': '`', '%': '-', '^': '=', '&': '!', '*': '@',
    '(': '#', ')': '$', '_': '%', "+": '^', "'": '&', '₹': '*'
}
cnv4d = {v: k for k, v in cnv4.items()}


def conv4(inp_conv4):
    string4 = ''
    for x in inp_conv4:
        temp = x
        string4 = string4 + cnv4[temp]

    return string4


def de_converter4(encrypted_str):
    decrypted_str = ''
    for char in encrypted_str:
        if char in cnv4d:
            decrypted_str += cnv4d[char]
        else:
            decrypted_str += char
    return decrypted_str


cnv5 = {
    '1': '8', '2': '9', '3': '0', '4': 'a', '5': 'b', '6': '7',
    '7': 'd', '8': 'e', '9': 'f', '0': 'g', 'a': 'h', 'b': 'c',
    'c': 'j', 'd': 'k', 'e': 'l', 'f': 'm', 'g': 'n', 'h': 'i',
    'i': 'p', 'j': 'q', 'k': 'r', 'l': 's', 'm': 't', 'n': 'o',
    'o': 'v', 'p': 'w', 'q': 'x', 'r': 'y', 's': 'z', 't': 'u',
    'u': '2', 'v': '3', 'w': '4', 'x': '5', 'y': '6', 'z': '1',
    'A': 'H', 'B': 'I', 'C': 'J', 'D': 'K', 'E': 'L', 'F': 'G',
    'G': 'N', 'H': 'O', 'I': 'P', 'J': 'Q', 'K': 'R', 'L': 'M',
    'M': 'T', 'N': 'U', 'O': 'V', 'P': 'W', 'Q': 'X', 'R': 'S',
    'S': 'Z', 'T': '[', 'U': ']', 'V': '\\', 'W': ';', 'X': 'Y',
    'Y': ',', 'Z': '.', '[': '/', ']': '{', '\\': '}', ';': ' ',
    ' ': 'B', ',': 'C', '.': 'D', '/': 'E', '{': 'F', '}': 'A',
    '|': '+', ':': '(', '"': ')', '<': '~', '>': '@', '?': '!',
    '~': '$', '`': '|', '-': ':', '=': '"', '!': '?', '@': '>',
    '#': '=', '$': '_', '%': '`', '^': '-', '&': '₹', '*': "'",
    '(': '^', ')': '#', '_': '<', "+": '%', "'": '*', '₹': '&'
}
cnv5d = {v: k for k, v in cnv5.items()}


def conv5(inp_conv5):
    string5 = ''
    for x in inp_conv5:
        temp = x
        string5 = string5 + cnv5[temp]

    return string5


def de_converter5(encrypted_str):
    decrypted_str = ''
    for char in encrypted_str:
        if char in cnv5d:
            decrypted_str += cnv5d[char]
        else:
            decrypted_str += char
    return decrypted_str


cnv6 = {
    '1': '6', '2': '5', '3': '4', '4': '3', '5': '2', '6': '1',
    '7': 'b', '8': 'a', '9': '0', '0': '9', 'a': '8', 'b': '7',
    'c': 'h', 'd': 'g', 'e': 'f', 'f': 'e', 'g': 'd', 'h': 'c',
    'i': 'n', 'j': 'm', 'k': 'l', 'l': 'k', 'm': 'j', 'n': 'i',
    'o': 't', 'p': 's', 'q': 'r', 'r': 'q', 's': 'p', 't': 'o',
    'u': 'z', 'v': 'y', 'w': 'x', 'x': 'w', 'y': 'v', 'z': 'u',
    'A': 'F', 'B': 'E', 'C': 'D', 'D': 'C', 'E': 'B', 'F': 'A',
    'G': 'L', 'H': 'K', 'I': 'J', 'J': 'I', 'K': 'H', 'L': 'G',
    'M': 'R', 'N': 'Q', 'O': 'P', 'P': 'O', 'Q': 'N', 'R': 'M',
    'S': 'X', 'T': 'W', 'U': 'V', 'V': 'U', 'W': 'T', 'X': 'S',
    'Y': ';', 'Z': '\\', '[': ']', ']': '[', '\\': 'Z', ';': 'Y',
    ' ': '{', ',': '}', '.': '/', '/': '.', '{': ',', '}': ' ',
    '|': '?', ':': '>', '"': '<', '<': '"', '>': ':', '?': '|',
    '~': '@', '`': '!', '-': '=', '=': '-', '!': '`', '@': '~',
    '#': '*', '$': '&', '%': '^', '^': '%', '&': '$', '*': '#',
    '(': '₹', ')': "'", '_': '+', "+": '_', "'": ')', '₹': '('
}
cnv6d = {v: k for k, v in cnv6.items()}


def conv6(inp_conv6):
    string6 = ''
    for x in inp_conv6:
        temp = x
        string6 = string6 + cnv6[temp]

    return string6


def de_converter6(encrypted_str):
    decrypted_str = ''
    for char in encrypted_str:
        if char in cnv6d:
            decrypted_str += cnv6d[char]
        else:
            decrypted_str += char
    return decrypted_str


cnv7 = {
    '1': '(', '2': ')', '3': '_', '4': '+', '5': "'", '6': '₹',
    '7': '#', '8': '$', '9': '%', '0': '^', 'a': '&', 'b': '*',
    'c': '~', 'd': '`', 'e': '-', 'f': '=', 'g': '!', 'h': '@',
    'i': '|', 'j': ':', 'k': '"', 'l': '<', 'm': '>', 'n': '?',
    'o': ' ', 'p': ',', 'q': '.', 'r': '/', 's': '{', 't': '}',
    'u': 'Y', 'v': 'Z', 'w': '[', 'x': ']', 'y': '\\', 'z': ';',
    'A': 'S', 'B': 'T', 'C': 'U', 'D': 'V', 'E': 'W', 'F': 'X',
    'G': 'M', 'H': 'N', 'I': 'O', 'J': 'P', 'K': 'Q', 'L': 'R',
    'M': 'G', 'N': 'H', 'O': 'I', 'P': 'J', 'Q': 'K', 'R': 'L',
    'S': 'A', 'T': 'B', 'U': 'C', 'V': 'D', 'W': 'E', 'X': 'F',
    'Y': 'u', 'Z': 'v', '[': 'w', ']': 'x', '\\': 'y', ';': 'z',
    ' ': 'o', ',': 'p', '.': 'q', '/': 'r', '{': 's', '}': 't',
    '|': 'i', ':': 'j', '"': 'k', '<': 'l', '>': 'm', '?': 'n',
    '~': 'c', '`': 'd', '-': 'e', '=': 'f', '!': 'g', '@': 'h',
    '#': '7', '$': '8', '%': '9', '^': '0', '&': 'a', '*': 'b',
    '(': '1', ')': '2', '_': '3', "+": '4', "'": '5', '₹': '6'
}
cnv7d = {v: k for k, v in cnv7.items()}


def conv7(inp_conv7):
    string7 = ''
    for x in inp_conv7:
        temp = x
        string7 = string7 + cnv7[temp]

    return string7


def de_converter7(encrypted_str):
    decrypted_str = ''
    for char in encrypted_str:
        if char in cnv7d:
            decrypted_str += cnv7d[char]
        else:
            decrypted_str += char
    return decrypted_str


cnv8 = {
    '1': 'M', '2': 'N', '3': 'O', '4': 'P', '5': 'Q', '6': 'R',
    '7': 'S', '8': 'T', '9': 'U', '0': 'V', 'a': 'W', 'b': 'X',
    'c': 'Y', 'd': 'Z', 'e': '[', 'f': ']', 'g': '\\', 'h': ';',
    'i': ' ', 'j': ',', 'k': '.', 'l': '/', 'm': '{', 'n': '}',
    'o': '|', 'p': ':', 'q': '"', 'r': '<', 's': '>', 't': '?',
    'u': '~', 'v': '`', 'w': '-', 'x': '=', 'y': '!', 'z': '@',
    'A': '#', 'B': '$', 'C': '%', 'D': '^', 'E': '&', 'F': '*',
    'G': '(', 'H': ')', 'I': '_', 'J': '+', 'K': "'", 'L': '₹',
    'M': '1', 'N': '2', 'O': '3', 'P': '4', 'Q': '5', 'R': '6',
    'S': '7', 'T': '8', 'U': '9', 'V': '0', 'W': 'a', 'X': 'b',
    'Y': 'c', 'Z': 'd', '[': 'e', ']': 'f', '\\': 'g', ';': 'h',
    ' ': 'i', ',': 'j', '.': 'k', '/': 'l', '{': 'm', '}': 'n',
    '|': 'o', ':': 'p', '"': 'q', '<': 'r', '>': 's', '?': 't',
    '~': 'u', '`': 'v', '-': 'w', '=': 'x', '!': 'y', '@': 'z',
    '#': 'A', '$': 'B', '%': 'C', '^': 'D', '&': 'E', '*': 'F',
    '(': 'G', ')': 'H', '_': 'I', "+": 'J', "'": 'K', '₹': 'L'
}
cnv8d = {v: k for k, v in cnv8.items()}


def conv8(inp_conv8):
    string8 = ''
    for x in inp_conv8:
        temp = x
        string8 = string8 + cnv8[temp]

    return string8


def de_converter8(encrypted_str):  # encrypted_str:
    decrypted_str = ''
    for char in encrypted_str:
        if char in cnv8d:
            decrypted_str += cnv8d[char]
        else:
            decrypted_str += char

    return decrypted_str


if int(dec) == 0:
    ana_1 = anagram(inp, len(inp))
    odd, even = split_string(ana_1)

    if rnd % 8 == 0:
        a = (str(rnd) + conv8(odd))
    elif rnd % 8 == 1:
        a = (str(rnd) + conv1(odd))
    elif rnd % 8 == 2:
        a = (str(rnd) + conv2(odd))
    elif rnd % 8 == 3:
        a = (str(rnd) + conv3(odd))
    elif rnd % 8 == 4:
        a = (str(rnd) + conv4(odd))
    elif rnd % 8 == 5:
        a = (str(rnd) + conv5(odd))
    elif rnd % 8 == 6:
        a = (str(rnd) + conv6(odd))
    elif rnd % 8 == 7:
        a = (str(rnd) + conv7(odd))
    else:
        a = ""

    if rnd1 % 8 == 0:
        b = (str(rnd1) + conv8(a))
    elif rnd1 % 8 == 1:
        b = (str(rnd1) + conv1(a))
    elif rnd1 % 8 == 2:
        b = (str(rnd1) + conv2(a))
    elif rnd1 % 8 == 3:
        b = (str(rnd1) + conv3(a))
    elif rnd1 % 8 == 4:
        b = (str(rnd1) + conv4(a))
    elif rnd1 % 8 == 5:
        b = (str(rnd1) + conv5(a))
    elif rnd1 % 8 == 6:
        b = (str(rnd1) + conv6(a))
    elif rnd1 % 8 == 7:
        b = (str(rnd1) + conv7(a))
    else:
        b = ""

    if rnd2 % 8 == 0:
        c = (str(rnd2) + conv8(b))
    elif rnd2 % 8 == 1:
        c = (str(rnd2) + conv1(b))
    elif rnd2 % 8 == 2:
        c = (str(rnd2) + conv2(b))
    elif rnd2 % 8 == 3:
        c = (str(rnd2) + conv3(b))
    elif rnd2 % 8 == 4:
        c = (str(rnd2) + conv4(b))
    elif rnd2 % 8 == 5:
        c = (str(rnd2) + conv5(b))
    elif rnd2 % 8 == 6:
        c = (str(rnd2) + conv6(b))
    elif rnd2 % 8 == 7:
        c = (str(rnd2) + conv7(b))
    else:
        c = ""

    if rnd3 % 8 == 0:
        d = (str(rnd3) + conv8(c))
    elif rnd3 % 8 == 1:
        d = (str(rnd3) + conv1(c))
    elif rnd3 % 8 == 2:
        d = (str(rnd3) + conv2(c))
    elif rnd3 % 8 == 3:
        d = (str(rnd3) + conv3(c))
    elif rnd3 % 8 == 4:
        d = (str(rnd3) + conv4(c))
    elif rnd3 % 8 == 5:
        d = (str(rnd3) + conv5(c))
    elif rnd3 % 8 == 6:
        d = (str(rnd3) + conv6(c))
    elif rnd3 % 8 == 7:
        d = (str(rnd3) + conv7(c))
    else:
        d = ""

    if rnd4 % 8 == 0:
        e = (str(rnd4) + conv8(d))
    elif rnd4 % 8 == 1:
        e = (str(rnd4) + conv1(d))
    elif rnd4 % 8 == 2:
        e = (str(rnd4) + conv2(d))
    elif rnd4 % 8 == 3:
        e = (str(rnd4) + conv3(d))
    elif rnd4 % 8 == 4:
        e = (str(rnd4) + conv4(d))
    elif rnd4 % 8 == 5:
        e = (str(rnd4) + conv5(d))
    elif rnd4 % 8 == 6:
        e = (str(rnd4) + conv6(d))
    elif rnd4 % 8 == 7:
        e = (str(rnd4) + conv7(d))
    else:
        e = ""

    if rnd5 % 8 == 0:
        f = (str(rnd5) + conv8(e))
    elif rnd5 % 8 == 1:
        f = (str(rnd5) + conv1(e))
    elif rnd5 % 8 == 2:
        f = (str(rnd5) + conv2(e))
    elif rnd5 % 8 == 3:
        f = (str(rnd5) + conv3(e))
    elif rnd5 % 8 == 4:
        f = (str(rnd5) + conv4(e))
    elif rnd5 % 8 == 5:
        f = (str(rnd5) + conv5(e))
    elif rnd5 % 8 == 6:
        f = (str(rnd5) + conv6(e))
    elif rnd5 % 8 == 7:
        f = (str(rnd5) + conv7(e))
    else:
        f = ""

    if rnd6 % 8 == 0:
        g = (str(rnd6) + conv8(f))
    elif rnd6 % 8 == 1:
        g = (str(rnd6) + conv1(f))
    elif rnd6 % 8 == 2:
        g = (str(rnd6) + conv2(f))
    elif rnd6 % 8 == 3:
        g = (str(rnd6) + conv3(f))
    elif rnd6 % 8 == 4:
        g = (str(rnd6) + conv4(f))
    elif rnd6 % 8 == 5:
        g = (str(rnd6) + conv5(f))
    elif rnd6 % 8 == 6:
        g = (str(rnd6) + conv6(f))
    elif rnd6 % 8 == 7:
        g = (str(rnd6) + conv7(f))
    else:
        g = ""

    if rnd7 % 8 == 0:
        h = (str(rnd7) + conv8(g))
    elif rnd7 % 8 == 1:
        h = (str(rnd7) + conv1(g))
    elif rnd7 % 8 == 2:
        h = (str(rnd7) + conv2(g))
    elif rnd7 % 8 == 3:
        h = (str(rnd7) + conv3(g))
    elif rnd7 % 8 == 4:
        h = (str(rnd7) + conv4(g))
    elif rnd7 % 8 == 5:
        h = (str(rnd7) + conv5(g))
    elif rnd7 % 8 == 6:
        h = (str(rnd7) + conv6(g))
    elif rnd7 % 8 == 7:
        h = (str(rnd7) + conv7(g))
    else:
        h = ""

    if rnd8 % 8 == 0:
        i = (str(rnd8) + conv8(h))
    elif rnd8 % 8 == 1:
        i = (str(rnd8) + conv1(h))
    elif rnd8 % 8 == 2:
        i = (str(rnd8) + conv2(h))
    elif rnd8 % 8 == 3:
        i = (str(rnd8) + conv3(h))
    elif rnd8 % 8 == 4:
        i = (str(rnd8) + conv4(h))
    elif rnd8 % 8 == 5:
        i = (str(rnd8) + conv5(h))
    elif rnd8 % 8 == 6:
        i = (str(rnd8) + conv6(h))
    elif rnd8 % 8 == 7:
        i = (str(rnd8) + conv7(h))
    else:
        i = ""

    if rnd0 % 8 == 0:
        a1 = (str(rnd0) + conv8(even))
    elif rnd0 % 8 == 1:
        a1 = (str(rnd0) + conv1(even))
    elif rnd0 % 8 == 2:
        a1 = (str(rnd0) + conv2(even))
    elif rnd0 % 8 == 3:
        a1 = (str(rnd0) + conv3(even))
    elif rnd0 % 8 == 4:
        a1 = (str(rnd0) + conv4(even))
    elif rnd0 % 8 == 5:
        a1 = (str(rnd0) + conv5(even))
    elif rnd0 % 8 == 6:
        a1 = (str(rnd0) + conv6(even))
    elif rnd0 % 8 == 7:
        a1 = (str(rnd0) + conv7(even))
    else:
        a1 = ""

    if rnd10 % 8 == 0:
        b1 = (str(rnd10) + conv8(a1))
    elif rnd10 % 8 == 1:
        b1 = (str(rnd10) + conv1(a1))
    elif rnd10 % 8 == 2:
        b1 = (str(rnd10) + conv2(a1))
    elif rnd10 % 8 == 3:
        b1 = (str(rnd10) + conv3(a1))
    elif rnd10 % 8 == 4:
        b1 = (str(rnd10) + conv4(a1))
    elif rnd10 % 8 == 5:
        b1 = (str(rnd10) + conv5(a1))
    elif rnd10 % 8 == 6:
        b1 = (str(rnd10) + conv6(a1))
    elif rnd10 % 8 == 7:
        b1 = (str(rnd10) + conv7(a1))
    else:
        b1 = ""

    if rnd20 % 8 == 0:
        c1 = (str(rnd20) + conv8(b1))
    elif rnd20 % 8 == 1:
        c1 = (str(rnd20) + conv1(b1))
    elif rnd20 % 8 == 2:
        c1 = (str(rnd20) + conv2(b1))
    elif rnd20 % 8 == 3:
        c1 = (str(rnd20) + conv3(b1))
    elif rnd20 % 8 == 4:
        c1 = (str(rnd20) + conv4(b1))
    elif rnd20 % 8 == 5:
        c1 = (str(rnd20) + conv5(b1))
    elif rnd20 % 8 == 6:
        c1 = (str(rnd20) + conv6(b1))
    elif rnd20 % 8 == 7:
        c1 = (str(rnd20) + conv7(b1))
    else:
        c1 = ""

    if rnd30 % 8 == 0:
        d1 = (str(rnd30) + conv8(c1))
    elif rnd30 % 8 == 1:
        d1 = (str(rnd30) + conv1(c1))
    elif rnd30 % 8 == 2:
        d1 = (str(rnd30) + conv2(c1))
    elif rnd30 % 8 == 3:
        d1 = (str(rnd30) + conv3(c1))
    elif rnd30 % 8 == 4:
        d1 = (str(rnd30) + conv4(c1))
    elif rnd30 % 8 == 5:
        d1 = (str(rnd30) + conv5(c1))
    elif rnd30 % 8 == 6:
        d1 = (str(rnd30) + conv6(c1))
    elif rnd30 % 8 == 7:
        d1 = (str(rnd30) + conv7(c1))
    else:
        d1 = ""

    if rnd40 % 8 == 0:
        e1 = (str(rnd40) + conv8(d1))
    elif rnd40 % 8 == 1:
        e1 = (str(rnd40) + conv1(d1))
    elif rnd40 % 8 == 2:
        e1 = (str(rnd40) + conv2(d1))
    elif rnd40 % 8 == 3:
        e1 = (str(rnd40) + conv3(d1))
    elif rnd40 % 8 == 4:
        e1 = (str(rnd40) + conv4(d1))
    elif rnd40 % 8 == 5:
        e1 = (str(rnd40) + conv5(d1))
    elif rnd40 % 8 == 6:
        e1 = (str(rnd40) + conv6(d1))
    elif rnd40 % 8 == 7:
        e1 = (str(rnd40) + conv7(d1))
    else:
        e1 = ""

    if rnd50 % 8 == 0:
        f1 = (str(rnd50) + conv8(e1))
    elif rnd50 % 8 == 1:
        f1 = (str(rnd50) + conv1(e1))
    elif rnd50 % 8 == 2:
        f1 = (str(rnd50) + conv2(e1))
    elif rnd50 % 8 == 3:
        f1 = (str(rnd50) + conv3(e1))
    elif rnd50 % 8 == 4:
        f1 = (str(rnd50) + conv4(e1))
    elif rnd50 % 8 == 5:
        f1 = (str(rnd50) + conv5(e1))
    elif rnd50 % 8 == 6:
        f1 = (str(rnd50) + conv6(e1))
    elif rnd50 % 8 == 7:
        f1 = (str(rnd50) + conv7(e1))
    else:
        f1 = ""

    if rnd60 % 8 == 0:
        g1 = (str(rnd60) + conv8(f1))
    elif rnd60 % 8 == 1:
        g1 = (str(rnd60) + conv1(f1))
    elif rnd60 % 8 == 2:
        g1 = (str(rnd60) + conv2(f1))
    elif rnd60 % 8 == 3:
        g1 = (str(rnd60) + conv3(f1))
    elif rnd60 % 8 == 4:
        g1 = (str(rnd60) + conv4(f1))
    elif rnd60 % 8 == 5:
        g1 = (str(rnd60) + conv5(f1))
    elif rnd60 % 8 == 6:
        g1 = (str(rnd60) + conv6(f1))
    elif rnd60 % 8 == 7:
        g1 = (str(rnd60) + conv7(f1))
    else:
        g1 = ""

    if rnd70 % 8 == 0:
        h1 = (str(rnd70) + conv8(g1))
    elif rnd70 % 8 == 1:
        h1 = (str(rnd70) + conv1(g1))
    elif rnd70 % 8 == 2:
        h1 = (str(rnd70) + conv2(g1))
    elif rnd70 % 8 == 3:
        h1 = (str(rnd70) + conv3(g1))
    elif rnd70 % 8 == 4:
        h1 = (str(rnd70) + conv4(g1))
    elif rnd70 % 8 == 5:
        h1 = (str(rnd70) + conv5(g1))
    elif rnd70 % 8 == 6:
        h1 = (str(rnd70) + conv6(g1))
    elif rnd70 % 8 == 7:
        h1 = (str(rnd70) + conv7(g1))
    else:
        h1 = ""

    if rnd80 % 8 == 0:
        i1 = (str(rnd80) + conv8(h1))
    elif rnd80 % 8 == 1:
        i1 = (str(rnd80) + conv1(h1))
    elif rnd80 % 8 == 2:
        i1 = (str(rnd80) + conv2(h1))
    elif rnd80 % 8 == 3:
        i1 = (str(rnd80) + conv3(h1))
    elif rnd80 % 8 == 4:
        i1 = (str(rnd80) + conv4(h1))
    elif rnd80 % 8 == 5:
        i1 = (str(rnd80) + conv5(h1))
    elif rnd80 % 8 == 6:
        i1 = (str(rnd80) + conv6(h1))
    elif rnd80 % 8 == 7:
        i1 = (str(rnd80) + conv7(h1))
    else:
        i1 = ""

    encrypted_text = combine_strings(i1, i)
    ana_2 = anagram(encrypted_text, len(encrypted_text))
    print("Encoded text:", ana_2)

elif int(dec) == 1:
    de_ana_1 = de_anagram(inp, len(inp))
    odd, even = split_string(de_ana_1)

    if odd[0] == '0':
        odd = de_converter8(odd)
    elif odd[0] == '1':
        odd = de_converter1(odd)
    elif odd[0] == '2':
        odd = de_converter2(odd)
    elif odd[0] == '3':
        odd = de_converter3(odd)
    elif odd[0] == '4':
        odd = de_converter4(odd)
    elif odd[0] == '5':
        odd = de_converter5(odd)
    elif odd[0] == '6':
        odd = de_converter6(odd)
    elif odd[0] == '7':
        odd = de_converter7(odd)
    else:
        odd = odd

    if odd[1] == '0':
        odd = de_converter8(odd)
    elif odd[1] == '1':
        odd = de_converter1(odd)
    elif odd[1] == '2':
        odd = de_converter2(odd)
    elif odd[1] == '3':
        odd = de_converter3(odd)
    elif odd[1] == '4':
        odd = de_converter4(odd)
    elif odd[1] == '5':
        odd = de_converter5(odd)
    elif odd[1] == '6':
        odd = de_converter6(odd)
    elif odd[1] == '7':
        odd = de_converter7(odd)
    else:
        odd = odd

    if odd[2] == '0':
        odd = de_converter8(odd)
    elif odd[2] == '1':
        odd = de_converter1(odd)
    elif odd[2] == '2':
        odd = de_converter2(odd)
    elif odd[2] == '3':
        odd = de_converter3(odd)
    elif odd[2] == '4':
        odd = de_converter4(odd)
    elif odd[2] == '5':
        odd = de_converter5(odd)
    elif odd[2] == '6':
        odd = de_converter6(odd)
    elif odd[2] == '7':
        odd = de_converter7(odd)
    else:
        odd = odd

    if odd[3] == '0':
        odd = de_converter8(odd)
    elif odd[3] == '1':
        odd = de_converter1(odd)
    elif odd[3] == '2':
        odd = de_converter2(odd)
    elif odd[3] == '3':
        odd = de_converter3(odd)
    elif odd[3] == '4':
        odd = de_converter4(odd)
    elif odd[3] == '5':
        odd = de_converter5(odd)
    elif odd[3] == '6':
        odd = de_converter6(odd)
    elif odd[3] == '7':
        odd = de_converter7(odd)
    else:
        odd = odd

    if odd[4] == '0':
        odd = de_converter8(odd)
    elif odd[4] == '1':
        odd = de_converter1(odd)
    elif odd[4] == '2':
        odd = de_converter2(odd)
    elif odd[4] == '3':
        odd = de_converter3(odd)
    elif odd[4] == '4':
        odd = de_converter4(odd)
    elif odd[4] == '5':
        odd = de_converter5(odd)
    elif odd[4] == '6':
        odd = de_converter6(odd)
    elif odd[4] == '7':
        odd = de_converter7(odd)
    else:
        odd = odd

    if odd[5] == '0':
        odd = de_converter8(odd)
    elif odd[5] == '1':
        odd = de_converter1(odd)
    elif odd[5] == '2':
        odd = de_converter2(odd)
    elif odd[5] == '3':
        odd = de_converter3(odd)
    elif odd[5] == '4':
        odd = de_converter4(odd)
    elif odd[5] == '5':
        odd = de_converter5(odd)
    elif odd[5] == '6':
        odd = de_converter6(odd)
    elif odd[5] == '7':
        odd = de_converter7(odd)
    else:
        odd = odd

    if odd[6] == '0':
        odd = de_converter8(odd)
    elif odd[6] == '1':
        odd = de_converter1(odd)
    elif odd[6] == '2':
        odd = de_converter2(odd)
    elif odd[6] == '3':
        odd = de_converter3(odd)
    elif odd[6] == '4':
        odd = de_converter4(odd)
    elif odd[6] == '5':
        odd = de_converter5(odd)
    elif odd[6] == '6':
        odd = de_converter6(odd)
    elif odd[6] == '7':
        odd = de_converter7(odd)
    else:
        odd = odd

    if odd[7] == '0':
        odd = de_converter8(odd)
    elif odd[7] == '1':
        odd = de_converter1(odd)
    elif odd[7] == '2':
        odd = de_converter2(odd)
    elif odd[7] == '3':
        odd = de_converter3(odd)
    elif odd[7] == '4':
        odd = de_converter4(odd)
    elif odd[7] == '5':
        odd = de_converter5(odd)
    elif odd[7] == '6':
        odd = de_converter6(odd)
    elif odd[7] == '7':
        odd = de_converter7(odd)
    else:
        odd = odd

    if odd[8] == '0':
        odd = de_converter8(odd)
    elif odd[8] == '1':
        odd = de_converter1(odd)
    elif odd[8] == '2':
        odd = de_converter2(odd)
    elif odd[8] == '3':
        odd = de_converter3(odd)
    elif odd[8] == '4':
        odd = de_converter4(odd)
    elif odd[8] == '5':
        odd = de_converter5(odd)
    elif odd[8] == '6':
        odd = de_converter6(odd)
    elif odd[8] == '7':
        odd = de_converter7(odd)
    else:
        odd = odd

    if even[0] == '0':
        even = de_converter8(even)
    elif even[0] == '1':
        even = de_converter1(even)
    elif even[0] == '2':
        even = de_converter2(even)
    elif even[0] == '3':
        even = de_converter3(even)
    elif even[0] == '4':
        even = de_converter4(even)
    elif even[0] == '5':
        even = de_converter5(even)
    elif even[0] == '6':
        even = de_converter6(even)
    elif even[0] == '7':
        even = de_converter7(even)
    else:
        even = even

    if even[1] == '0':
        even = de_converter8(even)
    elif even[1] == '1':
        even = de_converter1(even)
    elif even[1] == '2':
        even = de_converter2(even)
    elif even[1] == '3':
        even = de_converter3(even)
    elif even[1] == '4':
        even = de_converter4(even)
    elif even[1] == '5':
        even = de_converter5(even)
    elif even[1] == '6':
        even = de_converter6(even)
    elif even[1] == '7':
        even = de_converter7(even)
    else:
        even = even

    if even[2] == '0':
        even = de_converter8(even)
    elif even[2] == '1':
        even = de_converter1(even)
    elif even[2] == '2':
        even = de_converter2(even)
    elif even[2] == '3':
        even = de_converter3(even)
    elif even[2] == '4':
        even = de_converter4(even)
    elif even[2] == '5':
        even = de_converter5(even)
    elif even[2] == '6':
        even = de_converter6(even)
    elif even[2] == '7':
        even = de_converter7(even)
    else:
        even = even

    if even[3] == '0':
        even = de_converter8(even)
    elif even[3] == '1':
        even = de_converter1(even)
    elif even[3] == '2':
        even = de_converter2(even)
    elif even[3] == '3':
        even = de_converter3(even)
    elif even[3] == '4':
        even = de_converter4(even)
    elif even[3] == '5':
        even = de_converter5(even)
    elif even[3] == '6':
        even = de_converter6(even)
    elif even[3] == '7':
        even = de_converter7(even)
    else:
        even = even

    if even[4] == '0':
        even = de_converter8(even)
    elif even[4] == '1':
        even = de_converter1(even)
    elif even[4] == '2':
        even = de_converter2(even)
    elif even[4] == '3':
        even = de_converter3(even)
    elif even[4] == '4':
        even = de_converter4(even)
    elif even[4] == '5':
        even = de_converter5(even)
    elif even[4] == '6':
        even = de_converter6(even)
    elif even[4] == '7':
        even = de_converter7(even)
    else:
        even = even

    if even[5] == '0':
        even = de_converter8(even)
    elif even[5] == '1':
        even = de_converter1(even)
    elif even[5] == '2':
        even = de_converter2(even)
    elif even[5] == '3':
        even = de_converter3(even)
    elif even[5] == '4':
        even = de_converter4(even)
    elif even[5] == '5':
        even = de_converter5(even)
    elif even[5] == '6':
        even = de_converter6(even)
    elif even[5] == '7':
        even = de_converter7(even)
    else:
        even = even

    if even[6] == '0':
        even = de_converter8(even)
    elif even[6] == '1':
        even = de_converter1(even)
    elif even[6] == '2':
        even = de_converter2(even)
    elif even[6] == '3':
        even = de_converter3(even)
    elif even[6] == '4':
        even = de_converter4(even)
    elif even[6] == '5':
        even = de_converter5(even)
    elif even[6] == '6':
        even = de_converter6(even)
    elif even[6] == '7':
        even = de_converter7(even)
    else:
        even = even

    if even[7] == '0':
        even = de_converter8(even)
    elif even[7] == '1':
        even = de_converter1(even)
    elif even[7] == '2':
        even = de_converter2(even)
    elif even[7] == '3':
        even = de_converter3(even)
    elif even[7] == '4':
        even = de_converter4(even)
    elif even[7] == '5':
        even = de_converter5(even)
    elif even[7] == '6':
        even = de_converter6(even)
    elif even[7] == '7':
        even = de_converter7(even)
    else:
        even = de_converter7(even)

    if even[8] == '0':
        even = de_converter8(even)
    elif even[8] == '1':
        even = de_converter1(even)
    elif even[8] == '2':
        even = de_converter2(even)
    elif even[8] == '3':
        even = de_converter3(even)
    elif even[8] == '4':
        even = de_converter4(even)
    elif even[8] == '5':
        even = de_converter5(even)
    elif even[8] == '6':
        even = de_converter6(even)
    elif even[8] == '7':
        even = de_converter7(even)
    else:
        even = even

    decrypted_text = combine_strings(even[9:], odd[9:])
    de_ana_2 = de_anagram(decrypted_text, len(decrypted_text))
    print("Decrypted String :", de_ana_2)

else:
    print("Next time!")

time.sleep(125)
