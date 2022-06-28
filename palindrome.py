#if palindrome
def isPal(s):
    return s == s[::-1]
s = input("Enter a string: ")
if(isPal(s) == True):
    print("Yes")
else:
    print("No")

#print palindrome
s = input("Enter a string: ")
rev = s[::-1]
print("Reverse: ", rev)

