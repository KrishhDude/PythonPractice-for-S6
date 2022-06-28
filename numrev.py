#simple
n = input("Enter a number: ")
s = n[::-1]
print(s)

#using loop
num = int(input("Enter a number"))
rev = 0
while(num != 0):
    digit = num % 10
    rev = rev*10 + digit
    num //= 10
print("Reverse: ", str(rev))