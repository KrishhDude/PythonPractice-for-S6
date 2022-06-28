# Enter your code here. Read input from STDIN. Print output to STN=DOUT
N=int(input())
for i in range(N):
    for j in range(N-1):
        print(end=' ')
    print('*')
    N=N-1