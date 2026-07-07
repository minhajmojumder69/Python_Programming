# def sum(num1,num2):
#     result = num1 + num2
#     return result
# print(sum(20,34))

# def sub(*numbers):     
#     print(numbers)
#     result = 0
#     for num in numbers:
#         result += num 
#         print(result)

# sub(20,30,49)

def sub(num1,num2,*numbers):     
    print(numbers)
    result = 0
    for num in numbers:
        result += num 
        print(result)

sub(20,30,49,40,33) 