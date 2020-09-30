#insertion sort O(n^2), Om(n), theta(n^2)
def insertion_sort(arr):
  for i in range(len(arr)):
    print(arr)
    e = i-1
    while arr[i]<arr[e]:
      e-=1
    arr = arr[:e+1]+[arr[i]] + arr[e+1:i] + arr[i+1:]
  return arr

insertion_sort([9, 4, 5, 1])
