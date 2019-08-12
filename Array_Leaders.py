def array_leaders(numbers):
    numbers.append(0)
    print(numbers)

    num=[]

    sum=0
    
    for j in range(len(numbers)-1):
        x=numbers.pop(0)
        sum=0
        print(x)

        for i in range(len(numbers)):
            sum += numbers[i]
            
        if x >sum:
            num.append(x)
            

        # print(sum)
    print(num)
    return num

array_leaders([1,2,3,4,0]), [4]
array_leaders([16,17,4,3,5,2]), [17,5,2]