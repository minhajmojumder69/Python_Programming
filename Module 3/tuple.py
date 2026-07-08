def multiple():
    return 3,4
# print(multiple()) 

things = 'pen','pencil','laptop','tab','mobile'
# print(type(things))
# print(things)

mega = ([2,3,5,6],[43,45,67,39],[12,45,23,56])   # list in tuple
print(type(mega))
# mega[0] = [1,2,3,4]  its not possible
mega[0][2] = 69  
print(mega)