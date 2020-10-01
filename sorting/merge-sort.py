def merge_sort(arr): #time complexity (all 3 cases = n log n)
  # print(arr)
  if len(arr)>1:
    arr = merge(merge_sort(arr[:int(len(arr)/2)]), merge_sort(arr[int(len(arr)/2):]))
  return arr
    

def merge(l, r):
  n = []
  while (len(l)!=0 and len(r)!=0):
    if l[0]>r[0]:
      n.append(r[0])
      del r[0]
    else:
      n.append(l[0])
      del l[0]
  n.extend(l)
  n.extend(r)
  # print(n)
  return n
