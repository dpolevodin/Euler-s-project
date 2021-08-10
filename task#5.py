#2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
#
#Какое самое маленькое число делится нацело на все числа от 1 до 20? Ответ: 232792560

def div_without_rem(min_range, max_range):
    num_list = list(range(min_range,max_range))
    print('Searchin min value of division withot remainder in range: ', num_list)
    min_int = 1
    sum_result = []
    result = []
    while sum_result != 0:
        result = []
        for i in num_list:
            div_num = min_int % i
            result.append(div_num)
        sum_result = sum(result)
        if sum_result == 0:
            print('Min value of division withot remainder in range is: ', min_int)
            break
        else: 
            min_int += 1

div_without_rem(1,21)
