import sys

for i in range(int(input())):
    x = int(sys.stdin.readline())
		# 2 이하인 경우 가장 가까운 소수는 2이다.
    if x <= 2:
        print(2)
        continue

    # 2보다 큰 경우
    while True:
				# 1보다 큰 자연수 x 의 약수가 sqrt(x) 범위까지 없다면 소수이다.
        std_num = int(x**(1/2))
        check = True
        
        for i in range(2,std_num+1):
            if x % i == 0:
                check = False
                break

        if check:
            print(x)
            break

        else: x+=1