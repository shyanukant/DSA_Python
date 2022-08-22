'''                                           |          
Merge Sort - divide and conquer technique     |          4|6|3|5|2|9
1. divide array into two part (half, half)    |     4|6|3           5|2|9              2|3|4|5|6|9
2. repeat step 1                              |    4    6|3        5    2|9         3|4|6       2|5|9
3. compare elements and merge                 |        6   3           2   9 --->    3|6         2|9
'''
def mergeSort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)

    compare_merge(left, right, arr)
    
def compare_merge(a, b,arr):
    i = j = k = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    while i < len(a):
        arr[k] = a[i]
        i+=1
        k+=1
    while j < len(b):
        arr[k] = b[j]
        j+=1
        k+=1
    
if __name__=='__main__':
    arr =[14, 6, 13, 5, 2, 9, 12, 32, 29, 18, 30, 25, 15, 8, 27]
    mergeSort(arr)
    print(arr)