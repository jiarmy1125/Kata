# count_sheep(1), "1 sheep..."
# count_sheep(2), "1 sheep...2 sheep..."
# count_sheep(3), "1 sheep...2 sheep...3 sheep..."

def count_sheep(n):

    word=''
    for i in range(1,n+1):
        sheep='sheep...'
        word += str(i)+ " " +sheep
    print(word)



count_sheep(2)