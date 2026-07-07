def double_it(num):
    result = num * 2
    print(result)
    return result

double_it(50)

def sum(num1,num2):
    result = num1 + num2
    return result
total = sum(30,23)
print('total value',total)

final = double_it(40) + sum(33,23)
print('Final result',final)
