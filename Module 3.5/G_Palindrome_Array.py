n = int(input())

array = input().split()

if array == array[::-1]:
    print('YES')
else:
    print('NO')