#Name: CARDINALE
#Prog Purpose: This program computers college tuition and fees based on the number of credits
#   PVCC Tuition rates are from: http://www.pvcc.edu/tuition-and-fees
#   Note all fees are per credit
#       In-state: $155, out-of-state: $331.60
#       Capital Fee: $23.50 (out-of-state students only)
#       Instition fee : $1.75
#       Activity fee: $2.90

import datetime
#define tuition & fee rates
RATE_TUT_IN = 155
RATE_TUT_OUT = 331.6
RATE_CAP = 23.5
RATE_INS = 1.75
RATE_ACT = 2.9

#define global variables
inout = 1 # 1 = in-state 2 = out-of-state
numcredits = 0
scholarshipamt = 0
tuitionfee = 0
capitalfee = 0
institutionfee = 0
activityfee = 0
totalowed = 0
balance = 0

##define program functions
def main():
    another_student = True
    while another_student:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to calculate tuition and fees for another student (Y/N): ")
        if yesno.upper() !="Y":
            another_student = False
    

def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter 1 for IN-STATE; enter a 2 for OUT-OF-STATE:  "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = float(input("Scholarship amount received: "))

def perform_calculations():
    global tuitionfee, capitalfee, institutionfee, activityfee, totalowed, balance
    if inout == 1:
        tuitionfee = numcredits * RATE_TUT_IN
        capitalfee = 0
    else:
        tuitionfee = numcredits * RATE_TUT_OUT
        capitalfee = numcredits * RATE_CAP

    institutionfee = numcredits * RATE_INS
    activityfee = numcredits * RATE_ACT
    totalowed = tuitionfee + capitalfee + institutionfee + activityfee
    balance = totalowed - scholarshipamt

def display_results():
    print('\n------------------------------------')
    print('Number of credits : ' + str(numcredits))
    print('--------------------------------------')
    print('Tuition           $ ' + format(tuitionfee,'10,.2f'))
    print('Capital fee       $ ' + str(capitalfee))
    print('Institution fee   $ ' + str(institutionfee))
    print('Activity fee      $ ' + str(activityfee))
    print('Total             $ ' + str(totalowed))
    print('Scholarship       $ ' + str(scholarshipamt))
    print('--------------------------------------')
    print('Balance owed      $ ' + str(balance))
    print('--------------------------------------')
    print(str(datetime.datetime.now()))
    print('Note: PVCC Fee Rates: https://www.pvcc.edu/tuition-and-fees')

##Call on main program to execute
main()


