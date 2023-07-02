cnv1 = {
    '1': 'ax', '2': 'bM', '3': 'cH', '4': 'dA', '5': 'ey', '6': 'fl',
    '7': 'go', '8': 'hr', '9': 'id', '0': 'j-', 'a': 'k{', 'b': 'l"',
    'c': 'm^', 'd': "n'", 'e': 'oT', 'f': 'pR', 'g': 'qW', 'h': 'rL',
    'i': 's[', 'j': 't1', 'k': 'u)', 'l': 'vK', 'm': 'w4', 'n': 'x@',
    'o': 'yB', 'p': 'z#', 'q': 'A:', 'r': 'BU', 's': 'C*', 't': 'D|',
    'u': 'Eh', 'v': 'F<', 'w': 'Gt', 'x': 'Hj', 'y': 'IS', 'z': 'J(',
    'A': 'Km', 'B': 'L7', 'C': 'MO', 'D': 'Nv', 'E': 'Oe', 'F': 'P+',
    'G': 'Q;', 'H': 'R?', 'I': 'S0', 'J': 'TX', 'K': 'U6', 'L': 'Vu',
    'M': 'WQ', 'N': 'XC', 'O': 'YN', 'P': 'Zg', 'Q': '02', 'R': '1$',
    'S': '25', 'T': '3E', 'U': '48', 'V': '5_', 'W': '6P', 'X': '7!',
    'Y': '8,', 'Z': '9G', '[': '1=', ']': '1n', '\\': '1S', ';': '1Z',
    ' ': '1a', ',': '1&', '.': ' V', '/': ' F', '{': '  ', '}': ' p',
    '|': ' w', ':': ' `', '"': ' >', '<': ' v', '>': ' b', '?': ' 3',
    '~': 'Rz', '`': 'Rq', '-': 'RI', '=': 'Ri', '!': 'RJ', '@': 'R]',
    '#': '7}', '$': '4f', '%': 'Ic', '^': 'Y%', '&': 'RY', '*': 'R\\',
    '(': '7~', ')': '4₹', '_': 'I.', "+": 'Y/', "'": 'R9', '₹': 'Rk'
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
    a_ = int(len(encrypted_str))
    for char in range(0, a_, 2):
        str_a = encrypted_str[char]
        str_b = encrypted_str[char+1]
        text = str_a + str_b
        if text in cnv1d:
            decrypted_str += cnv1d[text]
        else:
            decrypted_str += char
    return decrypted_str


dec = int(input("Enter dec :"))
inp = input("Enter text :")


if dec == 0:
    enc_t = conv1(inp)
    print("Encrypted text :", enc_t)
else:
    de_enc_t = de_converter1(inp)
    print("Decrypted text :", de_enc_t)
