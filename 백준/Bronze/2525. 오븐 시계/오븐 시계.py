A, B = tuple(map(int, input().split()))
C = int(input())

if B+C >= 60:
    A += (B+C)//60
    B = (B+C) - 60*((B+C)//60)

    if B+C > 60:
        B = B-60*(B//60)
        A += 1*(B//60)
    if A >= 24:
        A = A % 24

else:
    B = B+C
    
print(A, B)