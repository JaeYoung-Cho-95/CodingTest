import sys

# x가 주어지면 x보다 작은 소수를 모두 구해 list 와 dict 에 담아서 반환
def prime_numbers(x):
    prime_dict = {}
    prime_list = []

		# 에라토스테네스의 체 로직
    for i in range(2,x):
        try: 
            if prime_dict[i] == 0: pass
            
        except:
            prime_dict[i] = 1
            prime_list.append(i)
            
            for j in range(2*i,x,i):
                prime_dict[j] = 0
                
    return prime_dict, prime_list


# 입력받기
datas = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
# 입력받은 값중 가장 큰 값
max_data = max(datas)
# 가장 큰 값으로 에라토스테네스의 체 구해놓기
prime_dict,prime_list = prime_numbers(max_data)

# 입력받은 짝수 - 특정 소수 = 소수라면 cnt += 1
for num in datas:
    std_num, cnt = num/2, 0

		# 소수만 담겨있는 list
    for i in prime_list:
				# 만약, 입력받은 짝수의 절반보다 i가 커지면 더이상 계산할 필요 없음 
        if i > std_num: break
        
        if (prime_dict[i] == 1) and (prime_dict[num-i] == 1):
            cnt += 1    
    print(cnt)