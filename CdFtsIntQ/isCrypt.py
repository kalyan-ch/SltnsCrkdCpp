num_dict = {}


def getSum(word):
    count = 0
    n = len(word)
    for i in range(n):
        if i == 0 and num_dict[word[i]] == 0 and n > 1:
            count = -1
            break
        count += ((10**(n-i-1))*num_dict[word[i]])

    return count

def isCryptSolution(crypt, solution):
    
    for arr in solution:
        num_dict[arr[0]] = int(arr[1])

    word1 = getSum(crypt[0])
    word2 = getSum(crypt[1])
    word3 = getSum(crypt[2])

    if word1 == -1 or word2 == -1 or word3 == -1:
        return False

    if word1 + word2 != word3:
        return False

    return True


if __name__ == '__main__':
    crypt = ["A","A","A"]
    solution = [["A","0"]]

    print isCryptSolution(crypt,solution)