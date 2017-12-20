# Enter your code here. Read input from STDIN. Print output to STDOUT

def getSet(arr,k):
    a = [0]*k
    for x in arr:
        a[x%k] += 1
    
    count = min(a[0],1)
    for i in range(1,k/2 + 1):
        if i != k-i:
            count += max(a[i],a[k-i])

    if k % 2 == 0:
        count += 1

    return count

if __name__ == '__main__':
    
    n,k = raw_input("").split(" ")
    arr = map(int, raw_input("").split(" "))
    n = int(n)
    k = int(k)
    
    print getSet(arr,k)