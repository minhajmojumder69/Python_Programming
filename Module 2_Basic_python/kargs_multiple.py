# def full_name(first,last):
#     # name = first + ' ' + last
#     name = f'{first} {last}'
#     return name
# # take parameters in order (serial wise)
# # name = full_name('alu','potol')

# name = full_name(last='potol',first='alu')
# print(name)

# def famous(**kargs)
def famous_name(first,last,**additional):
    name = f'{first} {last}'
    # print(additional['title'])
    for key, value in additional.items():
        print(key,value)

    return name
# name = famous_name(first='taher',last='Mia',title="Dr",additional="mc")
name = famous_name('taher','mia',title="Dr",additional="mc")
print(name)

# def famous(first,last,*args,**args)

# return multiple things
def a_lot(num1,num2):
    sum = num1 + num2
    multi = num2 * num1
    remain = num1 - num2
    return sum,multi,remain
everything = a_lot(28,23)
print(everything)