#selection sort
def selection_sort(arr):
  unsorted = arr
  sorted_ = []
  #can directly use min function, but better to visualize

  for x in range(len(arr)):
    curr_min = unsorted[0]
    ind = 0
    for e, i in enumerate(unsorted):
      if i<curr_min:
        curr_min = i
        ind = e
    sorted_.append(curr_min)
    unsorted = unsorted[:ind] + unsorted[ind+1:]#might there be a better way?
  return sorted_

selection_sort([9, 4, 5, 1 ])
