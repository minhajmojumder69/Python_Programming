# string = list(input().split())
# for i in string:
#     print(i[::-1], end=" ")

string = list(input().split())
string2 = []
for i in string:
    string2.append(i[::-1])
print(*string2)