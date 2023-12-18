from sys import stdin

def gcd_(a,b):
    a,b = a,b
    if a == b:
        gcd = a
    else:
        gcd = b
        while True:
            if a % b == 0:
                break
            gcd = a % b
            a = b
            b = gcd
    return gcd

N = int(input())
for _ in range(N):
    # a,b = map(int, input().split())
    a,b = map(int, stdin.readline().rstrip().split())
    print(int(a * b / gcd_(a,b)))