# find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5

def find_it(seq):
    for j in seq:
        if ((seq.count(j))%2 == 1):
            return j

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))