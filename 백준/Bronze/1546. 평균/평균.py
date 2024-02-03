n = int(input())
arr = list(map(int, input().split()))
M = max(arr)
s=0

for i in range(0, n):
    arr[i] = (arr[i] / M) * 100
    s += arr[i]
    
avg = s/len(arr)
print(avg)