# Your task is to sort odd numbers within the array in ascending order, and even numbers in descending order.
# Note that zero is an even number. If you have an empty array, you need to return it.

# sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 8, 4, 5, 2]

def sort_array(a):
    x = []
    y = []
    z = []

    for i in a:
        if i%2==0:
            x.append(i)

        else:
            y.append(i)

    b = sorted(x,reverse=True)
    c = sorted(y)

    j=0
    k=0
    for i in a:
        if i%2==0:
            z.append(b[j])
            j += 1
            
        else: 
            z.append(c[k])
            k += 1

    return z

result = sort_array([5, 3, 2, 8, 1, 4])
print(result)


