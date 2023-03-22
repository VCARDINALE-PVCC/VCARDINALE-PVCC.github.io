# Name: Cardinale
# Prog Purpose: To convert temprature in celsius to fehrenheit

#define variables
c_temp = 0
f_temp = 0

another_temp = True
while another_temp:
        c_temp = int(input("Enter the degrees Celsius you want to convert: "))

        #calculate fahrenheit
        f_temp = (c_temp * 1.8) + 32

        #display result
        print("Celsius   : " + str(c_temp))
        print("Fehrenheit: " + str(f_temp))
        yesno = input("\nWould you like to convert another Celsius temprature? (Y/N): ")
        if yesno == "n" or yesno == "N":
            another_temp = False

