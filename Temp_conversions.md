#Temperature Conversions
print("Python program to convert temperature to and from Celsius, Fahrenheit.\n")

#Converting Celcius to Farenheit
C1=input ("Enter temperature in Celcius to be converted into Fahrenheit: ")
F1=((float(C1)*(9/5))+32)
print("The temperature {0} in Celcius is {1} in Fahrenheit.\n\n". format (C1,F1))


#Converting Fahrenheit to Celcius
F2=input ("Enter temperature in Farenheit to be converted into Celsius: ")
C2=((float(F2)-32)*(5/9))
print("The temperature {0} in Fahrenheit is {1} in Celcius. \n ". format (F2,C2))
