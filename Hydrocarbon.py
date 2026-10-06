# Calculator of name of "Saturated Hydrocarbon"

C = int(input()) # Taking calculated number of hydrogen from user
n = 1 # Puting the number of carbon
form_1 = "ane"
form_2 = "ene"
form_3 = "yen"

name = ["Meth", "Eth", "Prop", "But", "Pent", "Hex", "Hept", "Oct", "Non", "Dec"]

# For 1st form

if n == 1 and C == 2*n + 2:
 print(name[0] + form_1)
if n == 2 and C == 2*n + 2:
 print(name[1] + form_1)
if n == 3 and C == 2*n + 2:
 print(name[2] + form_1)
if n == 4 and C == 2*n + 2:
 print(name[3] + form_1)
if n == 5 and C == 2*n + 2:
 print(name[4] + form_1)
if n == 6 and C == 2*n + 2:
 print(name[5] + form_1) 
if n == 7 and C == 2*n + 2:
 print(name[6] + form_1)
if n == 8 and C == 2*n + 2:
 print(name[7] + form_1)
if n == 9 and C == 2*n + 2:
 print(name[8] + form_1)
if n == 10 and C == 2*n + 2:
 print(name[9] + form_1)

# For 2nd form  

if n == 1 and C == 2*n:
 print('• Methene does not exist and it has two reason')
 print("1> It does not satisfy the valency of C-atom.")
 print("2> It require minimum two C-atom for double covalent bond.")
if n == 2 and C == 2*n:
 print(name[1] + form_2)
if n == 3 and C == 2*n:
 print(name[2] + form_2)
if n == 4 and C == 2*n:
 print(name[3] + form_2)
if n == 5 and C == 2*n:
 print(name[4] + form_2)
if n == 6 and C == 2*n:
 print(name[5] + form_2) 
if n == 7 and C == 2*n:
 print(name[6] + form_2)
if n == 8 and C == 2*n:
 print(name[7] + form_2)
if n == 9 and C == 2*n:
 print(name[8] + form_2)
if n == 10 and C == 2*n:
 print(name[9] + form_2) 

# Fore 3rd form

if n == 1 and C == 2*n - 2:
 print('• Methyne does not exist and it has two reason')
 print("1> It does not satisfy the valency of C-atom.")
 print("2> It require minimum two C-atom for triple covalent bond.")
if n == 2 and C == 2*n - 2:
 print(name[1] + form_3)
if n == 3 and C == 2*n - 2:
 print(name[2] + form_3)
if n == 4 and C == 2*n - 2:
 print(name[3] + form_3)
if n == 5 and C == 2*n - 2:
 print(name[4] + form_3)
if n == 6 and C == 2*n - 2:
 print(name[5] + form_3) 
if n == 7 and C == 2*n - 2:
 print(name[6] + form_3)
if n == 8 and C == 2*n - 2:
 print(name[7] + form_3)
if n == 9 and C == 2*n - 2:
 print(name[8] + form_3)
if n == 10 and C == 2*n - 2:
 print(name[9] + form_3) 
