def getPrimes(number):
    factors_list = []
    i = 2   
    while number>1:     
        while number%i == 0:
            factors_list.append(i)
            number/=i
        i+=1
    
    return factors_list

print getPrimes(5)