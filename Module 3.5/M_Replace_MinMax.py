n = input()
array = list(map(int,input().split()))
min_nmbr = array.index(min(array))
max_nmbr = array.index(max(array))

array[min_nmbr],array[max_nmbr] = array[max_nmbr],array[min_nmbr]

print(*array)