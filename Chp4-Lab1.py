#Jackie_Merritt-Chp4_Lab1-6/24/2025

#Initial Inputs
def main():
    print("Temperature Converter")
    print()
    t = input("What is the current Temp? ")
    
    o = c_or_f()
    validation(o)
    math(o, t)
    

#Validation check
def c_or_f():
    print()
    o = input("Is the current Temperature you just entered in (c)elsius or (f)ahrenheit? ")
    return o

def validation(o):
    
    if o == "c" or o == "f":
        return

    else:
        print("Invalid response, please input c or f")
        c_or_f()



def math(o, t):
    if o == "c":
        i = float(int(t) * 1.8 + 32)
        print(f'The current temperature is {t} celsius, this temperature in fahrenheit is {i:.2f}')
    if o == "f":
        i = float((int(t) - 32) * 5/9)
        print(f'The current temperature is {t} fahrenheit, this temperature in celsius is {i:.2f}')

main()
