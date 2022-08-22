'''Lomuto method - Quick Sort Algorithm
1. in this method, we choose last(or middle) element as pivot and compare with first element.
2. if first element less than pivot move to second and so on.
3. if element greater than pivot than select element compare with count(next element of select element) after that swap 
4. left elments should be less than pivot and right elements should be greater than pivot.
Here, we divide arr into two partition left partition and right
5. repeat step 1 to 4 untill arr sort.
'''

def swap(a, b, arr):
    if a!=b:
        arr[a], arr[b] = arr[b], arr[a]

def partition(start, pindex, arr):
    pivot = arr[pindex]
    for count in range(start, pindex):
        if arr[count] <= pivot:
            swap(start, count, arr)
            start+=1

    swap(start, pindex, arr)
    return start

def lomuto(start, pindex, arr):
    if len(arr) == 1:
        return
    # sorting partiion recursively
    if start < pindex:
        index = partition(start, pindex, arr)
        lomuto(start, index-1, arr) # left
        lomuto(index+1, pindex, arr) # right

if __name__=='__main__':
    test = (
        [10, 4, 12, 1, 23, 15],
        [4, 9, 2, 1, 23, 10, 12, 35, 34, 29, 45, 39, 22 ,11, 50, 42],
        [2],
        [344, 89, 32, 213, 456, 343, 879, 674, 453, 98, 106, 547, 490, 76])

    for arr in test:
        lomuto(0, len(arr)-1, arr)
        print(arr)