arr=[1,23,32,45,13,7,69,8,36,12]


for i in range(1, 10):
  imax=i
  for j in range(i, 10):
    if arr[j]< arr[imax]:
     imax=j
    arr[i], arr[imax] = arr[imax], arr[i]  
print(arr[0] + arr[1] + arr[2] + arr[3],arr[6] + arr[7] + arr[8] + arr[9],"программа, используя сортировку методом выбора, которая в массиве целых чисел находит сумму наименьших четырех элементов и сумму наибольших четырех элементов")