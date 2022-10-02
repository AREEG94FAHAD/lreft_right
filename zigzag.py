def solution(a):
    b = []
    len_a = len(a)

    for i in range(len_a//2):
        b.append(a[i])
        b.append(a[-1-i])
        
    if len(b) != len_a:
        b.append(a[math.ceil(len_a//2)])
        
    len_b = len(b)
    if len(set(b)) != len_b:
        return False
    return b == sorted(a)

