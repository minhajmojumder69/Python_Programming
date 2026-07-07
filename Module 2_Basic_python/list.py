numbers = [23,41,45,35,46,75,31,24,56,31,34,54,90]

# print(numbers[3],numbers[-3])

# list (start : end )
# print(numbers[3:-3])
# print(numbers[0:3])

# list (start : end : steps)
# print(numbers[0:8:1])
# print(numbers[0:8:2])   # 2 steps
# print(numbers[2:8:-1])
# print(numbers[8:2:-1])
# print(numbers[3:])    # index 3 to last  
# print(numbers[:8])    # index 0 to 7
# print(numbers[:])     # shortcut copy list
# print(numbers[::-1])  # shortcut reverse

numbers.append(420)   # add a element at the last of list
print(numbers[:])

numbers.insert(3,69)  # insert a element in index 3
print(numbers[3])

if 90 in numbers:
    numbers.remove(90)  # remove(value)
if 23 in numbers:
    numbers.remove(23)

print(numbers[:])

index = numbers.index(35)
print(index)