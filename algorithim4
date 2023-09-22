# HW 4
# Task 1

def sum_even_an_product_odd(arr: list):
    sum_even = 00
    product_odd = 1

    for e in arr:
        if e % 2 == 0:
            sum_even += e
        else:
            product_odd *= e
    return [sum_even, product_odd]

print(sum_even_an_product_odd([1, 2, 3, 4]))



# Task 2

def sum_between_range(arr: list, min_val: int, max_val: int):

    total_sum = 0
    for num in arr:
        if min_val <= num <= max_val:
            total_sum += num
    return total_sum

arr = [3, 2, 1, 4, 10, 8, 7, 6, 9, 5]
min_val = 3
max_val = 7
result = sum_between_range(arr, min_val, max_val)
print(result)



# Task 3

def buy_and_sell_stock(prices: list):
    maximum = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            maximum += prices[i] - prices[i - 1]
    return maximum

prices = [7, 1, 5, 3, 6, 4]
result = buy_and_sell_stock(prices)
print(result)




# Task 4

def plus_one(arr: list):
    n = len(arr)
    carry = 1

    for i in range(n - 1, -1, -1):
        total = arr[i] + carry
        arr[i] = total % 10
        carry = total // 10

        if carry:
            arr.insert(0, carry)

input_digits = [1, 2, 9]
plus_one(input_digits)
print(input_digits)