import math as m

print("Choose from the following ")
print("1. arc sin           2. arc cos")
print("3. arc tan           4. arc cot")
print("5. arc sec           6. arc cosec")


def arc_sin(var):
    if var**2 - 1 <= 0:
        result1 = str(m.asin(var))
    else:
        pi2 = m.pi/2
        calc1 = m.log(var + (var**2 - 1)**0.5)
        result1 = (str(pi2) + " ± (" + str(calc1)+")i")

    return result1


def arc_cos(var):
    if var**2 - 1 <= 0:
        result1 = m.acos(var)
    else:
        calc1 = m.log(var + (var**2 - 1)**0.5)
        result1 = ("± (" + str(calc1)+")i")
    return result1


def arc_tan(var):
    return m.atan(var)

try:
    inverse_choice = int(input("Enter Choice : "))
    number_choice = float(input("Enter a value  of whose inverse you want to find: "))
    if inverse_choice == 1:
        decision = 'arc sin'
        calculated_output = arc_sin(number_choice)
    elif inverse_choice == 2:
        decision = 'arc cos'
        calculated_output = arc_cos(number_choice)
    elif inverse_choice == 3:
        decision = 'arc tan'
        calculated_output = arc_tan(number_choice)
    elif inverse_choice == 4:
        decision = 'arc cot'
        calculated_output = arc_tan(1/number_choice)
    elif inverse_choice == 5:
        decision = 'arc sec'
        calculated_output = arc_cos(1/number_choice)
    elif inverse_choice == 6:
        decision = 'arc cosec'
        calculated_output = arc_sin(1/number_choice)
    else:
        decision = 'Unidentified Function!'
        calculated_output = "Get a Life!"
except ValueError:
    decision = '(►__◄)'
    number_choice = '😒'
    calculated_output = '🤙'

print(f"{decision} of {number_choice} is '{calculated_output}'")