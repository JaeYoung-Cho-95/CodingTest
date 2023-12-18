# A,B 입력받기
A,B = map(int, input().split())
# 1 ~ A 까지 있는 리스트 생성
data_list = [x for x in range(1,A+1)]

# 결과로 출력할 리스트 생성
result = []

# 접근할 인덱스 변수 생성
index_num = B - 1

# 1~A 까지 모두 요세푸스 수열로 변환해야하기 때문에 A 만큼 반복
for _ in range(A):
    # 만약 index_num 이 data_list 의 길이보다 작다면
    if index_num < len(data_list):
        
        # 결과 리스트에 담아준다.
        # string 타입으로 변환하는 이유는 나중에 출력을 편리하게 하려고
        result.append(str(data_list[index_num]))
        # result 리스트에 담고 data_list 에서는 제거
        del data_list[index_num]

        # 다음에 접근할 index_num 은 B 만큼이 아니라 (B-1) 만큼 접근한다.
        # data_list 의 길이가 하나만큼 짧아지기 때문
        index_num += (B-1)
        
    # 만약, index_num 이 data_list 의 길이보다 길다면
    elif index_num >= len(data_list):
        
        # index_num 에서 data_list 의 길이만큼 빼줘서 0부터 다시 접근하게 한다.
        # 단, data_list 의 길이가 1 또는 2와 같이 작은 경우 
        # index_num 에서 빼도 data_list 의 길이보다 클 수 있기 때문에 작아질 때 까지 빼준다.
        while True:
            index_num = index_num - len(data_list) 
            
            # 빼주다가 만약, data_list 의 길이보다 작아지면
            if index_num < len(data_list):
                # result 에 append 하고
                result.append(str(data_list[index_num]))
                # data_list 에서 삭제
                del data_list[index_num]
                # index_num B-1만큼 증가
                index_num += (B-1)

                break

print('<' + ', '.join(result) + '>')