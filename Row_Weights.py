# row_weights([50,60,70,80]), (120,140)
# row_weights([13,27,49]), (62,27)
# row_weights([70,58,75,34,91]), (236,92)
# row_weights([29,83,67,53,19,28,96]), (211,164)

def row_weights(array):
    num_1=0
    num_2=0
    num=[]
    for i in range(len(array)):
        if i%2==0:
            # print("even",i)
            num_1 += array[i]

        else:
            # print("odd",i)
            num_2 += array[i]
            
            
    # print("even",num_1)
    num.append(num_1)
    # print("odd",num_2)
    num.append(num_2)
    
    # print(tuple(num))

    return num_1,num_2

print(row_weights([50,60,70,80]))
row_weights([29,83,67,53,19,28,96])