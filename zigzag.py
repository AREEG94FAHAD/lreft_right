def solution(a):
    b = []
    for i in range(len(a)//2):
        b.append(a[i])
        b.append(a[-1-i])
        
    if len(b) != len(a):
        b.append(a[math.ceil(len(a)//2)])
        
    print(b)
    if len(set(b)) != len(b):
        return False
    return b == sorted(a)

