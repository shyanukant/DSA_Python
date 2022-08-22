'''Hoare method - Quick Sort Algorithm
1. in this method, we choose first element as pivot and put in middle of array.
2. left elments should be less than pivot and right elements should be greater than pivot.
Here, we divide arr into two partition left partition and right
3. repeat step 1 to 2 for partition untill arr sort.
'''
def swap(a, b, arr):
    if a!= b:
        arr[a], arr[b] = arr[b], arr[a]

def partition(start, end, arr):
    pindex = start
    pivot = arr[pindex]
    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start+=1
        
        while arr[end] > pivot:
            end -= 1
        
        if start < end:
            swap(start, end, arr)

    swap(end, pindex, arr)
    return end

def hoare(start, end, arr):
    if len(arr) == 1:
        return
    if start < end:
        new_pindex = partition(start, end, arr) 
        hoare(start, new_pindex-1, arr) # left
        hoare(new_pindex+1, end, arr) #right

if __name__=='__main__':
    test = (
        [10, 4, 12, 1, 23, 15],
        [4, 9, 2, 1, 23, 10, 12, 35, 34, 29, 45, 39, 22 ,11, 50, 42],
        [2],
        [344, 89, 32, 213, 456, 343, 879, 674, 453, 98, 106, 547, 490, 76])

    for arr in test:
        hoare(0, len(arr)-1, arr)
        print(arr)