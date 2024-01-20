import time
import Functions
from colorama import init, Fore
import sys
init()
init(autoreset=True)

# All the Necessary  and variables

useful_variables = []
tempPass = []
mainPass = []
modules = ['time', 'colorama']
modules_not_exist = []
modules_exists = 0
Basic_variables = []
finalPass = []


for x in modules:
    if x in sys.modules:
        print(Fore.GREEN+'[+]'+Fore.CYAN+'Module '+x+' exists')
        time.sleep(1)
        modules_exists = modules_exists+1
    else:
        print('[-]'+'Module '+x+' Doesnt exist')
        modules_not_exist.append(x)
# Loop for checking module ends here
# Main structure of program
if modules_exists == len(modules):
    print(Fore.GREEN + "[+]" + Fore.CYAN + 'All the  required modules were found')
    time.sleep(1)
    print(Fore.GREEN + '[+]' + Fore.CYAN + "Continuing")
    time.sleep(1)
    VictimName = input("Enter the First Name: ")
    VictimLastName = input("Enter the Last Name: ")
    VictimOrg = input("Enter the Organisation: ")
    VictimDOB = input("Enter the YOB: ")
    VictimPhone = input("Enter the Phone Number: ")
    VictimPets = input("Enter the Pet Name: ")
    VictimFather = input("Enter the Father Name: ")
    VictimMother = input("Enter the Mother's Name: ")
    VictimGF = input("Enter the Victim GF or Wife's Name: ")
    VictimNickName = input("Enter the Nick Name: ")
    VictimState = input("Enter the State where he lives: ")
    VictimBornState = input("Enter the State where he was born: ")
    VictimIdol = input("Enter the idol of the victim: ")
    VictimCity = input("Enter the City where he lives: ")
    VictimBornCity = input("Enter the City where he was Born: ")
    VictimBornCountry = input("Enter the Country where he was Born: ")
    VictimCountry = input("Enter the Country where he lives: ")
    VictimChild = input("Enter the name of there Child: ")
    VictimChild2 = input("Enter the name of there second Child: ")
    VictimLoves = input("Enter something/someone they love:")

    #  Use the VarChecker to filter useful_variables

    Functions.VarChecker(VictimName, useful_variables)
    Functions.VarChecker(VictimOrg, useful_variables)
    Functions.VarChecker(VictimDOB, useful_variables)
    Functions.VarChecker(VictimPhone, useful_variables)
    Functions.VarChecker(VictimPets, useful_variables)
    Functions.VarChecker(VictimFather, useful_variables)
    Functions.VarChecker(VictimMother, useful_variables)
    Functions.VarChecker(VictimGF, useful_variables)
    Functions.VarChecker(VictimNickName, useful_variables)
    Functions.VarChecker(VictimState, useful_variables)
    Functions.VarChecker(VictimBornState, useful_variables)
    Functions.VarChecker(VictimIdol, useful_variables)
    Functions.VarChecker(VictimCity, useful_variables)
    Functions.VarChecker(VictimBornCity, useful_variables)
    Functions.VarChecker(VictimBornCountry, useful_variables)
    Functions.VarChecker(VictimCountry, useful_variables)
    Functions.VarChecker(VictimChild, useful_variables)
    Functions.VarChecker(VictimLoves, useful_variables)
    Functions.VarChecker(VictimChild2, useful_variables)
    Functions.VarChecker(VictimLastName, useful_variables)

    # Check how much input was provided by the user
    if not useful_variables:
        time.sleep(1)
        Functions.byebye()

    elif len(useful_variables) <= 8:
        if len(useful_variables) == 0:
            print(Fore.RED+'[-]'+Fore.CYAN+"Seriously !")
        else:
            print(Fore.RED+'[-]'+Fore.CYAN+"Not Enough Input was Given")
            time.sleep(2)
            ContinueorNot = input("Do you still want to continue (Y/n) :")

            if ContinueorNot == 'Y' or ContinueorNot == 'y':
                time.sleep(1)
                print(Fore.RED+'[-]'+Fore.CYAN+"The Number of Keywords Generated would be effected")
                time.sleep(1)
                print(Fore.GREEN+'[+]'+Fore.CYAN+"Continuing")
                time.sleep(1)
                Functions.PassGenBasic(useful_variables, mainPass)
                Functions.PassGen1(mainPass, tempPass)
                Functions.PassGen2(mainPass, tempPass)
                Functions.remove_waste(tempPass, finalPass)
                Functions.FilePrint(tempPass, VictimName)
                print(Fore.GREEN+'[+]'+Fore.CYAN+'The No of Keywords generated are :'+str(len(tempPass)))
            elif ContinueorNot == "N" or ContinueorNot == "n":
                time.sleep(1)
                Functions.byebye()
            else:
                time.sleep(1)
                print('\n'+Fore.RED+'[-]'+Fore.CYAN+"Wrong Input was Provided!")
                Functions.byebye()

    else:
        # Continues the program
        print("")
        Functions.PassGenBasic(Basic_variables, mainPass)
        Functions.FilePrint(tempPass, VictimName)
        Functions.remove_waste(tempPass, finalPass)

else:
    print("[-] Required modules were not found")
    print("Run the below listed command in your cmd or terminal")
    for x in modules_not_exist:
        print("\npython -m pip install ", x)
    print("[?]For more info refer to readme file")
