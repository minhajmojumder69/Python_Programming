balance =  3000
def buy_things(item,price):
    # you can access global variable without using the global keyword
    print(f'Balance before buying',balance)
    print(f'Remaining balance after buying {item}',balance)

buy_things('sunglass', 1200)
print('global balance after buying',balance) 


balance2 =  5000
def buy_things2(item,price):
    # but if you want to modify a global variable, you have to use the global keyword
    global balance2
    print(f'Balance before buying',balance2)
    balance2 = balance2 - price
    print(f'Remaining balance after buying {item}',balance2)

buy_things2('sunglass', 800)
print('global balance after buying',balance2)