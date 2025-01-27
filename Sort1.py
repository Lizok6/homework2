arr=[1,23,32,45,13,7,69,8,36,12]

for i in range(1, 10):
  for j in range(10-i):
    if arr[j]> arr[j+1]:
      arr[j], arr[j+1]= arr[j+1], arr[j]
print(arr,"сортировка массива по возрастанию методом пузырька")


