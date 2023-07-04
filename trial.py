from Encrypter_Programs import encrypter2

main = [
    " ",    "!",    '"',    "#",    "$",    "%",    "&",    "'",    "(",    ")",    "*",    "+",
    ",",    "-",    ".",    "/",    "0",    "1",    "2",    "3",    "4",    "5",    "6",    "7",
    "8",    "9",    ";",    "<",    "=",    ">",    "?",    "@",    "A",    "B",    "C",    "D",
    "E",    "F",    "G",    "H",    "I",    "J",    "K",    "L",    "M",    "N",    "O",    "P",
    "Q",    "R",    "S",    "T",    "U",    "V",    "W",    "X",    "Y",    "Z",    "[",    "\\",
    "]",    "^",    "_",    "`",    "a",    "b",    "c",    "d",    "e",    "f",    "g",    "h",
    "i",    "j",    "k",    "l",    "m",    "n",    "o",    "p",    "q",    "r",    "s",    "t",
    "u",    "v",    "w",    "x",    "y",    "z",    "{",    "|",    "}",    "~",    "₹",    ":",
]

text_original = ' ₹abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-=_+[];,./\{}|:"<>?\''

key = 1111111111111111

def func(s):
    print(len(s))
    f = []
    for element in s:
        if element not in main:
            f.append(element)
            
    if f:
        print("Iteration Unsuccessful")
        print("Elemnts left include: ",f)
    else:
        print("Iteration Successful")

for x in range(0,10):
    output = encrypter2.main(0,text_original,str(int(key*x)))
    print("Iteration :", x)
    func(output)