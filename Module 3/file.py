# with open('message.txt','w') as file:
#     file.write('O sokina,gesos kina.. vuilla amare')

# with open('message.txt','a') as file:
#     file.write('O sokina,gesos kina.. vuilla amare\n')

with open('message.txt','r') as file:
    text = file.read()
    print(text)
