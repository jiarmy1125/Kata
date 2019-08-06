# min_sum([5,4,2,3]), 22
# min_sum([12,6,10,26,3,24]), 342
# min_sum([9,2,8,7,5,4,0,6]), 74

def min_sum(arr):
    x=[]
    y=[]

    sum=0
    for i in range(len(arr)//2):
        arr=sorted(arr,reverse=True)
        # print(arr[i])
        x.append(arr[i])
    for j in range(len(arr)//2):
        arr=sorted(arr)
        # print(arr[j])
        y.append(arr[j])

    print(x,y)

    for k in range(len(x)):
        sum += x[k]*y[k]

    print(sum)
    return sum

min_sum([9,2,8,7,5,4,0,6])