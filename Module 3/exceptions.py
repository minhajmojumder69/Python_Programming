try:
    result = 43/0
except:
    print('error happened')
finally:
    print('finally')
print('done')