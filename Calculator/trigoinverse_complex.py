import math as m

print("Choose from the following ")
print("1. arc sin           2. arc cos")
print("3. arc tan           4. arc cot")
print("5. arc sec           6. arc cosec")


def arc_sin(a, b):
    alpha = a + ((a**2 - b**2 -1 + (((a-1)**2 + b**2)*(((a-1)**2 + b**2)))**(0.5))/2)**(0.5)
    beta = b + a*b/(alpha-a)
    
    result_imaginary = m.log(alpha**2 + beta**2)/2
    result_real = m.atan(beta/alpha) 

    result1 = (str(result_real)+ ' -i'+str(result_imaginary))
    return result1


def arc_cos(a,b):
    if a==0:
        real = m.pi/2
        imag = m.log(b + (b*b +1)**0.5)
        result1 = (str(real)+" -i("+str(imag)+")")
    elif b!=0:
        alpha = a + ((a*a - b*b -1 + ((a*a + b*b + 1)**2 -4*a*a)**0.5)/2)**(0.5)
        beta = b + a*b/(alpha-a)
        
        result_imaginary = m.log(alpha**2 + beta**2)/2
        result_real = m.atan(beta/alpha) 

        result1 = (str(result_real)+ ' -i('+str(result_imaginary)+')')
    else:
        if a**2 - 1 <= 0:
            result1 = m.acos(a)
        else:
            calc1 = m.log(a + (a**2 - 1)**0.5)
            result1 = ("± (" + str(calc1)+")i")
    return result1


def arc_tan(a,b):
    alpha = a + ((a**2 - b**2 -1 + (((a-1)**2 + b**2)*(((a-1)**2 + b**2)))**(0.5))/2)**(0.5)
    beta = b + a*b/(alpha-a)
    
    result_imaginary = m.log(alpha**2 + beta**2)/2
    result_real = m.atan(beta/alpha) 

    result1 = (str(result_real)+ ' -i'+str(result_imaginary))
    return result1

try:
    inverse_choice = int(input("Enter Choice : "))
    real_part = float(input("Enter a real part of whose inverse you want to find: "))
    complex_part = float(input("Enter the imaginary part of whose inverse you want to find: "))
    if inverse_choice == 1:
        decision = 'arc sin'
        calculated_output = arc_sin(real_part, complex_part)
    elif inverse_choice == 2:
        decision = 'arc cos'
        calculated_output = arc_cos(real_part, complex_part)
    elif inverse_choice == 3:
        decision = 'arc tan'
        calculated_output = arc_tan(real_part, complex_part)
    elif inverse_choice == 4:
        decision = 'arc cot'
        calculated_output = arc_tan(1/real_part, complex_part)
    elif inverse_choice == 5:
        decision = 'arc sec'
        calculated_output = arc_cos(1/real_part, complex_part)
    elif inverse_choice == 6:
        decision = 'arc cosec'
        calculated_output = arc_sin(1/real_part, complex_part)
    else:
        decision = 'Unidentified Function!'
        calculated_output = "Get a Life!"
except ValueError:
    calculated_output = "Anpad Gawar!!"

print(calculated_output)