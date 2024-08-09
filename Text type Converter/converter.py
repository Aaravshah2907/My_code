from ast import literal_eval

print("Select a number to convert your input from:")
print("1. String")
print("2. Binary")
print("3. Octal")
print("4. Decimal")
print("5. Hexadecimal")

in_type = int(input("Enter number from 1-5 : "))
input_text = input("Enter text to convert: ")

print("Select a number to convert your input to:")
print("1. String")
print("2. Binary")
print("3. Octal")
print("4. Decimal")
print("5. Hexadecimal")
out_type = int(input("Enter number from 1-5 : "))


def convert_to_int(string):
    li = list(string.split(", ",))
    list1 = []
    for element in li:
        list1.append(int(element))
    return list1


def convert(string):
    lis = list(string.split(", "))
    return lis


def word_to_number_list_converter(inp):
    ord_list = []
    for char in inp:
        ord_list.append(ord(char))
    return ord_list


def number_to_binary_list(inp):
    num_list = []
    for element in inp:
        num_list.append(bin(element))
    return num_list


def number_to_octal_list(inp):
    oct_list = []
    for element in inp:
        oct_list.append(oct(element))
    return oct_list


def number_to_hexadecimal_list(inp):
    hex_list = []
    for element in inp:
        hex_list.append(hex(element))
    return hex_list


def ascii_to_string(inp):
    string = []
    for element in inp:
        string.append(chr(element))
    return string


def list_to_string(inp):
    string = ''
    for element in inp:
        string = string + element
    return string


def output_function(var):
    if out_type == 1:
        a = ascii_to_string(var)
        return list_to_string(a)
    elif out_type == 2:
        return number_to_binary_list(var)
    elif out_type == 3:
        return number_to_octal_list(var)
    elif out_type == 4:
        return var
    elif out_type == 5:
        return number_to_hexadecimal_list(var)
    else:
        return "Next time Asshole!"


def binary_to_decimal(inp):
    num_list = []
    for binary in inp:
        decimal, index = 0, 0
        while binary != 0:
            dec = binary % 10
            decimal = decimal + dec * pow(2, index)
            binary = binary//10
            index += 1
        num_list.append(decimal)
    return num_list


def octal_to_number(inp):
    oct_list = []
    for oct_num in inp:
        i, dec_num = 0, 0
        while oct_num != 0:
            rem = oct_num % 10
            if rem > 7:
                break
            dec_num = dec_num + (rem * (8 ** i))
            i = i + 1
            oct_num = int(oct_num / 10)
        oct_list.append(dec_num)
    return oct_list


def hex_to_number(inp):
    oct_list = []
    inp = list(inp)
    for element in inp:
        res = literal_eval(element)
        oct_list.append(res)
    return oct_list


if in_type != 1:
    input_text = input_text.replace("'", "")
    input_text = input_text.replace("0b", "")
    input_text = input_text.replace("0o", "")
    input_text = input_text.replace("[", "")
    input_text = input_text.replace("]", "")

if in_type != 5 and in_type != 1:
    input_text = convert_to_int(input_text)

if in_type == 1:
    ascii_list = word_to_number_list_converter(input_text)
    output = output_function(ascii_list)
elif in_type == 2:
    number_list_to_do = binary_to_decimal(input_text)
    output = output_function(number_list_to_do)
elif in_type == 3:
    octal_list_to_do = octal_to_number(input_text)
    output = output_function(octal_list_to_do)
elif in_type == 4:
    number = input_text
    output = output_function(number)
elif in_type == 5:
    input_text = convert(input_text)
    hex_list_to_do = hex_to_number(input_text)
    output = output_function(hex_list_to_do)
else:
    output = "Next Time Asshole"

print(output)
