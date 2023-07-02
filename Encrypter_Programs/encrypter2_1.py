import os

path1 = r"D:\Others\Encryptedtext"  # folder for exported text files
path1_exist = os.path.exists(path1)

if path1_exist:
    pass
else:
    os.mkdir(path1)

key_file = open(f'{path1}/key_file.txt', 'r')
key = key_file.read()[-11:]
dec = key[0]
key = key + "0123456789"
key = key[1:11]
key_file.close()

input_file = open(f'{path1}/input_file.txt', 'r')
inp = input_file.read()
input_file.close()

if key[0:10] == '0000000000':
    key = '8741890795'
elif key[0:9] == '000000000':
    key = '9123648714'
elif key[0:8] == '00000000':
    key = '1001001001'
elif key[0:7] == '0000000':
    key = '2568725687'
elif key[0:6] == '000000':
    key = '1357924680'
else:
    key = key

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

a_ = len(inp)


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


def anagram(text):
    printable = ''
    for x in range(0, a_, 3):
        str_a = text[x]
        str_b = text[x+1]
        str_c = text[x+2]
        printable = printable + str_b + str_c + str_a

    return printable


def de_anagram(text):
    printable = ''
    for x in range(0, a_, 3):
        str_a = text[x]
        str_b = text[x+1]
        str_c = text[x+2]
        printable = printable + str_c + str_a + str_b

    return printable


key_odd, key_even = split_string(key)

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


cnv9 = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f',
    '7': 'g', '8': 'h', '9': 'K', '0': 'j', 'a': 'k', 'b': 'l',
    'c': 'r', 'd': 'q', 'e': 'p', 'f': 'o', 'g': 'n', 'h': 'm',
    'i': 's', 'j': 't', 'k': 'u', 'l': 'v', 'm': 'w', 'n': 'X',
    'o': 'L', 'p': 'S', 'q': '`', 'r': 'J', 's': '~', 't': 'U',
    'u': '?', 'v': 'R', 'w': '>', 'x': '<', 'y': '"', 'z': ':',
    'A': '|', 'B': '}', 'C': '{', 'D': 'Q', 'E': '\\', 'F': '/',
    'G': '.', 'H': ',', 'I': 'T', 'J': ';', 'K': 'I', 'L': ']',
    'M': '[', 'N': '=', 'O': '-', 'P': 'P', 'Q': '+', 'R': '_',
    'S': ')', 'T': 'E', 'U': '(', 'V': 'H', 'W': '*', 'X': '&',
    'Y': 'A', 'Z': '^', '[': 'x', ']': '%', '\\': '$', ';': '#',
    ' ': '@', ',': '!', '.': '₹', '/': "'", '{': 'G', '}': ' ',
    '|': '0', ':': '9', '"': 'B', '<': '8', '>': 'y', '?': '7',
    '~': '5', '`': 'O', '-': 'D', '=': 'F', '!': '6', '@': 'Z',
    '#': '4', '$': 'M', '%': '3', '^': 'V', '&': '2', '*': '1',
    '(': 'Y', ')': 'W', '_': 'N', "+": 'C', "'": 'z', '₹': 'i'
}
cnv9d = {v: k for k, v in cnv9.items()}


def conv9(inp_conv9):
    string9 = ''
    for x in inp_conv9:
        temp = x
        string9 = string9 + cnv9[temp]

    return string9


def de_converter9(encrypted_str):
    decrypted_str = ''
    for char in encrypted_str:
        if char in cnv9d:
            decrypted_str += cnv9d[char]
        else:
            decrypted_str += char

    return decrypted_str


if int(dec) == 0:
    ana_1 = anagram(inp)
    odd, even = split_string(ana_1)

    if key_odd[0] == '0':
        a = odd
    elif key_odd[0] == '1':
        a = conv1(odd)
    elif key_odd[0] == '2':
        a = conv2(odd)
    elif key_odd[0] == '3':
        a = conv3(odd)
    elif key_odd[0] == '4':
        a = conv4(odd)
    elif key_odd[0] == '5':
        a = conv5(odd)
    elif key_odd[0] == '6':
        a = conv6(odd)
    elif key_odd[0] == '7':
        a = conv7(odd)
    elif key_odd[0] == '8':
        a = conv8(odd)
    elif key_odd[0] == '9':
        a = conv9(odd)
    else:
        a = ""

    if key_odd[1] == '0':
        b = a
    elif key_odd[1] == '1':
        b = conv1(a)
    elif key_odd[1] == '2':
        b = conv2(a)
    elif key_odd[1] == '3':
        b = conv3(a)
    elif key_odd[1] == '4':
        b = conv4(a)
    elif key_odd[1] == '5':
        b = conv5(a)
    elif key_odd[1] == '6':
        b = conv6(a)
    elif key_odd[1] == '7':
        b = conv7(a)
    elif key_odd[1] == '8':
        b = conv8(a)
    elif key_odd[1] == '9':
        b = conv9(a)
    else:
        b = ""

    if key_odd[2] == '0':
        c = b
    elif key_odd[2] == '1':
        c = conv1(b)
    elif key_odd[2] == '2':
        c = conv2(b)
    elif key_odd[2] == '3':
        c = conv3(b)
    elif key_odd[2] == '4':
        c = conv4(b)
    elif key_odd[2] == '5':
        c = conv5(b)
    elif key_odd[2] == '6':
        c = conv6(b)
    elif key_odd[2] == '7':
        c = conv7(b)
    elif key_odd[2] == '8':
        c = conv8(b)
    elif key_odd[2] == '9':
        c = conv9(b)
    else:
        c = ""

    if key_odd[3] == '0':
        d = c
    elif key_odd[3] == '1':
        d = conv1(c)
    elif key_odd[3] == '2':
        d = conv2(c)
    elif key_odd[3] == '3':
        d = conv3(c)
    elif key_odd[3] == '4':
        d = conv4(c)
    elif key_odd[3] == '5':
        d = conv5(c)
    elif key_odd[3] == '6':
        d = conv6(c)
    elif key_odd[3] == '7':
        d = conv7(c)
    elif key_odd[3] == '8':
        d = conv8(c)
    elif key_odd[3] == '9':
        d = conv9(c)
    else:
        d = ""

    if key_odd[4] == '0':
        e = d
    elif key_odd[4] == '1':
        e = conv1(d)
    elif key_odd[4] == '2':
        e = conv2(d)
    elif key_odd[4] == '3':
        e = conv3(d)
    elif key_odd[4] == '4':
        e = conv4(d)
    elif key_odd[4] == '5':
        e = conv5(d)
    elif key_odd[4] == '6':
        e = conv6(d)
    elif key_odd[4] == '7':
        e = conv7(d)
    elif key_odd[4] == '8':
        e = conv8(d)
    elif key_odd[4] == '9':
        e = conv9(d)
    else:
        e = ""

    if key_even[0] == '0':
        a1 = even
    elif key_even[0] == '1':
        a1 = conv1(even)
    elif key_even[0] == '2':
        a1 = conv2(even)
    elif key_even[0] == '3':
        a1 = conv3(even)
    elif key_even[0] == '4':
        a1 = conv4(even)
    elif key_even[0] == '5':
        a1 = conv5(even)
    elif key_even[0] == '6':
        a1 = conv6(even)
    elif key_even[0] == '7':
        a1 = conv7(even)
    elif key_even[0] == '8':
        a1 = conv8(even)
    elif key_even[0] == '9':
        a1 = conv9(even)
    else:
        a1 = ""

    if key_even[1] == '0':
        b1 = a1
    elif key_even[1] == '1':
        b1 = conv1(a1)
    elif key_even[1] == '2':
        b1 = conv2(a1)
    elif key_even[1] == '3':
        b1 = conv3(a1)
    elif key_even[1] == '4':
        b1 = conv4(a1)
    elif key_even[1] == '5':
        b1 = conv5(a1)
    elif key_even[1] == '6':
        b1 = conv6(a1)
    elif key_even[1] == '7':
        b1 = conv7(a1)
    elif key_even[1] == '8':
        b1 = conv8(a1)
    elif key_even[1] == '9':
        b1 = conv9(a1)
    else:
        b1 = ""

    if key_even[2] == '0':
        c1 = b1
    elif key_even[2] == '1':
        c1 = conv1(b1)
    elif key_even[2] == '2':
        c1 = conv2(b1)
    elif key_even[2] == '3':
        c1 = conv3(b1)
    elif key_even[2] == '4':
        c1 = conv4(b1)
    elif key_even[2] == '5':
        c1 = conv5(b1)
    elif key_even[2] == '6':
        c1 = conv6(b1)
    elif key_even[2] == '7':
        c1 = conv7(b1)
    elif key_even[2] == '8':
        c1 = conv8(b1)
    elif key_even[2] == '9':
        c1 = conv9(b1)
    else:
        c1 = ""

    if key_even[3] == '0':
        d1 = c1
    elif key_even[3] == '1':
        d1 = conv1(c1)
    elif key_even[3] == '2':
        d1 = conv2(c1)
    elif key_even[3] == '3':
        d1 = conv3(c1)
    elif key_even[3] == '4':
        d1 = conv4(c1)
    elif key_even[3] == '5':
        d1 = conv5(c1)
    elif key_even[3] == '6':
        d1 = conv6(c1)
    elif key_even[3] == '7':
        d1 = conv7(c1)
    elif key_even[3] == '8':
        d1 = conv8(c1)
    elif key_even[3] == '9':
        d1 = conv9(c1)
    else:
        d1 = ""

    if key_even[4] == '0':
        e1 = d1
    elif key_even[4] == '1':
        e1 = conv1(d1)
    elif key_even[4] == '2':
        e1 = conv2(d1)
    elif key_even[4] == '3':
        e1 = conv3(d1)
    elif key_even[4] == '4':
        e1 = conv4(d1)
    elif key_even[4] == '5':
        e1 = conv5(d1)
    elif key_even[4] == '6':
        e1 = conv6(d1)
    elif key_even[4] == '7':
        e1 = conv7(d1)
    elif key_even[4] == '8':
        e1 = conv8(d1)
    elif key_even[4] == '9':
        e1 = conv9(d1)
    else:
        e1 = ""

    encrypted_text = combine_strings(e1, e)
    ana_2 = anagram(encrypted_text)

elif int(dec) == 1:
    de_ana_1 = de_anagram(inp)
    odd_de, even_de = split_string(de_ana_1)
    if key_odd[4] == '0':
        a_de = odd_de
    elif key_odd[4] == '1':
        a_de = de_converter1(odd_de)
    elif key_odd[4] == '2':
        a_de = de_converter2(odd_de)
    elif key_odd[4] == '3':
        a_de = de_converter3(odd_de)
    elif key_odd[4] == '4':
        a_de = de_converter4(odd_de)
    elif key_odd[4] == '5':
        a_de = de_converter5(odd_de)
    elif key_odd[4] == '6':
        a_de = de_converter6(odd_de)
    elif key_odd[4] == '7':
        a_de = de_converter7(odd_de)
    elif key_odd[4] == '8':
        a_de = de_converter8(odd_de)
    elif key_odd[4] == '9':
        a_de = de_converter9(odd_de)
    else:
        a_de = ""

    if key_odd[3] == '0':
        b_de = a_de
    elif key_odd[3] == '1':
        b_de = de_converter1(a_de)
    elif key_odd[3] == '2':
        b_de = de_converter2(a_de)
    elif key_odd[3] == '3':
        b_de = de_converter3(a_de)
    elif key_odd[3] == '4':
        b_de = de_converter4(a_de)
    elif key_odd[3] == '5':
        b_de = de_converter5(a_de)
    elif key_odd[3] == '6':
        b_de = de_converter6(a_de)
    elif key_odd[3] == '7':
        b_de = de_converter7(a_de)
    elif key_odd[3] == '8':
        b_de = de_converter8(a_de)
    elif key_odd[3] == '9':
        b_de = de_converter9(a_de)
    else:
        b_de = ""

    if key_odd[2] == '0':
        c_de = b_de
    elif key_odd[2] == '1':
        c_de = de_converter1(b_de)
    elif key_odd[2] == '2':
        c_de = de_converter2(b_de)
    elif key_odd[2] == '3':
        c_de = de_converter3(b_de)
    elif key_odd[2] == '4':
        c_de = de_converter4(b_de)
    elif key_odd[2] == '5':
        c_de = de_converter5(b_de)
    elif key_odd[2] == '6':
        c_de = de_converter6(b_de)
    elif key_odd[2] == '7':
        c_de = de_converter7(b_de)
    elif key_odd[2] == '8':
        c_de = de_converter8(b_de)
    elif key_odd[2] == '9':
        c_de = de_converter9(b_de)
    else:
        c_de = ""

    if key_odd[1] == '0':
        d_de = c_de
    elif key_odd[1] == '1':
        d_de = de_converter1(c_de)
    elif key_odd[1] == '2':
        d_de = de_converter2(c_de)
    elif key_odd[1] == '3':
        d_de = de_converter3(c_de)
    elif key_odd[1] == '4':
        d_de = de_converter4(c_de)
    elif key_odd[1] == '5':
        d_de = de_converter5(c_de)
    elif key_odd[1] == '6':
        d_de = de_converter6(c_de)
    elif key_odd[1] == '7':
        d_de = de_converter7(c_de)
    elif key_odd[1] == '8':
        d_de = de_converter8(c_de)
    elif key_odd[1] == '9':
        d_de = de_converter9(c_de)
    else:
        d_de = ""

    if key_odd[0] == '0':
        e_de = d_de
    elif key_odd[0] == '1':
        e_de = de_converter1(d_de)
    elif key_odd[0] == '2':
        e_de = de_converter2(d_de)
    elif key_odd[0] == '3':
        e_de = de_converter3(d_de)
    elif key_odd[0] == '4':
        e_de = de_converter4(d_de)
    elif key_odd[0] == '5':
        e_de = de_converter5(d_de)
    elif key_odd[0] == '6':
        e_de = de_converter6(d_de)
    elif key_odd[0] == '7':
        e_de = de_converter7(d_de)
    elif key_odd[0] == '8':
        e_de = de_converter8(d_de)
    elif key_odd[0] == '9':
        e_de = de_converter9(d_de)
    else:
        e_de = ""

    if key_even[4] == '0':
        a1_de = even_de
    elif key_even[4] == '1':
        a1_de = de_converter1(even_de)
    elif key_even[4] == '2':
        a1_de = de_converter2(even_de)
    elif key_even[4] == '3':
        a1_de = de_converter3(even_de)
    elif key_even[4] == '4':
        a1_de = de_converter4(even_de)
    elif key_even[4] == '5':
        a1_de = de_converter5(even_de)
    elif key_even[4] == '6':
        a1_de = de_converter6(even_de)
    elif key_even[4] == '7':
        a1_de = de_converter7(even_de)
    elif key_even[4] == '8':
        a1_de = de_converter8(even_de)
    elif key_even[4] == '9':
        a1_de = de_converter9(even_de)
    else:
        a1_de = ""

    if key_even[3] == '0':
        b1_de = a1_de
    elif key_even[3] == '1':
        b1_de = de_converter1(a1_de)
    elif key_even[3] == '2':
        b1_de = de_converter2(a1_de)
    elif key_even[3] == '3':
        b1_de = de_converter3(a1_de)
    elif key_even[3] == '4':
        b1_de = de_converter4(a1_de)
    elif key_even[3] == '5':
        b1_de = de_converter5(a1_de)
    elif key_even[3] == '6':
        b1_de = de_converter6(a1_de)
    elif key_even[3] == '7':
        b1_de = de_converter7(a1_de)
    elif key_even[3] == '8':
        b1_de = de_converter8(a1_de)
    elif key_even[3] == '9':
        b1_de = de_converter9(a1_de)
    else:
        b1_de = ""

    if key_even[2] == '0':
        c1_de = b1_de
    elif key_even[2] == '1':
        c1_de = de_converter1(b1_de)
    elif key_even[2] == '2':
        c1_de = de_converter2(b1_de)
    elif key_even[2] == '3':
        c1_de = de_converter3(b1_de)
    elif key_even[2] == '4':
        c1_de = de_converter4(b1_de)
    elif key_even[2] == '5':
        c1_de = de_converter5(b1_de)
    elif key_even[2] == '6':
        c1_de = de_converter6(b1_de)
    elif key_even[2] == '7':
        c1_de = de_converter7(b1_de)
    elif key_even[2] == '8':
        c1_de = de_converter8(b1_de)
    elif key_even[2] == '9':
        c1_de = de_converter9(b1_de)
    else:
        c1_de = ""

    if key_even[1] == '0':
        d1_de = c1_de
    elif key_even[1] == '1':
        d1_de = de_converter1(c1_de)
    elif key_even[1] == '2':
        d1_de = de_converter2(c1_de)
    elif key_even[1] == '3':
        d1_de = de_converter3(c1_de)
    elif key_even[1] == '4':
        d1_de = de_converter4(c1_de)
    elif key_even[1] == '5':
        d1_de = de_converter5(c1_de)
    elif key_even[1] == '6':
        d1_de = de_converter6(c1_de)
    elif key_even[1] == '7':
        d1_de = de_converter7(c1_de)
    elif key_even[1] == '8':
        d1_de = de_converter8(c1_de)
    elif key_even[1] == '9':
        d1_de = de_converter9(c1_de)
    else:
        d1_de = ""

    if key_even[0] == '0':
        e1_de = d1_de
    elif key_even[0] == '1':
        e1_de = de_converter1(d1_de)
    elif key_even[0] == '2':
        e1_de = de_converter2(d1_de)
    elif key_even[0] == '3':
        e1_de = de_converter3(d1_de)
    elif key_even[0] == '4':
        e1_de = de_converter4(d1_de)
    elif key_even[0] == '5':
        e1_de = de_converter5(d1_de)
    elif key_even[0] == '6':
        e1_de = de_converter6(d1_de)
    elif key_even[0] == '7':
        e1_de = de_converter7(d1_de)
    elif key_even[0] == '8':
        e1_de = de_converter8(d1_de)
    elif key_even[0] == '9':
        e1_de = de_converter9(d1_de)
    else:
        e1_de = ""

    decrypted_text = combine_strings(e1_de, e_de)
    ana_2 = de_anagram(decrypted_text)

else:
    ana_2 = "Error"

print(ana_2)

file_to_write = open(f'{path1}/export_file.txt', 'a')
print(f'The encoded text was :{ana_2}', file=file_to_write)
file_to_write.close()
"""
"""
