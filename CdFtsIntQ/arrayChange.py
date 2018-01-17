
def arrayChange(arr):
    resMov = 0
    i = 0
    while i < len(arr)-1:
        if arr[i+1]<=arr[i]:
            break
        i += 1
    
    i += 1
    if i == len(arr):
        return 0
    
    while i < len(arr):
        diff = arr[i-1]-arr[i]+1
        if(diff >= 0):
            arr[i] += diff
            resMov += diff
        i += 1
    
    return resMov


if __name__ == '__main__':
    print arrayChange([2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15])