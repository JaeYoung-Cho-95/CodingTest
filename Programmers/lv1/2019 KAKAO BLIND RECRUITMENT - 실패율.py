def solution(N, stages):
    import collections
    stages = collections.Counter(stages)
    try: 
        cnt = 0
        zeros = []
        cnt += stages[N+1]
    finally:
        result = {}
        for i in range(N,0,-1):
            cnt += stages[i]
            try:
                if stages[i] / cnt == 0:
                    zeros.append(i)
                    continue
            except:
                zeros.append(i)
                continue
            result[i] = stages[i] / cnt

        result = sorted(result, key= lambda x : result[x])
        result.reverse()
        zeros.sort()

        return result + zeros