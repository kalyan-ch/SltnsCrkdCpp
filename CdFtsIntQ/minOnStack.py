stk = []
minStk = []

def getMin():
    if stk:
        return minStk[-1]
    else:
        return 10**10


def minimumOnStack(operations):
    res = []
    for op in operations:
        arr = op.split(" ")
        if arr[0] == "push":
            num = int(arr[1].strip())
            stk.append(num)

            if num < getMin():
                minStk.append(num)

        elif arr[0] == "pop":
            val = stk.pop()

            if val == getMin():
                minStk.pop()

        elif arr[0] == "min":

            res.append(getMin())


    return res
            



