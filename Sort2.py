arr=[1,23,32,45,13,7,69,8,36,12]

for i in range(10-1):
  imax=i
  for j in range(i, 10):
    if arr[j]< arr[imax]:
      imax=j
    arr[i], arr[imax] = arr[imax], arr[i]
print(arr,"сортировка массива по возрастанию методом выбора")