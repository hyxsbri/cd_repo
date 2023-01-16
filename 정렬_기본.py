

arr = [7,5,9,0,3,1,6,2,4,8]

# 선택 정렬

for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)

# 삽입 정렬

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break

print(arr)

# 퀵 정렬

arr2 = [5,7,9,0,3,1,6,2,4,8]
def quick(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right <= start and array[right] <= array[pivot]):
            right -= 1
        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick(array, start, right-1)
    quick(array, right+1, end)

# 퀵2
def quick2(array):
    if len(array)<=1:
        return array
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick2(left) + [pivot] + quick2(right)

print(quick2(arr2))     
        























