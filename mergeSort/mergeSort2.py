def mergeSort(elements, key):
    if len(elements) <= 1:
        return

    mid = len(elements)//2
    left = elements[mid:]
    right = elements[:mid]
    mergeSort(left, key)
    mergeSort(right,key)

    mergeTwo(left, right, elements , key)

def mergeTwo(left, right, elements, key ):
    a = len(left)
    b = len(right)
    i = j = k = 0
    while i < a and j < b:
        if left[i][key] <= right[j][key]:
            elements[k] = left[i]
            i+=1

        else:
            elements[k] = right[j]
            j+=1
        k+=1

    while i < a:
        elements[k] = left[i]
        i+=1
        k+=1
    while j < b:
        elements[k] = right[j]
        j+=1
        k+=1

if __name__=='__main__':
    elements = [ 
                {'name': 'shyanukant', 'device' : 'samsung', 'amount': 20000},
                {'name': 'swetank', 'device' : 'iphone', 'amount': 95000},
                {'name': 'devashish', 'device' : 'redmi', 'amount': 18000},
                {'name': 'swati', 'device' : 'nokia', 'amount': 12000}
            ]

    mergeSort(elements, 'amount')
    print(elements)