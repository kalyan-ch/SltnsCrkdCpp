def findProfession(level, pos):
    answer = "Engineer"
    num_nds = 2**(level-1)
    last_ind = 2**(level) - 1
    first_ind = 2**(level-1)

    ind_pos = first_ind+pos-1
    count = 0
    par_ind = ind_pos
    
    while par_ind > 0:       
        if par_ind % 2 != 0 and par_ind!=1:
            count += 1
        par_ind = par_ind/2
        
    if count%2 !=0:
        answer = "Doctor"
    return answer
