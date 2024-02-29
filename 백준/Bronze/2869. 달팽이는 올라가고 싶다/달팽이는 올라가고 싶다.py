arr = list(map(int, input().split()))
A = arr[0]
B = arr[1]
V = arr[2]
x=0
if((V-B)%(A-B) == 0):
    x = (V-B)/(A-B)
    print(int(x))
else:
    x = ((V-B)//(A-B))+1
    print(int(x))