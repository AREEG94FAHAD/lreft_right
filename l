def solution(numbers, left, right):


    nums = [i for i in range(left, right+1)]
    resutls = []
    
    for i in range(len(numbers)):
        ok = numbers[i] in [(i+1) * j for j in nums]
        resutls.append(ok)
    return (resutls)
        
        
        
        
        
        
