# way 1:
# print('I need Money')
# input('Give me some money: ')

# way 2:
# money = input('Give me some money: ')
# print("Here is your money",money)

# way 3:
first_money = input('From Ome: ')
second_money = input('From Nafish: ')

print('Ome give me',first_money, 'tk and nafish give me',second_money, 'tk')
total = first_money + second_money
print(type(first_money))    # by default its takes input as string
print(total)

print('after converting into int')
first_money_int = int(first_money)      # converting str into int
second_money_int = int(second_money)    # converting str into int
total = (first_money_int + second_money_int)
print(total)
print(type(first_money_int))