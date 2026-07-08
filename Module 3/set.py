# list --> []
# tuple --> ()
# set --> {}

# set is a collection of unique items. No duplicate
numbers = [23,41,45,35,46,75,31,45,35,23,52,56,47]
number_set = set(numbers)
print('size of numbers',len(numbers))
print('size of number set',len(number_set))
print(number_set)

A = {1,2,3,4}
B = {2,4,6,8}
print(A&B)
print(A|B)