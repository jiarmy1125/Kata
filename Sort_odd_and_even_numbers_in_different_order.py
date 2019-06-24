# Your task is to sort odd numbers within the array in ascending order, and even numbers in descending order.
# Note that zero is an even number. If you have an empty array, you need to return it.

# sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 8, 4, 5, 2]

def sort_array(a):
    odd = []
    even = []
    new = []

    for i in a: #分奇數偶數
        if i%2==0:
            odd.append(i)

        else:
            even.append(i)

    odd_reverse = sorted(odd,reverse=True) #將偶數降冪排列
    even_sort = sorted(even)   #將奇數升冪排列

    j=0
    k=0
    for i in a: #將數字重新放回原陣列中
        if i%2==0:
            new.append(odd_reverse[j])
            j += 1
            
        else: 
            new.append(even_sort[k])
            k += 1

    return new

result = sort_array([5, 3, 2, 8, 1, 4])
print(result)


