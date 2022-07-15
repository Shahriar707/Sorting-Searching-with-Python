def binarySearch(a, left, right, value):
    if left > right:
        return -1

    middle = (left + right) // 2

    if value == a[middle]:
        return middle
    elif value > a[middle]:
        return binarySearch(a, middle+1, right, value)
    else:
        return binarySearch(a, left, middle-1, value)

a = [-5,-2,15,20,23,30,56]
value = 20

(left, right) = (0, len(a)-1)
position = binarySearch(a, left, right, value)

if position != -1:
    print("The value is found at Index - ", position)
else:
    print("The value is not found at Index")