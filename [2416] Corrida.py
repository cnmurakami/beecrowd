C, N = input().split(" ")
C, N = int(C), int(N)

voltas = C//N
R = C - (N*voltas)
print(R)
