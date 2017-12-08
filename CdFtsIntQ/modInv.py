def modInverse(n, m):
    res = -1
    for x in range(m):
        if (n*x)%m == 1:
            res = x
            break
    return res


if __name__ == '__main__':
	print modInverse(5,300)