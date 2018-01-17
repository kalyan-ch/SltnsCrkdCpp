
def rev(s):
    s1 = ""
    i = len(s) - 1
    while i >= 0:
        s1 += s[i]
        i -= 1
    return s1

def reverseB(s):
    stk = []
    arr = [x for x in s]

    for i in range(len(s)):
        if s[i] == "(":
            stk.append(i)
        elif s[i] == ")":
            j = stk.pop();
            a = rev(arr[j+1: i])
            ind = 0
            for x in range(j+1,i):
                arr[x] = a[ind]
                ind += 1
    res = ""
    for x in arr:
        if x != "(" and x != ")":
            res += x

    return res



if __name__ == '__main__':
    print reverseB("The ((quick (brown) (fox) jumps over the lazy) dog)")