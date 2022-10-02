def solution(a, k):
    count = []
    for i in range(1,max(a)):
        sum_ = 0
        for j in a:
            sum_+=j//i
        count.append(sum_)
    print(count)
    for i in range(len(count)):
        if count[i] == k:
            return i+1
        else:
            if count[i] > k and count[i+1]< k:
                 return i+1
        
