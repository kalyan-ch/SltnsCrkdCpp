def possibleSums(coins,quantity):
    arrSum = sum(map(lambda t: t[0] * t[1], zip(coins, quantity)))

    dp = [False]*(arrSum+1)
    dp[0] = True
    
    print dp
    
    for c,q in zip(coins,quantity):
        for i in range(c):
            num = -1
            for j in range(i,arrSum+1,c):
                if dp[j]:
                    num = 0
                elif num >= 0:
                    num += 1

                dp[j] = 0 <= num <= q

    return (sum(dp)-1)



if __name__ == '__main__':
    print possibleSums([2,1,5],[1,2,1])