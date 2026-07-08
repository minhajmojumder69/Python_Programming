# def double_it(num):
#     return num*2

double_it = lambda num : num*2
squared = lambda num : num**2

# result = squared(44)
# print(result) 

# add = lambda x,y : x+y
# sum = add(29+3)

numbers = [29,12,34,56,74,21,45,67,75,12,12]
double_num = map(double_it, numbers)
print(numbers)
print(list(double_num))
squared_num = map(lambda num : num**2,numbers)
print(list(squared_num))

actors = [
    {'name' : 'priyanka', 'age' : 49},
    {'name' : 'Sunny Leone', 'age' : 35},
    {'name' : 'Srabonti', 'age' : 69},
    {'name' : 'Hasina', 'age' : 29},
    {'name' : 'Nusrat', 'age' : 25},
    {'name' : 'Sheon', 'age' : 23},
    {'name' : 'layla', 'age' : 43},
]

juniors = filter(lambda x : x['age'] < 30,actors)
print(list(juniors))