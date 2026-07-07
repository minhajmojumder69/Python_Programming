numbers = [10,24,45,88,65,43,85,39,20,44,90]
odds = []
even = []
# for num in numbers:
#     if num %2 == 1:
#         odds.append(num)
#     elif num %2 == 0:
#         even.append(num)
# print('Odd numbers :',odds)
# print('Even numbers :',even)

# odd_numbers = [num for num in numbers if num %2 == 1]
odd_numbers = [num for num in numbers if num %2 == 1 if num % 5 == 0]
print(odd_numbers)

players = ['sakib','musfik','mustafis']
ages = [38,36,34]

# for player in players:
#     print(player)
#     for age in ages:
#         print(player,age)

player_age = [[player,age] for player in players for age in ages]
print(player_age)