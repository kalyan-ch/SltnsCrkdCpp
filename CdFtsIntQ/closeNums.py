import itertools

def containsCloseNums(nums, k):
    num_dict = {}
    nu_dic = {}
    n = len(nums)
    res = False
    
    for i in range(n):
        num = nums[i]
        num_dict[i] = num
        
        cnt = nu_dic.get(num,0)
        cnt += 1
        nu_dic[num] = cnt
    
    
    arr = []
    for num in nu_dic:
        if nu_dic[num] > 1:
            for x in num_dict:
                if num_dict[x] == num:
                    arr.append(x)
    
    for x,y in itertools.combinations(arr,2):
        if abs(x-y) <= k:
            res = True
            break
    
    return res
    


if __name__ == '__main__':
    arr = []
    k = 0
    print containsCloseNums(arr,k)