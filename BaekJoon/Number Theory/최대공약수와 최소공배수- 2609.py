a,b = map(int, input().split())
copy_a, copy_b = a,b

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

lcm = int(copy_a * copy_b / gcd)

print(gcd)
print(lcm)