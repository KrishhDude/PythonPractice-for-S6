#password flagidation
'''
 At least 1 letter between [a-z] and 1 letter between [A-Z].
 At least 1 number between [0-9].
 At least 1 character from [$#@].
 Minimum length 6 characters.
 Maximum length 16 characters.
'''
def checkPass(password):
      
    specialChars =['$', '#', '@']
    flag = True    
    if len(password) < 6 or len(password)>16:
        flag = False

    if not any(char.isdigit() for char in password):
        flag = False
          
    if not any(char.isupper() for char in password):
        flag = False
          
    if not any(char.islower() for char in password):
        flag = False
          
    if not any(char in specialChars for char in password):
        flag = False
        
    if flag:
        return flag

password = input("Enter password: ")
if (checkPass(password)):
    print("Password is valid")
else:
    print("Invalid Password !!")
