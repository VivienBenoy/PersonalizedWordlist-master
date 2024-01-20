import time
from colorama import init, Fore
init()
def byebye():
    print(Fore.GREEN+'[+]'+Fore.RESET+"Thanks for Using :)")
    time.sleep(1)
    print(Fore.YELLOW+'[?]'+Fore.RESET+'For any Suggestions or to Contact Us See The Readme.md File')

#  Check if Variable's are Empty
def VarChecker(Variable_Name,useful_Variables):
    if not Variable_Name.strip():
        print()

    else:
        useful_Variables.append(Variable_Name)

def EqualChecker(var1,var2,PasswordsGenerated):
    if var1 == var2:
        print("")
    else:
        PasswordsGenerated.append(str(var2))


def PassGenBasic(useful_Variables,PasswordsGenerated):
    i = 0
    for x in useful_Variables:
        PasswordsGenerated.append(useful_Variables[i])
        current_vr = useful_Variables[i]
        current_vr2 = current_vr.upper()
        EqualChecker(current_vr, current_vr2,PasswordsGenerated)
        current_vr = useful_Variables[i]
        current_vr2 = current_vr.lower()
        EqualChecker(current_vr, current_vr2,PasswordsGenerated)
        current_vr = useful_Variables[i]
        current_vr2 = current_vr.title()
        EqualChecker(current_vr, current_vr2,PasswordsGenerated)
        i = i+1


def FilePrint(PasswordsGenerated,vc):
    with open(vc+'.txt', 'wt') as file:
        for words in PasswordsGenerated:
            file.write(words+'\n')


def PassGen1(TempPAsses,PassqordsGenerated):
    for x in TempPAsses:
        PassqordsGenerated.append(x+'@123')
        PassqordsGenerated.append(x+'@007')
        PassqordsGenerated.append(x+'@098')
        PassqordsGenerated.append(x+'@089')
        PassqordsGenerated.append(x+'123')
        PassqordsGenerated.append(x+'456')
        PassqordsGenerated.append(x+'789')
        PassqordsGenerated.append(x+'098')
        PassqordsGenerated.append(x+'089')



def PassGen2(useful_Variables,PasswordsGen):
    for x in useful_Variables:
        for y in useful_Variables:
            if x == y:
                continue
            else:
                PasswordsGen.append(x + y)
                PasswordsGen.append(x + '@' + y)
                PasswordsGen.append(x+'loves'+y)
                PasswordsGen.append(x+'.'+y)

def remove_waste(TempPasses, FinalPasses):
    for x in TempPasses:
        for z in TempPasses:    
            if z not in FinalPasses:
                FinalPasses.append(z)
            else:
                continue
