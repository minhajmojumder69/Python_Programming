# in, not, not in, is , is not
# >, <, >=, <=, == !=
# and, or

# a = input()         # user input
# a_int = int(a)      # str to int
boss = True

# if a_int > 4:
#     print('4 ar beshi')
#     print('but koto beshi k jane..')
# elif a_int == 4:
#     print('4 ar soman soman')
# else:
#     print('4 ar kom')
#     print('koto kom k janee..')

# if boss is True:
#     print('Tel ar bakso niye astesi, boss re tel marmu')
# else:
#     print('akhon na,, lunch ar pore ashen')

# if boss is not True:
#     print('akhon na,, lunch ar pore ashen')
# else:
#     print('Tel ar bakso niye astesi, boss re tel marmu') 

# Nested conditions
coin = 'head'
if boss == True:
    print('boss you are joss')
    if coin == 'tail':
        print('batting')
    else:
        print('bowling')
else:
    print('boss tui murii khaa..')