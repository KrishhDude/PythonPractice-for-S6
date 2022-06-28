n = int(input("Enter the limit: "))
n1, n2 = 0, 1
count = 0
if(n<=0):
    print("Enter a positive integer")
elif(n==1):
    print("Fibonacci sequence upto 1 term: ", n1)
else:
    print("Fibonacci seq:")
    while(count <= n):
        print(n1, end=' ')
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1  