# order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est"
# order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople"
# order(""), ""

def order(sentence):
    sen = sentence.split()
    # print(sen)

    word=''

    for i in range(len(sen)+1):
        x = str(i)

        for j in sen:
            if x in j:
                # print(j)
                word += j+ " "
    # print(word)
    return word.strip(" ")
            
            



print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))