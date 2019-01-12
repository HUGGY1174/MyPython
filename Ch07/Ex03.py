def get_sum(start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum

def get_odd_sum(start, end):
    sum = 0
    for i in range(start, end + 1):
        if i % 2 == 1:
            sum += i
    return sum

result = get_sum(1, 100)
odd_result = get_odd_sum(1, 100)
print(result)
print(odd_result)
