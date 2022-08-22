'''Bubble Sort 
1. Here, we compare first element to second element
2. Chosse greater element then compare next element and so on
3. put grater element last
4. repeat step 1 to 3 untill array sort
Time complexity - O(n^2)
Space complexity - O(1) or constant
'''


def bubbleSort(arr):
    for i in range(len(arr)-1):
        # if list already sorted break loop - time complexity O(n)
        swap = False
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            break

if __name__=='__main__':
    arr = [10, 4, 12, 1, 23, 15]
    bubbleSort(arr)
    print(arr)