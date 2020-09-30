#bubble sort O(n^2), Om(n), theta(n^2)
def bubble_sort(arr):
  swap_occur = True #if no swaps occur list is sorted, so we use this to check
  while swap_occur == True:
    swap_occur = False
    for i in range(len(arr)):
      if i!=len(arr)-1:
        if arr[i]>arr[i+1]:
          swap_occur = True
          arr[i], arr[i+1] = arr[i+1], arr[i]
  return arr

bubble_sort([9, 4, 5, 1 ])
