H, M = tuple(map(int, input().split()))

if H == 0 and M == 0:
    print(23-H, 60-45)
elif H == 0 and M < 45:
    print(23-H, 15+M)
elif H == 0 and M >= 45:
    print(H, M-45)
elif H != 0 and M < 45:
    print(H-1, 15+M)
else:
    print(H, M-45)