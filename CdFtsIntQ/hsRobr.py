import copy

def addNtoC(a,n):
    ar = copy.deepcopy(a)
    
    for x in ar:
        x.append(n)

    return ar

def getCombs(n,memo):

    if memo.get(n,[]):
        return memo[n]

    if n == 0:
        memo[0] = [[0]]
        return [[0]]
    if n == 1:
        memo[1] = [[0],[1]]
        return [[0],[1]]
    
    a = getCombs(n-2,memo)
    ar = addNtoC(a,n)
    res = getCombs(n-1,memo)
    ar1 = copy.deepcopy(ar)
    ar2 = []
    ar2.extend(ar1)
    ar2.extend(res)
    memo[n] = ar2
    return ar2

def houseRobber(nums):
    gold = []
    n = len(nums)
    if n == 0:
        return 0
    memo = {}
    res = getCombs(n-1,memo)

    for x in res:
        g = 0
        for y in x:
            g += nums[y]
        gold.append(g)
    
    return max(gold)


if __name__ == '__main__':
    print houseRobber([4,2,7,3,5,8])

