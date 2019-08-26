# :) :D ;-D :~) ;( :> :} :]
# count_smileys([]), 0
# count_smileys([':D',':~)',';~D',':)']), 4
# count_smileys([':)',':(',':D',':O',':;']), 2
# count_smileys([';]', ':[', ';*', ':$', ';-D']), 1

def count_smileys(arr):
    sum = 0 
    for arr_1 in arr:
        if ':)' in arr_1:
            # print(arr_1)
            sum+=1

        elif ':D' in arr_1:
            # print(arr_1)
            sum+=1

        elif ';)' in arr_1:
            # print(arr_1)
            sum+=1

        elif ';D' in arr_1:
            # print(arr_1)
            sum+=1

        elif ';~D' in arr_1:
            # print(arr_1)
            sum+=1

        elif ';-D' in arr_1:
            # print(arr_1)
            sum+=1

        elif ':~)' in arr_1:
            # print(arr_1)
            sum+=1

        elif ':-)' in arr_1:
            # print(arr_1)
            sum+=1

        elif ':~D' in arr_1:
            # print(arr_1)
            sum+=1

        elif ':-D' in arr_1:
            # print(arr_1)
            sum+=1

        elif ';-)' in arr_1:
            # print(arr_1)
            sum+=1

        elif ';~)' in arr_1:
            # print(arr_1)
            sum+=1

    print(sum)

count_smileys([]), 0
count_smileys([':D',':~)',';~D',':)']), 4
count_smileys([':)',':(',':D',':O',':;']), 2
count_smileys([';]', ':[', ';*', ':$', ';-D']), 1