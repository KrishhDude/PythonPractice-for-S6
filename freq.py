#for a number
n = int(input("Enter a number: "))
f = input("Enter digit whose frequency to be checked: ")
count = 0
s = str(n)
for i in range(len(s)):
    if(s[i] == f):
        count+=1
print(count)

#for a string
string=input("Enter the string: ")
char=input("Enter the char to find frequency ")

count=0
for i in range(len(string)):
    if(string[i]==char):
        count=count+1
print(count)

