#Jackie_Merritt-Chp4_Lab1-6/24/2025

#Initial Inputs
def main():
    print('Temperature Converter')
    print()
    #Attaches user input to variable 't'
    t = float(input('What is the current Temp? '))

    #Assigns valid_data to false and repeats if valid_data is considered False still at later point.
    valid_data = False
    while valid_data == False:

        #Assigns user input to variable 'o'
        o = input('Is the current Temperature you just entered in (c)elsius or (f)ahrenheit? ')

        if o.lower() == 'c' or o.lower() == 'f':
            #Valid data is considered True and so question does not repeat and Python moves on
            valid_data = True

        #Prints error message when incorrect and repeats question
        else:
            print('Invalid response, please input c or f')
        
    #Determines if o = celsius or fahrenheit and uses the correlating function to convert it to opposite temperature
    if o == 'c':
        c = celsius(t)
        print(f'The current temperature is {t} celsius, this temperature in fahrenheit is {c:.2f}')
    if o == 'f':
        fahrenheit(t)


#Translates celsisus to fahrenheit
def celsius(t):
    return float(t * 1.8 + 32)

#Translates fahrenheit to celsius
def fahrenheit(t):
    i = float((t - 32) * 5/9)
    print(f'The current temperature is {t} fahrenheit, this temperature in celsius is {i:.2f}')

if __name__ == '__main__':
    main()
