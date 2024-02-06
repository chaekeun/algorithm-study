# selection sort

for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[min_idx], arr[i] = arr[i], arr[min_idx] #swap

# insertion sort

for i in range(1, len(arr)): #데이터를 하나씩 확인하면서 어떤 위치에 들어갈지 j반복문을 이용해서 찾는다
    for j in range(i, 0, -1): #삽입하고자 하는 원소의 위치 : i부터 1까지 -1씩 반복하는 문법 
        if arr[j-1]>arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춘다
            break

# quick sort

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end
    while(left<=right):
        # 왼쪽에서부터 pivot보다 큰 데이터를 선택(ft 오름차순..)
        while(left <= end and arr[left] <= arr[pivot]):
            left += 1
        # 오른쪽에서부터 pivot보다 작은 데이터를 찾을 때까지 반복
        while(right > start and arr[right] >= arr[pivot]):
            right -= 1
        if (left>right):
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)

quick_sort(arr, 0, len(arr)-1)

