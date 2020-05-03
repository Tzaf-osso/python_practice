def func(num):
    print(num)
    print(type(num))




# 0 1 1 2 3 5 8 13 21 34

def get_index_from_fib(num):
    prev_index = 0
    curr_index = 1
    count = 2

    sum = prev_index + curr_index
    print(sum)

    while sum < num:
        sum = prev_index + curr_index
        prev_index = curr_index
        curr_index = sum
        count = count + 1
        print(sum)
    print(count)


func("tzaf")
get_index_from_fib(21)




